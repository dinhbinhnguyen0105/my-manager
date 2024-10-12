import os, json
MY_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.abspath(os.path.join( MY_DIR, os.path.pardir, os.path.pardir, os.path.pardir, "bin", "template" ))

class TemplateHandle():
    @staticmethod
    def _read_template(template_name):
        _ = os.path.abspath(os.path.join(TEMPLATE_DIR, f"{template_name}.json"))
        if not os.path.exists(_): return { "data": False, "message": f"{_} is not existed"}
        with open(_) as f:
            return json.load(f)
    
    @staticmethod
    def get_template(payload):
        if "template_name" not in payload.keys(): return { "data": False, "message": "'template_name' not in payload.keys()"}
        else: template_obj = TemplateHandle._read_template(payload["template_name"])
        if "default" not in template_obj.keys(): return { "data": False, "message": "'default' not in template_obj.keys()"}
        else: pass
            


TemplateHandle._read_template("real-estate")
