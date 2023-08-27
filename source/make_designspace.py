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

a2 = AxisDescriptor()
a2.maximum = 0
a2.minimum = -10
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

s2 = SourceDescriptor()
s2.path = "OverusedGrotesk-LightItalic.ufo"
s2.familyName = familyName
s2.styleName = "Light Italic"
s2.location = dict(weight=300,slant=-10)
doc.addSource(s2)

s3 = SourceDescriptor()
s3.path = "OverusedGrotesk-BlackItalic.ufo"
s3.familyName = familyName
s3.styleName = "Black Italic"
s3.location = dict(weight=900,slant=-10)
doc.addSource(s3)

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
i1.location = dict(weight=350,slant=0)
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
i2.location = dict(weight=400,slant=0)
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
i3.location = dict(weight=500,slant=0)
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
i4.location = dict(weight=600,slant=0)
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
i5.location = dict(weight=700,slant=0)
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

i8 = InstanceDescriptor()
i8.name = 'OverusedGrotesk-LightItalic'
i8.familyName = familyName
i8.styleName = "Light Italic"
i8.path = os.path.join(root, "instances", "OverusedGrotesk-LightItalic.ufo")
i8.location = dict(weight=300,slant=-10)
i8.kerning = True
i8.info = True
i8.styleMapFamilyName = "Overused Grotesk Light"
i8.styleMapStyleName = "italic"
doc.addInstance(i8)

i9 = InstanceDescriptor()
i9.name = 'OverusedGrotesk-BookItalic'
i9.familyName = familyName
i9.styleName = "Book Italic"
i9.path = os.path.join(root, "instances", "OverusedGrotesk-BookItalic.ufo")
i9.location = dict(weight=350,slant=-10)
i9.kerning = True
i9.info = True
i9.styleMapFamilyName = "Overused Grotesk Book"
i9.styleMapStyleName = "italic"
doc.addInstance(i9)

i10 = InstanceDescriptor()
i10.name = 'OverusedGrotesk-Italic'
i10.familyName = familyName
i10.styleName = "Italic"
i10.path = os.path.join(root, "instances", "OverusedGrotesk-Italic.ufo")
i10.location = dict(weight=400,slant=-10)
i10.kerning = True
i10.info = True
i10.styleMapFamilyName = "Overused Grotesk"
i10.styleMapStyleName = "italic"
doc.addInstance(i10)

i11 = InstanceDescriptor()
i11.name = 'OverusedGrotesk-MediumItalic'
i11.familyName = familyName
i11.styleName = "Medium Italic"
i11.path = os.path.join(root, "instances", "OverusedGrotesk-MediumItalic.ufo")
i11.location = dict(weight=500,slant=-10)
i11.kerning = True
i11.info = True
i11.styleMapFamilyName = "Overused Grotesk Medium"
i11.styleMapStyleName = "italic"
doc.addInstance(i11)

i12 = InstanceDescriptor()
i12.name = 'OverusedGrotesk-SemiBoldItalic'
i12.familyName = familyName
i12.styleName = "SemiBold Italic"
i12.path = os.path.join(root, "instances", "OverusedGrotesk-SemiBoldItalic.ufo")
i12.location = dict(weight=600,slant=-10)
i12.kerning = True
i12.info = True
i12.styleMapFamilyName = "Overused Grotesk SemiBold"
i12.styleMapStyleName = "italic"
doc.addInstance(i12)

i13 = InstanceDescriptor()
i13.name = 'OverusedGrotesk-BoldItalic'
i13.familyName = familyName
i13.styleName = "Bold Italic"
i13.path = os.path.join(root, "instances", "OverusedGrotesk-BoldItalic.ufo")
i13.location = dict(weight=700,slant=-10)
i13.kerning = True
i13.info = True
i13.styleMapFamilyName = "Overused Grotesk"
i13.styleMapStyleName = "bold italic"
doc.addInstance(i13)

i14 = InstanceDescriptor()
i14.name = 'OverusedGrotesk-ExtraBoldItalic'
i14.familyName = familyName
i14.styleName = "ExtraBold Italic"
i14.path = os.path.join(root, "instances", "OverusedGrotesk-ExtraBoldItalic.ufo")
i14.location = dict(weight=800,slant=-10)
i14.kerning = True
i14.info = True
i14.styleMapFamilyName = "Overused Grotesk ExtraBold"
i14.styleMapStyleName = "italic"
doc.addInstance(i14)

i15 = InstanceDescriptor()
i15.name = 'OverusedGrotesk-BlackItalic'
i15.familyName = familyName
i15.styleName = "Black Italic"
i15.path = os.path.join(root, "instances", "OverusedGrotesk-BlackItalic.ufo")
i15.location = dict(weight=900,slant=-10)
i15.kerning = True
i15.info = True
i15.styleMapFamilyName = "Overused Grotesk Black"
i15.styleMapStyleName = "italic"
doc.addInstance(i15)

#-------
# rules
#-------

#r1 = RuleDescriptor(name='latin-a_italic')
#r1.conditionSets = [ 
#    [
#        {'name': "slant", 'minimum': -10, 'maximum': -5 },
#    ],
#]
#r1.subs = [("a", "a.ss01"),]
#doc.addRule(r1)

#--------
# saving
#--------

path = "OverusedGrotesk.designspace"
doc.write(path)