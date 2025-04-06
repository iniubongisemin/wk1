"""
7. File Extension Extractor
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""
def file_name_extractor():
    file_name = input("Please type your file name: ")
    output = file_name.split(".") 
    print("." + output[1])
    # split_file_name = file_name[-5:]
    # print(f"Output : {split_file_name}")

    # split_file_name = [dot for dot in file_name if dot=="." break return ]

file_name_extractor()