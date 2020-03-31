def Rabbit1():
	try:
		from One.Two.Deux import Target
		print('Target Found')
		Target()
	except ImportError:
		print('Target Lost')
hello         
