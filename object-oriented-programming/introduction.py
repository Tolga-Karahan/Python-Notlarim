# Sinif tanimlandiktan sonra uye degisken ve metodlari sonradan saglanabilir fakat bu kacinilmasi
# gereken bir davranistir.

def print_name(obj):
	print(obj.name)

class Robot:
	call_name = print_name

obj = Robot()
obj.name = 'Marvin'

Robot.call_name(obj)
obj.call_name()	

# __init__ metodu constructor gibi gorev gorerek nesne ilk olusturuldugunda baslatilmasini saglar. 
# Fakat constructor ve ya destructor gibi built-in yapilar bulunmaz. Benzer sekilde __del__ metodu
# destructor gorevi gorur


# Python da access specifierlar isimlendirme yoluyla belirlenir. Degisken isminden once gelen tek bir
# _ degiskenin protected oldugu anlamina gelir, eger iki tane __ varsa bu degiskenin private oldugu
# anlamina gelir. Eger isimlendirme yapilirken hic bir _ kullanilmamissa bu durumda degisken public tir

class OOPRobot:

	def __init__(self, name=None, build_year=None):
		self.__name 			= name
		self.__build_year		= build_year

	def __del__(self):
		pass

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_build_year(self, build_year):
		self.__build_year = build_year

	def get_build_year(self):
		return self.__build_year

	# str() ve ya repr()fonksiyonlari kullanildiginda Python sinif icerisinde __str__ ve ya __repr__
	# metodlarini arar __str__ daha cok tanimlayici bir string dondurmek icin kullanilir, __repr__
	# ise Python  yorumlayicisinin parse ederek esdeger bir nesne uretebilecegi bir cikti vermelidir
	# Bu nesne eval() fonksiyonuna repr() metodunun dondurdugu deger verilerek elde edilebilir
	def __str__(self):
		return "I'm robot " + str(self.__name) + " and I was built in " + str(self.__build_year)	

	def __repr__(self):
		return "OOPRobot(\"" + self.__name + "\"," + str(self.__build_year) + ")"

def main():
	print(OOPRobot("Marvin", 2005))
	print(eval(repr(OOPRobot("Marvin", 2005))))

if __name__ == "__main__":
	main()			



	