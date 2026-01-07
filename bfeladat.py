nyelvek = []
with open('ujadat/fajl.csv', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        year = int(adatok[0])
        language = adatok[1]
        first_name = adatok[2]
        last_name = adatok[3]
        nyelvek.append([year, language, first_name, last_name])

#print(nyelvek)     
# legfiatalabb nyelv
legfiatalabb_nyelv_kora = nyelvek[0] [0]  
legfiatalabb_nyelv = nyelvek[0]
for nyelv in nyelvek:
    if nyelv[0] > legfiatalabb_nyelv_kora:
        legfiatalabb_nyelv_kora = nyelv[0]
        legfiatalabb_nyelv = nyelv
print(legfiatalabb_nyelv_kora)
print(legfiatalabb_nyelv)
#legidősebb
legidosebb_nyelv_kora = nyelvek[0] [0]  
legidosebb_nyelv = nyelvek[0]
for nyelv in nyelvek:
    if nyelv[0] < legidosebb_nyelv_kora:
        legidosebb_nyelv_kora = nyelv[0]
        legidosebb_nyelv = nyelv
print(legidosebb_nyelv_kora)
print(legidosebb_nyelv)