import os, sys, json, shutil

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir, os.path.pardir))
DB_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "bin", "db"))

sys.path.append(SRC_DIR)
from logic.utils.file_handle import FileHandle

def info_write(payload):
    if "option" not in payload.keys(): return { "data": False, "message": "option not in payload.keys()" }
    option = payload["option"]
    option_dir = os.path.abspath(os.path.join(DB_DIR, option))
    FileHandle.create_dir(option_dir)
    img_dir = os.path.abspath(os.path.join(option_dir, "images"))
    if "real-estate" == option:
        if "images" not in payload.keys() or not payload["images"]: return { "data": False, "message": "images not in payload.keys()"}
        if "id" not in payload.keys(): return { "data": False, "message": "id not in payload.keys()"}
        current_img_dir = os.path.abspath(os.path.join(img_dir, payload["id"]))
        if os.path.exists(current_img_dir): return { "data": False, "message": f"image dir with name [{payload['id']}] existed"}
        else:
            FileHandle.create_dir(current_img_dir)
            destination_imgs = img_save(payload["images"], current_img_dir)
            if not destination_imgs: return { "data": False, "message": f"An error occurred while copying the image from directory {payload['images']} to directory {current_img_dir}."}
        payload["images"] = destination_imgs
        FileHandle.create_dir(img_dir)
        file_info = None
        real_estate_file = os.path.abspath(os.path.join(option_dir, "real-estate.json"))
        if not os.path.exists(real_estate_file): file_info = {}
        else:
            with open(real_estate_file, "r", encoding="utf8") as f:
                file_info = json.load(f)
        if file_info == {}: file_info = {
            "rent": [],
            "sell": [],
            "assignment": [],
        }
        if "type" not in payload.keys(): return { "data": False, "message": "type not in payload.keys()" }
        file_info[payload["type"]].append(payload)
        
        with open(real_estate_file, "w", encoding="utf8") as f:
            json.dump(file_info, f, indent=4)
        return { "data": payload, "message": "successfully"}
    elif "fashion" == option: pass
    elif "food" == option: pass
    elif "travel" == option: pass
    elif "miscellaneous" == option:
        if "images" not in payload.keys() or not payload["images"]: return { "data": False, "message": "images not in payload.keys()"}
        if "id" not in payload.keys(): return { "data": False, "message": "id not in payload.keys()"}
        if "title" not in payload.keys() or not payload["title"]: return { "data": False, "message": "title not in payload.keys() or not title"}
        if "description" not in payload.keys() or not payload["description"]: return { "data": False, "message": "description not in payload.keys() or not description"}
        current_img_dir = os.path.abspath(os.path.join(img_dir, payload["id"]))
        if os.path.exists(current_img_dir): return { "data": False, "message": f"image dir with name [{payload['id']}] existed"}
        else:
            FileHandle.create_dir(current_img_dir)
            destination_imgs = img_save(payload["images"], current_img_dir)
            if not destination_imgs: return { "data": False, "message": f"An error occurred while copying the image from directory {payload['images']} to directory {current_img_dir}."}
        payload["images"] = destination_imgs
        FileHandle.create_dir(img_dir)
        file_info = None
        miscellaneous_file = os.path.abspath(os.path.join(option_dir, "miscellaneous.json"))
        if not os.path.exists(miscellaneous_file): file_info = {}
        else:
            with open(miscellaneous_file, "r", encoding="utf8") as f:
                file_info = json.load(f)
        file_info[payload["id"]] = {
            "images": payload["images"],
            "title": payload["title"],
            "description": payload["description"]
        }
        with open(miscellaneous_file, "w", encoding="utf8") as f:
            json.dump(file_info, f, indent=4)
        return { "data": payload, "message": "successfully"}

def info_read():

    pass

def info_del():

    pass

def img_save(imgs, destination_dir):
    if not os.path.exists(destination_dir): return { "data": False, "message": f"{destination_dir} is not existed"}
    destination_name = destination_dir.split("/")[-1] if destination_dir.split("/")[-1] != "" else destination_dir.split("/")[-2]
    for index, img in enumerate(imgs):
        ext_name = os.path.basename(img).split(".")[-1]
        if ext_name.lower() not in ["jpg", "jpeg", "png", "gif"]: continue
        destination_path = os.path.abspath(os.path.join(destination_dir, f"{destination_name}_{index}.{ext_name}"))
        shutil.copy2(img, destination_path)

    return { "data": destination_dir, "message": "successfully"}

def img_get(img_dir):
    if not os.path.exists(img_dir): return { "data": False, "message": f"{img_dir} is not existed"}
    files = os.listdir(img_dir)
    imgs = []
    for file in files:
        ext_name = os.path.basename(file).split(".")[-1]
        if ext_name.lower() in ["jpg", "jpeg", "png", "gif"]:
            imgs.append(os.path.abspath(os.path.join(img_dir, file)))
    return { "data" : imgs, "message": "successfullly"}

def img_del(img_dir):
    if not os.path.exists(img_dir): return { "data": False, "message": f"{img_dir} is not existed"}
    shutil.rmtree(img_dir)
    return { "data" : True, "message": "successfullly"}
    
