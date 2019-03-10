def Rabbit2():
	try:
		from Two.Three.Trois import Target
		print('Target Found')
		Target()
	except ImportError:
		print('Target Lost')
