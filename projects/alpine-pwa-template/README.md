# Alpine PWA Template

A **single-page Alpine.js Progressive Web App (PWA)** template built for easy hosting on **GitHub Pages** or any static web server.  
It loads Markdown files from your repository (like recipes, art presets, or docs) and can export data in Markdown, CSV, or image format.

---

## 🌟 Features

- 🧩 **Single-file PWA** — all logic in one HTML file, no build tools required.
- ⚙️ **Dynamic manifest & icons** — generated at runtime, installable on desktop and mobile.
- 🧠 **Alpine.js 3 + Tailwind CSS** — reactive, lightweight, no dependencies.
- 📂 **Repo content loader** — fetches `files.json` and renders `/files/*.md` using Marked + DOMPurify.
- 💾 **LocalStorage persistence** — demo tasks persist between sessions.
- 🔐 **CSP + DOMPurify** — basic security hardening for hosted Markdown.
- 🔄 **Offline caching** via `sw.js` — works offline after first visit.
- 📤 **Export tools** — export demo data to Markdown, CSV, or image snapshot.
- 🕶️ **Dark mode toggle** — syncs with system preference.

---

## 🪶 Files Included

| File | Purpose |
|------|----------|
| **alpine-pwa-template.html** | Main single-page PWA template |
| **sw.js** | Service worker for offline caching |
| **files.json** *(you create)* | Lists Markdown files to load (see below) |
| **/files/** | Folder containing your Markdown content |

---

## 📦 Quick Start (GitHub Pages)

1. **Clone or copy** this repo structure into your own GitHub repository:
   ```text
   yourrepo/
   ├── alpine-pwa-template.html
   ├── sw.js
   ├── files.json
   └── files/
       ├── example-01.md
       ├── example-02.md
       └── ...
   ```

2. **Create `files.json`** at the root. It can be a simple list:
   ```json
   [
     "example-01.md",
     "example-02.md"
   ]
   ```
   or a detailed structure:
   ```json
   [
     { "name": "example-01.md", "path": "files/example-01.md", "size": 1234 }
   ]
   ```

3. **Enable GitHub Pages** in your repo settings:  
   - Source: `Deploy from branch`  
   - Branch: `main` (or `master`)  
   - Folder: `/ (root)`

4. Visit your published URL, e.g.  
   `https://yourname.github.io/yourrepo/`

   You should see the app load your Markdown list.  
   Use “Install” in the header or browser menu to add it to your home screen.

---

## ⚡ Service Worker Notes

- The included `sw.js` caches:
  - The app shell (`index.html`, CSS/JS from CDNs you list).
  - Any `/files/*.md` you open — available offline after first load.
- Uses **cache-first** for same-origin requests with fallback to `index.html`.
- Versioned cache name (`v1`) — bump it when you want to invalidate.

If you don’t need offline, you can omit the `sw.js` file. Chrome will still allow installation.

---

## 🧰 Local Development

You can preview locally with any static server (must use HTTPs for full PWA features):

```bash
python3 -m http.server 8000
# then open http://localhost:8000/alpine-pwa-template.html
```

To test installation:
- In Chrome or Edge, open DevTools → Application → Manifest → “Add to Home Screen.”

---

## 🛡️ Security

- **DOMPurify** sanitizes Markdown-rendered HTML to prevent XSS.
- **CSP** header (in `<meta>`) restricts allowed sources to your own domain and CDNs.
- Keep untrusted scripts out of Markdown content for safety.

---

## 🌓 Dark Mode

Dark mode toggles manually via the button in the header and also respects the user's system setting.

---

## 🧾 Data Export Example

The demo “Tasks” section demonstrates exporting structured data:

- **Markdown:** checkboxes with priorities.
- **CSV:** spreadsheet-ready.
- **PNG:** snapshot of task stats via Canvas.

These examples show how you can easily adapt the export logic for your own content.

---

## 🧩 Credits

- [Alpine.js](https://alpinejs.dev) — reactive UI in HTML.
- [Tailwind CSS](https://tailwindcss.com) — utility-first styling.
- [Marked](https://marked.js.org) — Markdown parser.
- [DOMPurify](https://github.com/cure53/DOMPurify) — XSS sanitizer.
- [Bootstrap Icons](https://icons.getbootstrap.com) — optional icon set.

---

## 🪄 License

MIT — free to use and modify. Attribution appreciated.

---

**Enjoy your lightweight Alpine.js PWA!**
