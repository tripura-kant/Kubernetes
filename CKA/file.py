for i in range(1, 50):
    file_name = f"question{i}.yaml"
    with open(file_name, "w") as file:
        file.write("# This is file " + file_name)