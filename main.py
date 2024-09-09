import os
import shutil
import tempfile
from pathlib import Path

def delete_folder_contents(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except PermissionError:
                print(f"Skipped (in use): {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
                
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                shutil.rmtree(dir_path)
                print(f"Deleted folder: {dir_path}")
            except PermissionError:
                print(f"Skipped (in use): {dir_path}")
            except Exception as e:
                print(f"Error deleting {dir_path}: {e}")

def clear_temp_and_prefetch():
    # Get the user's TEMP directory
    user_temp_dir = tempfile.gettempdir()

    # Get the system's TEMP directory
    system_temp_dir = Path("C:/Windows/Temp")

    # Get the system's PREFETCH directory
    prefetch_dir = Path("C:/Windows/Prefetch")

    # Clear user's TEMP directory
    print("Clearing user's TEMP directory...")
    delete_folder_contents(user_temp_dir)

    # Clear system's TEMP directory
    print("Clearing system's TEMP directory...")
    if system_temp_dir.exists():
        delete_folder_contents(system_temp_dir)
    else:
        print("System TEMP directory does not exist or is inaccessible.")

    # Clear PREFETCH directory
    print("Clearing PREFETCH directory...")
    if prefetch_dir.exists():
        delete_folder_contents(prefetch_dir)
    else:
        print("PREFETCH directory does not exist or is inaccessible.")

if __name__ == "__main__":
    clear_temp_and_prefetch()
