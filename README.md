# XENOTHAR SKY VISION

An Android-focused Minecraft Bedrock visual-pack project for MB Loader.

## Target
- Minecraft Bedrock 1.26.60+
- Android with MB Loader
- Visual direction: moonlit blue Overworld sky and a purple/pink cosmic End, based on the project's supplied visual references.
- Performance target: conservative wave and reflection effects; prioritize stable frame pacing on mid-range Adreno devices.

## Planned visual modules
- Overworld: day/night sky, stars, moon/sun presentation, cloud styling and atmospheric color.
- Water: restrained wave motion and reflection-style appearance where the supported RenderDragon pipeline permits it.
- Underwater: blue depth atmosphere and carefully limited light/visibility effects.
- World: lightweight foliage motion and shadow/lighting refinements where supported.
- The End: purple/pink cosmic atmosphere inspired by the supplied reference.

## Important compatibility note
This project targets MB Loader, not the official Vibrant Visuals pipeline. Actual shader features depend on the Minecraft version, RenderDragon material format and MB Loader compatibility. Features that cannot be implemented by the selected material pipeline will not be advertised as working.

## Build
The Android build workflow checks out the upstream Newb X Legacy source, applies this project's pack configuration, installs its pinned build dependencies and builds an Android mcpack artifact. Run it from Actions > Build Android pack > Run workflow.

The first build is a branded compatibility baseline. Custom material effects are developed and validated incrementally; the full visual wishlist is not claimed complete until tested in-game.

## Upstream
Build pipeline: [Newb X Legacy](https://github.com/devendrn/newb-x-mcbe) by devendrn. See the upstream repository for its source license and compiled-pack redistribution terms. This project builds from upstream source rather than redistributing its compiled pack.

## Install
1. Download the mcpack from the successful GitHub Actions run artifact.
2. Import it into Minecraft.
3. Activate it in Global Resources.
4. Launch Minecraft through MB Loader.
