# Santiago López Viñao — Portfolio

Single-page portfolio: hero with halo, Projects carousel, About timeline and Ideas box (Web3Forms).

## Structure

```
index.html        → the whole site
support.js        → runtime (loads React from unpkg)
assets/           → photos, icons and favicon
.nojekyll         → tells GitHub Pages to serve files as-is
```

## Ideas box (Web3Forms)

The form posts to Web3Forms with the access key set in `index.html` (search for `web3formsKey`). Messages arrive at the email linked to that key. To change it, replace the key and re-upload `index.html`.

### Spam protection (hCaptcha)

The form renders hCaptcha with Web3Forms' free sitekey and sends the `h-captcha-response` token with every submission — no extra setup needed. hCaptcha won't load from `file://`; test it on GitHub Pages or a local server.

## Local preview

Open with any static server (e.g. `npx serve .`) — opening the file directly with `file://` may block some assets.
