from fontTools.ttLib import TTFont

style = [
    "Light",
    "Book",
    "Roman",
    "Medium",
    "SemiBold",
    "Bold",
    "ExtraBold",
    "Black",
    "LightItalic",
    "BookItalic",
    "Italic",
    "MediumItalic",
    "SemiBoldItalic",
    "BoldItalic",
    "ExtraBoldItalic",
    "BlackItalic"
    ]

for x in range(0, len(style)):
    f = TTFont("instance_otf/OverusedGrotesk-" + style[x] + ".otf")
    f.flavor = "woff2"
    f.save("instance_woff2/OverusedGrotesk-" + style[x] + ".woff2")
    print("OverusedGrotesk-",style[x],".woff2 generated.", sep="")

for x in range(0, len(style)):
    f = TTFont("instance_otf/OverusedGrotesk-" + style[x] + ".otf")
    f.flavor = "woff"
    f.save("instance_woff/OverusedGrotesk-" + style[x] + ".woff")
    print("OverusedGrotesk-",style[x],".woff generated.", sep="")

f = TTFont("variable_ttf/OverusedGrotesk-VF.ttf")
f.flavor = "woff2"
f.save("instance_woff2/OverusedGrotesk-VF.woff2")
print("OverusedGrotesk-VF.woff2 generated.")

f = TTFont("variable_ttf/OverusedGrotesk-VF.ttf")
f.flavor = "woff"
f.save("instance_woff/OverusedGrotesk-VF.woff")
print("OverusedGrotesk-VF.woff generated.")
