"""
	Memoization(kullanimi bu sekilde) bilgisayar programlarinin hizini arttirmak icin
kullanilan bir tekniktir. Fonksiyon cagrilarinin sonuclari gibi islenen girdilerin
sonuclarinin animsanmasina dayanir. Eger ayni girdiler ve ya ayni parametreler kullanilarak
yapilan bir fonksiyon cagrisi soz konusu ise onceden saklanan sonuclar kullanilarak gereksiz
hesaplamalardan kacinilir. Bu teknik programci tarafindan haricen programlanabilse de Python
otomatik olarak bu islevi yerine getiren mekanizmalar sunar.
"""

"""
	Asagida verilen ornekte memoize() fonksiyonu ile fonksiyon sonuclarinin saklanmasi saglanmistir.
Boylece hesaplanan sonuclarin saklanmasi ile ileride yapilmasi muhtemel gereksiz hesaplamalarin 
onune gecilir. Bu teknik decoratorlar kullanilarak gerceklestirilir. Dolayisiyla basitce decorator
syntaxini kullanabiliriz(@memoize).
"""	

def memoize(f):
	memo = {}
	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]
	return helper

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else
		return fib(n-1) + fib(n-2)

fib = memoize(fib)
print(fib(40))			

# Memoization teknigini decorator olarak bir sinif kullanarakta gerceklestirebiliriz.

class Memoize:

	def __init__(self, f):
		self.f 	  = f
		self.memo = {} 

	def __call__(self, *args):
		if args not in memo:
			memo[args] = self.f(*args)
		return self.memo[args]

@Memoize
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)					
