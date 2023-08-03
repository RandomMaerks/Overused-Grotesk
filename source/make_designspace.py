import os
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Overused Grotesk"

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

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "OverusedGrotesk-Light.ufo"
s0.familyName = familyName
s0.styleName = "Light"
s0.location = dict(weight=300)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "OverusedGrotesk-Black.ufo"
s1.familyName = familyName
s1.styleName = "Black"
s1.location = dict(weight=900)
doc.addSource(s1)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'OverusedGrotesk-Light'
i0.familyName = familyName
i0.styleName = "Light"
i0.path = os.path.join(root, "instances", "OverusedGrotesk-Light.ufo")
i0.location = dict(weight=300)
i0.kerning = True
i0.info = True
doc.addInstance(i0)

i1 = InstanceDescriptor()
i1.name = 'OverusedGrotesk-Book'
i1.familyName = familyName
i1.styleName = "Book"
i1.path = os.path.join(root, "instances", "OverusedGrotesk-Book.ufo")
i1.location = dict(weight=350)
i1.kerning = True
i1.info = True
doc.addInstance(i1)

i2 = InstanceDescriptor()
i2.name = 'OverusedGrotesk-Roman'
i2.familyName = familyName
i2.styleName = "Regular"
i2.path = os.path.join(root, "instances", "OverusedGrotesk-Roman.ufo")
i2.location = dict(weight=400)
i2.kerning = True
i2.info = True
doc.addInstance(i2)

i3 = InstanceDescriptor()
i3.name = 'OverusedGrotesk-Medium'
i3.familyName = familyName
i3.styleName = "Medium"
i3.path = os.path.join(root, "instances", "OverusedGrotesk-Medium.ufo")
i3.location = dict(weight=500)
i3.kerning = True
i3.info = True
doc.addInstance(i3)

i4 = InstanceDescriptor()
i4.name = 'OverusedGrotesk-SemiBold'
i4.familyName = familyName
i4.styleName = "SemiBold"
i4.path = os.path.join(root, "instances", "OverusedGrotesk-SemiBold.ufo")
i4.location = dict(weight=600)
i4.kerning = True
i4.info = True
doc.addInstance(i4)

i5 = InstanceDescriptor()
i5.name = 'OverusedGrotesk-Bold'
i5.familyName = familyName
i5.styleName = "Bold"
i5.path = os.path.join(root, "instances", "OverusedGrotesk-Bold.ufo")
i5.location = dict(weight=700)
i5.kerning = True
i5.info = True
doc.addInstance(i5)

i6 = InstanceDescriptor()
i6.name = 'OverusedGrotesk-ExtraBold'
i6.familyName = familyName
i6.styleName = "ExtraBold"
i6.path = os.path.join(root, "instances", "OverusedGrotesk-ExtraBold.ufo")
i6.location = dict(weight=800)
i6.kerning = True
i6.info = True
doc.addInstance(i6)

i7 = InstanceDescriptor()
i7.name = 'OverusedGrotesk-Black'
i7.familyName = familyName
i7.styleName = "Black"
i7.path = os.path.join(root, "instances", "OverusedGrotesk-Black.ufo")
i7.location = dict(weight=900)
i7.kerning = True
i7.info = True
doc.addInstance(i7)

#--------
# saving
#--------

path = "OverusedGrotesk.designspace"
doc.write(path)