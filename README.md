# Orienteering-Startlist-Screen
Description...

---
# Development
## Build minimal css

```bash
npm install -D tailwindcss @tailwindcss/cli
```
assets\tailwind\input.css
```css
@import "tailwindcss";
```
```bash
npx @tailwindcss/cli `
  -i ./assets/tailwind/input.css `
  -o ./src/orienteering_startlist_screen/utils/static/css/app.css `
  --minify
```
