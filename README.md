<a href="./assets/hero-dark.svg#gh-dark-mode-only">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="./assets/hero-mobile-dark-static.svg?v=blue-ribbons">
    <source media="(prefers-reduced-motion: reduce)" srcset="./assets/hero-dark-static.svg?v=blue-ribbons">
    <source media="(max-width: 600px)" srcset="./assets/hero-mobile-dark.svg?v=blue-ribbons">
    <img src="./assets/hero-dark.svg?v=blue-ribbons" width="100%" alt="Bernard Freund. Student developer in the Bay Area.">
  </picture>
</a>
<a href="./assets/hero-light.svg#gh-light-mode-only">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="./assets/hero-mobile-light-static.svg?v=blue-ribbons">
    <source media="(prefers-reduced-motion: reduce)" srcset="./assets/hero-light-static.svg?v=blue-ribbons">
    <source media="(max-width: 600px)" srcset="./assets/hero-mobile-light.svg?v=blue-ribbons">
    <img src="./assets/hero-light.svg?v=blue-ribbons" width="100%" alt="Bernard Freund. Student developer in the Bay Area.">
  </picture>
</a>


<p>
  <a href="mailto:bernard.w.freund@gmail.com">Email</a> &nbsp; / &nbsp;
  <a href="https://www.linkedin.com/in/bernard-freund-753b0b288/">LinkedIn</a>
</p>

[Skills](#skills) &nbsp; · &nbsp; [Projects](#projects) &nbsp; · &nbsp; [Experience](#experience) &nbsp; · &nbsp; [Education](#education)

## Skills

| Area | Languages & tools |
| :--- | :--- |
| Languages | [TypeScript](#manua), [JavaScript](https://github.com/BernardCode/FBLA-WEBSITE-CODING/tree/main/assets/js), [Python](#manua), [Java](#bobtutor), [C++](#knok-lok), [SQL](#located) |
| Web | React, Next.js, HTML/CSS, Tailwind CSS |
| Data & vision | PostgreSQL, Supabase, MediaPipe, scikit-learn, NumPy, pandas |
| Embedded | ESP32, Arduino, sensor input, serial communication |

<details>
<summary>Testing & development workflow</summary>

| Tools | Where I use them |
| :--- | :--- |
| Vitest & React Testing Library | Application logic and component behavior |
| Playwright | Browser flows and end-to-end checks |
| pytest | Data validation, preprocessing, and model-pipeline checks |
| Git, GitHub Actions & Vercel | Version control, automated checks, and web deployments |

</details>

## Projects

### Manua

<sub>Developer · In development</sub>

Browser-based fingerspelling practice with adaptive review, teacher-managed classes, and assignments.

<a href="https://manua-asl.vercel.app/demo#gh-dark-mode-only">
  <picture>
    <source media="(max-width: 600px)" srcset="./assets/manua-mobile-dark.svg?v=blue-ribbons">
    <img src="./assets/manua-dark.svg?v=blue-ribbons" width="100%" alt="Two separate parts of Manua: on-device hand landmarks and a scripted practice example comparing MARTEN with MARTIN.">
  </picture>
</a>
<a href="https://manua-asl.vercel.app/demo#gh-light-mode-only">
  <picture>
    <source media="(max-width: 600px)" srcset="./assets/manua-mobile-light.svg?v=blue-ribbons">
    <img src="./assets/manua-light.svg?v=blue-ribbons" width="100%" alt="Two separate parts of Manua: on-device hand landmarks and a scripted practice example comparing MARTEN with MARTIN.">
  </picture>
</a>


[Try the learner walkthrough ↗](https://manua-asl.vercel.app/demo) &nbsp; / &nbsp; [Open the educator preview](https://manua-asl.vercel.app/demo?view=educator)

<details>
<summary>Camera processing, model evaluation & current limits</summary>

Camera frames stay in the browser for hand tracking and framing feedback. A separate training pipeline groups samples by signer before splitting the data, preventing the same signer from appearing in both training and evaluation sets. It also checks the split for overlap.

An approved letter classifier and signer recordings are still to come. The public walkthrough uses scripted examples and contains no real learner data.

</details>

### LocatED

<sub>Co-developer with Jerry Li · Pre-launch</sub>

A school lost-and-found platform covering item reports, search, claims, and returns. Our team placed 2nd nationally in FBLA Website Coding &amp; Development.

<a href="https://locateed.vercel.app/#gh-dark-mode-only">
  <picture>
    <source media="(max-width: 600px)" srcset="./assets/located-mobile-dark.svg?v=blue-ribbons">
    <img src="./assets/located-dark.svg?v=blue-ribbons" width="100%" alt="Matching pipeline: text, visual description, recency, location, and category feed candidate ranking. A suggested match still needs a verified claim.">
  </picture>
</a>
<a href="https://locateed.vercel.app/#gh-light-mode-only">
  <picture>
    <source media="(max-width: 600px)" srcset="./assets/located-mobile-light.svg?v=blue-ribbons">
    <img src="./assets/located-light.svg?v=blue-ribbons" width="100%" alt="Matching pipeline: text, visual description, recency, location, and category feed candidate ranking. A suggested match still needs a verified claim.">
  </picture>
</a>


[Explore the interface ↗](https://locateed.vercel.app/)

<details>
<summary>Candidate retrieval, scoring & campus locations</summary>

The database retrieves candidate items, then an application scoring layer combines the available evidence. Weights are renormalized when a signal is missing. Location evidence distinguishes a staff correction from an inferred location instead of treating both as equally certain.

Campus locations use named zones and room refinements, so a report can say “near the gym” without needing GPS coordinates. A match enters a separate claim-verification flow before an item can be returned.

</details>

### Knok Lok

<sub>Embedded prototype · MakerHacks</sub>

A sound-sensor project that recognizes a knock rhythm and signals whether it is accepted.

[Watch the build demo ↗](https://devpost.com/software/knok-lok) &nbsp; / &nbsp; [Read the firmware](https://github.com/DVeldhurthi/Knok_Lok/blob/main/Knok_Lok.ino)

<details>
<summary>How the timing check works</summary>

After three seconds without another knock, the firmware compares adjacent time intervals. It accepts ratios between 0.6 and 1.4, allowing some variation in the rhythm. This is a timing prototype, not a production access-control system.

</details>

## Experience

### Synthesis Hacks

<sub>Founder & Lead Organizer · May 2026</sub>

Organized a free, 12-hour student hackathon at Google Humboldt in Sunnyvale for 100+ participants. Led 15+ volunteers and coordinated sponsorship, outreach, and event logistics.

[Event & photos ↗](https://www.synthesishacks.com/) &nbsp; / &nbsp; [Website source](https://github.com/BernardCode/synthesis-hacks)

<details>
<summary>Sponsorship & event delivery</summary>

Secured $5,000+ in total sponsor support from 10+ companies, including credits and scholarships. The event included two student-led workshops, dedicated work rooms, food, and participant T-shirts. I also worked on the event website.

</details>

### Tinovation

<sub>Co-President · Cupertino High School computing club</sub>

Co-lead a club of approximately 25 active members. Give technical presentations and help students develop their projects; previously served as an officer.

### BOBTutor

<sub>Program Director & Coding Tutor · Completed</sub>

Led weekly coding sessions with a team of approximately five tutors. Taught Python, Scratch, and Java through the Africa and U.S. programs.

## Education

Cupertino High School · Senior

Additional coursework at De Anza College: Systems Design and Fundamentals of Digital Security. Completed AP Computer Science A.

Competitive programming: USACO Silver division.

[Back to skills ↑](#skills)
