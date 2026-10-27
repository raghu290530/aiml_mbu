import os

# Folder containing the files
folder_path = "C:\\Users\\raghu\\PycharmProjects\\AIML\\aiml-b2\\modules\\demo1"

# Get all files in the folder
files = os.listdir(folder_path)

for filename in files:
    old_path = os.path.join(folder_path, filename)

    # Skip folders
    if os.path.isfile(old_path):
        new_filename = "Python_" + filename
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)

        print(filename, "->", new_filename)

print("All files renamed successfully!")