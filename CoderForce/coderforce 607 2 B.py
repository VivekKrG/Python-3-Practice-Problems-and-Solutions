def check():
    pass


tests = int(input())
for __ in range(tests):
    st1, st2 = input().split()
    if st1[0] < st2[0]:
        print(st1)
        continue
    i = 0
    while i < len(min(st1, st2)) and st1[i] == st2[i]:
        i += 1
    if i < len(st1) and i < len(st2):
        if st1[i] < st2[i]:
            print(st1)
        elif i < len(st1):
            k = i
            j = 0
            newk = 0

            while k < len(st1):
                if st1[k] < st2[i]:
                    newk = k
                elif st1[k] == st2[i]:
                        j = k
                        # print("J updated ", j)
                k += 1

            if newk:
                k = newk
                st1 = st1[:i] + st1[k] + st1[i + 1:k] + st1[i] + st1[k + 1:]
                print(st1)
            elif j:
                k = j
                st1 = st1[:i] + st1[k] + st1[i + 1:k] + st1[i] + st1[k + 1:]
                newst1 = st1[i+1:]
                st2 = st2[i+1:]
                l = 0
                while l < min(len(newst1), len(st2)) and newst1[l] == st2[l]:
                    l += 1
                if l < len(newst1) and l < len(st2):
                    if newst1[l] < st2[l]:
                        print(st1)
                    else:
                        print('---')
                elif len(newst1) < len(st2):
                    print(st1)
                else:
                    print('---')
            else:
                print('---')
        else:
            print('---')
    elif len(st1) < len(st2):
        print(st1)
    else:
        print('---')

'''
9
AZAMON APPLE
AZAMON AAAAAAAAAAALIBABA
APPLE BANANA
BB AA
BBCDA ABC
BBCA AC
AAAB AAA
AAA AAB
BA A

AMAZON
---
APPLE

6
BB AA
BBCDA ABC
BBCA AC
AAAB AAA
AAA AAB
BA A

13
TTT TTTTTTTTTT
QQ QRE
SK KJQQ
PV EP
UU ZZN
BS BSSSS
GYYYYYYYTTTTTTTZ GTYYYYYYTTTTTTYZ
RC QCC
QA AQ
YA LAL
YY NYY
QZ ZQR
DGPX DE



TTT
QQ
---
---
UU
BS
---
CR
AQ
AY
---
QZ
---

ABCDFGHIJKLNPQTUWXZ input
ABCDFGHIJKLNPQTUWXZ
ABCDFGHIJKLNPQTUWXZ

ABCDEFGHIJKLMNOPRSTUVWXYZ
IUWWWWWWUUUUUUWZ
KV
NNNNN

ABCDEFGHIJKLMNOPRSTUVWXYZ
---
KV
NNNNN
---
---
'''