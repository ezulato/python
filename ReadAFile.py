# access a file
file = open ("numero.txt", "r")
content = file.readlines()
print(content)
file.close()
