# XENOTHAR SKY VISION

A custom Android-oriented Minecraft Bedrock visual pack for MB Loader, built from shader source and tuned around the project's blue moonlit Overworld and violet/pink cosmic End references.

## Target
- Minecraft Bedrock 1.26.60+
- Android using MB Loader / the compatible RenderDragon material pipeline
- Conservative water movement and restrained visual complexity for mid-range devices

## Included in v1.0.1 Android build
- Custom blue/violet day, dusk and night color grading.
- Sun, moon and star rendering with sunrise/sunset color transitions from the shader pipeline.
- Moving soft clouds, optional rounded/box/realistic cloud subpacks.
- Night aurora and occasional shooting-star effects supported by the upstream shader code.
- Tuned block lighting, shadow strength, glow and foliage/lantern wave settings.
- Calm water wave/bump tuning and blue underwater atmosphere with restrained caustics/streaks.
- Purple cosmic End sky/fog palette.
- Optional reduced-wave and reduced-fog subpacks.

## Subpacks
- **Balanced default** — custom tuned visual profile.
- **Realistic cloud profile** — more detailed cloud rendering.
- **Rounded cloud profile** — rounded cloud shape.
- **Box cloud profile** — vanilla-style cloud geometry path.
- **Reduced wave effects** — disables plant, lantern and water wave motion.
- **Reduced fog** — disables shader fog.

## Compatibility and testing
The Android resource pack compiled successfully in GitHub Actions from the pinned upstream source revision. The generated .mcpack archive passed ZIP integrity validation and contains compiled RenderDragon material binaries.

A successful build is not the same as an in-game device test. This pack has not yet been verified on the target phone or inside the user's exact MB Loader installation. Visual output and individual effects still depend on the Minecraft build, RenderDragon and MB Loader compatibility. If the loader rejects the pack or a feature does not render, report the exact error/screenshot so the material path can be adjusted. This project targets MB Loader, not the official Vibrant Visuals pipeline.

## Build
GitHub Actions builds the Android .mcpack on pushes to the shader configuration or workflow, and can also be run manually from Actions > Build Android pack.

The workflow pins Newb X Legacy source to a specific commit and applies this project's own pack configuration and shader tuning before compiling.

## Upstream and licensing
The shader source/build pipeline is based on [Newb X Legacy](https://github.com/devendrn/newb-x-mcbe) by devendrn. The upstream source repository identifies its source code as MIT-licensed. The project builds from source and does not redistribute the upstream project's precompiled pack. See the upstream repository for full notices and asset terms.

## Install
1. Download `XENOTHAR-SKY-VISION-Android.mcpack`.
2. Open the file and choose Minecraft to import it.
3. In Minecraft, activate **XENOTHAR SKY VISION** under Global Resources.
4. Start Minecraft through MB Loader as required by your MB Loader setup.
5. Begin with **Balanced default**. If performance or compatibility is poor, try **Reduced wave effects**.


## Moon texture attribution
The in-pack lunar surface atlas is adapted from the 8K Solar System Scope Moon texture, based on NASA lunar elevation and imagery data. Source: https://commons.wikimedia.org/wiki/File:Solarsystemscope_texture_8k_moon.jpg. Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). The atlas is converted to Bedrock's eight moon phases by the build script.
