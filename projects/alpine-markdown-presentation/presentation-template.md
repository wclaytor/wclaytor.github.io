# Markdown Presentation Template Specification

## Overview

This document describes the Markdown format used by the Presentation Viewer PWA. Write your presentations in simple Markdown, and the viewer will automatically convert them into beautiful, interactive slides.

## Basic Structure

### Metadata (Optional)

Start your presentation with YAML-style metadata:

```markdown
---
title: Your Presentation Title
author: Your Name
date: 2025-11-04
theme: default
---
```

**Supported metadata fields:**
- `title`: Presentation title (used in PowerPoint export)
- `author`: Author name (used in PowerPoint export)
- `date`: Presentation date
- `theme`: Theme name (reserved for future use)

### Slide Separator

Separate slides using three or more hyphens on their own line:

```markdown
---
```

or

```markdown
-----
```

## Slide Content Syntax

### Headers

Headers define the hierarchy and styling of your content:

```markdown
# Main Title (Largest - typically for title slides)
## Section Header (Large)
### Subsection (Medium)
```

**Recommended usage:**
- Use `#` for slide titles
- Use `##` for main content headers
- Use `###` for sub-points

### Text Formatting

```markdown
**bold text**
*italic text*
***bold and italic***
~~strikethrough~~
`inline code`
```

### Lists

**Unordered lists:**
```markdown
- First item
- Second item
- Third item
  - Nested item
  - Another nested item
```

**Ordered lists:**
```markdown
1. First step
2. Second step
3. Third step
```

### Code Blocks

Use triple backticks for code blocks with optional syntax highlighting:

````markdown
```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}
```
````

Supported languages: javascript, python, java, html, css, bash, and many more.

### Quotes

Create blockquotes for emphasis or citations:

```markdown
> "The best presentations are simple and clear."
> — Albert Einstein
```

### Images

Include images using standard Markdown syntax:

```markdown
![Alt text](image-url.jpg)
![Company Logo](https://example.com/logo.png)
```

**Best practices:**
- Use descriptive alt text
- Optimize images for web (< 500KB)
- Use 16:9 aspect ratio images for full-slide backgrounds
- URLs can be absolute (https://...) or relative (./images/...)

### Links

```markdown
[Link text](https://example.com)
[Another presentation](./other-slides.md)
```

### Horizontal Rules

Create visual separators within a slide:

```markdown
---
```

Note: To avoid creating a new slide, ensure the `---` is not surrounded by blank lines on both sides.

### Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
```

## Slide Types and Templates

### Title Slide

```markdown
# Main Title 🎉

## Subtitle or tagline

**Author Name**  
*Date*

---
```

### Content Slide

```markdown
## Section Title

- Key point one
- Key point two
- Key point three

Supporting text goes here.

---
```

### Two-Column Layout (Simulated)

```markdown
## Features

**Column 1**
- Point A
- Point B

**Column 2**
- Point C
- Point D

---
```

### Image Slide

```markdown
## Visual Example

![Description](image-url.jpg)

Caption or explanation text

---
```

### Code Example Slide

````markdown
## Code Implementation

```python
def calculate_total(items):
    return sum(item.price for item in items)
```

This function calculates the total price of all items.

---
````

### Quote/Testimonial Slide

```markdown
## What People Say

> "This tool revolutionized how we do training sessions."

**— Sarah Johnson, CTO**

---
```

### List with Code Slide

```markdown
## Quick Tips

1. **Write clear headers**
   - Use descriptive titles
   - Keep them short

2. **Structure your content**
   ```markdown
   Use code blocks for examples
   ```

3. **Add visual elements**
   - Images tell stories
   - Charts show data

---
```

## Complete Example Template

```markdown
---
title: Training Session Template
author: Your Name
date: 2025-11-04
theme: default
---

# Training Session Title 🎓

## Session Overview
*Duration: 60 minutes*

---

## Agenda

1. Introduction (5 min)
2. Core Concepts (20 min)
3. Hands-on Exercise (25 min)
4. Q&A (10 min)

---

## Learning Objectives

By the end of this session, you will:

- ✅ Understand key concepts
- ✅ Apply practical techniques
- ✅ Build confidence in the topic

---

## Core Concept #1

### Definition

Clear explanation of the concept goes here.

**Key Points:**
- Important detail one
- Important detail two
- Important detail three

---

## Visual Example

![Diagram or screenshot](image-url.jpg)

*Figure 1: Description of what we're seeing*

---

## Code Example

```javascript
// Example implementation
function processData(input) {
  // Process the input
  return input.map(item => item * 2);
}
```

**What's happening:**
- Step 1: Receive input
- Step 2: Transform data
- Step 3: Return result

---

## Hands-on Exercise

### Task
Try implementing the following:

1. Open your development environment
2. Create a new file
3. Copy the example code
4. Modify it for your use case

**Time: 15 minutes**

---

## Common Pitfalls

⚠️ **Watch out for:**

- Mistake #1: Description
- Mistake #2: Description
- Mistake #3: Description

> "Prevention is better than debugging at 3 AM"

---

## Best Practices

✨ **Professional Tips:**

| Do This ✅ | Not This ❌ |
|-----------|------------|
| Write clear code | Use cryptic names |
| Add comments | Leave it unexplained |
| Test thoroughly | Hope it works |

---

## Resources

**Further Reading:**
- [Documentation](https://docs.example.com)
- [Tutorial](https://tutorial.example.com)
- [Community Forum](https://forum.example.com)

**Download:**
- [Code Examples](https://github.com/example/repo)

---

## Q&A Session

### Questions?

**Contact Information:**
- Email: your.email@example.com
- Slack: @yourname
- Teams: @yourname

---

# Thank You! 🙏

**Next Session:** Topic Name  
**Date:** Next week

*Don't forget to fill out the feedback form*

---
```

## Tips for Great Presentations

### Content Guidelines

1. **One main idea per slide**
   - Don't overcrowd slides
   - Use multiple slides if needed

2. **Use visuals effectively**
   - Images should enhance, not distract
   - Diagrams explain complex concepts
   - Screenshots show real examples

3. **Keep text concise**
   - Bullet points over paragraphs
   - Short sentences
   - Key words only

4. **Structure matters**
   - Start with overview
   - Build concepts progressively
   - End with summary/action items

### Technical Guidelines

1. **File organization**
   - Keep images in same directory or subdirectory
   - Use relative paths when possible
   - Name files clearly (no spaces)

2. **Image optimization**
   - Compress images before adding
   - Target 72-96 DPI for screen display
   - Maximum 1920px width recommended

3. **Code examples**
   - Keep code short (< 15 lines per slide)
   - Syntax highlighting automatically applied
   - Add comments for clarity

4. **Accessibility**
   - Use descriptive alt text for images
   - Ensure good contrast
   - Don't rely solely on color to convey meaning

## Keyboard Shortcuts

When viewing presentations:

- `→` or `Space` - Next slide
- `←` or `Backspace` - Previous slide
- `Home` - First slide
- `End` - Last slide
- `?` - Show/hide help
- `Esc` - Exit presentation

## Export Notes

When exporting to PowerPoint:

- Text formatting is preserved
- Images are embedded
- Code blocks become text boxes
- Lists maintain structure
- Themes match light mode colors

**Limitations:**
- Animations are not exported
- Custom CSS styling is simplified
- Tables have basic formatting
- Some Markdown features may render as plain text

## Troubleshooting

**Slide not separating correctly?**
- Ensure `---` is on its own line
- Check for blank lines before and after
- Use exactly 3 or more hyphens

**Images not displaying?**
- Verify image URL is accessible
- Check file extension is supported (.jpg, .png, .gif, .svg, .webp)
- Ensure proper Markdown syntax: `![alt](url)`

**Code block not formatting?**
- Use triple backticks (```)
- Optionally specify language after opening backticks
- Ensure closing backticks match

**Export issues?**
- Large presentations (50+ slides) may take time
- Complex content may simplify in PowerPoint
- Check browser console for errors

## Advanced Features (Coming Soon)

Future enhancements may include:

- Custom themes with CSS
- Speaker notes
- Slide transitions
- Animation triggers
- Embedded videos
- Interactive elements
- Presenter mode with timer
- Remote control via mobile device

---

## Need Help?

For questions, issues, or feature requests, please refer to the project documentation or contact your team's technical lead.

**Happy presenting! 🎉**
