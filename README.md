# Overused Grotesk
From a dumb mockery of the overutilised "Swiss" type design to a semi-serious workhorse, Overused Grotesk turns itself into a copycat by imitating the most distinguishing features of the ubiquitous Helvetica. However, the typeface doesn't stop at purely being a copycat; it wants to be a multipurpose and multilingual, though quirky and nonserious one.

This typeface was originally served as a form of "exhibition" for oblivious FontForge users. Unfortunately due to the superbly fast development, along with bad workflow and poor management, the project quickly became incomprehensible for an absolute beginner. Sooo oopsies

The fonts are free & open-source, and any contributions would be greatly appreciated. If you are planning to show this typeface to someone or submit it to a font collection, please remember to **link this repository**. It's not mandatory, but it saves a lot of headaches (trust me).

Also: thank yall for 500 stars


![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/og-f1.png)
![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/og-e1.png)

---
## Styles
| Style name | wght | wdth | slnt | - | Style name | wght | wdth | slnt |
| --------- | :---: | :---: | :---: | - | --------- | :---: | :---: | :---: |
| Light | 300 | 100 | 0 | - | Light Italic | 300 | 100 | -10 |
| Book | 350 | 100 | 0 | - | Book Italic | 350 | 100 | -10 |
| Roman | 400 | 100 | 0 | - | Italic | 400 | 100 | -10 |
| Medium | 500 | 100 | 0 | - | Medium Italic | 500 | 100 | -10 |
| SemiBold | 600 | 100 | 0 | - | SemiBold Italic | 600 | 100 | -10 |
| Bold | 700 | 100 | 0 | - | Bold Italic | 700 | 100 | -10 |
| ExtraBold | 800 | 100 | 0 | - | ExtraBold Italic | 800 | 100 | -10 |
| Black | 900 | 100 | 0 | - | Black Italic | 900 | 100 | -10 |

## Notable features & additions
- Includes Vietnamese & Cyrillic letters (w/ localised forms)
- 12 Stylistic sets + 5 Character variants
- Sub- & superscript, denominators & numerators, slashed zero, tabular figures, mathematical notations, fractions
- .ttf, .otf, .woff, .woff2, and variable .ttf fonts
- IPA letters (semifunctional diacritics and tone letters, still very basic)
- Currency symbols: $¢£¤¥֏฿₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿
- Arrows (way too much of them, 84 to be exact)
- Script-like discretionary ligatures (fi, ff, fl, ffi, ffl)

## Plans
_**After v1.0 - Before v2.0**_
- More widths (5 static widths: Compressed - Condensed - Normal - Extended - Wide)
- Greek
- Small caps
- Building more accented letters (Latin-specific)

### ⏳ In progress
- Fine tuning
- Finishing italics

## Variable fonts for the web
Both the source and the release folder include a .woff2 variable font, which you can include in your website and refer to using CSS by including something along the lines of:

**base.css**
```css
:root {
    --font-sans: "Overused Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
    --font-serif: Georgia, Times, serif;
    --font-mono: Menlo, Courier, monospace;
}

@font-face {
  font-family: "Overused Grotesk";
  src:
    url("../fonts/OverusedGrotesk-VF.woff2") format("woff2 supports variations"),
    url("../fonts/OverusedGrotesk-VF.woff2") format("woff2-variations");
  font-weight: 300 900;
}
```

To reduce [**Cumulative Layout Shift**](https://web.dev/cls/) you can preload font and use [**Font Face Observer**](https://fontfaceobserver.com/) to display font blazingly fast.

**base.html**
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Static HTML is King 👑</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="/css/base.css">
    <link rel="preload" href="/fonts/OverusedGrotesk-VF.woff2" as="font" type="font/woff2" crossorigin>
  </head>
  <body>

    <main>
      <h1>Static HTML is King 👑</h1>
    </main>
 
    <!--
    https://fontfaceobserver.com/
    To load a font, call the load method on a FontFaceObserver instance.
    It’ll return a promise that resolves when the font loads, or rejected when the font fails to load.
    -->
   <script src="/js/fontfaceobserver.js"></script>
   <script>
   var font = new FontFaceObserver('Overused Grotesk');

   font.load().then(function () {
     console.log('Overused Grotesk has loaded.');
   }).catch(function () {
     console.log('Overused Grotesk failed to load.');
   });
   </script>

  </body>
</html>
```

## License
This project is under the [SIL Open Font License 1.1](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/LICENSE.txt). If necessary, please save or print this document for future references.

## Contributing
You can contribute to this project by opening an issue, creating a pull request, or by directly editing the source.

For more information, see [CONTRIBUTING.md](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/CONTRIBUTING.md).
