# Contributing
This is an instruction on how to report an issue, build, and contribute to this project.

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
- Variable font (.ttf)

If you want to build variable font, use:
```
py -m fontmake -m OverusedGrotesk.designspace -o variable
```

- Static fonts — Desktop (.ttf, .otf)

Or you can generate instances by copy-and-pasting all of the commands below or run `source/build_instances.bat`: 
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


- Webfont (Variable + Static, .woff2)

To build woff2, you can follow the instructions from [@husenlovedisney](https://github.com/husenlovedisney) ([#4](https://github.com/RandomMaerks/Overused-Grotesk/pull/4)).

Or, if you are too lazy to open a new tab:

Open the command prompt as administrator (or use PowerShell). Run the command `wsl --install` or
`wsl --install -d Ubuntu` to install WSL and the Ubuntu distribution of Linux. For more information,
go to Microsoft's [Linux installation article](https://learn.microsoft.com/en-us/windows/wsl/install).

After installation, Ubuntu can be run as a program. Open Ubuntu, then run the following commands:
```
sudo apt update 
sudo apt install build-essential
```

Then, clone Google's [`woff2`](https://github.com/google/woff2) library:
```
git clone --recursive https://github.com/google/woff2.git
cd woff2
make clean all
```

THEN, copy the .ttf files into the `.woff2` directory (which could be found in \\wsl.localhost\Ubuntu
\home\..\woff2). You can also create a new separate folder for the font files (for example: ...\ttf).

Run `./woff2_compress ttf/OverusedGrotesk-VF.ttf` (replace name if necessary) to generate .woff2 for
variable font.

Or, copy the following straight into the command line to convert to .woff2 for static fonts:
```
./woff2_compress ttf/OverusedGrotesk-Light.ttf
./woff2_compress ttf/OverusedGrotesk-LightItalic.ttf
./woff2_compress ttf/OverusedGrotesk-Book.ttf
./woff2_compress ttf/OverusedGrotesk-BookItalic.ttf
./woff2_compress ttf/OverusedGrotesk-Roman.ttf
./woff2_compress ttf/OverusedGrotesk-Italic.ttf
./woff2_compress ttf/OverusedGrotesk-Medium.ttf
./woff2_compress ttf/OverusedGrotesk-MediumItalic.ttf
./woff2_compress ttf/OverusedGrotesk-SemiBold.ttf
./woff2_compress ttf/OverusedGrotesk-SemiBoldItalic.ttf
./woff2_compress ttf/OverusedGrotesk-Bold.ttf
./woff2_compress ttf/OverusedGrotesk-BoldItalic.ttf
./woff2_compress ttf/OverusedGrotesk-ExtraBold.ttf
./woff2_compress ttf/OverusedGrotesk-ExtraBoldItalic.ttf
./woff2_compress ttf/OverusedGrotesk-Black.ttf
./woff2_compress ttf/OverusedGrotesk-BlackItalic.ttf
```

### Designspace file
The `make_designspace.py` allows you to build `OverusedGrotesk.designspace` or whatever name is in the
`path = "..."`.

For more information on how to edit designspace files, check out RoboFont's 
[Creating designspace files with designSpaceLib](https://robofont.com/documentation/tutorials/creating-designspace-files/#creating-designspace-files-with-designspacelib)
and fonttools' [Scripting a designspace](https://fonttools.readthedocs.io/en/latest/designspaceLib/scripting.html).

## Warning

This is an oversimplification of what you can actually do with these tools. I've only included the
necessities required to build and run.

The instruction, which I have to mention again, is heavily dependent on the fact that you are running
a Windows machine, and has not had any required libraries or distributions installed beforehand. I
cannot be liable for any damages caused by improper setup, bugs, incorrect library installation, or
incompatibility.

It is also important that you do extensive research before installing any programs, libraries, or
distributions on your device, and you should at least know what you are doing. If there are 
uncertainties or incomprehension in the process of installing, building, or other, feel free to ask
other people by opening a discussion or an issue.
