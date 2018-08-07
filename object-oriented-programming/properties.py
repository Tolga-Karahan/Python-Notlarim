"""
	Java gibi dillerde getter ve setterlar degiskenlere olan erisimi ve atamalari sinirlamak
icin kullanilabilir. Bunun icin attributeler private tanimlanir. Python'da ise properties
sayesinde attributeleri private tanimlamak gibi bir zorunluluk yoktur. Attributeler public
tanimlansa da properties sayesinde sinirlamalar koyulabilir.
"""

class PropertyTest:

	def __init__(self, x):
		self.x = x

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, x):
		if x < 0:
			self.__x = 0
		elif x > 1000:
			self.__x = 1000
		else:
			self.__x = x


p1 = PropertyTest(1001)
print(p1.x)

p1.x = -20
print(p1.x)				

# Fakat properties disaridan erisilmek istenilen attributeler icin kullanilir. Sadece sinif icerisinde
# kullanilacak attributeler private yapilabilir.