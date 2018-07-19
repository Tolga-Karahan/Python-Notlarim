# Python list leri farkli tiplerde veriler tutabilir

mylist = [1, 'Tolga', 3.4, True, 'ceng']

# Python list leri yigin olarakta kullanilabilir. Herhangi bir list uzerinde
# cagirilan pop() fonksiyonu yiginlarda oldugu gibi son elemani siler ve geri dondurur.

print(mylist.pop())

# append(object) fonksiyonunun stack lardaki push islemine karsilik geldigini dusunebiliriz.
# Geriye none dondurur, dolayisiyla tekrar referansa esitlersek referans artik list e
# isaret etmez.

mylist.append('Samsun')
print(mylist)

# mylist = mylist.append('Samsun')
# print(mylist) konsola none yazdirir

# pop(index) fonksiyonuna bir index verirsek belirtilen indisteki elemani silerek geri dondurur
# Arguman olarak verilen indis gecersizse ve ya list bos ise IndexError exception firlatilir

mylist.pop(3)
print(mylist)

# list e baska bir list eklemek istersek ve append kullanirsak eklenecek olan list in tamami
# list in sonuna tek bir eleman olarak eklenir

mylist.append([1, 2, 3])
print(mylist)

# Eger eklenecek olan list in eleman eleman eklenmesini istiyorsak extend(object) fonksiyonunu kullanmaliyiz

mylist.pop()
mylist.extend([1, 2, 3])
print(mylist)

# extend() fonksiyonu ile string leri de list in sonuna eleman eleman ekleyebiliriz

mylist.extend('abc')
print(mylist)

# extend() yerine + operatoru kullanilarakta list ler birlestirilebilir
# Fakat list1 = list1 + list2 yerine list1 += list2 kullanimi tercih edilmelidir
# Aksi takdirde ciddi performans handikaplari olusabilir

# remove() fonksiyonu kullanilarak list ten arguman olarak verilen eleman silinebilir
# list icerisinde verilen arguman aranir ve ilk ornegi silinir
# list icerisinde belirtilen eleman yoksa ValueError exception i firlatilir

mylist.remove('a')
print(mylist)

# index() fonksiyonu ile list icerisindeki bir elemanin indisi dondurulebilir
# index(elem, i) kullanimi ile aramanin i. indisten itibaren yapilmasi saglanabilir
# index(elem, i, j) kullanimi ile aramanin i ve j indisleri arasinda yapilmasi saglanabilir

print(mylist.index('Tolga'))

# insert(index, elem) fonksiyonu ile belirtilen index e yeni bir eleman eklenebilir
# Elemanin eklendigi indeksten sonra olan elemanlar saga kaydirilir

mylist.insert(2, 3.2)
print(mylist)