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

## Leveraging Skills

This project has specialized Claude skills available in `.claude/skills/` that provide expert-level knowledge for specific domains. Agents should use these skills to enhance their work quality and efficiency.

### Available Skills

1. **frontend-design** 🎨
   - Creates production-grade interfaces with high design quality
   - Avoids generic AI aesthetics, produces creative polished designs
   - **Use for**: Building web components, pages, layouts, modernizing designs

2. **canvas-design** 🖼️
   - Creates beautiful visual art in PNG and PDF formats
   - **Use for**: Posters, graphics, diagrams, illustrations, static design pieces

3. **theme-factory** 🎨
   - 10 pre-set themes plus custom theme generation
   - **Use for**: Applying consistent styling to HTML pages, slides, docs, reports

4. **webapp-testing** 🧪
   - Playwright-based testing toolkit
   - **Use for**: Testing local apps, verifying functionality, debugging UI, capturing screenshots

5. **pdf** 📄
   - Comprehensive PDF manipulation (extract, create, merge, split, forms)
   - **Use for**: Resume generation, documentation handling

6. **brand-guidelines** 🏢
   - Applies Anthropic's official brand colors and typography
   - **Use for**: Branded content or artifacts

7. **skill-creator** 🛠️
   - Guide for creating new specialized skills
   - **Use for**: Extending capabilities with custom skills

### When Agents Should Use Skills

#### 🔍 Analysis Agents
- Use **webapp-testing** to verify functionality during audits
- Use **frontend-design** to evaluate design quality and modern patterns

#### 🎨 Design Agents
- **Primary tool**: Use **frontend-design** for all UI/UX work
- Use **theme-factory** to apply consistent styling
- Use **canvas-design** for graphics and visual assets
- Combine **frontend-design** + **theme-factory** for complete designs

#### 💻 Development Agents
- Use **frontend-design** when building new features
- Use **webapp-testing** before committing changes
- Use **theme-factory** for consistent styling implementation

#### 📝 Content Agents
- Use **pdf** for resume and document generation
- Use **canvas-design** for creating visual content
- Use **brand-guidelines** when creating branded materials

#### 🚀 Deployment Agents
- **Critical**: Use **webapp-testing** in pre-deploy checks
- Verify all functionality with automated tests
- Capture screenshots for documentation

### Skill Best Practices for Agents

1. **Read First**: Always read the skill's SKILL.md file before using
   ```
   Location: .claude/skills/[skill-name]/SKILL.md
   ```

2. **Match Task to Skill**: Choose the right specialist
   - Web pages → `frontend-design`
   - Static graphics → `canvas-design`
   - Testing → `webapp-testing`
   - Documents → `pdf`

3. **Combine Skills**: Use multiple skills for comprehensive solutions
   - Example: `frontend-design` + `theme-factory` + `webapp-testing`
   - Design → Style → Test → Deploy

4. **Trust Skill Expertise**: Skills contain specialized knowledge
   - Follow their recommendations
   - Let them guide implementation details
   - They know domain best practices

5. **Document Usage**: Note which skills were used in reports
   - Helps maintain consistency
   - Useful for future reference
   - Shows expertise was applied

### Skill Integration in Workflows

**Adding a New Project** (Updated):
1. Create folder structure
2. **Use `frontend-design`** to build modern, professional interface
3. **Use `theme-factory`** to apply consistent styling
4. Add content and documentation
5. **Use `webapp-testing`** to verify functionality
6. Add to projects index
7. Test and deploy

**Updating Design** (Updated):
1. Review current design
2. **Use `frontend-design`** for modern patterns and aesthetics
3. **Use `theme-factory`** for consistent color/typography
4. Implement changes
5. **Use `webapp-testing`** to verify across devices
6. Check accessibility and performance

**Improving Performance** (Updated):
1. Audit with Lighthouse
2. Optimize assets
3. **Use `webapp-testing`** to measure improvements
4. Implement optimizations
5. Re-test and validate

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
