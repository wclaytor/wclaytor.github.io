# CLAUDE.md - AI Assistant Context

> This file provides context for Claude (or other AI assistants) when working on the Pyrotechnica codebase.

## Project Overview

**Pyrotechnica** is a browser-based fireworks simulator and show designer. It allows users to launch fireworks, create sequences, choreograph performances, and export their creations as Markdown files.

### Core Philosophy

1. **Zero Dependencies** - Pure vanilla JavaScript, no frameworks, no build tools
2. **Single File Architecture** - Everything in `index.html` for maximum portability
3. **Offline First** - Works without internet, uses localStorage for persistence
4. **User Control** - No auto-launching; user triggers all fireworks manually

## File Structure

```
pyrotechnica/
├── index.html              # THE application (HTML + CSS + JS all-in-one)
├── README.md               # User documentation
├── PLAN.md                 # Project roadmap and task tracking
├── CLAUDE.md               # This file - AI assistant context
└── midnight-celebration.md # Example performance file
```

## Architecture

The application is structured as a single HTML file with embedded CSS and JavaScript. The JavaScript is organized into these logical sections (marked with comment headers):

```
CONFIGURATION          - Constants, firework types, palettes, SVG backgrounds
CANVAS SETUP          - Canvas initialization, resize handling
STATE MANAGEMENT      - Global state variables, localStorage load/save
AUDIO SYSTEM          - Web Audio API sound synthesis
VISUAL EFFECTS        - Screen flash, shake (contained to viewport)
STARS                 - Background star field
PARTICLES             - Core particle system with physics
ROCKETS               - Launch mechanics and trail rendering
EXPLOSIONS            - 10 explosion type implementations
CONFETTI              - Falling confetti system
SEQUENCES & PERFORMANCES - Playback logic, timeline execution
MARKDOWN IMPORT/EXPORT - Serialization to/from Markdown format
MAIN ANIMATION LOOP   - requestAnimationFrame render loop
UI RENDERING          - Dynamic UI generation
SEQUENCE EDITOR       - Modal for creating/editing sequences
PERFORMANCE EDITOR    - Modal for creating/editing performances
IMPORT/EXPORT         - File download/upload handling
NOTIFICATIONS         - Toast notification system
EVENT LISTENERS       - All UI event bindings
INITIALIZATION        - Startup code
```

## Key Data Structures

### Firework Types

```javascript
{ id: 0-9, name: string, icon: emoji, key: '1'-'0' }
```

### Palettes

```javascript
{ name: string, colors: [hex, hex, hex, hex] }
```

### Sequences

```javascript
{
  id: string,
  name: string,
  steps: [{ type: number, delay: ms, x: 0-100, palette: index }]
}
```

### Performances

```javascript
{
  id: string,
  name: string,
  duration: ms,
  events: [{ time: ms, type: 'sequence'|'firework'|'finale', ...params }]
}
```

### Particles

```javascript
{
  x,
    y,
    vx,
    vy, // Position and velocity
    color,
    rgb, // Color (hex and parsed RGB)
    size,
    gravity,
    drag, // Physics parameters
    life,
    maxLife, // Lifespan
    trailIdx,
    trailX,
    trailY; // Ring buffer for trail
}
```

## Important Patterns

### Viewport Container

All visual effects (shake, flash) are contained to the `.viewport` div, not the body. This prevents the header and control panel from shaking.

```javascript
function screenShake() {
  const viewport = document.getElementById("viewport");
  viewport.classList.remove("shake");
  viewport.offsetHeight; // Trigger reflow
  viewport.classList.add("shake");
}
```

### Ring Buffers for Trails

Trails use typed arrays with ring buffer indexing to avoid memory allocation:

```javascript
p.trailX[p.trailIdx] = p.x;
p.trailY[p.trailIdx] = p.y;
p.trailIdx = (p.trailIdx + 1) % TRAIL_LENGTH;
```

### SVG Backgrounds

Backgrounds are inline SVG strings, not external URLs. They're encoded as data URLs:

```javascript
const svgData = encodeURIComponent(bg.svg.trim());
bgLayer.style.backgroundImage = `url("data:image/svg+xml,${svgData}")`;
```

### Color Caching

Hex colors are parsed once and cached to avoid repeated parsing:

```javascript
const colorCache = new Map();
function getRGB(hex) {
  if (colorCache.has(hex)) return colorCache.get(hex);
  // ... parse and cache
}
```

## Common Tasks

### Adding a New Firework Type

1. Add to `FIREWORK_TYPES` array with unique id, name, icon, key
2. Add explosion logic in the `explode()` function's switch statement
3. Follow existing patterns for particle creation

### Adding a New Background

1. Add to `BACKGROUNDS` array with id, name, location, and svg property
2. SVG should use viewBox="0 0 1920 1080"
3. Use dark colors (#0a0a12, #08080f) for silhouettes
4. Include gradient definitions for sky

### Adding a New Palette

1. Add to `PALETTES` array with name and 4 hex colors
2. Colors should be harmonious and visible against dark backgrounds

### Modifying the Control Panel

1. Tab buttons are in `.tab-nav`
2. Tab content divs have id `tab-{name}` and class `tab-content`
3. Active state managed by adding/removing `.active` class

## Testing Approach

Since there's no test framework, verify changes manually:

1. **Fireworks**: Launch each type (keys 1-0), verify visual appearance
2. **Sequences**: Create, edit, play, delete a sequence
3. **Performances**: Create, edit, play, stop a performance
4. **Backgrounds**: Switch between all backgrounds
5. **Effects**: Trigger finale (F), verify shake doesn't move header
6. **Persistence**: Refresh page, verify sequences/performances persist
7. **Export/Import**: Export a performance, import it back

## Performance Considerations

- Particle limit: `MAX_PARTICLES = 1200`
- Rocket limit: `MAX_ROCKETS = 25`
- Confetti limit: `MAX_CONFETTI = 150`
- Trail length: `TRAIL_LENGTH = 6`
- Skip particles with alpha < 0.05
- Use typed arrays (Float32Array) for trails
- Cache gradients and parsed colors

## Known Gotchas

1. **Canvas height** accounts for header: `H = window.innerHeight - 50`
2. **Confetti disabled by default** - must be toggled on
3. **No auto-launch** - user must trigger all fireworks
4. **localStorage** can fill up with many sequences/performances
5. **SVG in data URLs** must be URI encoded

## Keyboard Shortcuts Reference

| Key    | Action                    |
| ------ | ------------------------- |
| 1-9, 0 | Launch firework types 0-9 |
| F      | Grand Finale              |
| S      | Toggle sound              |
| C      | Toggle confetti           |

## Markdown Performance Format

```markdown
# Performance Name

## Events

- MM:SS | sequence:Sequence Name
- MM:SS | firework:type | x:position | palette:name
- MM:SS | finale
```

## Future Development

See `PLAN.md` for the full roadmap. Key priorities:

1. Undo/Redo system for sequence editor
2. Custom color palette creator
3. Audio upload and sync
4. Drag-and-drop timeline

## Style Guidelines

### CSS

- Use CSS variables from `:root` for colors
- Follow existing naming: `.component-name`, `.component-name-element`
- Use `var(--accent-cyan)`, `var(--accent-magenta)`, `var(--accent-gold)`

### JavaScript

- Use `const` for constants, `let` for mutable state
- Document sections with comment block headers
- Keep functions focused and under 50 lines when possible
- Use template literals for HTML generation

### Commits

When describing changes for commit messages:

- Be specific: "Fix shake effect to only affect viewport"
- Group related changes: "Add confetti toggle with C keyboard shortcut"
- Reference issues if applicable

---

_Last updated: January 2025_
