import os
import shutil

def remove_pyc_and_pycache(root_dir="."):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Remove .pyc files
        for filename in filenames:
            if filename.endswith(".pyc"):
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    print(f"Removed file: {file_path}")
                except Exception as e:
                    print(f"Failed to remove {file_path}: {e}")
        # Remove __pycache__ directories
        for dirname in dirnames:
            if dirname == "__pycache__":
                dir_path = os.path.join(dirpath, dirname)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Removed directory: {dir_path}")
                except Exception as e:
                    print(f"Failed to remove {dir_path}: {e}")

if __name__ == "__main__":
    remove_pyc_and_pycache()
