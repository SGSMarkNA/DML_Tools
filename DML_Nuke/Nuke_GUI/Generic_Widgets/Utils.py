import nuke

#----------------------------------------------------------------------
def add_data_knob(node,name,knbtype,visable=True,defalutValue=None):
	"""Adds The knob of knob Class knbtype if the knob does not allready exist"""
	if not name in node.knobs().keys():
		knb = knbtype(name)
		node.addKnob(knb)
		knb.setVisable(visable)
		if defalutValue is not None:
			knb.setValue(defalutValue)
	else:
		knb = node.knob(name)
	return knb
