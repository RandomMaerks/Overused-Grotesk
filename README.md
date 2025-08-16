## ❗❕ Update (16/08/2025)

After one and a half months of procrastination, I have finally got up the courage to work on this project again. It has been quite a while now, hasn't it? When was the last release? A year ago ....? umm..,,,,llll;;;; uhh;'''''

anyway, expect some commits being committed very soon !

# Overused Grotesk
From a dumb mockery of the overutilised "Swiss" type design to a semi-serious workhorse, Overused Grotesk turns itself into a copycat by imitating the most distinguishing features of the ubiquitous Helvetica. However, the typeface doesn't stop at purely being a copycat; it wants to be a multipurpose and multilingual, though quirky and nonserious one.

This typeface was originally served as a form of "exhibition" for oblivious FontForge users. Unfortunately due to the superbly fast development, along with bad workflow and poor management, the project quickly became incomprehensible for an absolute beginner. Sooo oopsies

The fonts are free & open-source, and any contributions would be greatly appreciated. If you are planning to show this typeface to someone or submit it to a font collection, please remember to **link this repository**. It's not mandatory, but it saves a lot of headaches (trust me).

<img src="https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/collection%20h/og-h1.png" />
<img src="https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/collection%20h/og-h2.png" />

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

## Plans
_**After v1.0 - Before v2.0**_
- More widths (5 static widths: Tight - Narrow - Normal - Ample - Wide)
- Greek
- Small caps
- Building more accented letters (Latin-specific)

### ⏳ In progress
- Fine tuning
- Finishing italics

## Web variable font
Both the source and the release folder include a .woff2 variable font, which you can include in your website and refer to using CSS.

If you host the fonts yourself, you can insert the following:
```css
@font-face {
    font-family: "Overused Grotesk";
    src: url("../fonts/OverusedGrotesk-VF.woff2") format("woff2-variations");
    font-weight: 300 900;
}
```

Or, if you want to rip the variable font directly from this repository, put the source as:
```css
src: url('https://raw.githubusercontent.com/RandomMaerks/Overused-Grotesk/master/fonts/variable/OverusedGroteskRoman-VF.ttf')
```

To reduce [**Cumulative Layout Shift**](https://web.dev/cls/), you can preload the fonts using [**Font Face Observer**](https://fontfaceobserver.com/). For example, you can put the following JS script inside of an HTML file:

```html
<script src="/js/fontfaceobserver.js"></script>
<script>
    var font = new FontFaceObserver('Overused Grotesk');
    font.load().then(function () {
      console.log('Overused Grotesk has loaded.');
    }).catch(function () {
      console.log('Overused Grotesk failed to load.');
    });
</script>
```

## License
This project is under the [SIL Open Font License 1.1](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/LICENSE.txt). If necessary, please save or print this document for future references.

## Contributing
You can contribute to this project by opening an issue, creating a pull request, or by directly editing the source.

For more information, see [CONTRIBUTING.md](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/CONTRIBUTING.md).
