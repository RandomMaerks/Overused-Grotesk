# 🛠 Contributing
This is an instruction on how to contribute to this project.

Note that the instruction on building and generating font files are based on the assumption that you are using a Windows machine. If you are using other operating systems like Mac or Linux, please change the command lines appropriately.




## ⚠ Warning

This instruction is based on my own method to generate and compress fonts, and it is generally not the best practice. If you have a more efficient solution, please let me and potential contributors know.

Additionally, please do not follow any instruction that you do not understand. Feel free to ask other people for help, and make sure you have full control and sufficient knowledge of the things you are doing.




## ❗ Report an issue
If you find any issue with the design, features, or the source, please [open an issue](https://github.com/RandomMaerks/Overused-Grotesk/issues/new/choose). But if you're just here to have a conversation or discuss certain things, you can [create a discussion](https://github.com/RandomMaerks/Overused-Grotesk/discussions/new/choose).

You can follow this template when you're creating an issue:

```
[TITLE] Name the issue. Make it as short, but as informative as possible.

- Explain the issue in further detail.
- Include a screenshot or a video if possible.
- How to re-create the issue? Is there a workaround?
- What device/program are you using?
- Which version of the font? Where did you get the font files?
- A "please fix" at the end for a better chance of responding
```
Make sure that the issue has not already been reported before.




## 🔨 Build

### ▶ Requirements
This typeface is now developed and maintained using [FontLab](https://www.fontlab.com/font-editor/fontlab/). FontLab allows you to open and edit the .vfc files included in the source folder, and export .ttf, .otf, or .ufo for other uses.

[fontmake](https://github.com/googlefonts/fontmake) is also used to create variable font and generate instances.

By installing fontmake, [fonttools](https://github.com/fonttools/fonttools) is automatically included, which is used for compressing `.otf` fonts into `.woff` and `.woff2` fonts. Though, you will also need to install [brotli](https://github.com/google/brotli) as well.



### ▶ Installation & Setup
**FontLab** is commercially-licensed software. You can download the free trial or purchase a license from their [website](https://www.fontlab.com/font-editor/fontlab/) (though I advise only purchasing if you're using it professionally or you want to use it for many other projects).

Before installing **fontmake**, you have to make sure that you already installed Python 3.9 or later. A more detailed instruction can be found in the [fontmake repository](https://github.com/googlefonts/fontmake).

Note that you can also create a virtual environment so none of the installed dependencies interfere with any other libraries. Do:

```
py -m venv venv
```

where the second `venv` is the relative path to the virtual environment. You can change it to wherever you want, as long as you know where it is stored. Afterwards, activate the environment by doing:

```
venv\Scripts\activate
```

If successful, the `(venv)` prefix will appear in front of your command line. If you want to deactivate this at any time, type `deactivate`, press Enter, and it will automatically leave the virtual environment.

To install `fontmake`, run:

```
pip install fontmake
```

Once complete, redirect the current directory to the source folder. For example:
```
cd "C:\Users\...\Overused-Grotesk-main\source"
```


### ▶ Getting the appropriate files to generate the fonts
FontLab has a feature to export both `.designspace` and `.ufo` files at the same time. To do that, go to `File > Export Font As` or press `Ctrl + E`. The export menu will pop up, and you can select the option to export `DesignSpace + UFO`.

<img width="292" height="588" alt="image" src="https://github.com/user-attachments/assets/a06882ca-875d-4f42-afc6-f7dba6aa9825" />


The `.ufo` files (or folders) contain the information for each font master, and the `.designspace` file contains instruction to connect all masters together.



### ▶ Generate
- _**Variable font (`.ttf`)**_

If you want to build variable font, do:
```
py -m fontmake -m OverusedGrotesk.designspace -o variable
```

- _**Static fonts (`.ttf`, `.otf`)**_

You can generate instances by using: 
```
py -m fontmake -m OverusedGrotesk.designspace -i
```

The output font files will be in either `instance_otf` / `instance_ttf` (instance generation) or `variable_ttf` (variable font). When you generate instances, their respective `.ufo` file will also be in `instance`.


- _**Compression (`.woff`, `.woff2`)**_

You can compress the `.otf` fonts in the `instance_otf` folder into `.woff2` and `.woff` fonts by running the `webfont_gen.py` file in the source folder. After running, the compressed `.woff` fonts will be in the `instance_woff` folder and `.woff2` fonts in the `instance_woff2` folder.

If your fonts are in a different location, or you want to improve on the code, consider changing the script to your liking.
