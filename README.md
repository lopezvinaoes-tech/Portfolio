# Santiago López Viñao — Portfolio

Single-page portfolio: hero with halo, Projects carousel, About timeline and Ideas box (Web3Forms).

## Structure

```
index.html        → the whole site
support.js        → runtime (loads React from unpkg)
assets/           → photos, icons and favicon
.nojekyll         → tells GitHub Pages to serve files as-is
```

## Publish on GitHub Pages

1. Create a new repository (e.g. `portfolio`) on github.com.
2. Upload **all** files in this folder to the root of the repo (Add file → Upload files). Keep the `assets/` folder structure.
3. Go to **Settings → Pages**, set *Source* to **Deploy from a branch**, branch **main**, folder **/ (root)**, and save.
4. After a minute your site is live at `https://<your-user>.github.io/portfolio/`.

> Tip: name the repo `<your-user>.github.io` to publish at `https://<your-user>.github.io/`.

## Ideas box (Web3Forms)

The form posts to Web3Forms with the access key set in `index.html` (search for `web3formsKey`). Messages arrive at the email linked to that key. To change it, replace the key and re-upload `index.html`.

### Spam protection (hCaptcha)

The form renders hCaptcha with Web3Forms' free sitekey and sends the `h-captcha-response` token with every submission — no extra setup needed. hCaptcha won't load from `file://`; test it on GitHub Pages or a local server.

## Vercel Speed Insights

`index.html` already loads Speed Insights via `/_vercel/speed-insights/script.js` (the plain-HTML version of `@vercel/speed-insights` — this site is not Next.js, so the `<SpeedInsights />` component isn't needed).

1. Import the repo in Vercel (Framework preset: **Other**, no build command).
2. In the project dashboard → **Speed Insights** → **Enable**.
3. Redeploy. Data appears after the first visits.

The script only works on the Vercel deployment (on GitHub Pages or locally it returns 404, which is harmless).

## Local preview

Open with any static server (e.g. `npx serve .`) — opening the file directly with `file://` may block some assets.
