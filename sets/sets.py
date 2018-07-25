# set ler matematiksel kumelerin Python implementasyonudur
# Herhangi tipten nesneler icerebilirler fakat kume olduklari icin her bir elemandan
# yalnizca bir tane bulunmasi gerekir

# set ler olusturulurken herhangi bir sequence ve ya diger iterable nesneler kullanilabilir

set1	= set("A Python Tutorial")
set2 	= set(["Java", "Python", "Perl"])

# set ler mutable nesneler barindiramaz, dolayisiyla bir list set elemani olamaz
# fakat set lerin kendisi mutable dir, yani eleman ekleme, guncelleme gibi islemler yapilabilir

cities	= set(["Frankfurt", "Berlin"])
cities.add("Strassbourg")
print(cities)

# frozenset ler ise mutable degildir

cities = frozenset(["Frankfurt", "Berlin"])
# cities.add("Strassbourg") kullanimi exception firlatir

# set ler herhangi bir fonksiyon kullanilmaksizin suslu parantezler ile de olusturulabilir

adjectives = {"cheap", "expensive", "inexpensive", "economical"}

# Set Islemleri
# add() fonksiyonu ile set e yeni bir eleman eklenebilir fakat eklenecek olan eleman immutable olmalidir

colours = {"red", "blue"}
colours.add("yellow")
# colours.add(["pink", "purple"]) kullanimi exception firlatir

# clear() fonksiyonu ile set icerisindeki tum elemanlar silinebilir
colours.clear()
print(colours)

# difference() fonksiyonu ile set ler arasindaki fark bulunabilir

set1	= {'a', 'b', 'c', 'd', 'e'}
set2	= {'b', 'c'}
print(set1.difference(set2))

# iki set arasindaki fark - operatoru ile de bulunabilir

print(set1 - set2)

# difference_update() fonksiyonu ile arguman olarak alinan kumedeki elemanlar ana kumeden silinir

set1.difference_update(set2)
print(set1)

# discard(elem) fonksiyonu ile arguman olarak verilen eleman kumeden silinir eger eleman kumede
# bulunmuyorsa herhangi bir islem yapilmaz 

set1.discard('d')

# remove(elem) fonksiyonu discard ile ayni islevi gorur fakat arguman olarak verilen eleman kumede
# bulunmuyorsa KeyError firlatilir

# union(set) fonksiyonu ile iki kumenin birlesimi alinir

set1	= {'a', 'd', 'c', 'f'}
set2	= {'b', 'e', 'g'}
set1.union(set2)
print(set1)

# intersection(set) fonksiyonu ile iki kumenin kesisimi alinir

set1	= {'a', 'd', 'c', 'f'}
set2	= {'b', 'e', 'g'}
set1.intersection(set2)
print(set1)

# isdisjoint(set) fonksiyonu eger iki kumenin kesisimi yoksa true dondurur

set1	= {'a', 'd', 'c', 'f'}
set2	= {'b', 'e', 'g'}
print(set1.isdisjoint(set2)) 

# issubset(set) fonksiyonu, uzerinde cagirildigi kume arguman olarak aldigi kumenin alt kumesi ise
# true dondurur

set1	= {'a', 'd', 'c', 'f'}
set2	= {'b', 'e', 'g'}

print(set1.issubset(set2))

# issuperset(set) fonksiyonu, uzerinde cagirildigi kume arguman olarak aldigi kumenin ust kumesi ise
# true dondurur

set1	= {'a', 'b', 'c'}
set2	= {'a', 'c'}

print(set1.issuperset(set2))

# pop() fonksiyonu kume icerisindeki herhangi bir elemani rastgele olarak dondurur, kume bos ise 
# KeyError firlatir