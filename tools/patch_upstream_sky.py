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
  for (int i = 0; i < 12; ++i) {
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
      uv.x += phase * 2.0 - 1.0;
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

def make_moon_atlas():
    # Bedrock moon phase atlas: 4 columns x 2 rows, 256px per phase.
    size, cols, rows = 256, 4, 2
    atlas = Image.new("RGBA", (size * cols, size * rows), (0, 0, 0, 0))
    rng = random.Random(29032026)
    craters = []
    for _ in range(190):
        x, y = rng.uniform(-0.92, 0.92), rng.uniform(-0.92, 0.92)
        rad = rng.uniform(0.008, 0.085)
        if x*x + y*y < 0.92:
            craters.append((x, y, rad, rng.uniform(0.25, 0.85)))
    for phase_index in range(8):
        tile = Image.new("RGBA", (size, size), (0,0,0,0))
        px = tile.load()
        # Sequence of eight illuminated phases; 0 full, then waning to new and waxing.
        angle = 2.0 * math.pi * phase_index / 8.0
        light_x, light_z = math.sin(angle), math.cos(angle)
        for y in range(size):
            ny = (y - size/2) / (size*0.47)
            for x in range(size):
                nx = (x - size/2) / (size*0.47)
                rr = nx*nx + ny*ny
                if rr > 1.0:
                    continue
                nz = math.sqrt(max(0.0, 1.0-rr))
                illumination = max(0.0, nx*light_x + nz*light_z)
                if phase_index == 0:
                    illumination = max(0.0, nz)
                # Fine lunar maria and albedo variation.
                n = (math.sin(nx*43.0 + math.sin(ny*21.0))*0.5 +
                     math.sin(ny*57.0 + nx*19.0)*0.25 +
                     math.sin((nx+ny)*113.0)*0.12)
                shade = 0.68 + 0.12*n + 0.20*illumination
                # Soft terminator, natural limb darkening.
                shade *= 0.72 + 0.28*nz
                crater_delta = 0.0
                for cx, cy, cr, depth in craters:
                    dx, dy = nx-cx, ny-cy
                    d = math.sqrt(dx*dx+dy*dy)
                    if d < cr*1.35:
                        ring = math.exp(-((d-cr*0.82)/(cr*0.13))**2)
                        basin = math.exp(-((d)/(cr*0.72))**2)
                        crater_delta += 0.13*ring - 0.11*basin*depth
                shade = max(0.0, min(1.0, shade + crater_delta))
                # Moon texture stays subdued, neutral grey, not over-saturated.
                val = int(255 * shade)
                alpha = int(255 * min(1.0, illumination*1.25 + 0.03))
                px[x,y] = (val, int(val*0.985), int(val*0.95), alpha)
        tile = tile.filter(ImageFilter.GaussianBlur(0.25))
        atlas.alpha_composite(tile, ((phase_index % cols)*size, (phase_index // cols)*size))
    MOON.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(MOON, format="PNG", optimize=True)

if __name__ == "__main__":
    patch_meteors()
    make_moon_atlas()
    print("Patched 20 meteor starts/sec and generated 8-phase high-detail moon atlas.")
