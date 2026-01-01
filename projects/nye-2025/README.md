# 🎆 New Year 2025 Fireworks Spectacular

**A mesmerizing, fully interactive fireworks display built with pure vanilla JavaScript and HTML5 Canvas.**

No frameworks. No dependencies. No build tools. Just open and enjoy.

![Fireworks Preview](https://img.shields.io/badge/✨-Happy_New_Year_2025-gold?style=for-the-badge&labelColor=black)
![Vanilla JS](https://img.shields.io/badge/Vanilla-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas-E34F26?style=flat-square&logo=html5&logoColor=white)
![No Dependencies](https://img.shields.io/badge/Dependencies-Zero-success?style=flat-square)

---

## 🌟 Our New Year's Wishes

As the clock strikes midnight and the sky fills with light, we want to share our warmest wishes with you:

> **✨ Cheers to New Beginnings ✨**

May 2025 bring you:

- 🎯 **Clarity** in your goals and the courage to chase them
- 💪 **Strength** to overcome every obstacle in your path
- 🤝 **Connection** with the people who matter most
- 🌱 **Growth** in ways you never imagined possible
- 😊 **Joy** in the little moments that make life beautiful
- 🚀 **Success** in all your endeavors, big and small

Whether you're watching these fireworks alone in quiet reflection or surrounded by friends and family, know that this display was crafted with love and care for moments exactly like this one.

**Here's to new adventures, fresh starts, and a spectacular year ahead!**

_— From our screens to yours, Happy New Year 2025! 🥂_

---

## 🎮 Features

- **Instant Action** — Fireworks launch immediately when the page loads
- **10 Explosion Types** — Spherical, Chrysanthemum, Ring, Willow, Double Burst, Crossette, ❤️ Heart, ⭐ Star, 🌀 Spiral, 💥 Mega Crackle
- **10 Color Palettes** — Gold, Ruby, Sapphire, Emerald, Amethyst, Silver, Sunset, Azure, Rose, Lime
- **Particle Physics** — Gravity, drag, and realistic motion
- **Glowing Trails** — Rockets and particles leave luminous trails
- **Twinkling Starfield** — Hundreds of animated background stars
- **Falling Confetti** — Celebratory confetti with realistic physics
- **Click Interaction** — Click anywhere to launch bonus fireworks
- **🔊 Sound Effects** — Synthesized launch whooshes, booms, and crackles (Press `S`)
- **💥 Screen Flash** — Dynamic screen flash on explosions
- **🌊 Screen Shake** — Subtle shake on big explosions
- **🎊 Grand Finale** — Press `F` for an epic 10-second fireworks barrage!
- **Fully Responsive** — Works on any screen size
- **Zero Dependencies** — Pure vanilla JavaScript, no libraries needed
- **Performance Optimized** — Smooth 60fps with capped particles and efficient rendering

### 🎹 Controls

| Key     | Action                                            |
| ------- | ------------------------------------------------- |
| `F`     | Trigger Grand Finale (10 seconds of epic mayhem!) |
| `S`     | Toggle sound effects on/off                       |
| `Click` | Launch fireworks at cursor position               |

---

## 🚀 Quick Start

1. Download `index.html` (or rename `fireworks.html` to `index.html`)
2. Open in any modern browser
3. Enjoy the show! 🎆

For GitHub Pages deployment:

```bash
git add index.html README.md
git commit -m "🎆 Happy New Year 2025!"
git push origin main
```

Your fireworks will be live at `https://yourusername.github.io/your-repo/`

---

## 🔬 Technical Deep Dive

### Architecture Overview

The entire display runs on a single HTML5 Canvas element, orchestrated by a requestAnimationFrame loop running at 60fps. The architecture follows a classic game-loop pattern:

```
┌─────────────────────────────────────────────────────────────┐
│                      ANIMATION LOOP                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │  Clear  │→ │ Update  │→ │  Draw   │→ │  Next   │        │
│  │  Frame  │  │ Physics │  │ Objects │  │  Frame  │        │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### The Rendering Pipeline

Each frame follows this sequence:

1. **Sky Gradient** — Draw the night sky background
2. **Stars** — Render twinkling star field
3. **Confetti** — Update and draw falling confetti
4. **Rockets** — Update physics and draw ascending rockets
5. **Particles** — Update physics and draw explosion particles

### Particle System Deep Dive

The heart of the fireworks is the particle system. Each particle is a simple object with physics properties:

```javascript
{
  x, y,           // Position
  vx, vy,         // Velocity
  gravity,        // Downward acceleration (0.02 - 0.12)
  drag,           // Air resistance (0.98 - 0.992)
  life,           // Remaining frames
  maxLife,        // Initial lifespan
  size,           // Particle radius
  color,          // Hex color string
  trail: []       // Array of previous positions
}
```

#### Physics Update (per frame)

```javascript
// Apply gravity
vy += gravity;

// Apply air resistance
vx *= drag;
vy *= drag;

// Update position
x += vx;
y += vy;

// Age the particle
life -= 1;
```

The magic is in tuning these constants:

| Property  | Value Range     | Effect                               |
| --------- | --------------- | ------------------------------------ |
| `gravity` | 0.02 - 0.12     | Low = floaty (willow), High = droopy |
| `drag`    | 0.98 - 0.992    | Low = quick stop, High = long travel |
| `life`    | 40 - 140 frames | Duration of visibility               |

### Explosion Types Explained

#### 1. Spherical Burst

The classic firework. Particles are distributed evenly around a circle:

```javascript
for (let i = 0; i < count; i++) {
  const angle = (i / count) * Math.PI * 2; // Even distribution
  const speed = 3 + Math.random() * 4; // Varied speeds
  // Launch particle at this angle
}
```

#### 2. Chrysanthemum

Multiple concentric rings create a dense, layered effect:

```javascript
for (let layer = 0; layer < 4; layer++) {
  const speed = 2 + layer * 1.5; // Each layer faster
  // Alternate colors between layers
}
```

#### 3. Ring

Particles are launched horizontally with reduced vertical velocity:

```javascript
const vx = Math.cos(angle) * speed;
const vy = Math.sin(angle) * speed * 0.3; // Flatten the Y
```

#### 4. Willow

High drag + high gravity = graceful drooping trails:

```javascript
gravity: 0.12,  // Strong pull down
drag: 0.992,    // But slow decay = long trails
life: 120+      // Extra long lifespan
```

#### 5. Double Burst

Two spherical bursts at different speeds create depth:

```javascript
// Inner burst: speed 3-4
// Outer burst: speed 5.5-6.5
// Different colors for each
```

#### 6. Crossette

Particles grouped into arms radiating from center:

```javascript
const arms = 6;
for (let arm = 0; arm < arms; arm++) {
  const baseAngle = (arm / arms) * Math.PI * 2;
  // Particles spread slightly around baseAngle
}
```

### Glow Effect Technique

The signature glow effect uses radial gradients:

```javascript
const gradient = ctx.createRadialGradient(x, y, 0, x, y, size * 3);
gradient.addColorStop(0, rgba(color, alpha * 0.8)); // Bright center
gradient.addColorStop(0.5, rgba(color, alpha * 0.3)); // Mid fade
gradient.addColorStop(1, rgba(color, 0)); // Transparent edge
```

This creates a soft, luminous appearance without expensive blur filters.

### Trail Rendering

Each particle stores its recent positions:

```javascript
particle.trail.push({ x: particle.x, y: particle.y });
if (particle.trail.length > 8) particle.trail.shift();
```

Trails are drawn with decreasing size and opacity:

```javascript
for (let j = 0; j < trail.length; j++) {
  const progress = j / trail.length;
  const trailAlpha = progress * alpha * 0.5;
  const trailSize = size * progress * 0.6;
  // Draw circle at trail[j] position
}
```

### Rocket Mechanics

Rockets simulate upward thrust fighting gravity:

```javascript
// Initial velocity: strong upward
vy = -(10 + Math.random() * 5);

// Each frame: gravity slows it down
vy += 0.12;

// Explode when reaching target OR velocity near zero
if (y <= targetY || vy >= -1) {
  explode(rocket);
}
```

### Performance Optimizations

1. **Object Pooling Lite** — Dead particles are spliced from arrays, keeping memory bounded
2. **Single Canvas** — All rendering on one canvas eliminates compositing overhead
3. **Batch Operations** — Stars drawn in a single loop without state changes
4. **Conditional Trails** — Trail length varies by particle type (sparkles = 5, comets = 15)
5. **Early Exit** — Particles removed immediately when life ≤ 0

### Color Management

Colors are stored as hex strings and converted to RGBA on demand:

```javascript
function hexToRGBA(hex, alpha) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}
```

Each palette is curated for visual harmony:

```javascript
const palettes = [
  ["#FFD700", "#FFA500", "#FF8C00", "#FFEA00"], // Gold family
  ["#FF1744", "#FF5252", "#FF4081", "#F50057"], // Red/Pink family
  // ... 8 more palettes
];
```

### Responsive Design

The canvas automatically resizes to fill the viewport:

```javascript
function resize() {
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
  createStars(); // Regenerate stars for new dimensions
}

window.addEventListener("resize", resize);
```

### The Animation Loop

The core loop using requestAnimationFrame:

```javascript
function animate(time) {
  // 1. Clear & draw sky
  // 2. Draw stars
  // 3. Auto-launch rockets (time-based)
  // 4. Update all physics
  // 5. Draw all objects

  requestAnimationFrame(animate); // Schedule next frame
}

requestAnimationFrame(animate); // Start the loop
```

### Launch Timing

Rockets auto-launch at randomized intervals:

```javascript
if (time - lastLaunch > launchInterval) {
  launchRocket();
  lastLaunch = time;
  launchInterval = 150 + Math.random() * 400; // 150-550ms
}
```

This creates organic variation while maintaining constant spectacle.

---

## ⚡ Performance Optimizations

The fireworks display has been optimized for smooth 60fps performance even during extended viewing sessions.

### Memory Management

**Object Limits** — Hard caps prevent unbounded growth:
| Object Type | Max Count |
|-------------|-----------|
| Particles | 800 |
| Rockets | 15 |
| Confetti | 100 |
| Stars | 200 |

**Pre-allocated Buffers** — Trail data uses `Float32Array` ring buffers instead of dynamic arrays:

```javascript
// Before: Created new objects every frame (GC pressure)
p.trail.push({ x: p.x, y: p.y });
if (p.trail.length > 8) p.trail.shift();

// After: Fixed-size typed arrays with ring buffer index
p.trailX[p.trailIdx] = p.x;
p.trailY[p.trailIdx] = p.y;
p.trailIdx = (p.trailIdx + 1) % TRAIL_LENGTH;
```

**Color Caching** — Hex colors are parsed once and cached:

```javascript
const colorCache = new Map();
function getRGB(hex) {
  if (colorCache.has(hex)) return colorCache.get(hex);
  const rgb = { r, g, b }; // Parse once
  colorCache.set(hex, rgb);
  return rgb;
}
```

### Rendering Optimizations

**Canvas Context** — Alpha disabled for faster compositing:

```javascript
ctx.getContext("2d", { alpha: false });
```

**Cached Gradients** — Sky gradient created once, not every frame:

```javascript
// Before: New gradient every frame
function animate(time) {
  const skyGradient = ctx.createLinearGradient(0, 0, 0, H); // Expensive!
  ...
}

// After: Cache and reuse
if (!skyGradientCache) {
  skyGradientCache = ctx.createLinearGradient(0, 0, 0, H);
}
```

**Simplified Particle Rendering** — Replaced expensive radial gradients with `globalAlpha`:

```javascript
// Before: Gradient per particle (very expensive)
const gradient = ctx.createRadialGradient(x, y, 0, x, y, size * 3);
gradient.addColorStop(0, rgba(color, alpha * 0.8));
gradient.addColorStop(0.5, rgba(color, alpha * 0.3));
gradient.addColorStop(1, rgba(color, 0));

// After: Simple alpha blending (much faster)
ctx.globalAlpha = alpha * 0.4;
ctx.fillStyle = color;
ctx.beginPath();
ctx.arc(x, y, size * 2.5, 0, Math.PI * 2);
ctx.fill();
```

### Early Culling

- Skip particles with alpha < 0.05 (nearly invisible)
- Remove off-screen particles immediately
- Batch star rendering with single `fillStyle` change

### Reduced Particle Counts

| Element             | Before    | After     |
| ------------------- | --------- | --------- |
| Explosion particles | 150-250   | 80-120    |
| Flash particles     | 10        | 5         |
| Extra sparkles      | 30        | 15        |
| Trail length        | 8         | 5         |
| Launch interval     | 150-550ms | 250-750ms |

These optimizations maintain visual appeal while ensuring smooth performance on a wide range of devices.

---

## 📊 By The Numbers

| Metric                   | Value                             |
| ------------------------ | --------------------------------- |
| Lines of Code            | ~700                              |
| File Size                | ~22 KB                            |
| Dependencies             | 0                                 |
| Canvases                 | 1                                 |
| Particle Types           | 4 (normal, comet, sparkle, flash) |
| Explosion Types          | 10 (including special shapes!)    |
| Color Palettes           | 10                                |
| Max Concurrent Particles | 1000 (optimized)                  |
| Max Rockets              | 20                                |
| Max Confetti             | 120                               |
| Target Frame Rate        | 60 fps                            |
| Sound Effects            | 3 (launch, boom, crackle)         |
| Awesomeness Level        | SO AWESOME!!!                     |

---

## 🎨 Customization

### Change Colors

Edit the `palettes` array to use your own color schemes:

```javascript
const palettes = [
  ["#YOUR", "#CUSTOM", "#COLORS", "#HERE"],
  // ...
];
```

### Adjust Intensity

Modify launch timing for more or fewer fireworks:

```javascript
launchInterval = 150 + Math.random() * 400; // Decrease for more fireworks
```

### Change Particle Count

In the `explode()` function:

```javascript
const count = 150 + Math.floor(Math.random() * 100); // 150-250 particles
```

---

## 🌐 Browser Support

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 11+
- ✅ Edge 79+
- ✅ Mobile browsers (iOS Safari, Chrome for Android)

---

## 📜 License

MIT License — Feel free to use, modify, and share!

---

## 🙏 Acknowledgments

Built with love for everyone celebrating the new year, wherever you may be.

Special thanks to:

- The HTML5 Canvas API for making this possible
- Everyone who believes pure vanilla JavaScript can still create magic
- You, for taking the time to read this far!

---

<p align="center">
  <strong>🎆 Happy New Year 2025! 🎆</strong><br>
  <em>May your year be as bright as these fireworks!</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made_with-❤️-red?style=for-the-badge" alt="Made with love">
</p>
