# Behind the profile

The header pairs large, openly spaced name lettering with four blue ribbons that enter through the top edge and leave through the right. Opposite circular bends share their centers and use signed radius offsets, keeping the lanes evenly spaced through the entire turn. A soft light-blue highlight travels along the curves.

The layout follows a résumé hierarchy: skills, engineering projects, experience, and education. Skills use the owner's requested rectangular logo badges, grouped by discipline. Each badge links to a relevant project, public source, deployment, or workflow; its tooltip explains the connection. Section navigation lets readers jump directly to the material they need. Five native disclosures expose testing tools, camera/model boundaries, matching logic, knock timing, and event delivery. These remain keyboard-accessible without JavaScript. Manua also links directly to separate learner and educator walkthroughs.

Two original SVG diagrams expose the mechanisms inside the larger projects. They are schematics, not screenshots, benchmarks, or evidence of adoption. Leadership and teaching appear once, in experience. Education stays concise; no grades or unconfirmed dates are published.

## Assets

Run `python3 scripts/build_assets.py` from the repository root to regenerate the original illustrations. Run the same command with `--check` to verify the committed illustrations, saved badge checksums and SVG syntax, local README links, and image alternative text. Python's standard library is the only dependency. CI checks assets; it never rewrites the profile or needs write access.

The 26 badges in `assets/badges/` are saved, self-contained SVGs rendered once with [Shields' static badge API](https://shields.io/badges/static-badge), using its `for-the-badge` style. The profile makes no runtime requests to a badge service. Logos come from [Simple Icons](https://github.com/simple-icons/simple-icons), with Java and Playwright from [Devicon](https://github.com/devicons/devicon/tree/7330accdbc47e2dc0c19789a48533c4a3c50fe58); the Java logo is recolored white. Source recipes and checksums are in `assets/badges/sources.json`; upstream licenses are in `assets/badges/licenses/`. Brand colors are adjusted where needed for legibility. These are ordinary linked images, not GitHub-native interactive widgets. Inline placement lets the boxes wrap naturally on mobile, and every badge has text alternative content. Testing and delivery badges sit inside a disclosure to keep the visible inventory compact.

Each illustration has light, dark, narrow-light, and narrow-dark versions. GitHub's `#gh-light-mode-only` and `#gh-dark-mode-only` link hooks select the theme; a `<picture>` inside each link independently selects the narrow composition. This also handles an explicitly chosen GitHub theme that differs from the operating system. Combining theme and width in one source query does not work reliably: GitHub's `themed-picture` component rewrites theme queries and drops the width condition.

Narrow versions rearrange the composition instead of shrinking desktop text. SVG text uses system fonts, with no font downloads, scripts, embedded HTML, raster images, or external resources. The desktop image is the fallback if picture source selection is unavailable. The theme hooks target GitHub; another Markdown viewer may show both theme versions.

The header uses a seamless seven-second linear animation, only when `prefers-reduced-motion: no-preference` matches. Normalized path lengths coordinate a blurred halo, blue highlight, and pale core. The paths extend beyond the clipping area, so the light enters and exits at the card edges. The picture element also selects a separate static header for reduced motion, so this works even when a browser does not pass its motion preference into an embedded SVG. Unavailable CSS animation leaves the full blue illustration visible without movement. Diagram content is static.

The palette uses deep navy, blue, and light blue across all three illustrations. Text outside the illustrations inherits the reader's GitHub theme. Essential content also appears in image alternative text; the implementation notes use keyboard-accessible native disclosures.

## Content boundaries

Descriptions were checked against repository code and project records on September 19, 2026. Manua and LocatED have private source repositories, so the README does not send visitors to inaccessible code links. Manua's public walkthrough is a prototype. LocatED has not launched at school. No usage totals or model-accuracy figures are implied.

The skills inventory is grounded in application dependencies, database migrations, the Python training package, public JavaScript and embedded source, and owner-confirmed teaching experience. It does not assign proficiency percentages or claim certifications. Tinovation, BOBTutor, Synthesis Hacks participation/support totals, and coursework use the owner's current records. Sponsor support includes credits and scholarships; it is not represented as cash alone. Unconfirmed role dates and tutoring roster totals are omitted.

Manua's drawing separates camera calibration from the scripted word-feedback example in its public walkthrough. It does not depict a hand being translated into a word. The LocatED diagram separates candidate matching from ownership verification. Knok Lok is described as a rhythm-detection prototype, without claims about a working door actuator, notifications, or production security.

Public references: [Manua walkthrough](https://manua-asl.vercel.app/demo), [Synthesis Hacks](https://www.synthesishacks.com/), [event website source](https://github.com/BernardCode/synthesis-hacks), [Knok Lok project](https://devpost.com/software/knok-lok), and [Knok Lok firmware](https://github.com/DVeldhurthi/Knok_Lok/blob/main/Knok_Lok.ino). FBLA team placement and USACO division come from the owner's project records; the latter is a division, not a medal.
