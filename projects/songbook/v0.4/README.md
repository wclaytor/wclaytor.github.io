# 🎵 Songbook PWA

Songbook is an offline-first Progressive Web App for keeping your songs, chords, lyrics, and artist notes in one place — and for playing them live from a setlist. Install it on your phone, tablet, or laptop. It runs entirely in your browser, with no account and no server.

The whole app lives in one file, [`index.html`](./index.html), built with [Alpine.js](https://alpinejs.dev/) and [marked](https://marked.js.org/). A small service worker ([`sw.js`](./sw.js)) handles offline caching.

## ✨ Features

- **Songs**: browse, view, create, edit, and delete songs (title, artist, genre, lyrics/chords).
- **Artists**: browse artists, read their bios, and see every song in your collection by that artist.
- **Setlists**: build ordered setlists, add songs, reorder them, and remove them.
- **Perform mode**: open a song from a setlist and use previous/next to move through the set.
- **Search**: filter songs and artists as you type.
- **Import**: drag and drop (or select) Markdown song and artist files, or restore a JSON collection.
- **Export**: download your whole collection (songs, artists, setlists) as one JSON file for backup or transfer.
- **Dark mode**: switch between light and dark themes in Settings.
- **Offline and installable**: data is kept in the browser's IndexedDB, and the service worker caches the app so it works without a connection.

## 🚀 Getting Started

### Use the app

Service workers (offline support and installation) only run over `http://localhost` or `https://`, so serve the repository folder with any static file server:

```bash
# Option 1: Python
python3 -m http.server 8080

# Option 2: Node.js
npx serve .
```

Then open <http://localhost:8080> (or the URL that `serve` prints).

> Opening `index.html` straight from disk (`file://`) works for browsing and editing, but offline caching and installation won't be available.

To **install** it, use your browser's "Install app" / "Add to Home Screen" option.

### Load songs

The first time you open the app, the collection is empty. You can:

1. **Import a collection file**: choose **Import Collection File** and pick a JSON export, such as one from [`songbook/export/`](./songbook/export/).
2. **Import Markdown files**: drop `.md` files onto the drop zone, or click it to pick files. Song files live in [`songbook/songs/`](./songbook/songs/) and artist files in [`songbook/artists/`](./songbook/artists/).
3. **Create songs by hand**: use **New Song** on the Songs tab.

Later imports are done from the **Import** button in the header.

### Back up your data

Everything is stored in your browser. Use **Export** (header) or **Settings → Export Collection** to download a `songbook-export-YYYY-MM-DD.json` backup. **Settings → Clear All Data** deletes everything stored locally.

## 📝 Markdown File Formats

When you import, the app decides whether each file is a song or an artist. Files with a `## Lyrics` section or a `**Genre**:` field are treated as songs. Files with a `## About` or `## Songs` section are treated as artists.

### Song

````markdown
# Blackbird

**Artist**: [The Beatles](http://example.com/artists/29)
**Genre**: Classic Rock

## Lyrics

```
Blackbird singing in the dead of night
Take these broken wings and learn to fly
```
````

- Title comes from the first `#` heading; if there isn't one, the filename is used.
- `**Artist**:` can be plain text or a Markdown link.
- Lyrics/chords are read from the code block under `## Lyrics`. If there's no code block, the text under that heading is used.

### Artist

```markdown
# Glen Campbell

## About

Glen Travis Campbell was an American guitarist, singer, songwriter...

## Songs (2)

- [Gentle On My Mind](http://example.com/songs/2609)
- [Wichita Lineman](http://example.com/songs/2889)
```

- Name comes from the first `#` heading.
- The bio is taken from the `## About` section and rendered as Markdown.

## 📁 Project Structure

```
.
├── index.html            # The entire app (HTML, CSS, Alpine.js logic)
├── sw.js                 # Service worker for offline caching
├── songbook/
│   ├── songs/            # Song Markdown files (one folder per song)
│   ├── artists/          # Artist Markdown files (one folder per artist)
│   ├── data/             # Source song/artist data (JSON)
│   └── export/           # Sample JSON collection exports
├── tests/playwright/     # Playwright smoke tests
├── playwright.config.ts  # Playwright configuration
├── docs/                 # Roles, features (PRDs), guides, and notes
└── scripts/github/       # Python helpers for syncing GitHub issues/PRs
```

## 🧪 Development & Testing

No build step is needed. Edit `index.html` and reload the page.

The smoke tests use [Playwright](https://playwright.dev/) and load `index.html` directly:

```bash
npm ci
npx playwright install --with-deps chromium
npx playwright test
npx playwright show-report   # view the HTML report
```

The tests also run in GitHub Actions on every push and pull request to `main` (see [`.github/workflows/playwright.yml`](./.github/workflows/playwright.yml)).

> If you change `index.html` or other cached assets, bump `CACHE_NAME` in `sw.js` so installed clients pick up the new version.

## 🎭 Development Methodology

This project uses a seven-role development methodology: Director, Product-Owner, Architect, Developer, Designer, QA-Engineer, and Domain-Expert. Start here:

- [`AGENTS.md`](./AGENTS.md) and [`CLAUDE.md`](./CLAUDE.md): guides for AI assistants
- [`docs/roles/`](./docs/roles/): role definitions and collaboration patterns
- [`docs/features/`](./docs/features/): product requirement documents
- [`docs/notes/`](./docs/notes/): daily work notes
- [`.claude/skills/`](./.claude/skills/): reusable skills

## 📄 License

[MIT](./LICENSE.md) © William Claytor
