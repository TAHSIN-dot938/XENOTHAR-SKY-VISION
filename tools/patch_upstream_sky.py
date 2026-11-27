#!/usr/bin/env python3
"""Apply XENOTHAR night-sky enhancements to the pinned Newb X Legacy build tree."""
from pathlib import Path
import math, random
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1] / "upstream"
SKY = ROOT / "src/newb/functions/sky.h"
MOON = ROOT / "assets/textures/environment/moon_phases.png"

def patch_meteors():
    source = SKY.read_text(encoding="utf-8")
    start = source.index("// shooting star\nvec3 nlRenderShootingStar(")
    end = source.index("\n}\n", start) + 2
    replacement = r'''// XENOTHAR: dense meteor shower. 20 independently seeded entries per second.
vec3 nlRenderShootingStar(vec3 viewDir, vec3 FOG_COLOR, float t) {
  vec3 result = vec3(0.0);
  float nightMask = clamp(1.0 - FOG_COLOR.r - FOG_COLOR.g - FOG_COLOR.b, 0.0, 1.0);
  for (int i = 0; i < 3; ++i) {
    float eventId = floor(t * NL_SHOOTING_STAR_RATE) - float(i);
    float age = t - eventId / NL_SHOOTING_STAR_RATE;
    if (age >= 0.0 && age < NL_SHOOTING_STAR_LIFETIME) {
      float phase = clamp(age / NL_SHOOTING_STAR_LIFETIME, 0.0, 1.0);
      float r = fract(sin(eventId * 12.9898 + 78.233) * 43758.5453);
      float r2 = fract(sin(eventId * 39.3467 + 11.135) * 24634.6345);
      float a = 6.2831853 * r2;
      float ca = cos(a), sa = sin(a);
      vec2 uv = viewDir.xz * (6.0 + 4.0 * r);
      uv = vec2(ca * uv.x + sa * uv.y, -sa * uv.x + ca * uv.y);
      uv.x += 1.0 - 2.0 * phase;
      uv.x -= 2.0 * r + 3.5;
      uv.y += viewDir.y * 3.0;
      float glow = 1.0 - min(abs(uv.x - 0.95) * 20.0, 1.0);
      float streak = 1.0 - min(abs(8.0 * uv.y), 1.0);
      streak *= smoothstep(-1.0 + 1.96 * (1.0 - phase), 0.98 - phase, uv.x);
      streak *= smoothstep(1.0, 0.98 - phase * phase, uv.x);
      streak *= sin(phase * 3.14159265);
      streak *= 0.7 + 12.0 * glow * glow;
      streak *= nightMask;
      float hue = fract(sin(eventId * 17.13 + 4.7) * 15731.743);
      vec3 meteorColor = mix(vec3(0.78, 0.88, 1.0), vec3(0.48, 1.0, 0.78), step(0.62, hue));
      meteorColor = mix(meteorColor, vec3(1.0, 0.72, 0.43), step(0.88, hue));
      result += streak * meteorColor * 0.20;
    }
  }
  return result;
}'''
    SKY.write_text(source[:start] + replacement + source[end:], encoding="utf-8")


def patch_solar_cycle():
    """Add a time-of-day solar halo without changing the upstream Sun/Moon draw path."""
    source = SKY.read_text(encoding="utf-8")
    start = source.index("vec3 renderOverworldSky(")
    end = source.index("\\nvec3 renderEndSky(", start)
    section = source[start:end]
    marker = "  return sky;\\n}"
    if "// XENOTHAR solar-cycle glow" not in section:
        if marker not in section:
            raise RuntimeError("Could not locate renderOverworldSky return point for solar-cycle patch")
        glow = r'''  // XENOTHAR solar-cycle glow: warm atmospheric halo at dawn, golden hour and sunset.
  // env.dayFactor and env.sunDir are derived from Minecraft TIME_OF_DAY.
  float sunAlignment = max(dot(normalize(env.sunDir), normalize(viewDir)), 0.0);
  float twilight = 1.0 - smoothstep(0.015, 0.62, abs(env.dayFactor));
  float sunVisible = smoothstep(-0.12, 0.055, env.sunDir.y);
  float clearSky = 1.0 - env.rainFactor * 0.88;
  float innerGlow = exp(-max(0.0, 1.0 - sunAlignment) * 46.0);
  float outerGlow = exp(-max(0.0, 1.0 - sunAlignment) * 8.0);
  vec3 goldenGlow = vec3(1.0, 0.62, 0.27);
  vec3 redGlow = vec3(1.0, 0.19, 0.075);
  vec3 twilightGlow = mix(goldenGlow, redGlow, smoothstep(0.12, 0.88, twilight));
  vec3 solarGlowColor = mix(goldenGlow, twilightGlow, twilight);
  float glowStrength = sunVisible * clearSky * (0.12 * outerGlow + 0.18 * innerGlow);
  sky += solarGlowColor * glowStrength;

  return sky;
}'''
        section = section.replace(marker, glow, 1)
        source = source[:start] + section + source[end:]
        SKY.write_text(source, encoding="utf-8")

def make_moon_atlas():
    # Use a real equirectangular lunar surface map (8K source) and bake it
    # into Bedrock's 4x2 moon-phase atlas. The atlas keeps the game shader's
    # expected layout while retaining authentic lunar maria/crater patterns.
    import urllib.request
    import io

    source_url = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Solarsystemscope_texture_8k_moon.jpg"
    request = urllib.request.Request(
        source_url,
        headers={"User-Agent": "XENOTHAR-SKY-VISION/1.0 (Minecraft resource-pack build)"}
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        source_bytes = response.read()
    lunar_map = Image.open(io.BytesIO(source_bytes)).convert("RGB")
    src_w, src_h = lunar_map.size
    src = lunar_map.load()

    size, cols, rows = 512, 4, 2
    atlas = Image.new("RGBA", (size * cols, size * rows), (0, 0, 0, 0))
    for phase_index in range(8):
        tile = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        px = tile.load()
        angle = 2.0 * math.pi * phase_index / 8.0
        light_x, light_z = math.sin(angle), math.cos(angle)
        for y in range(size):
            ny = (y - size / 2) / (size * 0.47)
            for x in range(size):
                nx = (x - size / 2) / (size * 0.47)
                rr = nx * nx + ny * ny
                if rr > 1.0:
                    continue
                nz = math.sqrt(max(0.0, 1.0 - rr))

                # Project the sphere onto the real equirectangular lunar map.
                lon = math.atan2(nx, nz)
                lat = math.asin(max(-1.0, min(1.0, ny)))
                sx = int(((lon / (2.0 * math.pi)) + 0.5) * (src_w - 1)) % src_w
                sy = max(0, min(src_h - 1, int((0.5 - lat / math.pi) * (src_h - 1))))
                r, g, b = src[sx, sy]

                # Directional phase lighting; preserve map detail without
                # inventing craters or adding a synthetic surface pattern.
                lambert = max(0.0, nx * light_x + nz * light_z)
                limb = 0.68 + 0.32 * nz
                light = (0.10 + 0.90 * lambert) * limb
                alpha = int(255 * max(0.0, min(1.0, (lambert - 0.025) / 0.13)))
                px[x, y] = (
                    int(min(255, r * light)),
                    int(min(255, g * light)),
                    int(min(255, b * light)),
                    alpha
                )
        tile = tile.filter(ImageFilter.GaussianBlur(0.18))
        atlas.alpha_composite(tile, ((phase_index % cols) * size, (phase_index // cols) * size))

    MOON.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(MOON, format="PNG", optimize=True)

    credits = ROOT / "assets/textures/environment/MOON_TEXTURE_CREDITS.txt"
    credits.write_text(
        "Moon surface map: Solar System Scope, 8K lunar texture.\n"
        "Based on NASA lunar elevation and imagery data; colors are slightly "
        "more saturated and some gaps are filled with similar terrain.\n"
        "Source: https://commons.wikimedia.org/wiki/File:Solarsystemscope_texture_8k_moon.jpg\n"
        "License: Creative Commons Attribution 4.0 International (CC BY 4.0).\n"
        "Adapted into an 8-phase Bedrock moon atlas by XENOTHAR SKY VISION.\n",
        encoding="utf-8"
    )

if __name__ == "__main__":
    patch_meteors()
    patch_solar_cycle()
    make_moon_atlas()
    print("Patched meteor motion, time-driven solar halo, and real 8K-source lunar surface map into an 8-phase atlas.")
