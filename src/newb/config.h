#ifndef NL_CONFIG_H
#define NL_CONFIG_H
/* XENOTHAR SKY VISION v2 — restrained natural colour profile.
   Based on Newb X Legacy configuration; customized for Android/MB Loader.
   Renderer support depends on the Minecraft version and MB Loader build. */

/* Colour: natural daylight, restrained dawn tint, deep blue night. */
#define NL_TONEMAP_TYPE 3
#define NL_GAMMA 1.42
/* NL_TINT intentionally disabled to avoid a global colour cast. */

/* Lighting: brighter daytime visibility with stronger, higher-contrast shadows. */
#define NL_SUNLIGHT_INTENSITY 3.35
#define NL_TORCHLIGHT_INTENSITY 1.0
#define NL_SHADOW_INTENSITY 0.84
#define NL_MIN_LIGHTING_BOOST 1.55
#define NL_CLOUD_SHADOW

#define NL_NETHER_AMBIENT vec3(2.5,1.45,1.95)
#define NL_END_AMBIENT vec3(1.45,0.82,2.15)
#define NL_DAWN_SUNLIGHT_COL vec3(1.0,0.58,0.42)
#define NL_NOON_SUNLIGHT_COL vec3(1.0,0.88,0.76)
#define NL_NIGHT_MOONLIGHT_COL vec3(0.16,0.22,0.48)

#define NL_OVERWORLD_TORCH_COL vec3(1.0,0.58,0.30)
#define NL_UNDERWATER_TORCH_COL vec3(0.62,0.82,1.0)
#define NL_NETHER_TORCH_COL vec3(1.0,0.46,0.22)
#define NL_END_TORCH_COL vec3(0.72,0.48,1.0)

/* Moderate atmospheric depth; do not darken daytime with dense fog. */
#define NL_FOG 0.90
#define NL_MIST_DENSITY 0.15
#define NL_RAIN_MIST_OPACITY 0.10
#define NL_CLOUDY_FOG 0.10

#define NL_SKY_VOID_FACTOR 0.50
#define NL_SKY_VOID_DARKNESS 0.30
#define NL_SKY_RAIN_MIX_FACTOR 0.90

/* Day palette stays naturally blue and bright, not overexposed. */
#define NL_DAWN_ZENITH_COL vec3(0.12,0.30,0.55)
#define NL_DAWN_HORIZON_COL vec3(1.15,0.42,0.48)
#define NL_DAWN_EDGE_COL vec3(1.05,0.58,0.66)
#define NL_DAY_ZENITH_COL vec3(0.30,0.72,1.15)
#define NL_DAY_HORIZON_COL vec3(0.92,1.18,1.35)
#define NL_DAY_EDGE_COL vec3(1.05,1.18,1.30)
#define NL_NIGHT_ZENITH_COL vec3(0.008,0.020,0.075)
#define NL_NIGHT_HORIZON_COL vec3(0.025,0.050,0.15)
#define NL_NIGHT_EDGE_COL vec3(0.06,0.08,0.20)
#define NL_RAIN_ZENITH_COL vec3(0.34,0.38,0.48)
#define NL_RAIN_HORIZON_COL vec3(0.52,0.52,0.62)
#define NL_END_ZENITH_COL vec3(0.035,0.004,0.12)
#define NL_END_HORIZON_COL vec3(0.42,0.035,0.58)

#define NL_RAINBOW
#define NL_RAINBOW_CLEAR 0.0
#define NL_RAINBOW_RAIN 0.25

#define NL_GLOW_TEX 1.8
#define NL_GLOW_SHIMMER 0.40
#define NL_GLOW_SHIMMER_SPEED 0.65

/* More visible grass/foliage sway. This animates plants; it does not alter texture blade width. */
#define NL_PLANTS_WAVE 0.095
#define NL_LANTERN_WAVE 0.09
#define NL_WAVE_SPEED 2.45
#define NL_WAVE_RANGE 16.0

/* More pronounced waves and the upstream shader's reflection-mask effect. */
#define NL_WATER_TRANSPARENCY 0.88
#define NL_WATER_BUMP 0.075
#define NL_WATER_WAVE_SPEED 0.72
#define NL_WATER_TEX_OPACITY 0.34
#define NL_WATER_WAVE
#define NL_WATER_REFL_MASK
#define NL_WATER_TINT vec3(0.48,0.76,0.92)

/* Underwater: stronger refraction-like view distortion, caustics and light streaks. Blocks remain stationary; the view shimmer simulates moving water. */
#define NL_UNDERWATER_BRIGHTNESS 0.88
#define NL_CAUSTIC_INTENSITY 1.45
#define NL_UNDERWATER_WAVE 0.12
#define NL_UNDERWATER_STREAKS 0.82
#define NL_UNDERWATER_TINT vec3(0.52,0.76,0.92)

#define NL_CLOUD_TYPE 1
#define NL_CLOUD0_THICKNESS 2.0
#define NL_CLOUD0_RAIN_THICKNESS 3.0
#define NL_CLOUD0_OPACITY 0.86
#define NL_CLOUD0_MULTILAYER
#define NL_CLOUD1_SCALE vec2(0.018,0.024)
#define NL_CLOUD1_DEPTH 1.1
#define NL_CLOUD1_SPEED 0.028
#define NL_CLOUD1_DENSITY 0.48
#define NL_CLOUD1_OPACITY 0.86
#define NL_CLOUD2_THICKNESS 2.0
#define NL_CLOUD2_RAIN_THICKNESS 2.4
#define NL_CLOUD2_STEPS 4
#define NL_CLOUD2_SCALE vec2(0.032,0.032)
#define NL_CLOUD2_SHAPE vec2(0.48,0.42)
#define NL_CLOUD2_DENSITY 23.0
#define NL_CLOUD2_VELOCITY 0.50
#define NL_CLOUD3_SCALE vec2(0.028,0.028)
#define NL_CLOUD3_SPEED 0.004
#define NL_CLOUD3_SHADOW 0.76
#define NL_CLOUD3_SHADOW_OFFSET 0.24

/* Subtle aurora and occasional shooting stars, mainly visible at night. */
#define NL_AURORA 0.85
#define NL_AURORA_VELOCITY 0.018
#define NL_AURORA_SCALE 0.035
#define NL_AURORA_WIDTH 0.15
#define NL_AURORA_COL1 vec3(0.12,0.62,0.72)
#define NL_AURORA_COL2 vec3(0.38,0.18,0.72)
#define NL_CLOUD_AURORA_REFLECTION
#define NL_SHOOTING_STAR 0.65
#define NL_SHOOTING_STAR_PERIOD 8.0
#define NL_SHOOTING_STAR_DELAY 78.0
#define NL_GALAXY_VIBRANCE 0.72
#define NL_GALAXY_SPEED 0.016
#define NL_GALAXY_DAY_VISIBILITY 0.0

#define NL_SUN_SIZE 1.0
#define NL_MOON_SIZE 1.0
#define NL_SUN_PATH_YAW 15.0
#define NL_MOON_PATH_YAW 17.0
#define NL_SUN_PATH_TILT 31.0
#define NL_MOON_PATH_TILT -28.0
#define NL_SUN_TILT 45.0
#define NL_MOON_TILT 45.0

#define NL_GROUND_RAIN_WETNESS 0.78
#define NL_GROUND_RAIN_PUDDLES 0.38
#define NL_ENTITY_BRIGHTNESS 0.68
#define NL_ENTITY_EDGE_HIGHLIGHT 0.26
#define NL_WEATHER_SPECK 0.50
#define NL_WEATHER_RAIN_SLANT 3.2
#define NL_WEATHER_PARTICLE_SIZE 0.90
#define NL_LAVA_NOISE
#define NL_LAVA_NOISE_SPEED 0.16

#ifdef NO_WAVE_NO_FOG
 #define NO_WAVE
 #define NO_FOG
#endif
#ifdef NO_FOG
 #undef NL_FOG
#endif
#ifdef NO_WAVE
 #undef NL_PLANTS_WAVE
 #undef NL_LANTERN_WAVE
 #undef NL_UNDERWATER_WAVE
 #undef NL_WATER_WAVE
 #undef NL_RAIN_MIST_OPACITY
#endif
#ifdef ROUNDED_CLOUDS
 #undef NL_CLOUD_TYPE
 #define NL_CLOUD_TYPE 2
 #undef NL_CLOUD_SHADOW
#endif
#ifdef BOX_CLOUDS
 #undef NL_CLOUD_TYPE
 #define NL_CLOUD_TYPE 0
 #undef NL_CLOUD_SHADOW
#endif
#ifdef REALISTIC_CLOUDS
 #undef NL_CLOUD_TYPE
 #define NL_CLOUD_TYPE 3
 #undef NL_CLOUD_SHADOW
#endif
#endif
