# Iterable ve iterator lerin her ikisi uzerinde de iterasyon yapilabilir, fakat bu
# her zaman ayni sey olduklari anlamina gelmez. Her iterator ayni zamanda bir iterable
# dir, fakat her iterable iterator olmayabilir. Bir iterator herhangi bir iterable
# iter fonksiyonuna arguman olarak verilerek elde edilebilir. Bunun mumkun olmasi icin
# sinif icerisinde iterator donduren bir __iter__() metodu ve ya ardisil indekslerin
# 0'dan basladigi bir __getitem__() metodu olmalidir. 

# Iterator lerde next() fonksiyonu cagirildiginda kullanilan bir __next__() metodu 
# bulunur.  

# Nesnelerin iterable olup olmadigini donduren fonksiyon
def iterable(obj):
	try:
		iter(obj)
		return True
	except TypeError:
		return False

for element in [12, [1, 'a'], ('a', 'b', 'c'), {'city':'London'}, "abcdef", 3.76]:
	print(iterable(element))			

# Herhangi bir sinifa iterator davranisi eklemek icin __iter__() ve __next__() metodu
# tanimlanmalidir. __iter__() metodu bir iterator nesnesi dondurur. Eger __next__()
# metodu tanimlanmis ise sadece self dondurebilir.

class IterableClass:
	
	def __init__(self, data):
		self.data   = data
		self.index  = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

reversed = IterableClass([1, 2, 3, 4, 5])
for i in reversed:
	print(i)


		