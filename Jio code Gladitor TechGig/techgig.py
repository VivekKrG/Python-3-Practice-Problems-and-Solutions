def left_money(left_end):
    money = 0
    if left_end > 1:
        if left_end-1 in edges:
            money = edges[left_end - 1][0]
            if money+1 in edges:
                del edges[money+1]
            elif money in edges:
                del edges[money]
            del edges[left_end-1]
        else:
            money = left_end-1
    return money


def right_money(right_end):
    money = 0
    if right_end+1 <= length - 1:
        if right_end+1 in edges:
            money = edges[right_end + 1][1]
            if money-1 in edges:
                del edges[money-1]
            elif money in edges:
                del edges[money]
            del edges[right_end+1]
        else:
            money = right_end+1
#    edges[left_end] = edges[right_end] = edge_money(left_money-1, right_money+1)
    return money


def main():
    for i in range(number):
        money = 0
        left_end, right_end = map(int, input().split())
        money = right_end*(right_end+1) - (left_end-1)*left_end
        money //= 2
        left = left_money(left_end)
        right = right_money(right_end)
        money += left + right
        edges[left] = edges[right] = [left_money(left), right_money(right)]
        print(money)


length, number = map(int, input().split())
edges = dict()
main()