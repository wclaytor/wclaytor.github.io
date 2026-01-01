This `PLAN.md` serves as the strategic roadmap for **Pyrotechnica**. It documents the evolution from a festive holiday display to a professional-grade simulation tool and outlines the engineering steps required to reach "Version 1.0."

# 🗺️ Pyrotechnica Project Plan

## 🎯 The Vision

To create the world's most accessible, high-performance, and human-readable pyrotechnic simulator. Pyrotechnica allows anyone to become a "Director" by bridging the gap between high-fidelity visual effects and simple, versionable Markdown scripting.

---

## 🕒 Evolution Timeline

### Stage 1: The Spark (NYE 2025)

- **Goal:** Create a high-performance festive loop.
- **Outcome:** Developed a procedural engine using HTML5 Canvas and `Float32Array` for particle trails.
- **Key Achievement:** 60fps performance with 1,000+ simultaneous particles.

### Stage 2: The Blueprint (Modularization)

- **Goal:** Move away from hard-coded loops to a controllable system.
- **Outcome:** Refactored the codebase into the `Pyrotechnica` Class.
- **Key Achievement:** Decoupled the rendering engine from the trigger logic.

### Stage 3: The Dashboard (Current State)

- **Goal:** Provide UI and Scripting capabilities.
- **Outcome:** Integrated the "Director's Dock" and a Markdown-based timeline parser.
- **Current State:** Functional launcher rack, background switching, and ability to Save/Load scripts as `.md` files.

---

## 📍 Current State of Affairs

We currently have a **Functional Prototype**.

- **Visuals:** 10 firework types and 10 color palettes.
- **Environment:** 7 iconic global locations.
- **UI:** Bottom-docked control panel with a pop-out script editor.
- **Logic:** Regex-based Markdown parsing for centisecond-accurate triggers.

---

## 🚀 The Path Forward: Roadmap to v1.0

### Phase 4: Visual Fidelity & Immersion

The next step is to make the environment react more realistically to the pyrotechnics.

- [ ] **Task 4.1: Ray-Traced Reflections:** Implement a "Reflection Canvas" for water-based scenes (Baltimore, Sydney) that mirrors explosion colors with a blur filter.
- [ ] **Task 4.2: Dynamic Sky Lighting:** Apply a global "Glow" filter to the background image that pulses in sync with the explosion brightness.
- [ ] **Task 4.3: High-Resolution Assets:** Replace placeholder Unsplash links with optimized, darkened SVG/WebP silhouettes for faster loading.

### Phase 5: Advanced Scripting & "The Director's Recorder"

Enhance the Markdown engine to support complex choreography.

- [ ] **Task 5.1: Recording Mode:** Add a "Record" button. When active, every manual click in the Launcher Rack is timestamped and appended to the Markdown script automatically.
- [ ] **Task 5.2: Macro Support:** Allow users to define "Sequences" (e.g., `[00:05] Sequence: Finale_Burst`) that trigger groups of 10+ rockets at once.
- [ ] **Task 5.3: Camera Control:** Implement "Shake" and "Flash" effects for heavy explosions to increase the sense of power.

### Phase 6: Performance & Distribution

Ensure the project is stable for public use.

- [ ] **Task 6.1: Web Worker Physics:** Move particle calculations to a Web Worker to prevent UI lag during "Grand Finales."
- [ ] **Task 6.2: Asset Preloading:** Build a splash screen that pre-loads city backgrounds to prevent flickering when switching locations.
- [ ] **Task 6.3: Mobile UI Polish:** Optimize the Dock for touch interfaces, ensuring the "Launchers" are easily tappable.

---

## 🛠️ Implementation Checklist (Immediate Next Steps)

| Task ID  | Description                                                   | Priority |
| -------- | ------------------------------------------------------------- | -------- |
| **P1.1** | Integrate the "Recording Mode" into the Script Editor.        | 🔴 High  |
| **P1.2** | Add "Reflections" logic for Sydney and Baltimore backgrounds. | 🟡 Med   |
| **P1.3** | Implement the "Mega-Crackle" audio tail for heavy explosions. | 🟡 Med   |
| **P2.1** | Create a "Community Pack" of 3 preset `.md` performances.     | 🟢 Low   |

---

## 📈 Success Metrics

1. **Zero Frame Drops:** Maintain 60fps during a 50-rocket finale.
2. **Human-Readable:** A user with no coding experience should be able to edit a script to change a "Heart" to a "Star."
3. **Portability:** The entire project remains a single, dependency-free HTML/JS file.

---

**"Pyrotechnica: Turning data into displays, and scripts into spectacles."**
