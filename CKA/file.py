import os
for i in range(1, 50):
    file_name = f"question{i}"
    with open(file_name, "w") as file:
        os.remove("# This is file " + file_name)