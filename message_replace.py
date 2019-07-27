filename = 'learning_python.txt'
with open(filename) as f:
    messages = f.readlines()
for message in messages:#messages是一个list
    message = message.rstrip()#去掉换行符,message是str
    print(message.replace('Python','C'))#str才能用replace()
