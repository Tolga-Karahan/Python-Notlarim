# Listler in aksine dictionary ler sirali degildir ve icerdigi elemanlara
# key kullanilarak erisilir, yani indisler kullanilarak erisilmez
# Her bir key degeri belirli bir value ile iliskilidir ve dictionary icinde
# ayni key en fazla bir kez bulunabilir, yani bir hash table implementasyonudur
# Dictionary value leri herhangi bir Python tipinde olabilir

# Bir dictionary ornegi

city_population = {"New York City":8555405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546,
	"Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}

# Dictionary de bulunan herhangi bir sehrin nufusunu almak icin key(bu ornekte sehirler) kullanilir
# Dictionary lerde indisler kullanilamaz
# Key olarak kullanilan tipler immutable olmalidir, list ve ya baska bir dictionary kullanilamaz
# fakat tuple kullanilabilir 

print(city_population["Montreal"])

# Dictionary de bulunmayan bir key kullanilirsa KeyError firlatilir
# Dictionary lerde bulunan key-value ikilileri sirali degildir dolayisiyla key-value ikililerinin
# hepsi yazdirilmak istendiginde dictionary de bulunan tanimlama sirasi kullanilmayabilir

# Asagidaki kullanim ile dictionary e yeni bir key-value ikilisi eklenebilir

city_population["Halifax"] = 390096

# dictionary icerisinde baska dictionary ler kullanilabilir

en_tr={"red":"kirmizi", "yellow":"sari", "purple":"mor", "black":"siyah"}
tr_en={"kirmizi":"red", "sari":"yellow", "mor":"purple", "siyah":"black"}
dictionaries={"en_tr":en_tr, "tr_en":tr_en}
print(dictionaries["en_tr"]["yellow"])

# len(dictionary) fonksiyonu ile dictionary de bulunan key-value ikililerinin sayisi alinabilir

print(len(city_population))

# del() dictionary[key] kullanimi ile dictionary icerisinde bulunan bir value, key degeri kullanilarak silinebilir

del city_population["Calgary"]
print(city_population)

# key in dictionary belirtilen key degeri dictionary de bulunuyorsa true dondurur
# key not in dictionary belirtilen key degeri dictionary de bulunmuyorsa false dondurur

print("Los Angeles" in city_population)
print("Samsun" not in city_population)

# dictionary.pop(key) kullanimi ile belirtilen key e sahip key-value ikilisi silinir ve karsilik
# dusen deger dondurulur, belirtilen anahtar dictionaryde bulunmuyorsa KeyError firlatilir

print(city_population.pop("Vancouver"))

# pop fonksiyonuna pop(key, default_value) seklinde default_value verilerek belirtilen key e sahip
# key-pair ikilisi bulunamazsa default bir deger dondurulmesi saglanabilir
# Eger key, dictionary icerisinde bulunuyorsa default deger degil karsilik dusen deger dondurulur

# popitem() fonksiyonu dictionary icerisinde bulunan herhangi bir key-value ikilisini 2-tuple
# olarak dondurur

(en, tr) = en_tr.popitem();
print((en, tr))

# Belirtilen key dictionary de bulunmamasi durumunda exception firlatilmasinin onune gecilmek
# isteniyorsa get fonksiyonu kullanilabilir

population = city_population.get("Samsun")
print(population)

# get fonksiyonu saglanan key dictionary icerisinde bulunuyorsa karsilik dusen degeri dondurur
# eger saglanan key dictionary icerisinde bulunmuyorsa none dondurur

# copy fonksiyonu ile dictionary ler kopyalanabilir fakat kopyalama islemi shallow copy olur

copy_dictionary = dictionaries.copy()
print(copy_dictionary)

# clear fonksiyonu ile dictionary icerigi temizlenebilir

copy_dictionary.clear()
print(copy_dictionary)

# update fonksiyonu ile dictionary ler birlestirilebilir key leri ayni olan key-value ikilileri
# override edilir

devs1 = {"Frank":"Python", "Monica":"Perl"}
devs2 = {"Guido":"C++", "Frank":"Java, C#"}
devs1.update(devs2)
print(devs1)

# for dongusu ile key leri yazdirabiliriz

for key in devs1:
	print(key)

# key lere dictionary.keys() seklinde de erisilebilir

# for dongusunu ile key lere karsilik dusen degerleri de yazdirabiliriz

for value in devs1.values():
	print(value)

for key in devs1:
	print(devs1[key])


# dictionary leri list e donusturme
# items() fonksiyonu kullanilarak bir dictionary bir list e donusturulebilir
# list key-value ikililerini iceren tuple lardan olusur

items_view = en_tr.items()
items      = list(items_view)
print(items)

# key ve value ler de ayri ayri list e donusturulebilir

keys_view = en_tr.keys()
keys      = list(keys_view)
print(keys)

values_view = en_tr.values()
values      = list(values_view)
print(values)

# list lerin dictionary lere cevirilmesi
# zip fonksiyonu kullanilarak key ve value leri olusturan list ler birlestirilebilir
# zip fonksiyonu sonuc olarak bir list iterator dondurur, iterator list() fonksiyonu
# ile cast edilerek key-value ikililerinin tuple olarak tutuldugu bir list ve ya
# dict() fonksiyonu ile cast edilerek bir dictionary elde edilebilir 

keys       		= ["red", "yellow", "purple", "black"]
values     		= ["kirmizi", "sari", "mor", "siyah"] 
list_iter  		= zip(keys, values)
list_of_tuples  = list(list_iter)
dictionary      = dict(list_iter)
print(list_of_tuples)
print(dictionary)
