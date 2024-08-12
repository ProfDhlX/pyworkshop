# file = open("D:\codes\pyfile\lala.txt",'r')
# content = file.read()
# file.close()
# print(content)

# with open('D:\codes\pyfile\lala.txt','r') as file:
#     thing = file.read()
#     print(thing)

# with open('D:\codes\pyfile\lala.txt','a') as file:
    # content =("lala land")
    # content_2 = (input("enter name : "))
    # file.write(content)
    # file.write( content_2)

    # print(content_2)

with open('Screenshot 2024-07-27 154443.png','rb') as file:
    content = file.read()
    print(content)
file.close()