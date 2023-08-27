# Contributing
This is a detailed documentation on how to report an issue, build, and contribute to this project.

Note that the instruction on building and generating font files are based on the assumption that 
you are using a Windows machine. If you are using other operating systems like Mac or Linux, please 
change the command lines appropriately.

## Report an issue
If you find any issue with the design, features, or the source, please [open an issue](https://github.com/RandomMaerks/Overused-Grotesk/issues/new/choose). But if you're
just here to have a conversation or discuss certain things, you can [create a discussion](https://github.com/RandomMaerks/Overused-Grotesk/discussions/new/choose).

You can follow this template when you're creating an issue:

[TITLE] Name the issue. Make it as short, but as informative as possible.

- Explain the issue in further detail. What is the issue about? What might be causing the issue?
- Include a screenshot or a video if possible.
- How to re-create the issue? Is there a workaround?
- What device/program are you using?
- Which version of the font? Where did you get the font files?
- A "please fix" at the end for a better chance of responding

You also need to make sure that the issue you're reporting has not already been reported before.

## Build

### Requirements
This typeface is designed using [FontForge](https://github.com/fontforge/fontforge). FontForge 
allows you to open and edit the .sfd files included in the source folder, export .ttf, .otf, or
.ufo for other uses.

[fontmake](https://github.com/googlefonts/fontmake) was also used to create variable font and
generate instances. You can also see further information down below.

### Installation & Setup
You can download FontForge from their [repository](https://github.com/fontforge/fontforge) or their [official website](https://fontforge.org/en-US/).

Before installing fontmake, you have to make sure that you already installed Python 3.8 or later.
A more detailed instruction can be found in the [fontmake repository](https://github.com/googlefonts/fontmake).

Open **Run** and type `cmd`. Then type in the following to install `fontmake`:
```
py -m pip install fontmake
```

Once the installation is complete, enter `cd` then drag in the source directory (assuming you've
downloaded the .zip and extracted it). For example:
```
cd "C:\Users\...\Overused-Grotesk-main\source"
```

### Generate
If you want to build variable font, use:
```
py -m fontmake -m OverusedGrotesk.designspace -o variable
```

Or you can generate instances by copy-and-pasting all of the content from `source/build_instances.sh` 
into the command prompt:
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

The output font files will be in either instance_otf / _ttf (instance generation) or variable_ttf
(variable font). When you generate instances, their respective .ufo file will also be in instance_ufo.

### Designspace file
The `make_designspace.py` allows you to build `OverusedGrotesk.designspace` or whatever name is in the
`path = "..."`.

For more information on how to edit designspace files, check out RoboFont's 
[Creating designspace files with designSpaceLib](https://robofont.com/documentation/tutorials/creating-designspace-files/#creating-designspace-files-with-designspacelib)
and fonttools' [Scripting a designspace](https://fonttools.readthedocs.io/en/latest/designspaceLib/scripting.html).
