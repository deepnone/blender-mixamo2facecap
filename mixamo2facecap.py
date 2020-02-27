# https://blender.stackexchange.com    docet

import bpy

mixamoToapple = {
    "BrowsDown_Left":"browDown_L",  
    "BrowsDown_Right":"browDown_R", 
    "BrowsUp_Left":"browOuterUp_L",
    "BrowsUp_Right":"browOuterUp_R", 
    "Blink_Left":"eyeBlink_L",
    "Blink_Right":"eyeBlink_R", 
    "Squint_Left":"eyeSquint_L",
    "Squint_Right":"eyeSquint_R",
    "EyesWide_Left":"eyeWide_L",
    "EyesWide_Right":"eyeWide_R",
    "NoseScrunch_Left":"noseSneer_L" ,
    "NoseScrunch_Right":"noseSneer_R",
    "JawForeward":"jawForward",
    "Jaw_Left":"jawLeft",
    "Jaw_Right":"jawRight",
    "Midmouth_Left":"mouthLeft",
    "Midmouth_Right":"mouthRight" ,
    "UpperLipIn":"mouthRollUpper",
    "LowerLipIn":"mouthRollLower",
    "UpperLipOut":"mouthShrugUpper",
    "LowerLipOut":"mouthShrugLower",
    "MouthUp":"mouthClose",
    "Smile_Left":"mouthSmile_L",
    "Smile_Right":"mouthSmile_R",
    "Frown_Left":"mouthFrown_L",
    "Frown_Right":"mouthFrown_R",
    "UpperLipUp_Left":"mouthUpperUp_L",
    "UpperLipUp_Right":"mouthUpperUp_R" ,
    "LowerLipDown_Left":"mouthLowerDown_L",
    "LowerLipDown_Right":"mouthLowerDown_R",
    "JawRotateZ_Right":"mouthPress_L",
    "JawRotateZ_Left":"mouthPress_R",
    "JawRotateY_Right":"mouthStretch_L",
    "JawRotateY_Left":"mouthStretch_R",
    "TongueUp":"tongueOut",
    # the follow are tests
    "BrowsIn_Right":"browInnerUp",
    "CheekPuff_Left":"cheekPuff",
    "Jaw_Down":"jawOpen",
    "MouthNarrow_Left":"mouthFunnel",
    "MouthWhistle_NarrowAdjust_Right":"mouthPucker"
}


selected_object = bpy.context.object
shape_keys = selected_object.data.shape_keys.key_blocks

for myKey in mixamoToapple:
    shape_keys[myKey].name = mixamoToapple[myKey]