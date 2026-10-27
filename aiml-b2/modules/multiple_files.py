import os

# Folder to store files
folder = "C:\\Users\\raghu\\PycharmProjects\\AIML\\aiml-b2\\modules\\demo1"

# Create folder if it does not exist
os.makedirs(folder, exist_ok=True)

# Create 10 files
for i in range(1, 11):
    filename = f"file_{i}.txt"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as file:
        file.write(f"This is file number {i}")

    print(filename, "created successfully")

print("All files created!")