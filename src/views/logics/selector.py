def find_widgets_by_class(parent_widget, widget_object,class_name):
    results = []
    for widget in parent_widget.findChildren(widget_object):
        if class_name in widget.property("class"):
            results.append(widget)
    return results

def find_widget_by_id(parent_widget, widget_object, id):
    return parent_widget.findChild(widget_object, id)

def add_class(widget):
    
    pass
def remove_class(widget): pass