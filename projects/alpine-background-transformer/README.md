# Alpine Background Transformer

An interactive CSS gradient editor for experimenting with the portfolio's unified background theming system. Create, preview, and export gradient presets in real-time.

🎨 **[Launch App](https://wclaytor.github.io/projects/alpine-background-transformer/index.html)**

---

## Overview

This tool demonstrates how a single background image can be transformed into completely different visual experiences using CSS gradient overlays. It's the same technique used throughout the portfolio site to create visual cohesion while varying mood across sections.

## Features

### 🎛️ Interactive Controls
- **Gradient Angle** - Rotate from 0° to 360° with quick presets (vertical, horizontal, diagonal)
- **Three Color Stops** - Full control over start, middle, and end colors
- **Opacity Sliders** - Fine-tune transparency for each color stop
- **Position Control** - Adjust where the middle stop appears (10%-90%)

### 📚 Site Presets
Pre-loaded with the actual gradient settings from the portfolio:

| Preset | Description | Angle | Colors |
|--------|-------------|-------|--------|
| **Masthead** | Dark hero section | 180° | Black vertical fade |
| **About** | Teal diagonal sweep | 135° | Teal → Blue → Black |
| **Projects** | Light white overlay | 180° | White with subtle gray |
| **Contact** | Dark with blue tint | 180° | Black with blue undertone |

### 💾 Custom Presets
- Save your own gradient combinations
- Presets persist in localStorage
- Load, delete, and manage saved presets

### 💻 CSS Export
- Live-generated CSS code
- Syntax highlighting for readability
- One-click copy to clipboard
- Ready to paste into your stylesheet

## Usage

1. **Start with a Preset** - Click any site preset to see how it transforms the background
2. **Experiment** - Adjust angle, colors, and opacity to create your own look
3. **Preview** - See changes in real-time on the preview panel
4. **Copy** - Click "Copy" to grab the CSS code
5. **Save** - Optionally save your creation as a custom preset

## Technology

- **Alpine.js** - Reactive UI with minimal footprint
- **Pure CSS** - No external CSS framework
- **localStorage** - Persist custom presets
- **CSS Linear Gradients** - The core technique being demonstrated

## The Technique

The key insight is that CSS allows layering a `linear-gradient` on top of an image:

```css
background: 
  linear-gradient(
    135deg,
    rgba(100, 161, 157, 0.85) 0%,
    rgba(40, 80, 100, 0.75) 50%,
    rgba(0, 0, 0, 0.95) 100%
  ),
  url("../assets/img/bg-masthead.jpg");
```

By varying the:
- **Angle** (direction of the gradient)
- **Colors** (including transparency)
- **Stop positions** (where colors blend)

You can create dramatically different appearances from the same source image.

## Benefits of This Approach

✅ **Performance** - One image download, multiple visual treatments  
✅ **Consistency** - Unified visual language across sections  
✅ **Flexibility** - Easy to adjust without new assets  
✅ **File Size** - No need for multiple background images  

## Screenshots

The app features a split-panel layout:
- **Left**: Live preview with the background and overlay
- **Right**: Controls for angle, colors, and presets

## Related

- [Portfolio Homepage](../../index.html) - See the gradients in action
- [Main README](../../README.md) - Full documentation of the theming system

---

Built with 💚 using [Alpine.js](https://alpinejs.dev/)