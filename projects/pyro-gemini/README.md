# 🎆 Pyrotechnica: The Director's Fireworks Simulator

**Pyrotechnica** is a high-performance, modular fireworks simulation suite built with Vanilla JavaScript and HTML5 Canvas. Originally conceived as a New Year's 2025 celebration, it has evolved into a creative "Director’s Suite" that allows users to design, script, and perform professional-grade pyrotechnic displays.

---

## 🌟 Key Features

### 🎮 The Launcher Rack (Control Dock)

A persistent, blurred-glass UI at the bottom of the screen provides manual control over the simulation:

- **Individual Triggers:** Launch any of the 10 custom firework types (Spherical, ❤️ Heart, ⭐ Star, Willow, Mega Crackle, etc.) with a single click.
- **Palette Management:** Switch between 10 hand-crafted color palettes including _Ruby_, _Emerald_, _Sunset_, and _Sapphire_.
- **Master Triggers:** Dedicated buttons for "Grand Finales" and global sound toggles.

### 🌆 Global Scenery System

Transform your display by switching between high-contrast silhouettes of iconic global locations:

- **Sydney** (Opera House)
- **Tokyo** (Tokyo Tower)
- **Paris** (Eiffel Tower)
- **London** (London Eye)
- **Baltimore** (Inner Harbor)
- **Brooklyn** (Brooklyn Bridge)
- **Mount Rushmore**

### 📝 Markdown Performance Scripting

Pyrotechnica introduces a unique **Markdown-based sequencing engine**. You can "code" your performance in a simple, human-readable format that allows for easy versioning and sharing.

**Example Script (`finale.md`):**

```markdown
# Grand Finale Performance

- [00:00:10] Launch: Heart | Palette: Ruby
- [00:00:50] Launch: Star | Palette: Gold
- [00:01:20] Launch: Willow | Palette: Cyan
- [00:02:00] Sequence: Big_Boom (15x Random)
```

---

## ⚙️ Technical Architecture

### 1. The Pyrotechnica Engine

The core engine uses a modular Class-based architecture. It manages:

- **Physics Engine:** Real-time calculation of gravity (0.02 to 0.12), air resistance (drag), and particle lifespan.
- **Memory Optimization:** Uses `Float32Array` buffers for particle trails to ensure a smooth 60fps experience even with thousands of particles on screen.
- **Synthesized Audio:** Uses the Web Audio API to generate procedural "launch," "boom," and "crackle" sounds, avoiding the need for external MP3 files.

### 2. The Director Module

The `Director` class parses Markdown files and maps timestamps to the internal simulation clock.

- **Time-coded Events:** Each line in a performance file is converted into a high-precision event scheduled via `requestAnimationFrame`.
- **File I/O:** Leverages the Browser's Blob and FileReader APIs to allow users to **Save**, **Load**, and **Edit** their performances directly from their local machine.

---

## 🚀 Getting Started

1. **Open the Simulator:** Open the `index.html` file in any modern web browser.
2. **Manual Mode:** Use the buttons in the **Launcher Rack** to fire individual rockets.
3. **Scripting Mode:** \* Click **"Edit Script"** to open the Markdown editor.

- Write your sequence using the `[MM:SS:CC]` timestamp format.
- Press **"Play"** to watch the "Director" execute your performance.

4. **Exporting:** Click **"Save Markdown"** to download your performance as a `.md` file for future use.

---

## 🛠️ Development & Customization

### Adding New Palettes

In the `Pyrotechnica` class, you can extend the `palettes` array:

```javascript
this.palettes.push(["#COLOR1", "#COLOR2", "#COLOR3"]);
```

### Adjusting Physics

The physics constants are located in the `render()` loop and `launch()` method. You can modify `r.vy` for launch height or `p.gravity` for particle "weight."

---

## 📜 License

**MIT License** — Feel free to use Pyrotechnica for your own events, streams, or projects.

---

<p align="center">
<strong>🎇 Become the Director of the Night Sky. 🎇</strong>

<em>Built with precision and passion for the pyrotechnic arts.</em>

</p>
