# Overused Grotesk
A neo-grotesque sans serif typeface that looks spetacularly like a Helvetica alternative because it is one.

![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/image-3.png)
![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/image-4.png)
![Overused Grotesk](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/image-5.png)

---
## Styles
| Style name | wght | wdth |
| --------- | :---: | :---: |
| Light | 300 | 100 |
| Book | 350 | 100 |
| Roman | 400 | 100 |
| Medium | 500 | 100 |
| SemiBold | 600 | 100 |
| Bold | 700 | 100 |
| ExtraBold | 800 | 100 |
| Black | 900 | 100 |


## Plans
- Cyrillic next?
- Numbers-related characters (sub- & superscript, denominators & numerators, slashed zero, tabular figures)
- Arrows (like, lots of them)
- Ligatures (not necessary)
- Kerning (LATIN, NUMBERS, etc.)
- New widths? Compressed + Condensed + Extended + ExtraExtended (build Compressed & ExtraExtended then just interpolate from there)
- Italics, definitely. Just need to make the Upright version first.
- New styles? Mono, Text, Micro? maybe not yet

### Completed tasks
- Add diacritical marks & accented characters ([Vietnamese support](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/documentation/image-6.png))✅ (05/08/2023)


## License
This project is under the [SIL Open Font License 1.1](https://github.com/RandomMaerks/Overused-Grotesk/blob/main/LICENSE.txt). If necessary, please save or print this document for future references.


## Requirements
This typeface is designed using [FontForge](https://github.com/fontforge/fontforge). In order to open the .sfd files in the source folder, you must install FontForge.

[fontmake](https://github.com/googlefonts/fontmake) was also used to create variable font and generate instances.

### How to build & contribute
**For Windows users**

You can use FontForge to open the .sfd files. .ufo files coming soon cuz im lazy lol

If you want to build and generate variable fonts or instances, you will need to install Python 3.8 or later.

Open **Run** and type `cmd`. Then type in the following to install `fontmake`:
```
py -m pip install fontmake
```

Once the installation is complete, enter `cd` then drag in the source directory (assuming you've downloaded the .zip and extracted it). For example:
```
cd "C:\Users\...\Overused-Grotesk-main\source"
```

If you want to build variable font, use:
```
py -m fontmake -m OverusedGrotesk.designspace -o variable
```

Or you can generate instances by copy-and-pasting all of the content from `build_instances.sh` into the command prompt.

The `make_designspace.py` allows you to build `OverusedGrotesk.designspace` or whatever name is in the `path = "..."`. For more information on how to edit designspace files, check out RoboFont's [Creating designspace files with designSpaceLib](https://robofont.com/documentation/tutorials/creating-designspace-files/#creating-designspace-files-with-designspacelib).


## Additional documentation
This section is just here for additional references.
- Donny Trương's [Vietnamese Typography](https://vietnamesetypography.com) book
- Monotype's [Glossary of Typographic Terms and Definitions](https://www.monotype.com/resources/z-typographic-terms)
- [Cyrillic Local Forms](https://localfonts.eu/typography-basics/fonts-the-importance-of-localisation/local-features/cyrillic-local-forms/)
- Google's [Google Fonts Documentation](https://googlefonts.github.io/gf-guide/) (if this typeface's going to GF, which I doubt)
- RoboFont's [Creating designspace files with designSpaceLib](https://robofont.com/documentation/tutorials/creating-designspace-files/#creating-designspace-files-with-designspacelib)
