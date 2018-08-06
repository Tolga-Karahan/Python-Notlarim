# Sinif degiskenleri metodlarla sinif header i arasinda tanimlanir
class A:
	class_variable = "I'm a class variable"

# Sinif_ismi.sinif_degiskeni seklinde erisebiliriz.	
print(A.class_variable)

a = A()
b = A()

# Sinif degiskenlerine Sinif_ismi.sinif_degiskeni seklinde erismeliyiz aksi takdirde nesne icin
# yeni bir instance degiskeni tanimlariz

a.class_variable = "changing class variable"
print(A.class_variable)
print(a.class_variable)

# Basit bir nesne sayan sinif degiskeni ornegi
class Count_Instances:
	counter = 0

	def __init__(self):
		type(self).counter += 1

	def __del__(self):
		type(self).counter -= 1

obj1 = Count_Instances()
print("Number of instances %d" % Count_Instances.counter)
obj2 = Count_Instances()			
print("Number of instances %d" % Count_Instances.counter)	

# Nesne sayan degiskenimizi private yapabiliriz fakat bu durumda dogrudan erisemeyiz
# Bir instance metodu araciligiyla erisebiliriz fakat mantikli olmaz cunku herhangi 
# bir nesne uretilmeden degiskene erisemeyiz bu durumda daha mantikli bir cozum
# self parametresini kullanmamak olabilir fakat bu durumda da instancelar uzerinden 
# degiskene erisemeyiz. Dolayisiyla en mantikli yol bir static metod kullanmaktir

class Count_Instances:
	__counter = 0

	def __init__(self):
		type(self).__counter += 1

	def __del__(self):
		type(self).__counter -= 1

	@staticmethod
	def RobotInstances():
		return Count_Instances.__counter	

obj1 = Count_Instances()
print("Number of instances %d" % obj1.RobotInstances())
obj2 = Count_Instances()			
print("Number of instances %d" % obj2.RobotInstances())		

# Bazen sinif icerisindeki diger statik metodlari yine bir statik metod icerisinden
# cagirmamiz gerekebilir. Bu durumda sinif ismini haricen belirtmeliyiz, bu ise
# kalitim gibi bazi durumlarda sorunlara yol acabilir. Dolayisiyla siniftaki diger
# statik metodlari yine bir statik metod icerisinden cagirmak yerine bir sinif
# metodundan cagirabiliriz. Sinif metodlarini tanimlarken @classmethod seklinde
# decorator sintaksini kullaniriz ve sinif metodunun ait oldugu sinifi referanslayan
# (self gibi) bir arguman saglariz.

class Fraction(object):
	def __init__(self, numerator, denominator):
		self.numerator, self.denominator	=	Fraction.reduce(numerator, denominator)	

	@staticmethod
	def gcd(a, b):
		while b != 0:
			a, b = b, a % b
		return a
	
	@classmethod
	def reduce(cls, numerator, denominator):
		divisor = cls.gcd(numerator, denominator)
		return (numerator // divisor, denominator // divisor)			

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator)


print(Fraction(7, 28))

