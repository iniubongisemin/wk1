"METHODS FOR OPENING FILES"
"r" # Read - Default value: Opens a file for reading, error if the file does not exist
"a" # Append - Opens a file for appending, creates the file if it does not exist
"w" # Write - Opens a file for writing, creates the file if it does not exist
"x" # Create - Creates the specified file, returns an error if the file exists

"t" # Text - Default value: Text mode
"b" # Binary - Binary mode (e.g images)

f = open("demofile.txt")
# print(f.read())

# If the file is located in a different location, you will have to specify the file path
f = open("C:/Users/eugen/OneDrive/Documents/backend/wk1/first_class/demofile#2.txt", "r")
# print(f.read())

"READ ONLY PARTS OF THE FILE"
# Return first 5 characters of the file
f = open("demofile.txt", "r")
print(f.read(5))

# By calling readline() two times, you can read the two first lines:
f = open("C:/Users/eugen/OneDrive/Documents/backend/wk1/first_class/demofile#2.txt", "r")
# print(f.readline())
# print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:
# for x in f:
    # print(x)
    # pass

file = open("new_file.txt", "w") # Overwrites the entire file with new content!!!
file.write("Woops! I have deleted the content!")
file.close()

file = open("new_file.txt")
print(file.read())
file.close()

new_file = open("file.txt", "x")
new_file.write("new_file.txt created!")
file.close()

new_file = open("file.txt", "r")
print(new_file.read())

# Close files once you are done with them
# f.close()
