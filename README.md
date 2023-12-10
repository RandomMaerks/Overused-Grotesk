# Overused Grotesk
Do you want a free alternative to Helvetica because you refuse to pay good money for high-quality typefaces, or that you think neo-grotesk Swiss-like type design is peak minimalism? Then this is probably a good choice.

Overused Grotesk is heavily based off the classic neo-grotesk type design, especially the epic look of the ubiquitous typeface, Helvetica. It may look like the other thousand neo-grotesk typefaces out there, but I can guarantee that "it has its own charm and uniqueness".

If you like this typeface, download it, store it in your library, use it, share it with someone.

![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/og-f1.png)
![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/og-e1.png)
![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/og-f2.png)
![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/og-f3.png)

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

**fonts.css**
```css
@font-face {
  font-family: 'Overused Grotesk';
  src:
    url('../fonts/OverusedGrotesk-VF.woff2') format('woff2 supports variations'),
    url('../fonts/OverusedGrotesk-VF.woff2') format('woff2-variations');
  font-weight: 300 900;
}
```
**base.css**
```css
@import "fonts.css";

:root {
    --font-sans: Overused Grotesk, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif;
}
```
To reduce [**Cumulative Layout Shift**](https://web.dev/cls/), you can preload the font in the head of your HTML document:

**base.html**
```html
<link rel="preload" href="/fonts/OverusedGrotesk-VF.woff2" as="font" type="font/woff2" crossorigin>
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
- Cyrillic
- Kerning (LATIN, NUMBERS, etc.)

### ✅ Completed tasks
- Add diacritical marks & accented characters ([Vietnamese support](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/image-6.png))✅ (05/08/2023)
- Stylistic set + Accented characters ✅ (08/08/2023)
- Sub- & superscript, denominators & numerators, slashed zero, tabular figures ✅ (14/08/2023)
- Try to figure out why Black weight has massive vertical height ✅ (20/08/2023)
- Circled + squared numbers (Character variant 01 - 04) ✅ (20/08/2023)
  - 'cv01': Negative squared numbers
  - 'cv02': Squared numbers
  - 'cv03': Negative circled numbers
  - 'cv04': Circled numbers
- Arrows ✅ (25/08/2023)
- Webfont support + css code ✅
- More currency symbols ✅️ (24/09/2023)
- Italic (for now) ✅️
- IPA (for now) ✅️

### ☑ Completed side quests
- Add serif 'I' (20/09/2023)
- Figure out why the WriteUFOLayer error occurs when merging sfds (20/09/2023)
- Fix kerning for 'y' with Stylistic Set 07 (20/09/2023)
- Add 'a.spur' for aesthetic reasons (cv05), although no accents (20/09/2023)
- REMOVE UNIWIDTH (22/09/2023) - poorly designed
- Add Discretionary Ligatures (fi, fl, ff, ffi, ffl) (10/12/2023)
- Add fractions (10/12/2023)
- Add a few mathematical notations (10/12/2023)

## License
This project is under the [SIL Open Font License 1.1](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/LICENSE.txt). If necessary, please save or print this document for future references.


## Contributing
You can contribute to this project by opening an issue, creating a pull request, or by directly editing the source.

For more information, see [CONTRIBUTING.md](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/CONTRIBUTING.md).


## Additional documentation
This section is just here for additional references.
- Donny Trương's [Vietnamese Typography](https://vietnamesetypography.com) book
- Monotype's [Glossary of Typographic Terms and Definitions](https://www.monotype.com/resources/z-typographic-terms)
- [Cyrillic Local Forms](https://localfonts.eu/typography-basics/fonts-the-importance-of-localisation/local-features/cyrillic-local-forms/)
- RoboFont's [Creating designspace files with designSpaceLib](https://robofont.com/documentation/tutorials/creating-designspace-files/#creating-designspace-files-with-designspacelib)
- fontTools' [Creating a designspace](https://fonttools.readthedocs.io/en/latest/designspaceLib/scripting.html)

## A small warning about distribution of this typeface
When you share this typeface with someone else, or submitting it to a public font collection, please include the link to this repository.

This typeface had already gone through multiple major updates throughout August, with many addtions like KERNING, ITALICS, WEBFONTS, even STYLISTIC SETS, BUG FIXES, CHARACTER VARIANTS, etc.

It is VERY IMPORTANT that people are able to get the latest update. Outdated versions may cause a lot of problems and damages if used extensively.
