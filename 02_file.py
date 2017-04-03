file = open("input_file.txt", "r")
content = file.read()
print (content)


#transform content to a list of lines
file.seek(0)
content = file.readlines()
print (content)


#remove the last characters if exist
content = [i.rstrip('\n') for i in content]
print (content)

s = "hello"
print (s.rstrip('oe'))
print (s.rstrip('ol'))
print (s.rstrip('xol'))

file.close()