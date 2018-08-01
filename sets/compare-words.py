import re

ulysses_txt = open("./books/ulysses.txt").read().lower()
words 		= re.findall(r"\b[\w-]+\b", ulysses_txt)
print("\nThe novel Ulysses contains " + str(len(words)) + " words")

for word in ["the", "while", "good", "bad", "irish", "turkish"]:
	print("The word '" + word + "' occurs " + str(words.count(word)) + " times in the novel!")

# Ulyses romani kelime dagarcigiyla unlu James Joyce tarafindan yazilmistir. Romanda oldukca
# fazla kelime olsa da daha da onemlisi kelime sayisindan cok kac farkli kelime kullanildigidir
# Burada ise devreye Python in kume implementasyonu olan set ler giriyor. Baska tipteki bir
# veri yapisinda kac adet farkli eleman bulundugunu o veri yapisini set e cevirerek bulabiliriz
# Cunku set ler bir kume implementasyonudur ve dolayisiyla ayni elemandan en fazla bir adet bulunur

diff_words = set(words)
print("Ulysses contains " + str(len(diff_words)) + " different words!")

print("\nDifferent words in the other novels:")

novels =  ['metamorphosis.txt', 'robinson-crusoe.txt', 'the-light-house.txt',
		   'moby-dick.txt',     'sons-and-lovers.txt', 'the-way-of-all-flesh.txt',
		   'ulysses.txt']

for novel in novels:
	txt 		= open("./books/" + novel).read().lower()
	words		= re.findall(r"\b[\w-]+\b", txt)
	diff_words	= set(words)
	print("{name:38s}: {n:5d}".format(name=novel, n=len(diff_words)))   

# Simdide sadece Ulysses'te bulunan ve diger romanlarda bulunmayan kelimelerin sayisina bakalim

words_in_novels = {}

for novel in novels:
	txt 			= open("./books/" + novel).read().lower()
	words 			= re.findall(r"\b[\w-]+\b", txt)
	words_in_novels[novel] = words

words_only_in_ulysses = set(words_in_novels['ulysses.txt'])
novels.remove('ulysses.txt')

for novel in novels:
	words_only_in_ulysses -= set(words_in_novels[novel])

print("Number of the words only Ulysses contains is: " + str(len(words_only_in_ulysses)))		 

# Listede bulunan tum romanlardaki ortak kelimelerin sayisini su sekilde bulabiliriz

common_words = set(words_in_novels['ulysses.txt'])

for novel in novels:
	common_words &= set(words_in_novels[novel])

print("Number of the common words in the novels is: " + str(len(common_words)))