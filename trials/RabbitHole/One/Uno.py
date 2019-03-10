def Rabbit1():
	try:
		from Two.Deux import Target
		print('Target Found')
		Target()
	except ImportError:
		print('Target Lost')
