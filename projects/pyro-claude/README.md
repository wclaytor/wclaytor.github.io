# 🎆 Pyrotechnica - Fireworks Simulator

**A professional fireworks design and performance tool built with pure vanilla JavaScript and HTML5 Canvas.**

Create stunning fireworks displays, design custom sequences, choreograph performances to a timeline, and export your creations as Markdown files for easy editing and version control.

![Pyrotechnica](https://img.shields.io/badge/🎆-Pyrotechnica-ff00aa?style=for-the-badge&labelColor=000)
![Vanilla JS](https://img.shields.io/badge/Vanilla-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas-E34F26?style=flat-square&logo=html5&logoColor=white)
![No Dependencies](https://img.shields.io/badge/Dependencies-Zero-success?style=flat-square)

---

## ✨ Features

### 🚀 Firework Launchers

- **10 Explosion Types**: Spherical, Chrysanthemum, Ring, Willow, Double Burst, Crossette, Heart, Star, Spiral, and Mega Crackle
- **10 Color Palettes**: Gold, Ruby, Sapphire, Emerald, Amethyst, Silver, Sunset, Azure, Rose, and Lime
- **Individual Triggering**: Launch any firework type instantly with one click or keyboard shortcut

### 🌃 Scenic Backgrounds

- Night Sky (default animated starfield)
- Baltimore Inner Harbor
- Brooklyn Bridge, New York
- Mount Rushmore, South Dakota
- Eiffel Tower, Paris
- Tower Bridge, London
- Sydney Opera House
- Tokyo Tower

### 📋 Sequences

- Create named sequences of multiple fireworks
- Control timing delays between launches
- Set precise horizontal positions (10-90%)
- Choose specific color palettes per firework
- Play sequences with one click
- Edit and delete existing sequences

### 🎭 Performances

- Choreograph sequences and individual fireworks on a visual timeline
- Create complex shows with precise timing
- Include automatic finale triggers
- Visual timeline with playback marker
- Play/Stop controls

### 💾 Markdown Import/Export

- Save performances as human-readable Markdown files
- Easy editing in any text editor
- Version control friendly (Git compatible)
- Import performances from Markdown
- Share your creations with others

---

## 🎮 Controls

### Keyboard Shortcuts

| Key      | Action                        |
| -------- | ----------------------------- |
| `1-9, 0` | Launch specific firework type |
| `F`      | Trigger Grand Finale          |
| `S`      | Toggle sound on/off           |

### Mouse Controls

| Action                | Result                                    |
| --------------------- | ----------------------------------------- |
| Click canvas          | Launch random firework at cursor position |
| Click launcher button | Launch specific firework type             |

---

## 📝 Performance Script Format

Performances are saved as Markdown files with a simple, readable format:

```markdown
# My Performance

## Events

- 0:00 | sequence:Golden Cascade
- 0:05 | firework:heart | x:30
- 0:05 | firework:heart | x:70
- 0:10 | firework:star | x:50 | palette:gold
- 0:15 | sequence:Rainbow Wave
- 0:25 | finale
```

### Event Types

| Format                                            | Description                         |
| ------------------------------------------------- | ----------------------------------- |
| `MM:SS \| sequence:Name`                          | Play a named sequence               |
| `MM:SS \| firework:type`                          | Launch single firework at center    |
| `MM:SS \| firework:type \| x:position`            | Launch at specific position (0-100) |
| `MM:SS \| firework:type \| x:pos \| palette:name` | With specific palette               |
| `MM:SS \| finale`                                 | Trigger grand finale                |

### Firework Types

`spherical`, `chrysanthemum`, `ring`, `willow`, `double`, `crossette`, `heart`, `star`, `spiral`, `crackle`

### Palette Names

`gold`, `ruby`, `sapphire`, `emerald`, `amethyst`, `silver`, `sunset`, `azure`, `rose`, `lime`

---

## 🚀 Quick Start

1. Open `index.html` in any modern browser
2. Click the launcher buttons to fire individual fireworks
3. Press number keys `1-0` for quick launches
4. Click anywhere on the canvas to launch at that position
5. Press `F` for the Grand Finale!

### Creating a Sequence

1. Go to the **Sequences** tab
2. Click **+ New Sequence**
3. Enter a name for your sequence
4. Select a firework type from the grid
5. Set the delay (milliseconds before this firework)
6. Set the X position (10-90%)
7. Choose a palette (or Random)
8. Click **Add** to add the step
9. Repeat for more fireworks
10. Click **Save Sequence**

### Creating a Performance

1. Go to the **Performance** tab
2. Click **+ New Performance**
3. Enter a name
4. Write your performance script in Markdown format
5. Click **Save Performance**
6. Select your performance from the dropdown
7. Click **▶ Play** to watch the show!

---

## 💾 Data Storage

Pyrotechnica automatically saves your sequences and performances to browser localStorage. Your creations persist between sessions.

### Exporting

- **Sequences**: Click "Export All" in the Sequences tab to download all sequences as Markdown
- **Performances**: Select a performance and click "Export" to download as Markdown

### Importing

- Click "Import" and paste Markdown content or upload a `.md` file
- Imported data is merged with existing sequences/performances

---

## 🎆 Default Sequences

Pyrotechnica comes with four pre-built sequences:

| Sequence           | Description                                            |
| ------------------ | ------------------------------------------------------ |
| **Golden Cascade** | Three willow fireworks followed by a spherical burst   |
| **Heart Burst**    | Triple heart explosions                                |
| **Rainbow Wave**   | Five spherical bursts across the sky in rainbow colors |
| **Star Spiral**    | Star and spiral combination                            |

---

## 🎬 Demo Performance

Click the **🎬 DEMO** button to play the built-in "New Year Spectacular" - a 45-second choreographed show demonstrating all the features.

---

## 🔬 Technical Details

### Architecture

- Single HTML file with embedded CSS and JavaScript
- HTML5 Canvas for all firework rendering
- Web Audio API for synthesized sound effects
- CSS backgrounds for scenic locations
- localStorage for data persistence

### Performance Optimizations

- Object pooling with typed arrays
- Ring buffer trails
- Particle limits with early culling
- Cached color parsing
- Gradient caching

### Particle System

| Property | Range         | Effect                    |
| -------- | ------------- | ------------------------- |
| Gravity  | 0.02-0.12     | Floaty to droopy          |
| Drag     | 0.98-0.992    | Quick stop to long travel |
| Life     | 40-140 frames | Duration of visibility    |

---

## 🌐 Browser Support

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 11+
- ✅ Edge 79+
- ✅ Mobile browsers

---

## 📜 License

MIT License - Feel free to use, modify, and share!

---

## 🙏 Credits

Based on the NYE 2025 Fireworks Spectacular, enhanced with:

- Professional control panel interface
- Sequence creation system
- Performance timeline editor
- Markdown import/export
- Scenic backgrounds
- Futuristic UI design

---

<p align="center">
  <strong>🎆 Create Your Own Fireworks Show! 🎆</strong><br>
  <em>Design, choreograph, and share stunning pyrotechnic displays</em>
</p>
