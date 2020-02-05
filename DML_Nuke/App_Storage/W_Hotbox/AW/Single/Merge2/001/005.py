#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: conjoint-over
#
#----------------------------------------------------------------------------------------------------------

for nod in nuke.selectedNodes():
    knb = nod.knob("operation")
    knb.setValue("conjoint-over")