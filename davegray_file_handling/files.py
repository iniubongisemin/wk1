# r - read
# a - append
# w - write
# x - create

f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)
f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist!")
finally:
    f.close()

# Append - Creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Bryan")
f.close() # Close the file so changes are saved!

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of my context!")
f.close()

f = open()