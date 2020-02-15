def main():
    a = 10
    b = 2
    print(a+b)
    file = open("output.txt",'w')
    file.write(str(a+b)+'\n')
    file.write("My name is Vivek\n")
    #print(file.readline())
    file.close()


main()