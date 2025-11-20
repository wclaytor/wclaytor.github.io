# GitHub Copilot Instructions for wclaytor.github.io

## Project Overview
Personal portfolio and project showcase website hosted on GitHub Pages. This site serves as a professional representation of skills, experience, and projects, targeting potential employers, collaborators, and the tech community.

## Core Principles

### Professional First
- **Clean, professional design** that instills confidence in technical abilities
- **Error-free**: Zero console errors, no broken links, perfect accessibility scores
- **Fast loading**: Optimize for performance (target: Lighthouse score 90+)
- **Secure**: Use HTTPS, implement proper CSP headers where possible, sanitize inputs

### Modern & Fresh Design
- **Contemporary aesthetics**: Clean typography, purposeful whitespace, subtle animations
- **Current web standards**: HTML5 semantic markup, CSS Grid/Flexbox, ES6+ JavaScript
- **Design trends**: Glassmorphism, neumorphism, or minimalist approaches as appropriate
- **Dark mode support**: Respect user preferences with `prefers-color-scheme`
- **Smooth interactions**: Subtle transitions, micro-interactions, tasteful hover effects

### Universal Compatibility
- **Cross-browser**: Test in Chrome, Firefox, Safari, Edge (latest 2 versions)
- **Mobile-first**: Responsive design from 320px to 4K displays
- **Touch-friendly**: Adequate tap targets (min 44x44px), swipe gestures where appropriate
- **Keyboard accessible**: Full keyboard navigation, visible focus states
- **Screen readers**: Proper ARIA labels, semantic HTML, alt text for images
- **VR/AR ready**: Consider WebXR compatibility for future enhancements

### Easy Maintenance
- **Modular architecture**: Separate concerns (HTML structure, CSS styling, JS behavior)
- **Reusable components**: DRY principle, component-based patterns with Alpine.js
- **Clear documentation**: Inline comments for complex logic, README updates
- **Consistent patterns**: Follow established conventions in the codebase
- **Simple content updates**: Markdown where possible, JSON data files for structured content

## Technical Stack

### Current Technologies
- **Alpine.js**: Lightweight reactive framework for interactive UI components
- **Tailwind CSS / Bootstrap**: Utility-first CSS (migrate to Tailwind for consistency)
- **Vanilla JavaScript**: ES6+ for enhanced functionality
- **PWA Features**: Service workers for offline capability and performance
- **p5.js / Three.js**: Creative coding and 3D visualizations in projects

### Standards & Best Practices
- **HTML5**: Semantic elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`)
- **CSS3**: Modern features (Grid, Flexbox, Custom Properties, Container Queries)
- **Accessibility**: WCAG 2.1 AA compliance minimum
- **SEO**: Proper meta tags, Open Graph, structured data (Schema.org)
- **Performance**: Lazy loading, code splitting, optimized assets
- **Progressive Enhancement**: Core content accessible without JavaScript

## Code Style Guidelines

### HTML
- Use semantic HTML5 elements
- Include proper meta tags (viewport, description, keywords, Open Graph)
- Add structured data for SEO (JSON-LD)
- Ensure all images have meaningful alt text
- Use BEM or utility classes for styling

### CSS
- Mobile-first responsive design
- Use CSS custom properties for theming
- Prefer Grid/Flexbox over floats
- Implement smooth transitions (200-300ms)
- Avoid `!important` unless absolutely necessary
- Keep specificity low, prefer classes over IDs for styling

### JavaScript
- Use ES6+ features (const/let, arrow functions, destructuring, modules)
- Prefer Alpine.js directives for reactive UI
- Keep vanilla JS for utilities and enhancements
- Handle errors gracefully
- Comment complex logic
- Use async/await for asynchronous operations

### File Organization
```
/
├── index.html              # Homepage
├── css/
│   └── styles.css         # Global styles
├── js/
│   └── scripts.js         # Global scripts
├── assets/
│   ├── img/               # Images, icons, logos
│   └── data/              # JSON data files (future)
├── projects/
│   ├── index.html         # Projects gallery/listing
│   └── [project-name]/    # Individual project folders
└── .github/
    └── copilot-instructions.md
```

## Content Management

### Resume/About
- Store resume content in structured format (JSON or Markdown)
- Make it easy to update skills, experience, education
- Include downloadable PDF version
- Link to LinkedIn, GitHub, other professional profiles

### Projects
- Each project in its own folder under `/projects/`
- Consistent structure: `index.html`, `README.md`, assets
- Project metadata: title, description, tech stack, links (demo, repo)
- Screenshots or video demos
- Live demo links where applicable

### Easy Updates
- Use data files (JSON) for repetitive content (projects list, skills, etc.)
- Markdown for long-form content when possible
- Clear comments indicating where to update content
- Version control friendly (no minified files in repo)

## Design Guidelines

### Color Palette
- Professional, modern color scheme
- High contrast for readability (WCAG AA minimum, AAA preferred)
- Consistent use of brand colors
- Dark mode variant for all colors

### Typography
- System font stack or fast-loading web fonts (preload if custom)
- Clear hierarchy (headings, body, captions)
- Readable line length (45-75 characters)
- Appropriate line height (1.5-1.8 for body text)

### Layout
- Consistent spacing scale (e.g., 4px, 8px, 16px, 24px, 32px, 48px, 64px)
- Maximum content width for readability (typically 1200-1400px)
- Balanced whitespace
- Clear visual hierarchy

### Components
- Buttons: Clear states (default, hover, active, disabled, focus)
- Cards: Consistent padding, shadow, hover effects
- Navigation: Clear, accessible, mobile-friendly
- Forms: Proper labels, validation, error states
- Loading states: Skeletons or spinners for async content

## Testing & Quality Assurance

### Pre-Commit Checks
- Validate HTML (W3C Validator)
- Lint CSS and JavaScript
- Check for broken links
- Verify all images load and have alt text
- Test responsive breakpoints

### Browser Testing
- Chrome/Edge (Chromium)
- Firefox
- Safari (desktop and iOS)
- Test on actual devices when possible

### Performance
- Run Lighthouse audits (target 90+ in all categories)
- Optimize images (WebP with fallbacks)
- Minify CSS/JS for production
- Use CDN for libraries when appropriate
- Implement lazy loading for images and heavy content

### Accessibility
- Keyboard navigation works throughout
- Screen reader testing (NVDA, JAWS, VoiceOver)
- Color contrast meets WCAG standards
- Focus indicators visible
- No accessibility errors in automated tools (axe, WAVE)

## GitHub Pages Specifics

### Deployment
- Push to `main` branch for automatic deployment
- Test on feature branches before merging
- Use meaningful commit messages
- Keep production files clean (no commented-out code)

### URLs & Paths
- Use relative paths for assets: `./assets/img/photo.jpg`
- Link to projects: `/projects/project-name/`
- Base URL: `https://wclaytor.github.io/`

### Limitations
- Static hosting only (no server-side processing)
- Jekyll is available but not required
- Custom domains supported (add CNAME file)

## AI Collaboration Guidelines

### When Suggesting Changes
- Explain the rationale (why this improves the site)
- Consider impact on existing functionality
- Ensure changes align with project principles
- Provide complete, working code (not pseudo-code)

### File Modifications
- Always review existing code before modifying
- Maintain consistent style with existing code
- Update related files if needed (e.g., CSS when changing HTML structure)
- Test changes don't break other features

### New Features
- Start with user stories or use cases
- Consider mobile experience from the start
- Ensure accessibility from the beginning
- Think about content management (how to update easily)

### Communication
- Be clear and concise
- Ask for clarification when requirements are ambiguous
- Suggest alternatives when appropriate
- Provide context for technical decisions

## Current Priorities

1. **Content Audit**: Review existing pages, identify missing content
2. **Design Refresh**: Modernize visual design while maintaining professionalism
3. **Consistency**: Ensure all projects follow similar patterns
4. **Performance**: Optimize loading speed and Lighthouse scores
5. **Accessibility**: Achieve WCAG 2.1 AA compliance across all pages
6. **Content System**: Implement easy-to-update content management
7. **Resume Section**: Add comprehensive resume/about page
8. **Documentation**: Update README with development instructions

## Success Metrics

- **Professional**: Would you hire this person based on this site?
- **Modern**: Does it look current and follow best practices?
- **Fast**: Loads in under 2 seconds on 3G
- **Accessible**: Works for all users, all devices, all abilities
- **Maintainable**: Can content be updated in under 5 minutes?

---

**Remember**: Every change should ask "Does this make the site more professional, more modern, more accessible, or easier to maintain?" If not, reconsider the approach.
