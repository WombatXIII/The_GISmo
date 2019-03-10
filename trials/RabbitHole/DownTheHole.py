def FindRabbits():
	try:
		from One.Uno import Rabbit1
		print('Rabbit 1 ready for duty')
		Rabbit1()
	except ImportError:
		print('rabbit 1 not found')
	try:
		from One.Two.Dos import Rabbit2
		print('Rabbit 2 ready for duty')
		Rabbit2()
	except ImportError:
		print('rabbit 2 not found')
	try:
		from One.Two.Three.Tres import Rabbit3
		print('Rabbit 1 ready for duty')
		Rabbit3()
	except ImportError:
		print('rabbit 3 not found')


FindRabbits()

print('         ')
print('Rabbit 1 should Hit.')
print('rabbit 2 should report but lose target')
print('Rabbit 3 should not be found.')
