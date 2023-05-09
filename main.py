import re
import random
def beolvas(kategoria):
    dict=[]


    if kategoria=='1' or kategoria=='2' or kategoria=='3' or kategoria=='4' or kategoria=='5' or kategoria=='6' or kategoria=='7' :
        with open(kategoria+'.txt', 'r', encoding='utf-8') as f:
            kerdessorok = [sor.rstrip() for sor in f]
        for kerdes in kerdessorok:
            valaszok=re.findall("%(.*?)%", kerdes)
            dictitem={
                'kerdes': re.sub("%(.*?)%", "____", kerdes),
                'valaszok': valaszok
            }
            dict.append(dictitem)
    else:
        for i in range(1,7):
            with open(str(i) + '.txt', 'r', encoding='utf-8') as f:
                kerdessorok = [sor.rstrip() for sor in f]
            for kerdes in kerdessorok:
                valaszok = re.findall("%(.*?)%", kerdes)
                dictitem = {
                    'kerdes': re.sub("%(.*?)%", "____", kerdes),
                    'valaszok': valaszok
                }
                dict.append(dictitem)

    return dict



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print('Írjon be egy válaszhoz x-et, ha vissza akar lépni a főmenübe!\n1. Félvezető technológia, bevezető\n2. Trendek, IC gyártás\n3. Félvezetők fizikája\n4. PN átmenet, dióda 1\n5. PN átmenet, dióda 2\n6. Bipoláris tranzisztor\n7. JFET, MOSFET 1\n0. Kilépés')
        menu=input()
        if menu=='0':
            break
        dict=beolvas(menu)
        #print(dict)
        while True:
            br=False
            index=random.randint(0, len(dict)-1)
            print(dict[index]['kerdes'])
            helyes=True
            for i, valasz in enumerate(dict[index]['valaszok']):
                print(i+1,': ')
                felhvalasz=input()
                if(felhvalasz=='x'):
                    br=True
                    break;
                if(felhvalasz.strip().lower()!=valasz.lower()):
                    helyes=False
            if(br==True):
                break
            if(helyes):
                print('Helyes válasz(ok)! ', dict[index]['valaszok'])
            else:
                print('Helytelen, a válaszok:', dict[index]['valaszok'])



