# a = ["dent","hole"]
# b = ["burr","thread_presence"]
# c = ["thread_absence","chamfer_presence"]
# d = ["chamfer_absence"]

# n = a + b + c + d
# print(n)

# import os

# path = "/home/divya/Desktop/Divya/txt"
# os.chdir(path)
# def read_text_file(file_path):
#     with open(file_path, 'r') as f:
#         print(f.read())
       
# for file in os.listdir():
#     if file.endswith(".txt"):
#         file_path = f"{path}/{file}"
#         read_text_file(file_path)


# import os
# new_list = []
# for root, dirs, files in os.walk("/home/divya/Desktop/Divya/txt"):
#     for file in files:
#         if file.endswith('.txt'):
#             with open(os.path.join(root, file), 'r') as f:
#                 text = f.read()
#                 new_list.append(text)
# print(new_list)


filenames = ["1.txt", "2.txt", "3.txt", "4.txt"]
list = []
with open("output.txt","w") as output:
    for filename in filenames:
        with open(filename) as f:
            contents = f.read()
            list.append(contents)
            output.write(contents)
            print(contents)
print(list)
