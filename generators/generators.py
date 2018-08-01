# Python generatorleri fonksiyonlara benzesede semantic ve syntax olarak farklar vardir
# Fonksiyonlar ile generator leri ayirt eden ozelliklerden biri yield ifadesidir
# yield ifadesi ile bir fonksiyon generator e donusturulur. Generator ise bir generator nesnesi 
# donduren bir fonksiyondur. Fakat bu nesnenin kendisi de sonuc olarak tek bir deger yerine
# bir dizi deger donduren bir fonksiyon gibidir. Bu degerler dizisi ise ornegin bir for
# dongusu ile uzerinde iterasyon yapilarak uretilebilir. Uzerinde iterasyon yapilabilen degerler
# yield ifadesi tarafindan uretilir. Kodun icrasi bir yield ifadesi goruldugunde durur ve
# yield ifadesinden sonraki deger dondurulur. Bu noktada generator interrupt edilir
# Generator uzerinde bir sonraki next() icra edildiginde generator fonksiyonu son cagrinin
# cikis yaptigi noktadan devam eder. Yani kod icrasi en son icra edilen yield ifadesinden
# sonraki durumdan devam eder. Dolayisiyla generator de bulunan tum lokal degiskenler korunur
# Fonksiyonlarda ise bu lokal degiskenler korunmaz ve her cagrida fonksiyon bastan baslar
# Generator kodunun icinde birden fazla yield ifadesi bulunabilir ve eger kod icerisinde bir
# return ifadesi varsa kodun icrasi StopIteration exception firlatilarak durdulur 

def city_generator():
	yield ('London')
	yield ('Hamburg')
	yield ('Konstanz')
	yield ('Amsterdam')
	return 0

city = city_generator()

print(next(city))
print(next(city))
print(next(city))
print(next(city))
#print(next(city)) #StopIteration firlatir

# Generatorler sadece nesne gondermez, kendileri de nesne alabilir. Generator e bir nesne
# gondermek icin generator nesnesi uzerinde send() fonksiyonu kullanilir. send() fonksiyonu
# generator e bir nesne gonderirken ayni zamanda generator tarafindan yield edilen degeri dondurur
# Aslinda next() cagrisi da hem nesne gonderir hem de yield tarafindan dondurulen nesneyi alir
# Fakat bu durumda next() fonksiyonunun gonderdigi mesaj None nesnesidir
# send() fonksiyonunu kullanabilmek icin generator un baslatilmasi ve yield ifadesinde bekliyor
# olmasi gerekir, bu da basitce next() fonksiyonu ile  yapilir

def simple_coroutine():
	print("coroutine has been started")
	x = yield 
	print("coroutine received " + str(x))

try:
	print("\nSimple Coroutine")
	gen = simple_coroutine()
	next(gen)
	gen.send('Hi')	    
except StopIteration:
	pass

def infinite_looper(objects):
	count = 0;
	while True:
		if count >= len(objects):
			count = 0;
		message = yield objects[count]
		if message != None:
			count = 0 if message < 0 else message
		else:
			count = count + 1	

print("\nInfinite Looper")
gen = infinite_looper("Learning Python")
print(next(gen))
print(gen.send(5))
print(next(gen))
#print(gen.send(-4))

# Yukaridaki orneklerde Iterator'u(generatorden donen generator nesnesi ve ya iterator) baslatmadan
# herhangi bir index gonderemiyorduk. Yani ilk olarak bir next() cagrisi ile baslatmamiz gerekiyordu.
# Bu sekilde generator un baslayarak bir sonraki yield ifadesine konumlanmasini sagliyorduk 
# Iterator un baslar baslamaz yield ifadesine konumlanmasini saglamak icin bir decorator olusturabiliriz

from functools import wraps

def get_ready(gen):
	
	""" 
	Bir generator alarak ilk yield 
	ifadesine ilerletir
	"""

	@wraps(gen)
	def generator(*args, **kwargs):
		g = gen(*args, **kwargs)
		next(g)
		return g
	return generator

@get_ready
def infinite_looper(objects):
	count = 0
	while True:
		if	count >= len(objects):
			count = 0

		message = yield objects[count]

		if message is not None:
			count = 0 if message < 0 else message
		else:
			count += 1		

gen = infinite_looper("Learning Python")
print(gen.send(9))
print(gen.send(3))