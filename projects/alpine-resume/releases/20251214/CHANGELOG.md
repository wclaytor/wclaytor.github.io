# Changelog

All notable changes to Alpine Resume will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-15

### Added
- **Progressive Web App (PWA) Support**
  - Offline functionality with service worker and Workbox
  - App installation capability on desktop and mobile
  - Standalone mode detection and optimizations
  - Service worker update notifications
  
- **Core Features**
  - Markdown resume rendering with syntax highlighting
  - Interactive collapsible sections with state persistence
  - Section navigation with scroll tracking
  - Responsive mobile and desktop layouts
  
- **Theme System**
  - Light and dark theme toggle
  - System preference detection
  - Persistent theme selection
  - Smooth theme transitions
  
- **State Management**
  - Unified application state with localStorage
  - Section expand/collapse state persistence
  - Scroll position restoration
  - State migration system
  
- **Accessibility**
  - WCAG 2.1 AA compliance
  - Keyboard navigation support
  - Screen reader optimizations
  - Skip links and ARIA labels
  - Print-optimized styles
  
- **Network Features**
  - Online/offline status detection
  - Offline indicator with user feedback
  - Cached asset management
  
- **iOS Enhancements**
  - Safe area inset support for notched devices
  - Standalone mode optimizations
  - iOS splash screen support

### Technical
- Alpine.js 3.x for reactive components
- Tailwind CSS for styling
- Marked.js for Markdown parsing
- DOMPurify for XSS protection
- Playwright for E2E testing
- Service worker with cache versioning

---

[1.0.0]: https://github.com/wclaytor/alpine-resume/releases/tag/v1.0.0
