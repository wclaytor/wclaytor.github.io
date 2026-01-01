# 🎆 Pyrotechnica - Project Plan

> **Version:** 1.0  
> **Last Updated:** January 2025  
> **Status:** Phase 1 Complete ✅

---

## 📋 Table of Contents

1. [Vision](#-vision)
2. [Project History](#-project-history)
3. [Current State](#-current-state)
4. [Roadmap](#-roadmap)
5. [Phase 2 Tasks](#-phase-2-tasks)
6. [Phase 3 Tasks](#-phase-3-tasks)
7. [Future Considerations](#-future-considerations)
8. [Technical Debt](#-technical-debt)

---

## 🎯 Vision

**Pyrotechnica** is a professional-grade fireworks simulator and show designer that empowers users to:

- **Create** stunning firework displays with intuitive controls
- **Design** complex sequences and choreograph them to a timeline
- **Perform** live shows with real-time triggering
- **Share** their creations through portable Markdown files
- **Experience** fireworks against beautiful real-world backdrops

### Core Principles

1. **Zero Dependencies** - Pure vanilla JavaScript, works anywhere
2. **Instant Gratification** - Open and enjoy immediately
3. **Professional Power** - Deep enough for serious show design
4. **Portable Creations** - Markdown files that humans can read and edit
5. **Beautiful by Default** - Stunning visuals out of the box

### Target Users

- **Casual Users** - Click and enjoy beautiful fireworks
- **Hobbyists** - Create and save custom sequences
- **Designers** - Choreograph full performances with precise timing
- **Educators** - Demonstrate physics and particle systems
- **Developers** - Learn from and extend the codebase

---

## 📜 Project History

### Stage 1: Foundation (NYE 2025 Fireworks)

The project began as a New Year's 2025 celebration display featuring:

- ✅ HTML5 Canvas rendering engine
- ✅ 10 firework explosion types
- ✅ 10 color palettes
- ✅ Particle physics system (gravity, drag, trails)
- ✅ Rocket launch mechanics
- ✅ Synthesized sound effects (Web Audio API)
- ✅ Screen flash and shake effects
- ✅ Falling confetti system
- ✅ Twinkling star background
- ✅ Grand Finale mode
- ✅ Click-to-launch interactivity
- ✅ Keyboard controls (F for finale, S for sound)
- ✅ Performance optimizations (typed arrays, object pooling)

### Stage 2: Pyrotechnica v1.0 (Current)

Transformed the celebration into a full simulator:

- ✅ Professional control panel UI (collapsible, tabbed interface)
- ✅ Individual firework launcher buttons with keyboard shortcuts
- ✅ 8 scenic background options (world landmarks)
- ✅ Sequence creation and management system
- ✅ Performance timeline editor with visual playback
- ✅ Markdown import/export for all creations
- ✅ localStorage persistence
- ✅ Demo performance ("New Year Spectacular")
- ✅ 4 pre-built sequences
- ✅ Real-time timeline display
- ✅ Futuristic cyberpunk UI design
- ✅ Comprehensive documentation

---

## 📊 Current State

### What Works Well

| Feature                | Status       | Notes                           |
| ---------------------- | ------------ | ------------------------------- |
| Firework rendering     | ✅ Excellent | Smooth 60fps, beautiful effects |
| All 10 explosion types | ✅ Complete  | Heart, star, spiral, etc.       |
| Sound effects          | ✅ Complete  | Launch, boom, crackle           |
| Background switching   | ✅ Complete  | 8 locations available           |
| Sequence creation      | ✅ Complete  | Full CRUD operations            |
| Performance playback   | ✅ Complete  | Timeline with marker            |
| Markdown export        | ✅ Complete  | Human-readable format           |
| Data persistence       | ✅ Complete  | localStorage                    |
| Keyboard shortcuts     | ✅ Complete  | 1-0, F, S keys                  |
| Mobile responsive      | ⚠️ Basic     | Works but not optimized         |

### Known Limitations

1. **Timeline Editor** - Text-based only, no drag-and-drop
2. **No Music Sync** - Performances can't sync to audio
3. **No Undo/Redo** - Destructive edits in sequence builder
4. **Single User** - No sharing or collaboration features
5. **No Custom Colors** - Limited to 10 preset palettes
6. **No Video Export** - Can't save as video file
7. **Background Images** - External URLs only, no upload

### File Structure

```
pyrotechnica/
├── index.html              # Main application (all-in-one)
├── README.md               # User documentation
├── PLAN.md                 # This file
└── midnight-celebration.md # Example performance file
```

---

## 🗺️ Roadmap

```
Phase 1 (v1.0) ████████████████████ COMPLETE
   └── Core simulator with sequences and performances

Phase 2 (v1.5) ░░░░░░░░░░░░░░░░░░░░ PLANNED
   └── Enhanced editor, music sync, more effects

Phase 3 (v2.0) ░░░░░░░░░░░░░░░░░░░░ FUTURE
   └── Collaboration, video export, mobile app
```

---

## 🔨 Phase 2 Tasks

### 2.1 Timeline Editor Improvements

- [ ] **Task 2.1.1**: Drag-and-drop timeline events
  - Click and drag events to reposition
  - Snap to grid option
  - Visual feedback during drag
- [ ] **Task 2.1.2**: Timeline zoom and scroll
  - Zoom in/out for precision editing
  - Horizontal scroll for long performances
  - Minimap overview
- [ ] **Task 2.1.3**: Multi-select and group operations
  - Select multiple events
  - Move/delete groups
  - Copy/paste events
- [ ] **Task 2.1.4**: Undo/Redo system
  - Command pattern implementation
  - Keyboard shortcuts (Ctrl+Z, Ctrl+Y)
  - History panel

### 2.2 Audio Integration

- [ ] **Task 2.2.1**: Audio file upload and playback
  - Support MP3, WAV, OGG
  - Waveform visualization
  - Play/pause/seek controls
- [ ] **Task 2.2.2**: Audio-synced playback
  - Performance events sync to audio position
  - Visual beat markers
  - BPM detection (stretch goal)
- [ ] **Task 2.2.3**: Audio timeline track
  - Waveform display in timeline
  - Zoom synced with event timeline

### 2.3 Enhanced Firework System

- [ ] **Task 2.3.1**: Custom color palette creator
  - Color picker interface
  - Save custom palettes
  - Import/export palettes
- [ ] **Task 2.3.2**: New firework types
  - Waterfall (cascading effect)
  - Brocade (glittering trails)
  - Peony (large soft spheres)
  - Palm (palm tree shape)
  - Comet (single trailing star)
- [ ] **Task 2.3.3**: Firework parameter tuning
  - Adjustable particle count
  - Gravity/drag sliders
  - Size and lifetime controls
- [ ] **Task 2.3.4**: Launch angle control
  - Angled launches (not just vertical)
  - Fan patterns
  - Crossfire effects

### 2.4 Background Enhancements

- [ ] **Task 2.4.1**: Custom background upload
  - Drag-and-drop image upload
  - Crop and position controls
  - Save to localStorage
- [ ] **Task 2.4.2**: Animated backgrounds
  - Subtle water reflections
  - Moving clouds
  - City lights twinkling
- [ ] **Task 2.4.3**: Weather effects
  - Wind affecting particles
  - Light rain/snow overlay
  - Fog/haze layers

### 2.5 UI/UX Improvements

- [ ] **Task 2.5.1**: Firework preview thumbnails
  - Animated previews on hover
  - Preview in sequence builder
- [ ] **Task 2.5.2**: Improved mobile experience
  - Touch-optimized controls
  - Swipe gestures
  - Portrait/landscape layouts
- [ ] **Task 2.5.3**: Accessibility improvements
  - Keyboard navigation
  - Screen reader support
  - High contrast mode
- [ ] **Task 2.5.4**: Theming system
  - Light/dark mode toggle
  - Custom accent colors
  - Preset themes

### 2.6 Performance & Quality

- [ ] **Task 2.6.1**: Performance monitor
  - FPS counter
  - Particle count display
  - Memory usage
- [ ] **Task 2.6.2**: Quality presets
  - Low/Medium/High/Ultra
  - Auto-detect device capability
  - Battery saver mode

---

## 🚀 Phase 3 Tasks

### 3.1 Sharing & Collaboration

- [ ] **Task 3.1.1**: Share via URL
  - Encode performance in URL
  - QR code generation
  - Social media previews
- [ ] **Task 3.1.2**: Cloud storage integration
  - Google Drive sync
  - Dropbox support
  - Account system (optional)
- [ ] **Task 3.1.3**: Community gallery
  - Browse shared performances
  - Like and favorite
  - Featured showcases

### 3.2 Export Capabilities

- [ ] **Task 3.2.1**: Video export
  - Record to WebM/MP4
  - Resolution options
  - Include audio
- [ ] **Task 3.2.2**: GIF export
  - Animated GIF creation
  - Loop options
  - Optimized file size
- [ ] **Task 3.2.3**: Image export
  - Screenshot current frame
  - High-resolution render
  - Transparent background option

### 3.3 Advanced Features

- [ ] **Task 3.3.1**: Multi-track timeline
  - Separate tracks for different launcher positions
  - Track muting/soloing
  - DAW-style interface
- [ ] **Task 3.3.2**: Scripting support
  - JavaScript-based automation
  - Procedural generation
  - Random variations
- [ ] **Task 3.3.3**: 3D perspective mode
  - Three.js integration
  - Camera controls
  - Depth of field

### 3.4 Platform Expansion

- [ ] **Task 3.4.1**: Progressive Web App (PWA)
  - Offline support
  - Install to home screen
  - Push notifications
- [ ] **Task 3.4.2**: Desktop app (Electron)
  - Native file system access
  - System tray integration
  - Keyboard shortcuts
- [ ] **Task 3.4.3**: Mobile apps
  - React Native or Flutter
  - Native performance
  - App store distribution

---

## 🔮 Future Considerations

### Ideas for Exploration

1. **VR/AR Support** - Immersive fireworks experience
2. **Multiplayer Mode** - Synchronized shows across devices
3. **AI Generation** - Generate performances from prompts
4. **Hardware Integration** - Trigger real fireworks (DMX protocol)
5. **Educational Mode** - Physics explanations and tutorials
6. **Event Templates** - 4th of July, Diwali, Chinese New Year themes
7. **Accessibility Mode** - Haptic feedback, audio descriptions

### Technical Explorations

1. **WebGPU Rendering** - Next-gen graphics performance
2. **Web Workers** - Offload physics to background threads
3. **WASM Physics** - High-performance particle simulation
4. **WebRTC** - Real-time collaboration

---

## 🔧 Technical Debt

### Current Issues to Address

| Priority | Issue          | Description                                      |
| -------- | -------------- | ------------------------------------------------ |
| Medium   | Modularization | Single file is getting large, consider splitting |
| Low      | TypeScript     | Add type safety for maintainability              |
| Low      | Testing        | No automated tests currently                     |
| Medium   | Error handling | Need better user feedback for errors             |
| Low      | Code comments  | Some complex sections need documentation         |

### Refactoring Opportunities

1. **Separate concerns** - Split into modules (renderer, audio, data, UI)
2. **Event system** - Implement proper pub/sub pattern
3. **State management** - Centralized state with clear mutations
4. **CSS organization** - Consider CSS-in-JS or separate stylesheet
5. **Build system** - Add bundler for production optimization

---

## 📝 Notes

### Design Decisions

- **Why Markdown for saves?** - Human readable, version control friendly, easy to edit manually
- **Why no framework?** - Zero dependencies means instant loading and maximum portability
- **Why localStorage?** - Works offline, no server needed, respects privacy

### Lessons Learned

1. Particle systems benefit enormously from typed arrays
2. Radial gradients are expensive - simplify for performance
3. Ring buffers prevent memory allocation in hot loops
4. Users love immediate visual feedback

---

## ✅ Next Actions

**Immediate priorities for Phase 2:**

1. [ ] Start with Task 2.1.4 (Undo/Redo) - Foundation for safe editing
2. [ ] Then Task 2.3.1 (Custom palettes) - High user value, moderate effort
3. [ ] Then Task 2.2.1 (Audio upload) - Key differentiating feature
4. [ ] Then Task 2.1.1 (Drag-and-drop timeline) - Major UX improvement

---

<p align="center">
  <em>This is a living document. Update as the project evolves.</em>
</p>
