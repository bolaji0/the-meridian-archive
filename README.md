# The Meridian Archive

Self-initiated visual identity and static website by Mustapha Fathiu. Mara Vey, all books, excerpts and essays are fictional original concept content. This is not client work.

## Run & host

Serve `dist/` with any static web server, for example `python3 -m http.server 8080 --directory dist`. Upload its contents to GitHub Pages, Netlify, Cloudflare Pages or other static hosting. No build is required. Paths are relative and support subdirectory hosting.

## Architecture

Homepage; books catalogue; three book pages; author; field-note index; two full essays; signup; contact; design notes. All pages are fully rendered HTML. `assets/style.css` is the shared design system. `assets/site.js` only enhances two local form demonstrations. `build.py` regenerates the pages and artwork; it requires fontTools and the URW Base35 font paths in this development environment, but is unnecessary for hosting or editing the finished site.

## Visual system

Paper #E9E5D8; ink #252820; vermilion #BA4B32; olive #6B7050; lavender #C3BCD0. Nimbus Sans regular/bold, P052 Italic, Nimbus Mono. Fluid headings; catalogue labels; limited text measures; offset grids; original split-sun, portal and contour SVGs. Breakpoints: 1000px and 700px. Reduced motion, keyboard focus, skip link, semantic navigation and local validation are supported.

## Forms

Demonstration only. No endpoint, storage, subscription or email delivery. Button labels and result messages state this explicitly. To use for a real author, connect an appropriate service, revise privacy/consent language and replace all fictional content.

## Font licensing

Locally bundled WOFF files are conversions of URW Base35 OpenType fonts, licensed under AGPL with the font embedding exception. License text is included in assets/FONT-LICENSE.txt. Original graphics and concept writing are part of this portfolio project.
