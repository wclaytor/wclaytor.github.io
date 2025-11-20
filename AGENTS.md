# Agent Guidelines for wclaytor.github.io

## Mission
Transform this GitHub Pages portfolio into a world-class professional showcase that demonstrates technical excellence, modern design sensibility, and attention to detail.

## Agent Responsibilities

### 🔍 Analysis Agents
When analyzing the codebase or planning changes:

1. **Audit First**: Review existing code before making changes
   - Check current HTML structure and semantic markup
   - Review CSS organization and naming conventions
   - Identify unused styles or scripts
   - Look for accessibility issues
   - Check for performance bottlenecks

2. **Context Gathering**: Understand the full picture
   - Read related files (HTML, CSS, JS) together
   - Check for dependencies between components
   - Review existing patterns and conventions
   - Identify impact on other pages/projects

3. **Report Findings**: Provide actionable insights
   - List specific issues with file locations and line numbers
   - Prioritize by impact (critical, high, medium, low)
   - Suggest concrete improvements
   - Note any breaking changes

### 🎨 Design Agents
When working on visual design and user experience:

1. **Professional Aesthetics**: 
   - Clean, modern layouts with purposeful whitespace
   - Consistent color palette across all pages
   - Professional typography hierarchy
   - Subtle, tasteful animations and transitions

2. **Responsive Design**:
   - Mobile-first approach (320px to 4K)
   - Test all breakpoints
   - Touch-friendly interactions (44x44px minimum)
   - Optimize for various screen orientations

3. **Accessibility**:
   - WCAG 2.1 AA compliance minimum (AAA preferred)
   - High contrast ratios (4.5:1 for normal text, 3:1 for large)
   - Keyboard navigation and focus states
   - Screen reader compatibility
   - Alt text for all images

4. **Dark Mode**:
   - Respect `prefers-color-scheme`
   - Maintain readability in both themes
   - Test all interactive states

### 💻 Development Agents
When writing or modifying code:

1. **Code Quality**:
   - Follow established conventions in the codebase
   - Write clean, readable, self-documenting code
   - Add comments for complex logic only
   - Use semantic HTML5 elements
   - Implement progressive enhancement

2. **Performance**:
   - Optimize images (WebP with fallbacks)
   - Minimize CSS/JS (only in production)
   - Lazy load images and heavy content
   - Avoid render-blocking resources
   - Target Lighthouse score 90+ in all categories

3. **Testing**:
   - Validate HTML (W3C)
   - Check for console errors
   - Test in multiple browsers
   - Verify keyboard navigation
   - Run accessibility audits

4. **Standards**:
   - Modern ES6+ JavaScript
   - CSS Grid and Flexbox for layouts
   - Alpine.js for reactive components
   - No jQuery or legacy dependencies
   - Progressive Web App best practices

### 📝 Content Agents
When managing content or documentation:

1. **Structure**:
   - Use JSON for structured data (projects, skills, etc.)
   - Markdown for long-form content
   - Clear content hierarchy
   - SEO-optimized meta tags

2. **Maintainability**:
   - Clear update instructions in comments
   - Separate content from presentation
   - Version control friendly (no binary files)
   - Easy to add new projects/content

3. **SEO & Metadata**:
   - Descriptive titles and meta descriptions
   - Open Graph tags for social sharing
   - Structured data (Schema.org JSON-LD)
   - Semantic HTML for better indexing

### 🚀 Deployment Agents
When preparing for production:

1. **Pre-Deploy Checks**:
   - All links work (no 404s)
   - Images load and have alt text
   - No console errors or warnings
   - HTML/CSS validation passes
   - Lighthouse audits pass

2. **GitHub Pages**:
   - Test on feature branches first
   - Use relative paths for assets
   - Meaningful commit messages
   - Clean production files (no commented code)

3. **Monitoring**:
   - Check site after deployment
   - Verify all projects load correctly
   - Test on different devices/browsers
   - Monitor for broken links

## Workflow Guidelines

### Before Starting Work
1. **Read** the Copilot instructions (`.github/copilot-instructions.md`)
2. **Review** existing code and patterns
3. **Plan** the changes and potential impacts
4. **Confirm** alignment with project principles

### During Work
1. **Implement** changes incrementally
2. **Test** each change before moving on
3. **Document** complex decisions
4. **Maintain** consistent style

### After Completing Work
1. **Verify** all changes work as expected
2. **Check** for unintended side effects
3. **Update** documentation if needed
4. **Report** what was done and why

## Decision Framework

When making decisions, ask:

1. **Professional?** Does this make the site more credible and impressive?
2. **Modern?** Does this follow current best practices and trends?
3. **Accessible?** Can everyone use this, regardless of ability or device?
4. **Fast?** Does this maintain or improve performance?
5. **Maintainable?** Will this be easy to update in the future?

If the answer to any question is "no," reconsider the approach.

## Common Tasks

### Adding a New Project
1. Create folder: `/projects/[project-name]/`
2. Add `index.html` with consistent structure
3. Add `README.md` with project details
4. Update `/projects/index.html` with new entry
5. Update main site `README.md`
6. Add screenshots to `/assets/img/projects/`
7. Test all links and functionality

### Updating Design
1. Review current design system
2. Update CSS custom properties for theme changes
3. Test in light and dark modes
4. Verify responsive breakpoints
5. Check accessibility (contrast, focus states)
6. Run Lighthouse audit

### Improving Performance
1. Audit with Lighthouse
2. Optimize images (compress, use WebP)
3. Minify CSS/JS for production
4. Implement lazy loading
5. Add caching strategies
6. Re-audit to measure improvement

### Enhancing Accessibility
1. Run automated tests (axe, WAVE)
2. Test keyboard navigation
3. Check color contrast ratios
4. Verify ARIA labels
5. Test with screen reader
6. Fix identified issues

## Communication Guidelines

### When Reporting
- **Be specific**: Include file names, line numbers, exact issues
- **Be clear**: Use plain language, avoid jargon when possible
- **Be helpful**: Suggest solutions, not just problems
- **Be concise**: Get to the point quickly

### When Asking Questions
- **Clarify requirements**: If something is unclear, ask before implementing
- **Offer alternatives**: Present options with pros/cons
- **Explain tradeoffs**: Help the user make informed decisions
- **Provide examples**: Show what you mean with code snippets

### When Explaining Changes
- **State the goal**: What problem does this solve?
- **Describe the approach**: How does this work?
- **Note the impact**: What changes as a result?
- **Mention alternatives**: What else was considered?

## Quality Standards

### Must Have (Blockers)
- ✅ Valid HTML5
- ✅ No console errors
- ✅ All links work
- ✅ Mobile responsive
- ✅ Keyboard accessible
- ✅ Alt text on images

### Should Have (High Priority)
- ✅ Lighthouse score 90+
- ✅ WCAG AA compliance
- ✅ Dark mode support
- ✅ Fast loading (< 2s on 3G)
- ✅ Cross-browser compatible
- ✅ SEO optimized

### Nice to Have (Enhancements)
- ✅ WCAG AAA compliance
- ✅ Lighthouse score 95+
- ✅ Offline functionality (PWA)
- ✅ Advanced animations
- ✅ WebXR compatibility
- ✅ I18n support

## Anti-Patterns to Avoid

❌ **Don't**:
- Use `!important` in CSS (except for utilities)
- Add inline styles
- Use deprecated HTML elements
- Ignore accessibility
- Sacrifice performance for aesthetics
- Create unmaintainable complexity
- Leave commented-out code
- Use hardcoded values (use CSS variables)
- Skip testing
- Make assumptions (ask if unclear)

✅ **Do**:
- Use semantic HTML
- Leverage CSS Grid/Flexbox
- Implement progressive enhancement
- Prioritize accessibility
- Optimize for performance
- Keep code clean and maintainable
- Test thoroughly
- Document complex logic
- Follow established patterns
- Communicate clearly

## Resources

### Validation & Testing
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [WAVE Accessibility Tool](https://wave.webaim.org/)
- [Lighthouse (Chrome DevTools)](https://developers.google.com/web/tools/lighthouse)
- [axe DevTools](https://www.deque.com/axe/devtools/)

### Standards & Guidelines
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [web.dev](https://web.dev/)
- [Alpine.js Documentation](https://alpinejs.dev/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

### Design & UX
- [Material Design](https://material.io/design)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Inclusive Design Principles](https://inclusivedesignprinciples.org/)
- [Color Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

**Remember**: We're not just building a website—we're crafting a professional showcase that demonstrates mastery of modern web development. Every decision should reflect that standard.
