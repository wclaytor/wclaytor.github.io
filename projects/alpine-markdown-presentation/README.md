# Presentation Viewer PWA 📊

A beautiful, offline-capable Progressive Web App for creating and presenting Markdown-based slide decks. Perfect for remote training sessions, team meetings, and conference presentations.

[GitHub Pages Live Preview](https://wclaytor.github.io/alpine-markdown-presentation/index.html)

## Features ✨

- 📝 **Markdown-Based** - Write slides in simple, clean Markdown
- 🎨 **Beautiful Themes** - Built-in light/dark mode with system preference support
- ⌨️ **Keyboard Shortcuts** - Navigate presentations efficiently
- 📱 **Mobile-Friendly** - Touch swipe support and responsive design
- 🔌 **Offline-Capable** - Works without internet after first load
- 💾 **PowerPoint Export** - Generate .pptx files for sharing
- ⚡ **Lightning Fast** - Minimal bundle size (~160KB total)
- 🎯 **No Build Process** - Pure HTML/CSS/JS with CDN libraries
- 🔒 **Secure** - Runs entirely client-side, no server required

## Quick Start 🚀

### Option 1: Use Directly (Recommended)

1. Download all files to a folder
2. Open `presentation-viewer.html` in a modern web browser
3. Upload your Markdown file or try the sample presentation
4. Present!

### Option 2: Serve via HTTP Server

For full PWA features (installation, service worker), serve via HTTP:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (http-server)
npx http-server -p 8000

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000/presentation-viewer.html`

### Option 3: Deploy to Production

Deploy to any static hosting service:

**Netlify:**
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod
```

**Vercel:**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

**GitHub Pages:**
1. Create a repository
2. Push files to `main` branch
3. Enable GitHub Pages in repository settings

## Project Structure 📁

```
presentation-viewer/
├── presentation-viewer.html        # Main application
├── service-worker.js              # PWA offline support
├── sample-presentation.md         # Example presentation
├── markdown-template-specification.md  # Documentation
└── README.md                      # This file
```

## Creating Your Presentation 📝

### Basic Structure

Create a `.md` file with optional metadata and slides separated by `---`:

```markdown
---
title: My Presentation
author: Your Name
date: 2025-11-04
---

# First Slide 🎉

Your content here

---

## Second Slide

More content

---
```

### Supported Markdown Features

- **Headers:** `#`, `##`, `###`, etc.
- **Text Formatting:** `**bold**`, `*italic*`, `` `code` ``
- **Lists:** Ordered and unordered
- **Code Blocks:** With syntax highlighting
- **Images:** `![alt](url)`
- **Links:** `[text](url)`
- **Blockquotes:** `> quote`
- **Tables:** GitHub Flavored Markdown tables

See `markdown-template-specification.md` for complete documentation and templates.

## Keyboard Shortcuts ⌨️

| Key | Action |
|-----|--------|
| `→` or `Space` | Next slide |
| `←` or `Backspace` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| `?` | Toggle help |
| `Esc` | Exit presentation |

## Touch Gestures 👆

- **Swipe Left** - Next slide
- **Swipe Right** - Previous slide

## Technical Stack 🛠️

### Core Technologies

- **Alpine.js** (15KB) - Reactive framework for UI
- **Marked.js** (7.87KB) - Markdown parsing
- **PptxGenJS** (127KB) - PowerPoint export (lazy-loaded)
- **Native CSS** - Theme system with custom properties
- **Service Workers** - Offline functionality

### Why This Stack?

**Total bundle size: ~150KB gzipped** (excluding lazy-loaded PowerPoint export)

- ✅ No build process required
- ✅ Works fully offline after first load
- ✅ All libraries via CDN
- ✅ Progressive enhancement
- ✅ Fast performance on mobile
- ✅ Easy to customize and extend

## Browser Support 🌐

### Full Support
- Chrome 90+
- Edge 90+
- Firefox 88+
- Safari 14+

### Partial Support (no offline features)
- Older browsers may lack service worker support
- Install functionality requires modern browser

## Customization 🎨

### Change Theme Colors

Edit the CSS variables in `presentation-viewer.html`:

```css
:root {
  --accent: var(--light, #4f46e5) var(--dark, #818cf8);
  --bg-primary: var(--light, #ffffff) var(--dark, #0f172a);
  /* ... more variables ... */
}
```

### Add Custom Fonts

Add font imports in the `<head>`:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

<style>
  :root {
    --font-sans: 'Inter', sans-serif;
  }
</style>
```

### Modify Slide Transitions

Update the CSS transition properties:

```css
.slide {
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1), 
              opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## PowerPoint Export 💾

The export feature converts your Markdown presentation to PowerPoint format:

### Features
- Text formatting preserved
- Images embedded
- Lists maintained
- Code blocks converted to text boxes
- One slide per Markdown section

### Limitations
- No animations in exported file
- Complex layouts simplified
- Custom CSS not exported
- Tables have basic formatting

### Optimization Tips

To improve export quality:
- Keep text concise
- Use simple formatting
- Optimize images before adding
- Test export regularly

## Performance Optimization ⚡

### Current Performance

Typical Lighthouse scores:
- **Performance:** 95+
- **Accessibility:** 95+
- **Best Practices:** 95+
- **SEO:** 90+
- **PWA:** ✅

### Optimization Tips

1. **Optimize Images**
   ```bash
   # Use ImageOptim, TinyPNG, or similar
   # Target: < 200KB per image
   ```

2. **Lazy Load PptxGenJS**
   - Already implemented
   - Only loads when user clicks "Export"

3. **Compress Resources**
   ```bash
   # Enable gzip/brotli on your server
   # Most static hosts do this automatically
   ```

4. **Use CDN for Libraries**
   - Already implemented
   - Libraries cached by service worker

## Troubleshooting 🔧

### Service Worker Not Working

**Problem:** Offline functionality not available

**Solutions:**
- Serve over HTTPS or localhost
- Check browser console for errors
- Clear browser cache and reload
- Verify service worker registration in DevTools

### Slides Not Separating

**Problem:** Multiple slides show as one

**Solutions:**
- Ensure `---` is on its own line
- Add blank lines before and after `---`
- Use exactly 3 or more hyphens

### Images Not Loading

**Problem:** Images don't display in slides

**Solutions:**
- Check image URLs are accessible
- Verify correct Markdown syntax: `![alt](url)`
- Ensure images are served over HTTPS if app is HTTPS
- Check browser console for CORS errors

### Export Not Working

**Problem:** PowerPoint export fails or hangs

**Solutions:**
- Wait for PptxGenJS to load (first export may be slow)
- Check browser console for errors
- Reduce presentation size (try <50 slides)
- Ensure images are accessible
- Try in different browser

### Theme Not Saving

**Problem:** Theme preference resets on reload

**Solutions:**
- Enable localStorage in browser
- Check for browser privacy modes
- Verify no errors in console

## Security Considerations 🔒

### Input Sanitization

The app uses Marked.js which sanitizes HTML by default. However:

- ⚠️ Do not load Markdown from untrusted sources
- ⚠️ User-uploaded files are processed client-side only
- ✅ No server-side processing required
- ✅ All data stays on user's device

### Privacy

- ✅ No tracking or analytics by default
- ✅ No data sent to external servers
- ✅ Presentations stored locally only
- ✅ Export happens client-side

## Contributing 🤝

This is a reference implementation. Feel free to:

- Fork and customize
- Add features
- Improve documentation
- Share improvements with your team

## License

This project is provided as-is for educational and commercial use. Modify freely for your organization's needs.

## Credits & Acknowledgments

### Libraries Used

- [Alpine.js](https://alpinejs.dev) by Caleb Porzio
- [Marked.js](https://marked.js.org) by Christopher Jeffrey
- [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) by Brent Ely

### Inspiration

- PWA best practices from [web.dev](https://web.dev)
- Design patterns from [Reveal.js](https://revealjs.com)
- Alpine.js patterns from community examples

## Support & Resources 📚

### Documentation
- Full Markdown specification: See `markdown-template-specification.md`
- Sample presentation: See `sample-presentation.md`

### Learning Resources
- [Alpine.js Documentation](https://alpinejs.dev)
- [Progressive Web Apps Guide](https://web.dev/progressive-web-apps/)
- [Markdown Guide](https://www.markdownguide.org)

### Community
- Share with your team
- Customize for your needs
- Build amazing presentations!

## Roadmap 🗺️

Potential future enhancements:

- [ ] Custom theme builder UI
- [ ] Speaker notes view
- [ ] Timer and progress indicator
- [ ] Presentation recording
- [ ] Collaborative editing
- [ ] Animation support
- [ ] Video embedding
- [ ] Interactive polls
- [ ] Multiple layout templates
- [ ] PDF export option

## Version History 📋

### Version 1.0.0 (Current)
- Initial release
- Markdown parsing with Marked.js
- Alpine.js reactive UI
- Service worker for offline
- PowerPoint export
- Theme system with dark mode
- Keyboard shortcuts
- Touch gesture support
- Full PWA compliance

---

## Getting Help 💬

For questions, issues, or customization help:

1. Check the `markdown-template-specification.md` file
2. Review the sample presentation
3. Inspect browser console for errors
4. Consult your team's technical lead

---

**Built with ❤️ for amazing presentations**

Happy presenting! 🎉
