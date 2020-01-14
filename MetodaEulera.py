#Metoda Eulera
from  __future__  import  division
import  numpy as np
import  matplotlib.pyplot  as plt
# Prawa strona równania różniczkowego
def f(x):
    return  -x + 1
# Definiuje stan poczatkowy
x0 = 0
# Krok czasu
dt = 0.01
# Rozwiąuje równanie różniczkowe od czasu 0 do czasu T
T = 5
# Określam dyskretny czas; zakładam, że dt dzieli się na T
t = np.linspace(0, T, int(T/dt)+1)
# Tablica do przechowywania rozwiązania
x = np.zeros(len(t))
# Równanie różniczkowe za pomocą metody Euler'a
x[0] = x0
for i in  xrange(1, len(t)):
    x[i] = x[i-1] + f(x[i -1])* dt
    # zapisuhe rozwiazanie w notatniku
    np.savetxt(’t.txt’, t)
    np.savetxt(’x.txt’, x)
    # Tworze nowa figure
    plt.figure ()
    # Drukuje rozwiazanie
    plt.plot(t, x, color = ’blue’)
    # Etykieta osi
    splt.xlabel(’t’)
    plt.ylabel(’x(t)’)
    # Zapisuje figure
    plt.savefig(’plot.pdf’)
