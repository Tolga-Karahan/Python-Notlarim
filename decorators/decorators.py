"""
	Python'da iki tipte decorator bulunur: sinif ve fonksiyon decoratorleri. Genel olarak decoratorler
bir fonksiyon ve ya sinifi degistirmek icin kullanilan cagirilabilen Python nesneleridir. 
"""

# Fonksiyon isimleri sadece fonksiyon referanslaridir ve ayni fonksiyona birden fazla isim atanabilir.

def succ(x):
	return x + 1

successor = succ
print(successor(10))


# Python'da fonksiyon icerisinde fonksiyon tanimlanabilir

def temperature(t):
	def celcius2fahrenheit(x):
		return 9 * x / 5 + 32
	result = celcius2fahrenheit(t)
	return result

# Ilk olarak distaki fonksiyonun kodu kosulur

# Fonksiyon isimleri sadece fonksiyon referanslari oldugundan baska fonksiyonlara gecirilebilir

import math

def foo(func):
	print("The function " + func.__name__ + " is passed to foo")
	
	res = 0
	for x in [1, 2, 2.5]:
		res += func(x)

	return res

print(foo(math.sin))
print(foo(math.cos))

# Fonksiyonlar nesneleri dondurdukleri icin bir fonksiyonun geri donus degeri ayni zamanda bir
# baska fonksiyon olabilir

def f(x):
	def g(y):
		return x + y + 3
	return g

f1 = f(1)
f2 = f(2)

print(f1(1))
print(f2(2))

def polynomial_factory(*coefficients):
	def polynomial(x):
		res = 0

		for index, coeff in enumerate(coefficients):
			res += coeff * x ** index
		return res
	return polynomial

p1 = polynomial_factory(4)	
p2 = polynomial_factory(2, 4)
p3 = polynomial_factory(2, 3, -1, 8, 1)

for x in range(-2, 2, 1):
	print(x, p1(x), p2(x), p3(x))			

# Python fonksiyonlari ile bu bilgilerden sonra decoratorlara gecebiliriz
# Basit bir decorator ornegi, bu ornekte basitce foo() fonksiyonunun implementasyonu degistirildi

def our_decorator(func):
	def function_wrapper(x):
		print("Before calling " + str(func.__name__))
		func(x)
		print("After calling " + str(func.__name__))
	return function_wrapper
	
def foo(x):
	print("Hi, foo called with " + str(x))	

print("We call foo before decoration:")
foo("Hi")

print("Now, we decorate foo")
foo = our_decorator(foo)

print("We call foo after decoration")
foo(55)	

# Genellikle decorator lar icin yukaridaki syntax kullanilmaz. Yukarıdaki ornek icin decoration,
# fonksiyon headerindan onceki satira @our_decorator yazilarak yapilabilir
# Boylece fonksiyon degistirilmis olur

# Decorator ler ile 3. parti fonksiyonlarda decorate edilebilir, fakat fonksiyon headeri bulunmadigindan
# @ syntaxi kullanilamaz

from random import random, randint, choice

def decorator(func):
	def function_wrapper(*args, **kwargs):
		print("We are decorating the function passed")
		return func(*args, **kwargs)
	return function_wrapper
	
random	= decorator(random)
randint = decorator(randint)
choice  = decorator(choice)

print(random())
print(randint(1, 5))
print(choice([1, 8, 5]))


