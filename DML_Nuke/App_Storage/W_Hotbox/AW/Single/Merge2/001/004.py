#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: color-dodge
#
#----------------------------------------------------------------------------------------------------------

for nod in nuke.selectedNodes():
    knb = nod.knob("operation")
    knb.setValue("color-dodge")