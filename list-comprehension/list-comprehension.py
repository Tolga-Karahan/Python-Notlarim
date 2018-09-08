"""
	List comprehension matematiksel kume notasyonlarinin Python implementasyonu olarak dusunulebilir.
Ornegin matematikte dogal sayilarin kareleri su sekilde tanimlanir:	{ x2 | x ∈ ℕ }. List comprehension
kullanarak matematiksel notasyonlardaki gibi bir mantiga uyan elemanlardan olusan listeler olusturabiliriz.

"""

# Ornegin Celcius degerlerini Fahrenheit'a ceviren bir list comprehension tanimlayarak bir liste elde edebiliriz:

Celcius = [14,8, 23.5, 36, 39.2]
Fahrenheit = [((float(9)/5)*x + 32) for x in Celcius]
print("\nFahrenheit values: " + str(Fahrenheit))

# Baska bir ornek ile Pisagor ucgenlerinden olusan bir liste elde edilir.

Pythagorian_triples = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y,30) if x**2 + y**2 == z**2]
print("\nPythagorian_triples: " + str(Pythagorian_triples))

# Iki kumenin kartezyen carpimi list comprehension ile elde edilebilir

set_A = ["red", "green", "blue"]
set_B = ["car", "tree", "house"]

cartesian = [(x, y) for x in set_A for y in set_B]
print("\nCartesian product of A and B sets is: " + str(cartesian))

"""
	Generator comprehensionlar List comprehensionlar ile ayni isi yapar. Sintaks olarak koseli parantez
yerine normal parantez kullanilir ve sonuc olarak bir liste degil bir generator dondururler.

"""

evens_up_to_30 = (x for x in range(30) if x%2==0)
print("\nEvens up to 30: " + str(list(evens_up_to_30)))

# 1 ve 100 arasindaki asal sayilari Eratosthenes yontemi ile List comprehension kullanarak elde edebiliriz

no_primes = [y for x in range (2, 8) for y in range (x**2, 100, x)]
primes    = [x for x in range(1, 100) if x not in no_primes]
print("/nPrimes up to 100: " + str(primes))

# Yukaridaki ornek iki asamadan olusuyor ve ilk asamada Eratosthenes yontemi ile elenen yani asal olmayan
# sayilar bulunuyor. Ikinci asamada ise 1'den 100'e kadar olan sayilar icerisinden asal olmayanlar cikartiliyor
# Dolayisiyla algoritma karmasikligi acisindan bakarsak Eratosthenes yonteminin amacina ulasildigi soylenemez
# Bir diger sorun ise asal olmayan sayilarin bulundugu listede ayni sayilarin birden fazla bulunmasi
# Bu sorunu set comprehension kullanarak cozebiliriz. Set comprehension tanimlarken koseli parantez yerine
# suslu parantez kullaniriz

from math import sqrt
n = 100
sqrt_n = int(sqrt(n))

no_primes = {y for x in range (2, sqrt_n + 1) for y in range(x**2, 100, x)}
print("No primes up to 100: " + str(no_primes))






