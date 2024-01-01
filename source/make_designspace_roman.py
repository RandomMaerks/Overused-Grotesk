import os
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Overused Grotesk Roman"

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 900
a1.minimum = 300
a1.default = 300
a1.name = "weight"
a1.tag = "wght"
doc.addAxis(a1)

a2 = AxisDescriptor()
a2.maximum = 0
a2.minimum = 0
a2.default = 0
a2.name = "slant"
a2.tag = "slnt"
doc.addAxis(a2)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "OverusedGrotesk-Light.ufo"
s0.familyName = familyName
s0.styleName = "Light"
s0.location = dict(weight=300,slant=0)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "OverusedGrotesk-Black.ufo"
s1.familyName = familyName
s1.styleName = "Black"
s1.location = dict(weight=900,slant=0)
doc.addSource(s1)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'OverusedGrotesk-Light'
i0.familyName = familyName
i0.styleName = "Light"
i0.path = os.path.join(root, "instances", "OverusedGrotesk-Light.ufo")
i0.location = dict(weight=300,slant=0)
i0.kerning = True
i0.info = True
i0.styleMapFamilyName = "Overused Grotesk Light"
i0.styleMapStyleName = "regular"
doc.addInstance(i0)

i1 = InstanceDescriptor()
i1.name = 'OverusedGrotesk-Book'
i1.familyName = familyName
i1.styleName = "Book"
i1.path = os.path.join(root, "instances", "OverusedGrotesk-Book.ufo")
i1.location = dict(weight=375,slant=0)
i1.kerning = True
i1.info = True
i1.styleMapFamilyName = "Overused Grotesk Book"
i1.styleMapStyleName = "regular"
doc.addInstance(i1)

i2 = InstanceDescriptor()
i2.name = 'OverusedGrotesk-Roman'
i2.familyName = familyName
i2.styleName = "Regular"
i2.path = os.path.join(root, "instances", "OverusedGrotesk-Roman.ufo")
i2.location = dict(weight=450,slant=0)
i2.kerning = True
i2.info = True
i2.styleMapFamilyName = "Overused Grotesk"
i2.styleMapStyleName = "regular"
doc.addInstance(i2)

i3 = InstanceDescriptor()
i3.name = 'OverusedGrotesk-Medium'
i3.familyName = familyName
i3.styleName = "Medium"
i3.path = os.path.join(root, "instances", "OverusedGrotesk-Medium.ufo")
i3.location = dict(weight=525,slant=0)
i3.kerning = True
i3.info = True
i3.styleMapFamilyName = "Overused Grotesk Medium"
i3.styleMapStyleName = "regular"
doc.addInstance(i3)

i4 = InstanceDescriptor()
i4.name = 'OverusedGrotesk-SemiBold'
i4.familyName = familyName
i4.styleName = "SemiBold"
i4.path = os.path.join(root, "instances", "OverusedGrotesk-SemiBold.ufo")
i4.location = dict(weight=610,slant=0)
i4.kerning = True
i4.info = True
i4.styleMapFamilyName = "Overused Grotesk SemiBold"
i4.styleMapStyleName = "regular"
doc.addInstance(i4)

i5 = InstanceDescriptor()
i5.name = 'OverusedGrotesk-Bold'
i5.familyName = familyName
i5.styleName = "Bold"
i5.path = os.path.join(root, "instances", "OverusedGrotesk-Bold.ufo")
i5.location = dict(weight=710,slant=0)
i5.kerning = True
i5.info = True
i5.styleMapFamilyName = "Overused Grotesk"
i5.styleMapStyleName = "bold"
doc.addInstance(i5)

i6 = InstanceDescriptor()
i6.name = 'OverusedGrotesk-ExtraBold'
i6.familyName = familyName
i6.styleName = "ExtraBold"
i6.path = os.path.join(root, "instances", "OverusedGrotesk-ExtraBold.ufo")
i6.location = dict(weight=800,slant=0)
i6.kerning = True
i6.info = True
i6.styleMapFamilyName = "Overused Grotesk ExtraBold"
i6.styleMapStyleName = "regular"
doc.addInstance(i6)

i7 = InstanceDescriptor()
i7.name = 'OverusedGrotesk-Black'
i7.familyName = familyName
i7.styleName = "Black"
i7.path = os.path.join(root, "instances", "OverusedGrotesk-Black.ufo")
i7.location = dict(weight=900,slant=0)
i7.kerning = True
i7.info = True
i7.styleMapFamilyName = "Overused Grotesk Black"
i7.styleMapStyleName = "regular"
doc.addInstance(i7)


#-------
# rules
#-------
# Currently dropping support for a_spur because i'm lazy
# and it will take a long time to add accents for it
# It looks cool but I'm not so just ignore it
"""
r1 = RuleDescriptor()
r1.name = 'latin-a_spur-wght'
r1.conditionSets = [
    [
        { 'name': "weight", 'minimum': 300, 'maximum': 650 },
        { 'name': "slant", 'minimum': -10, 'maximum': 0 },
    ]
]
r1.subs = [("a", "a.spur")]
doc.addRule(
"""
#--------
# saving
#--------

path = "OverusedGroteskRoman.designspace"
doc.write(path)
