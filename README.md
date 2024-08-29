# Overused Grotesk
From a dumb mockery of the overutilised "Swiss" type design to a semi-serious workhorse, Overused Grotesk turns itself into a copycat by imitating the most distinguishing features of the ubiquitous Helvetica. However the typeface doesn't stop at purely being a copycat; it wants to be a multipurpose and multilingual, though quirky and nonserious one.

This typeface was originally served as a form of "exhibition" for oblivious FontForge users. Unfortunately due to the superbly fast development, along with bad workflow and poor management, the project quickly became incomprehensible for an absolute beginner. Sooo oopsies

The fonts are free & open-source, and any contributions would be greatly appreciated. If you are planning to show this typeface to someone or submit it to a font collection, please remember to **link this repository**. It's not mandatory, but it saves a lot of headaches (trust me).


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

## Webfont usage

### Variable fonts
Traditionally, all possible weights and styles have been separated out into different font files, whereas variable fonts combine all of those variations into one. Because of this, overall file size is greatly reduced compared to loading multiple individual font files—and that’s a key consideration for web typography.

More information about variable font can be found on Google Fonts' [Introducing variable fonts](https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts) article written by Elliot Jay Stocks.

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

## Plans
_**Before v1.0**_
- More widths (5 static widths: Compressed - Condensed - Normal - Extended - Wide)
  - 3 width masters * 2 weight masters * 2 slant masters = 12 total masters

_**After v1.0 - Before v2.0**_
- Greek
- Small caps
- Building more accented letters (Latin-specific)

_**After v2.0**_
- New styles? Mono, Text, Micro? maybe not yet

### ⏳ In progress
- Fine tuning
- Width expansion

### ✅ Notable features & additions
- Includes Vietnamese & Cyrillic letters (w/ localised forms)
- 12 Stylistic sets + 6 Character variants
- Sub- & superscript, denominators & numerators, slashed zero, tabular figures, mathematical notations, fractions
- .ttf, .otf, .woff, .woff2, and variable .ttf fonts
- IPA letters (basic implementation)
- Currency symbols: $¢£¤¥֏฿₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿
- Arrows (way too much of them, 84 to be exact)
- Script-like discretionary ligatures (fi, ff, fl, ffi, ffl)

## License
This project is under the [SIL Open Font License 1.1](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/LICENSE.txt). If necessary, please save or print this document for future references.


## Contributing
You can contribute to this project by opening an issue, creating a pull request, or by directly editing the source.

For more information, see [CONTRIBUTING.md](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/CONTRIBUTING.md).


## Additional documentation
This section is just here for additional references.
- Donny Trương's [Vietnamese Typography](https://vietnamesetypography.com) book
- [Cyrillic Local Forms](https://localfonts.eu/typography-basics/fonts-the-importance-of-localisation/local-features/cyrillic-local-forms/)
- RoboFont's [Creating designspace files with designSpaceLib](https://robofont.com/documentation/tutorials/creating-designspace-files/#creating-designspace-files-with-designspacelib)
- fontTools' [Creating a designspace](https://fonttools.readthedocs.io/en/latest/designspaceLib/scripting.html)
