# Behind the profile

The visual identity is a lowercase b drawn as three routed circuit traces. A single signal travels through it when the header loads, then the graphic rests. It connects the web, vision, and hardware work without pretending to be a live dashboard.

The layout uses native GitHub text for project descriptions and links. Two original SVG diagrams expose the mechanisms inside the larger projects. They are schematics, not screenshots, benchmarks, or evidence of adoption. Smaller projects stay text-only so the page has a clear hierarchy.

## Assets

Run `python3 scripts/build_assets.py` from the repository root to regenerate the SVGs. Run the same command with `--check` to verify the committed assets. Python's standard library is the only dependency. CI checks generation; it never rewrites the profile or needs write access.

Each illustration has a light, dark, narrow-light, and narrow-dark version selected by a `<picture>` element. Narrow versions rearrange the composition instead of shrinking desktop text. SVG text uses system fonts, with no font downloads, scripts, embedded HTML, raster images, or external resources. The ordinary image is the light-theme fallback.

The header animation runs once for four seconds, only when `prefers-reduced-motion: no-preference` matches. Everything is visible before animation starts and after it finishes. Diagram content is static. If CSS animation is unavailable, the complete illustration remains visible.

The palette uses blue-black, cool white, and a single mint accent. Text outside the illustrations inherits the reader's GitHub theme. Essential content also appears in image alternative text; the implementation notes use keyboard-accessible native disclosures.

## Content boundaries

Descriptions were checked against repository code and project records on September 19, 2026. Manua and LocatED have private source repositories, so the README does not send visitors to inaccessible code links. Manua's public walkthrough is a prototype. LocatED has not launched at school. No usage totals or model-accuracy figures are implied.

Manua's drawing separates camera calibration from the scripted word-feedback example in its public walkthrough. It does not depict a hand being translated into a word. The LocatED diagram separates candidate matching from ownership verification. Knok Lok is described as a rhythm-detection prototype, without claims about a working door actuator, notifications, or production security.

Public references: [Manua walkthrough](https://manua-asl.vercel.app/demo), [Synthesis Hacks](https://www.synthesishacks.com/), [event website source](https://github.com/BernardCode/synthesis-hacks), [Knok Lok project](https://devpost.com/software/knok-lok), and [Knok Lok firmware](https://github.com/DVeldhurthi/Knok_Lok/blob/main/Knok_Lok.ino). FBLA team placement and USACO division come from the owner's project records; the latter is a division, not a medal.
