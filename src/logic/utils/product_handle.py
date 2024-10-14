import os, json, sys

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir,))
DB_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "bin", "db"))

class ProductHandle():
    @staticmethod
    def get_product_buy_id(payload):
        if "option" not in payload.keys(): return { "data": False, "message": "option not in payload.keys()"}
        if "id" not in payload.keys(): return { "data": False, "message": "id not in payload.keys()"}
        product_path = os.path.abspath(os.path.join(DB_DIR, payload["option"], f"{payload['option']}.json"))
        if not os.path.exists(product_path): return { "data": False, "message": "product path not exists" }
        with open(product_path, "r", encoding="utf8") as f:
            data = json.load(f)
            if payload["option"] == "real-estate":
                for products in data.values():
                    for product in products:
                        if "id" in product.keys() and product["id"].lower() == payload["id"].lower(): return product
            elif payload["option"] == "miscellaneous":
                for id in data.keys():
                    if id.lower() == payload["id"].lower(): return data[id]
        return { "data": False, "message": "id not in data" }
    @staticmethod
    def get_images_buy_path(_path):
        if not os.path.exists(_path): return { "data": False, "message": "images path not exists" }
        imgs_in_dir = []
        list_file = os.listdir(_path)
        list_file.sort()
        for index, file in enumerate(list_file):
            if index > 6: break
            if file.split(".")[-1] in ["jpg", "png", "jpeg"]: imgs_in_dir.append(os.path.abspath(os.path.join(_path, file)))
        return imgs_in_dir



if __name__ == "__main__":
    ProductHandle.get_images_buy_path("/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.s.100924.5244")