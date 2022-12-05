with open("Assets/Course_info.txt") as f:
    file_1 = f.read()

with open("Assets/Course_grade_output.txt") as d:
    file_2 = d.read()

new_file = file_1 + file_2
with open("New file.txt", 'w') as n:
    n.write(new_file)
    