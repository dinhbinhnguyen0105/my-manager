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
    
    @staticmethod
    def find_data_file(_path):
        print(os.path.isdir(_path))

        current_path = _path

        for root, dirs, files in os.walk(current_path):
            print(f"root: {root} - dirs: {dirs} - files: {files}")

    @staticmethod
    def get_data_file(_path):
        results = []
        for root, dirs, files in os.walk(_path):
            for file in files:
                file_ext = file.split(".")[-1].lower()
                if file_ext == "json":
                    results.append(os.path.abspath(os.path.join(root, file)))
        return results
