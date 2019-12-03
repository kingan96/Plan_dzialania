# ZADANIE: wykonaj wykres funkcji f(x), gdzie x = <-15;15> z krokiem 0.5
# f(x) = x/-8 + a dla x <= 0
# f(x) = x*x/8 dla x >= 0

import pylab

x = pylab.arange(-15, 15.5, 0.5)  # lista argumentów x
a = int(input("Podaj współczynnik a: "))
y1 = [i / -8 + a for i in x if i <= 0]
y2 = [i**2 / 8 for i in x if i >= 0]

print(x, len(x))
print(y1, len(y1))
print(y2, len(y2))

pylab.plot(x[:len(y1)], y1, x[-len(y2):], y2)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()
