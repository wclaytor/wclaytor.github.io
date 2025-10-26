# Getting Started with Alpine.js

Welcome to Alpine.js! This lightweight framework makes building reactive interfaces simple and intuitive.

## Key Features

### 1. Declarative Syntax
Alpine.js uses HTML attributes to add behavior to your markup:
- `x-data` - Define component state
- `x-bind` - Bind attributes dynamically  
- `x-on` - Listen to events
- `x-model` - Two-way data binding
- `x-if` / `x-show` - Conditional rendering

### 2. No Build Step Required
Just include the CDN script and start building!

```html
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
```

### 3. Small Footprint
Alpine.js is tiny (~15KB gzipped) compared to other frameworks.

## Quick Example

```javascript
<div x-data="{ count: 0 }">
  <button @click="count++">Increment</button>
  <span x-text="count"></span>
</div>
```

## Best Practices

- Keep components small and focused
- Use computed properties for derived state
- Leverage local storage for persistence
- Test with the file:// protocol for offline usage

## Learn More

Check out the official documentation at [alpinejs.dev](https://alpinejs.dev) for comprehensive guides and examples.
