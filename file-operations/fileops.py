"""
	Python'da dosyalari okumak icin open fonksiyonunu kullanabiliriz. Ilk parametre olarak dosyanin ismini
ve ikinci olarak okuma islemi yapmak istedigimizi belirten "r" argumanini saglariz. Ikinci arguman opsiyoneldir,
open fonksiyonu varsayilan olarak okuma islemi yapar. open fonksiyonu bir dosya nesnesi dondurur. Dosya nesnesinin
icinde cesitli attributeler ve manipulasyon icin kullanilabilecek cesitli metodlar bulunur. 

"""

fobj = open("ad_lesbiam.txt", "r") # open("ad_lesbiam.txt") de kullanilabilir
fobj.close()

# Dosya icerigini asagidaki gibi okuyabiliriz. rstrip metodu satirlarin sonundaki bosluklari siler
# Dosya icerigi Roma doneminden kalma bir siirmis. Lesbiam ise siirin yazildigi kadinin ismi, yanlis anlasilmasin :)

fobj = open("ad_lesbiam.txt")
for line in fobj:
	print(line.rstrip())
fobj.close()	

# Dosya yazma islemi icin dosyayi acarken open fonksiyonuna ilaveten "w" argumanini veririz, sadece dosya 
# sonuna ekleme yapmak istiyorsak "a" argumanini vermemiz gerekir
# open fonksiyonunun dondurdugu dosya nesnesinin write metodu ile yazma islemini gerceklestiririz
# with open ifadesi ile dosyalari actigimizda haricen kapatmamiz gerekmez, dosyalar kendiliginden kapatilir

with open("example.txt", "w") as fh:
	fh.write("some bullshit")

# Ayni anda okuyup yazabiliriz, ayni dosyaya ayni anda okuyup yazmak icin "w+" argumanini kullanabiliriz
# Boylece dosya icerigi silinmez

fobj_r = open("ad_lesbiam.txt")
fobj_w = open("ad_lesbiam2.txt", "w")

i = 1
for line in fobj_r:
	print(line)
	fobj_w.write(str(i) + ": " + line)
	i = i + 1

fobj_r.close()		
fobj_w.close()

# Tum dosya icerigi bir liste icerisine okunabilir
# readlines yerine read metodunu kullanirsak tum icerik bir stringe okunur

poem = open("ad_lesbiam.txt").readlines()
print("\n" + str(poem))

# seek metodu ile dosya icerisinde pozisyon belirlenebilir. tell metodu ise dosya icindeki o anki pozisyonu verir
# Dosya ilk acildiginda pozisyon 0'dir


# pickle modulunu kullanarak nesnelerimizi serialize edebiliriz. 
# pickle.dump(obj, file[,protocol, *, fix_imports=True])
# Yukaridaki cagri ile nesne, dosya nesnesinin belirttigi dosyaya yazilir
# Protokol argumani opsiyoneldir. 
# Protokol version 0 human-readable(ascii) formatini belirtir
# Protokol version 1 binary formati belirtir
# Protokol version 2 daha verimli bir serialization yapilmasini saglar 
# Protokol version 3 bytelar icin destek saglar ve Python3 surumu icin onerilen protokoldur
# Serialize edilen nesne pickle.load() metodu ile deserialize edilebilir

import pickle

cities = ["Istanbul", "LA", "Berlin"]
fh = open("data.pkl", "bw")
pickle.dump(cities, fh)
fh.close()

fh = open("data.pkl", "rb")
cities = pickle.load(fh)
print(cities)

# Iki ve ya daha fazla nesneyi ayni anda serialize etmek icin nesnelerin hepsini tek bir nesne icerisinde toplayabiliriz

programming_languages = ["C++", "Python", "Java"]
python_dialects = ["Jython", "IronPython", "CPython"]
pickle_object = (programming_languages, python_dialects)

pickle.dump(pickle_object, open("data.pkl", "bw"))
objects = pickle.load(open("data.pkl", "rb"))
print(objects)

"""
	Pickle modulunun dezavantaji ayni anda sadece tek bir nesneyi serialize edebilmesi ve tum nesnenin tek bir seferde
deserialize edilmesi gerekliligidir. Fakat ornegin bir dictionarynin sadece tek bir degerini saklayip tekrar elde etmek
isteyebiliriz. Bu durumda shelve modulunu kullaniriz. Shelve modulu icerisinde Shelf denilen dictionary benzeri yapilar
bulunur. Shelf degerleri pickle modulunun serialize edebilecegi herhangi bir nesne olabilir. Yani Shelf, degerleri
pickle modulunun serialize ettigi nesneler olan bir dictionarydir. 
"""

import shelve

tele = shelve.open("My_Phone_Book")

tele["Mike"]  = {"first":"Mike", "last":"Miller", "phone":"4689"}
tele["Steve"] = {"first":"Steve", "last":"Burns", "phone":"9069"}

# Shelf asagidaki gibi acilarak icindeki herhangi bir nesneye erisilebilir

tele = shelve.open("My_Phone_Book")
print(tele["Mike"]["phone"])



 	










