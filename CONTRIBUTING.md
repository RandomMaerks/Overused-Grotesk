# 🛠 Contributing
This is an instruction on how to contribute to this project.

Note that the instruction on building and generating font files are based on the assumption that 
you are using a Windows machine. If you are using other operating systems like Mac or Linux, please 
change the command lines appropriately.

## ⚠ Warning

This instruction is based on my own method to generate and compress fonts, and it is generally not the 
best practice. If you have a more efficient solution, please let me and potential contributors know.

Additionally, please do not follow any instruction that you do not understand. Feel free to ask other
people for help, and make sure you have full control and sufficient knowledge of the things you are doing.

‎
‎

## ❗ Report an issue
If you find any issue with the design, features, or the source, please [open an issue](https://github.com/RandomMaerks/Overused-Grotesk/issues/new/choose). But if you're
just here to have a conversation or discuss certain things, you can [create a discussion](https://github.com/RandomMaerks/Overused-Grotesk/discussions/new/choose).

You can follow this template when you're creating an issue:

```
[TITLE] Name the issue. Make it as short, but as informative as possible.

- Explain the issue in further detail. What is the issue about? What might be causing the issue?
- Include a screenshot or a video if possible.
- How to re-create the issue? Is there a workaround?
- What device/program are you using?
- Which version of the font? Where did you get the font files?
- A "please fix" at the end for a better chance of responding
```
Make sure that the issue has not already been reported before.

‎
‎ 

## 🔨 Build

### ▶ Requirements
This typeface is designed using [FontForge](https://github.com/fontforge/fontforge). FontForge 
allows you to open and edit the .sfd files included in the source folder, export .ttf, .otf, or
.ufo for other uses.

[fontmake](https://github.com/googlefonts/fontmake) is also used to create variable font and
generate instances.

By installing fontmake, [fonttools](https://github.com/fonttools/fonttools) is automatically included, 
which is used for compressing `.otf` fonts into `.woff` and `.woff2` fonts. Though, you 
will also need to install [brotli](https://github.com/google/brotli) as well.

‎

### ▶ Installation & Setup
You can download **FontForge** from their [repository](https://github.com/fontforge/fontforge) or their [official website](https://fontforge.org/en-US/).

Before installing **fontmake**, you have to make sure that you already installed Python 3.8 or later.
A more detailed instruction can be found in the [fontmake repository](https://github.com/googlefonts/fontmake).

Note that you can also create a virtual environment so none of the installed 
dependencies interfere with any other libraries. But if you're dumb like me, just 
directly install it on your machine like normal. (yes that's bad advice, i'm
just not good at this stuff)

Open the command prompt. To install `fontmake` and `brotli`, run:

```
py -m pip install fontmake
py -m pip install brotli
```

Once complete, redirect the current directory to the source folder. For example:
```
cd "C:\Users\...\Overused-Grotesk-main\source"
```

‎ 

### ▶ Setup a designspace
The `make_designspace.py` allows you to build `OverusedGrotesk.designspace` or whatever name is in the
`path = "..."`.

For more information on how to edit designspace files, check out RoboFont's 
[Creating designspace files with designSpaceLib](https://robofont.com/documentation/tutorials/creating-designspace-files/#creating-designspace-files-with-designspacelib)
and fonttools' [Scripting a designspace](https://fonttools.readthedocs.io/en/latest/designspaceLib/scripting.html).


‎

### ▶ Generate
- _**Variable font (`.ttf`)**_

If you want to build variable font, do:
```
py -m fontmake -m OverusedGrotesk.designspace -o variable
```

- _**Static fonts (`.ttf`, `.otf`)**_

You can generate instances by copy-and-pasting all of the commands below: 
```
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-Light
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-Book
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-Roman
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-Medium
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-SemiBold
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-Bold
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-ExtraBold
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-Black
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-LightItalic
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-BookItalic
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-Italic
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-MediumItalic
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-SemiBoldItalic
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-BoldItalic
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-ExtraBoldItalic
py -m fontmake -m OverusedGrotesk.designspace -i OverusedGrotesk-BlackItalic
```

The output font files will be in either `instance_otf` / `instance_ttf` (instance generation) or 
`variable_ttf` (variable font). When you generate instances, their respective .ufo file will 
also be in `instance`.


- _**Compression (`.woff`, `.woff2`)**_

You can compress the `.otf` fonts in the `instance_otf` folder into `.woff2` and `.woff` fonts by
running the `webfont_gen.py` file in the source folder. Note that you need to create the folders
`1nstance_woff` and `instance_woff2` in the same directory as the script file beforehand.

If your fonts are in a different location, or you want to improve on the code, consider changing
the script to your liking.