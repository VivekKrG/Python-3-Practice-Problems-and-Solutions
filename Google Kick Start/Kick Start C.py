t = int(input())
file = open("output.txt", "w")
case = 1
while case <= t:
    nrc = input()
    nrc = nrc.split()

    n = int(nrc[0])
    r = int(nrc[1])
    c = int(nrc[2])
    sr = int(nrc[3])
    sc = int(nrc[4])

    dir = input()

    gone = [(sr, sc)]
    for i in range(n):
        if dir[i] == 'N':
            sr -= 1
            while (sr, sc) in gone:
                sr -= 1
            gone += [(sr, sc)]
        elif dir[i] == 'S':
            sr += 1
            while (sr, sc) in gone:
                sr += 1
            gone += [(sr, sc)]
        elif dir[i] == 'E':
            sc += 1
            while (sr, sc) in gone:
                sc += 1
            gone += [(sr, sc)]
        else:
            sc -= 1
            while (sr, sc) in gone:
                sc -= 1
            gone += [(sr, sc)]
    file.write("case #{}: {} {}\n".format(case, sr, sc))
    case += 1
file.close()