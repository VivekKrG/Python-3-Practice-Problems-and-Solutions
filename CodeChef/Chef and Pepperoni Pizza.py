test = int(input())
temp = 0
while temp < test:
    temp += 1
    diff = 0
    n = int(input())
    present = {0}
    for i in range(n):
        given = input()
        curdiff = given[:len(given) // 2].count('1') - given[len(given) // 2:].count('1')

        if curdiff:
            present.add(curdiff)
            diff += curdiff

    if diff == 0:
        print(diff)
    else:
        print(min(abs(diff - 2*elem ) for elem in present))