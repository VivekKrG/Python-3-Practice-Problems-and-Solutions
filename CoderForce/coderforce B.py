tests = int(input())
for __ in range(tests):
    size = int(input())
    num_arr = list(map(int, input().split()))
    evens = set()
    for elem in num_arr:
        if elem%2 == 0:
            evens.add(elem)

    count = 0
    while evens:
        out_num = max(evens)
        evens.remove(out_num)
        count += 1
        new_val = out_num // 2
        if new_val%2 == 0:
            evens.add(new_val)
    print(count)
