import os

class FileHandle():

    @staticmethod
    def create_dir(_path):
        current_dir = ""
        for dir_name in _path.split("/"):
            current_dir += dir_name + "/"
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)
        return _path