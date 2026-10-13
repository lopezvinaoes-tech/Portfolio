# Santiago Lopez Viñao — Portfolio

Single-page portfolio: hero with halo, Projects carousel, About timeline and Ideas box (Web3Forms).

## Structure

```
index.html        → the whole site, English URL (icons are inlined as data URIs)
es/index.html     → Spanish URL, GENERATED from index.html — don't edit by hand
404.html          → bilingual "page not found"
support.js        → runtime that renders the page with React
assets/fonts/     → Inter (variable, Latin subset), self-hosted — no Google Fonts
assets/vendor/    → React + ReactDOM 18.3.1 (see below)
assets/           → photos, favicon and share image (og.jpg)
robots.txt        → lets search engines crawl the site (generated)
sitemap.xml       → both language URLs for Google Search Console (generated)
vercel.json       → security headers and cache rules
assets/cv/        → CV PDFs (ES + EN), generated — don't edit by hand
_source/cv/       → CV source + build script (not deployed, see .vercelignore)
_source/site/     → generator for es/, sitemap.xml, robots.txt and the site address
_source/og/       → generator for the link-preview images (assets/og.jpg, og-es.jpg)
```

## Languages (EN / ES)

All texts live in the `I18N` object inside `index.html` and are used in the template as `{{ t.key }}`.
The page opens in the visitor's language: a manual EN/ES choice (remembered) wins, then the page URL
(`/es/` is Spanish), then the device language (Spanish, Catalan, Galician and Basque → Spanish; anything else → English).

`/` and `/es/` are separate URLs so Google can index both languages (canonical + hreflang).
**After any change to `index.html`, regenerate the Spanish page:**

```
python3 _source/site/build_site.py
```

### Moving to your own domain

Change `SITE` at the top of `_source/site/build_site.py`, run it, and push. It updates the canonical,
hreflang, link-preview and JSON-LD addresses in both pages, plus `sitemap.xml` and `robots.txt`.

## Link-preview images

`assets/og.jpg` (EN) and `assets/og-es.jpg` (ES) are generated from `_source/og/photo.jpg`:

```
python3 _source/og/build_og.py
```

## Analytics

`index.html` loads Vercel Speed Insights and Vercel Web Analytics (cookie-free). They only collect
data once enabled in the Vercel project (Analytics / Speed Insights → Enable).

## React files

`assets/vendor/` holds the official React and ReactDOM 18.3.1 production builds (from unpkg). The `<script>` tags carry their integrity hashes, so a wrong or corrupted file is rejected; if that ever happens, `support.js` falls back to unpkg automatically.

## Icons

Icons are inlined in `index.html` as SVG data URIs. Inside them `viewBox` is written as `view%42ox`: the runtime rewrites camelCase attribute names it finds in the template, and the encoded form keeps it from breaking the icons. Browsers decode it back to `viewBox`.

## CV

The PDFs in `assets/cv/` are generated. To change the CV, edit the `CONTENT` block in `_source/cv/build_cv.py` and run:

```
python3 _source/cv/build_cv.py
```

It needs Python 3 and Playwright with Chromium. The PDF uses static Inter weights from `_source/cv/fonts/`: Chromium embeds the variable font as Type 3, which some CV parsers (ATS) read poorly.

## Caching

Fonts, React, `support.js` and the photos are cached for a year. When you replace one of them, change its URL so visitors get the new version:

- Photos: bump `?v=2` → `?v=3` in `index.html`.
- `support.js`: bump `support.js?v=2` in `index.html`.

## Ideas box (Web3Forms)

The form posts to Web3Forms with the access key set in `index.html` (search for `web3formsKey`). Messages arrive at the email linked to that key. To change it, replace the key and re-upload `index.html`.

### Spam protection (hCaptcha)

The form renders hCaptcha with Web3Forms' free sitekey and sends the `h-captcha-response` token with every submission — no extra setup needed. hCaptcha won't load from `file://`; test it on a local server or the deployed site.

## Local preview

Open with any static server (e.g. `npx serve .`) — opening the file directly with `file://` may block some assets.
