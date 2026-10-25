import os
from fontTools.ttLib import TTFont

style = (
    "Light",
    "Book",
    "Regular",
    "Medium",
    "SemiBold",
    "Bold",
    "ExtraBold",
    "Black"
    )
'''
    "LightItalic",
    "BookItalic",
    "Italic",
    "MediumItalic",
    "SemiBoldItalic",
    "BoldItalic",
    "ExtraBoldItalic",
    "BlackItalic"
    )
'''

fontname = "OverusedGrotesk"

if not os.path.exists("instance_woff"):
    os.makedirs("instance_woff")
if not os.path.exists("instance_woff2"):
    os.makedirs("instance_woff2")

for x in range(0, len(style)):
    f = TTFont(f"instance_otf/{fontname}-{style[x]}.otf", flavor="woff2")
    f.save(f"instance_woff2/{fontname}-{style[x]}.woff2")
    print(f"{fontname}-{style[x]}.woff2 generated.", sep="")

for x in range(0, len(style)):
    f = TTFont(f"instance_otf/{fontname}-{style[x]}.otf", flavor="woff")
    f.save(f"instance_woff/{fontname}-{style[x]}.woff")
    print(f"{fontname}-{style[x]}.woff generated.", sep="")

f = TTFont(f"variable_ttf/{fontname}-VF.ttf", flavor="woff2")
f.save(f"variable_ttf/{fontname}-VF.woff2")
print(f"{fontname}-VF.woff2 generated.")

f = TTFont(f"variable_ttf/{fontname}-VF.ttf", flavor="woff")
f.save(f"variable_ttf/{fontname}-VF.woff")
print(f"{fontname}-VF.woff generated.")
