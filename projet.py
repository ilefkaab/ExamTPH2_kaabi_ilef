def somme(T):
    s=0
    for t in T:
        s+=t
        return s

data=[1,3,5]
if data:
    print('la somme est :',sum(data))
    print('le min est:',min(data))
    print('le max est:',max(data))
else: 
    print('dossier vide')
