filename = 'learning_python.txt'
with open(filename) as file_object:
    print(file_object.read())
    print(file_object.readline())
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)
