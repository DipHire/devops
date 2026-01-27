
# writing file
# file = open("data.txt", "w")
# file.write("Welcome to Python File Handling")
# file.close()


#readling file
# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

#Appending Data to a File
# file = open("data.txt", "a")
# file.write("\nThis is new line")
# file.close()

#with keyword
# with open("marks.txt", "w") as f:
#     f.write("dip 85\nshubh 90\nparth 88")


# get specific lines
f=open("marks.txt","r")
lines=f.readlines() 
print(lines[1])
f.close()
