"""
	Python'da exception handling Java ve benzeri diller gibidir. Exception firlatmasi muhtemel olan kod
bir try blogu icerisine alinir. Java'da ki catch ifadeleri yerine Python'da except ifadesi kullanilir.
"""

import sys

try:
	file = open("integers.txt")
	line = file.readline()
	to_integer = int(line.strip())

except IOError as e:
	errno, strerror = e.args
	print("I/O error({0}): {1}".format(errno, strerror))
	# ve ya dogrudan print(e)

except ValueError:
	print("Couldn't convert to integer")

except:
	print("Unexpected error:", sys.exc_info()[0])
	raise		
	# except icerisinde raise kullanarak ayni exception ın cagirana donmesini saglayabiliriz
finally:
	file.close()

# Ayni except ifadesi icerisinde tuple kullanilarak birden fazla expception kontrol edilebilir
# except (IOError, ValueError):	

# Exception sinifindan miras alarak kendi exceptionlarimizi olusturabiliriz

# Suana kadar mekanizma cogu dil ile ayniydi. Farkli olan sey ise Python'da try-except ifadelerine bir
# else ifadesi ekleyebiliriz. Boylece try icerisinde herhangi bir exception olusmazsa else blogu kosulur

import sys

file_name = sys.argv[1]
text = []

try:
	file = open(file_name)
	text = file.readlines()
	file.close()
except IOError:
	print("cannot open ", file_name)	
else:
	print(text)


