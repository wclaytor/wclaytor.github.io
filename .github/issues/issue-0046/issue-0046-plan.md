# Plan: Transform NYE Fireworks into Pyrotechnica Simulator

Transform the existing NYE 2025 fireworks display into a full-featured fireworks simulator with control panel, background selection, sequence creation, and Markdown-based performance files.

### Steps

1. **Refactor core architecture** in index.html — Extract firework engine into modular components: `FireworkEngine`, `SequencePlayer`, `PerformanceRunner`, `BackgroundManager`, and `UIController`

2. **Add control panel UI** — Create a collapsible bottom panel with:

   - 10 launcher buttons (one per firework type: Spherical, Chrysanthemum, Ring, Willow, Double Burst, Crossette, Heart, Star, Spiral, Mega Crackle)
   - Color palette selector
   - Position controls (launch X coordinate)
   - Launch height slider

3. **Implement background system** — Add `BackgroundManager` with:

   - Gradient-only night sky (default, current)
   - Landmark silhouettes as CSS/SVG overlays (Baltimore Harbor, Brooklyn Bridge, Mount Rushmore, Paris/Eiffel Tower, London/Big Ben, Sydney Opera House, Tokyo skyline)
   - Background selector in UI

4. **Build sequence engine** — Create `Sequence` data structure:

   ```markdown
   # Sequence: Grand Opening

   - 0ms: spherical @ 50%, gold
   - 500ms: chrysanthemum @ 30%, ruby
   - 500ms: chrysanthemum @ 70%, sapphire
   - 1200ms: heart @ 50%, pink
   ```

5. **Add performance timeline** — Create `Performance` that chains sequences with:

   - Named sequences (Grand Opening, Climax, Finale)
   - Timeline UI showing sequence blocks
   - Play/pause/stop controls
   - Demo performance included

6. **Implement Markdown persistence** — Parse/generate Markdown files:
   - YAML frontmatter for metadata (name, author, duration)
   - Sequence definitions as lists
   - Performance structure with timing
   - Browser download/upload for files

### Further Considerations

1. **Alpine.js integration?** — Current code is vanilla JS; should we add Alpine.js for reactive UI per the project guidelines? Recommend: Add Alpine.js for control panel reactivity

2. **Landmark images** — Use SVG silhouettes (lightweight) or placeholder gradients initially? Recommend: Start with CSS gradient silhouettes, add SVGs later

3. **Persistence scope** — LocalStorage for quick saves, or Markdown-only? Recommend: Both (localStorage for autosave, Markdown for sharing/versioning)
