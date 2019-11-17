#Funkcja Kwadratowa

import math

#podajemy a b c

a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))

#instrukcja warunkowa

if a!=0:

#liczymy deltę

    delta = (b*b) - (4*a*c)
    print("Delta wynosi: ", delta)
    
    if delta==0:
        x0=(-b)/(2*a)
        print("Delta ma jedno miejsce zerowe i wynosi: ", x0)
    elif delta>0:
        # x1 x2
        x1 = ((-b - math.sqrt(delta)) / (2 * a))
        x2 = ((-b + math.sqrt(delta)) / (2 * a))
        print("Delta ma dwa miejsca zerowe, które wynoszą: ", x1 , "," , x2)
    else:
        print("Delta mniejsza od zera - brak miejsca zerowego! ")
else:
    print("A jest równe zero - nie można obliczyć funkcji! ")
