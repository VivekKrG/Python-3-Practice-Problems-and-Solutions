tests = int(input())
for __ in range(tests):
    string = input()
    if string[-2:] == 'po':
        print('FILIPINO')
    elif string[-2:] == 'su':
        print('JAPANESE')
    else:# string[-1:-3] == 'da':
        print('KOREAN')

'''
8
kamusta_po
genki_desu
ohayou_gozaimasu
annyeong_hashimnida
hajime_no_ippo
bensamu_no_sentou_houhou_ga_okama_kenpo
ang_halaman_doon_ay_sarisari_singkamasu
si_roy_mustang_ay_namamasu

FILIPINO
JAPANESE
JAPANESE
KOREAN
FILIPINO
FILIPINO
JAPANESE
JAPANESE

'''