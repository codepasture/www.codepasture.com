# Code Pasture Website Design Exploration

## Quick Start

```bash
cd designs
python3 serve.py
```

Then open:
- **Professional**: http://localhost:8080/style-professional/
- **Technical**: http://localhost:8080/style-technical/
- **Pastoral**: http://localhost:8080/style-pastoral/

## Design Directions

### 1. Professional/Corporate (`style-professional/`)
- **Vibe**: Clean, minimal, trustworthy
- **Colors**: Navy blue (#1e3a5f) + white + subtle blue accent
- **Typography**: System sans-serif, tight letter-spacing
- **Best for**: Enterprise clients, B2B, establishing credibility

### 2. Technical/Developer-focused (`style-technical/`)
- **Vibe**: Dark theme, terminal aesthetic, GitHub-inspired
- **Colors**: Dark (#0d1117) + green/blue/purple accents
- **Typography**: Monospace accents, code blocks
- **Best for**: Developer audience, tech-savvy clients, OSS community

### 3. Pastoral/Warm (`style-pastoral/`)
- **Vibe**: Farm-meets-tech, friendly, approachable
- **Colors**: Forest green (#2d5016) + golden accent (#d4a056) + warm cream
- **Typography**: Georgia serif for headings, warm and inviting
- **Best for**: Small business clients, personal brand, unique positioning

## Website Structure (All Designs)

```
Home (index)
├── Hero - Value proposition + CTA
├── Services
│   ├── Mobile Development (Flutter, React Native)
│   ├── Microservice Architecture (.NET, Go, Node)
│   ├── GenAI-Assisted Development
│   └── Cloud Infrastructure (K8s, Docker)
├── Apps Portfolio
│   ├── HayTracker
│   ├── Propane Tracker
│   └── (future apps)
├── About
│   ├── Experience (30+ years)
│   ├── Expertise list
│   └── Blog link (nathanfox.net)
└── Contact
    └── Email CTA
```

## Content Strategy

### Primary CTA
**Hire me for custom software development**
- All designs funnel to contact via email
- Could add: Calendly link, contact form, or project questionnaire

### Key Messaging
1. **0-to-1 development** - Greenfield projects from concept to production
2. **Cross-platform expertise** - Mobile apps that work everywhere
3. **Quality-first** - 100% test coverage, domain-driven design
4. **GenAI-powered** - Modern AI-assisted development practices
5. **30+ years experience** - Deep expertise, not just following trends

### App Portfolio Expansion
Current: HayTracker, Propane Tracker
Mentioned in code: DevHours (time tracking)
Future: Add apps as they're published

## Next Steps

1. **Choose a design direction** (or mix elements)
2. **Add real content**:
   - Professional headshot or avatar
   - Actual app screenshots/icons
   - Specific case studies if available
3. **Build with framework** (Nuxt recommended for familiarity)
4. **Add pages**:
   - Individual service pages with more detail
   - Individual app pages with screenshots, features, download links
   - Blog integration or links to nathanfox.net
5. **Deploy to Netlify**
