a = '''
"a very long string with  emails"
emails = []
3.seconds
'''
# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

#  file write 
# st = "bgoi."
# f = open("file.txt","w")
# f.write(st)
# f.close()

f=  open("file.txt")

# line1 = f.readline()
# print(line1,type(line1))
# f.close

# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()    

# st = "his highness"
# f1 = open("myfile.txt","a")
# f1.write(st)
# f1.close() 
print(f.read())
f.close()
with open ("file.txt") as f :
    print(f.read())