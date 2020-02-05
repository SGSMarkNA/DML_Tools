#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: min
#
#----------------------------------------------------------------------------------------------------------

for nod in nuke.selectedNodes():
    knb = nod.knob("operation")
    knb.setValue("min")