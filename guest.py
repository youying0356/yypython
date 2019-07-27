name = input ("pls input guest's name:")
filename = "guest.txt"
with open(filename,'w' ) as file_object:
    file_object.write(name)
with open(filename) as file_object1:
    lines = file_object1.readlines()
print(lines)

