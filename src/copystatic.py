import os
import shutil



def delete_dir():
    if os.path.exists("docs"):
        shutil.rmtree("docs")

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for name in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, name)
        dest_path = os.path.join(dest_dir_path, name)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path) 

