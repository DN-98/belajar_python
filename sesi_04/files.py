# file = open('Hack8_Sample_Text.txt')
# file.close()

# print(file)


try:
    f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
    # perform file operations
    # print(f.read().split("\n"))
    
    #    print(f.read(10))
    #    print(f.read())
    
    # print(f.tell())

    # f.seek(0)
    # for line in f:
    #     print(line, end = '')
    
    # f.seek(0)
    # print(f.readline())
except:
    print("cannot open file")
else:
    f.close()
finally:
    print("end of file routine")

# with open("sample.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")