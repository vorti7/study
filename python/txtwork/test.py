
for file in range(1,101):
    filenum = (str(file)).zfill(3)
    f1 = open("./problem/ex"+filenum+".txt", 'rt')
    f_ = open("./problem/ex/ex"+filenum+".txt", 'wt')
    # f2 = open("./problem/ex"+filenum+"_q.txt", 'wt')
    # f3 = open("./problem/ex"+filenum+"_input.txt", 'wt')
    # f4 = open("./problem/ex"+filenum+"_output.txt", 'wt')
    # f5 = open("./problem/ex"+filenum+"_s.txt", 'wt')
    # f6 = open("./problem/ex"+filenum+".txt", 'wt')
    # f7 = open("./problem/ex"+filenum+"_q.txt", 'wt')
    # f8 = open("./problem/ex"+filenum+"_input.txt", 'wt')
    # f9 = open("./problem/ex"+filenum+"_output.txt", 'wt')
    # f0 = open("./problem/ex"+filenum+"_s.txt", 'wt')


    f_.write(f1.read())

    f_.close()
    f1.close()


    # count = 0
    # for i in f1.readlines():
    #     if i is "\n":
    #         continue
    #     if "[입력]" in i:
    #         # f2.close()
    #         count = 1
    #         continue
    #     elif "[출력]" in i or "[결과]" in i:
    #         # f3.close()
    #         count = 2
    #         continue
    #     elif "import" in i:
    #         count = 3
    #     elif "public" in i:
    #         count = 3
    #     if count == 0 :
    #         f2.write(i.replace("//",""))
    #     elif count == 1:
    #         f3.write(i.replace("//",""))
    #     elif count == 2:
    #         f4.write(i.replace("//",""))
    #     elif count ==3:
    #         f5.write(i)
    # # f6.write(f1.read().rstrip("\n")+"\n")
    # # f7.write(f2.read().rstrip("\n")+"\n")
    # # f8.write(f3.read().rstrip("\n")+"\n")
    # # f9.write(f4.read().rstrip("\n")+"\n")
    # # f0.write(f5.read().rstrip("\n")+"\n")
    #
    # f2.write("\n")
    # f3.write("\n")
    # f4.write("\n")
    # f5.write("\n")
    # f1.close()
    # f2.close()
    # f3.close()
    # f4.close()
    # f5.close()
    # # f6.close()
    # # f7.close()
    # # f8.close()
    # # f9.close()
    # # f0.close()
