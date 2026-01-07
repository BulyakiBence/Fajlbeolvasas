"""
1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!

(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)

"""
nyelvek = []
with open('ujadat/fajl.csv', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nyelv = {'year': int(adatok[0]), 'language': adatok[1], 'first name': adatok[2],'last name of chief developer': adatok[3] }
        nyelvek.append(nyelv)

# print(f'{nyelvek=}')


# legfiatalabb nyelv
legfiatalabb_nyelv_kora = nyelvek[0] ["year"]  
legfiatalabb_nyelv = nyelvek[0]
for nyelv in nyelvek:
    if nyelv["year"] > legfiatalabb_nyelv_kora:
        legfiatalabb_nyelv_kora = nyelv["year"]
        legfiatalabb_nyelv = nyelv
print(legfiatalabb_nyelv_kora )
print(legfiatalabb_nyelv)

#legidősebb nyelv
legidosebb_nyelv_kora = nyelvek[0] ["year"]  
legidosebb_nyelv = nyelvek[0]
for nyelv in nyelvek:
    if nyelv["year"] < legidosebb_nyelv_kora:
        legidosebb_nyelv_kora = nyelv["year"]
        legidosebb_nyelv = nyelv
print(legidosebb_nyelv_kora)
print(legidosebb_nyelv)