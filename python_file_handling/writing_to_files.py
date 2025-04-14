"WRITING TO AN EXISTING FILE"
"To write to an existing file, you must add a parameter to the open() function:"

"a" # Append - will append to the end of the file
"w" # Write - will overwrite any existing content

f = open("C:/Users/eugen/OneDrive/Documents/backend/wk1/first_class/demofile#2.txt", "a")
f.write("Hey I'm the latest content in this page")
f.close()

f = open("C:/Users/eugen/OneDrive/Documents/backend/wk1/first_class/demofile#2.txt", "r")
print(f.read())

f = open("C:/Users/eugen/OneDrive/Documents/backend/wk1/first_class/demofile#2.txt", "w")
