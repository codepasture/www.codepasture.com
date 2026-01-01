# Code Pasture Website - Planning Document

## Overview
Marketing website for Code Pasture LLC, a software development consultancy.
- **Domain**: www.codepasture.com
- **Hosting**: Netlify (static)
- **Framework**: SvelteKit with adapter-static
- **Design**: Tech-Pastoral (dark theme, growth metaphors)

---

## Open Decisions

### CSS Approach

**Decision: CSS Variables + Svelte Scoped Styles**

- Global `tokens.css` with design tokens (colors, fonts, spacing)
- Svelte's built-in scoped `<style>` blocks for component styles
- No external CSS framework dependencies
- Clean markup, styles co-located with components

### Site Structure

```
/                   # Home (single page for now?)
/services           # Detailed services (future?)
/apps               # App portfolio (future?)
/about              # Extended about (future?)
/contact            # Contact form? (future?)
```

**Question**: Start with single-page or multi-page from the beginning?

---

## Content Inventory

### Hero
- Terminal line: `$ build --from scratch --deploy production`
- Headline: "Full-Stack Development" + **"0 → 1"** (large, green accent - key visual element)
- Tagline: Custom mobile apps and microservices, cultivated with 30 years of experience. From first commit to production.
- CTAs: Start a Project, Read the Blog

**Note**: The "0 → 1" visual is a signature element - emphasizes greenfield/from-scratch development specialty. Use `--color-accent` (green #7cb342) to match the logo and brand.

### Services
1. **Cross-Platform Apps** - Flutter, React Native, Expo
2. **Microservices** - .NET (C#/F#), Go, Node
3. **Cloud & DevOps** - Kubernetes, Docker, NGINX
4. **GenAI Development** - AI-assisted workflows, TDD, patterns

### Projects / Open Source

Showcase verifiable work across categories. Frame as "what I build and share" not client work.

#### Production Apps (iOS only for now, Android pending business dev account)
- DevHours - Time tracking (React Native) - https://apps.apple.com/us/app/devhours/id6756197386
- HayTracker - Inventory management (Flutter) - [coming soon]
- Propane Tracker - Tank monitoring (Flutter) - [coming soon]

#### Reference Architectures
- MFE Svelte Shell - Micro-frontend shell example - https://github.com/nathanfox/mfe-svelte-shell-example
- Rapid UI Prototype - GenAI rapid prototyping system (Nuxt) - https://github.com/nathanfox/rapid-ui-prototype-example

#### Developer Tools
- PulseURL - Lightweight URL traffic analytics for microservices (Go, .NET) - https://github.com/pulseurl
- k8s-vscode-remote-debug - Multi-language K8s debugging reference - https://github.com/nathanfox/k8s-vscode-remote-debug
- nginx-dev-gateway - Lightweight K8s API gateway - https://github.com/nathanfox/nginx-dev-gateway
- env-run - Environment management (Bash) - https://github.com/nathanfox/env-run
- env-run-pwsh - Environment management (PowerShell) - https://github.com/nathanfox/env-run-pwsh

#### Technical Writing
- nathanfox.net - 30+ articles on GenAI, architecture, DevOps, .NET/F#

### About
- 30 years experience
- Hobby farm in rural Michigan (chickens, goats, donkeys, turkeys, ducks)
- Focus on 0-to-1 development
- Tech stack list
- Link to nathanfox.net blog

### Contact
- Email: contact@codepasture.com
- Location: Michigan (remote work worldwide)

---

## Branding

### Logo Assets
Located in `static/`:
- `code-pasture-basic-logo.png` - Icon only (0→1 with sprouting leaf) - use for favicon, small icons
- `code-pasture-with-text-logo.png` - Full lockup with "Code Pasture" text - use for OG images, social sharing

### Logo Concept
The "0→1" with a sprouting leaf growing from the arrow:
- Represents greenfield/from-scratch development
- The leaf ties into "pasture" / growth metaphor
- Works at small sizes (favicon) and large (social)
- Single color (green #7cb342) on dark background (#0f1419)

### Usage
- **Favicon**: Crop basic logo to square, generate .ico
- **OG Image**: Use text version at 1200x630
- **Header**: Basic logo mark + "Code Pasture" text (or just text)

---

## Design Tokens (from tech-pastoral)

```css
--color-bg: #0f1419;
--color-bg-elevated: #1a2028;
--color-bg-hover: #232b35;
--color-border: #2d3640;
--color-text: #e8eaed;
--color-text-muted: #8b9298;
--color-accent: #7cb342;          /* Green - primary */
--color-accent-hover: #8bc34a;
--color-secondary: #4fc3f7;       /* Blue */
--color-orange: #ffb74d;
--color-purple: #b39ddb;
```

---

## Technical Requirements

### Must Have (v1)
- [ ] Single page with all sections
- [ ] Mobile responsive
- [ ] Fast load time (<1s)
- [ ] SEO basics (meta tags, OG images)
- [ ] Netlify deployment
- [ ] Contact email link

### Nice to Have (v1.1+)
- [ ] Contact form (Netlify Forms?)
- [ ] Separate pages for services
- [ ] App detail pages with screenshots
- [ ] Blog integration or feed from nathanfox.net
- [ ] Dark/light mode toggle
- [ ] Analytics (privacy-respecting)

---

## File Structure (Proposed)

```
www.codepasture.com/
├── src/
│   ├── lib/
│   │   ├── components/
│   │   │   ├── Header.svelte
│   │   │   ├── Hero.svelte
│   │   │   ├── Services.svelte
│   │   │   ├── Apps.svelte
│   │   │   ├── About.svelte
│   │   │   ├── Contact.svelte
│   │   │   └── Footer.svelte
│   │   └── styles/
│   │       └── global.css (or tokens.css)
│   ├── routes/
│   │   ├── +layout.svelte
│   │   └── +page.svelte
│   └── app.html
├── static/
│   ├── favicon.ico
│   └── og-image.png
├── svelte.config.js
├── netlify.toml
└── package.json
```

---

## Notes / Questions

1. ~~Do we want app store links for the mobile apps, or just descriptions for now?~~ **DevHours live on iOS, others coming soon**
5. Open source this repo as example of SvelteKit work? (Likely yes - adds to portfolio)
2. ~~Professional headshot or keep it text-only for about section?~~ **Text-only for now**
3. ~~Any testimonials or client logos to include?~~ **No - not available**
4. ~~Should the blog link go to nathanfox.net or embed/pull posts?~~ **Decision: Link to nathanfox.net directly**

---

## Next Steps

1. Decide on CSS approach
2. Scaffold SvelteKit project
3. Implement components from design
4. Deploy to Netlify
5. Iterate on content
