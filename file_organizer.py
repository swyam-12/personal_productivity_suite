import os
import shutil

class FileOrganizer:
    def organize(self, folder_path):
        try:
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)

                if os.path.isfile(file_path):
                    ext = file.split('.')[-1]
                    new_folder = os.path.join(folder_path, ext)

                    os.makedirs(new_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(new_folder, file))

            print("Files Organized Successfully!")
        except Exception as e:
            print("Error:", e)