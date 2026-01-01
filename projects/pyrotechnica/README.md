# Pyrotechnica 🎆

An interactive fireworks simulator with stunning visual effects, custom sequences, and choreographed performances.

## Features (Phase 1 - Core Engine)

- **10 Firework Types**: Spherical, Chrysanthemum, Ring, Willow, Double Burst, Crossette, Heart, Star, Spiral, Mega Crackle
- **11 Color Palettes**: Gold, Ruby, Sapphire, Emerald, Amethyst, Silver, Copper, Pink, Cyan, White, Rainbow
- **Interactive Launch**: Click anywhere on the canvas to launch fireworks
- **Keyboard Controls**: Quick access to all features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Smooth Animations**: 60fps particle physics with trails and sparkle effects

## Controls

| Input         | Action                                                    |
| ------------- | --------------------------------------------------------- |
| **Click/Tap** | Launch firework at position                               |
| **Space**     | Launch random firework                                    |
| **1-0**       | Select firework type (1=Spherical, 2=Chrysanthemum, etc.) |
| **F**         | Toggle fullscreen                                         |

## Roadmap

- [x] **Step 1**: Core architecture - Modular firework engine
- [ ] **Step 2**: Control panel UI - Launcher buttons, color picker, position controls
- [ ] **Step 3**: Background system - Landmark silhouettes
- [ ] **Step 4**: Sequence engine - Timed firework sequences
- [ ] **Step 5**: Performance timeline - Chain sequences with play controls
- [ ] **Step 6**: Markdown persistence - Save/load performances

## Technical Details

- **Framework**: Alpine.js for reactive UI
- **Rendering**: HTML5 Canvas with requestAnimationFrame
- **Physics**: Custom particle system with gravity, air resistance, and trails
- **Architecture**: Modular classes (FireworkEngine, Particle, Rocket)

## Development

Based on the NYE 2025 fireworks display, refactored into a full-featured simulator.

---

Part of [wclaytor.github.io](https://wclaytor.github.io)
