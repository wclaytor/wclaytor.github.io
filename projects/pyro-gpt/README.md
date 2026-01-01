# Pyrotechnica — Fireworks Simulator (single-file)

Open **pyrotechnica.html** in a browser.

## Controls

- **Click** canvas: set aim point (x + height) and fire the selected type
- **Shift+Click**: also record that shot as a cue
- **1–0**: firework hotkeys
- **Space**: play/pause timeline
- **R**: toggle recording
- **S**: toggle sound

## Performances as Markdown

In the app, the bottom panel includes a **Performance Markdown** editor.

Supported:
- YAML frontmatter (metadata)
- fenced JSON: ` ```json sequences ` and ` ```json timeline `

### Cue types

- `{ "t": 1234, "fire": { ... } }`
- `{ "t": 1234, "sequence": { "name": "fan_three" } }`
- `{ "t": 1234, "background": "Tokyo" }`

`fire` fields:
- `type`: chrysanthemum | peony | ring | willow | crackle | palm | comet | crossette | heart | mega
- `launcher`: a launcher name (varies by background)
- `height`: 0.12–0.88 (normalized)
- `palette`: one of the palette dropdown options
- `size`: roughly 0.6–2.2
- `seed`: integer for repeatability
- `x`: optional x override (0..1)

Generated: 2026-01-01 UTC
