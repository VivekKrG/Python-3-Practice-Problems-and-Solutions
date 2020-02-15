'''
Q2. https://gakusei2019.appspot.com/code/#/problem/5654313976201216
Q1. https://gakusei2019.appspot.com/code/#/problem/5635707817164800
'''

def main():
    file = open("task1-sample-input.txt",'r')
    out = open("task1-test-output.txt", "w")
    cases = int(file.readline())
    i=0
    while cases-i:
        i += 1
        file.readline()
        money = int(file.readline())

        nflr = int(file.readline())
        fcost = []
        for flr in range(nflr):
            fline = file.readline()
            fline = fline.split(" ")
            fcost.append(int(fline[1]))

        mopt = int(file.readline())
        ocost = []
        for opt in range(mopt):
            oline = file.readline()
            oline = oline.split(" ")
            ocost.append(int(oline[1]))

        spent = 0
        ops = []
        for flr in range(nflr):
            spent = fcost[flr]
            if spent == money:
                out.write("Case #{}: {}\n".format(i, spent))
                break
            if spent > money:
                ops.append(spent)
            else:
                for opt in range(mopt):
                    spent += ocost[opt]
                    if spent == money:
                        out.write("Case #{}: {}\n".format(i, spent))
                        break
                    elif spent > money:
                        ops.append(spent)
                    else:
                        for opt2 in range(opt+1, mopt):
                            spent += ocost[opt2]
                            if spent == money:
                                out.write("Case #{}: {}\n".format(i, spent))
                                break
                            elif spent > money:
                                ops.append(spent)
                            else:
                                ops.append(spent)
        else:
            if len(ops):
                spent = min(ops)
                out.write("Case #{}: {}\n".format(i, spent))
    out.close()
main()