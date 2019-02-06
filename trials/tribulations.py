import matplotlib.pyplot as plt
class Line():
    pass



Prime = Line()


def NewLine():
    ECS = input('Eastings Start -->')
    NCS = input('Northings Start -->')
    ECE = input('Eastings End -->')
    NCE = input('Northings End -->')
    try:
        float(ECS)
        float(NCS)
        float(ECE)
        float(NCE)
    except ValueError:
        Retry()
    Prime.ECS = float(ECS)
    Prime.NCS = float(NCS)
    Prime.ECE = float(ECE)
    Prime.NCE = float(NCE)
    # Origin()
    Mid()


def Mid():
    Prime.MidE = (Prime.ECS + Prime.ECE)/2
    Prime.MidN = (Prime.NCS + Prime.NCE)/2
    print (Prime.MidE)
    print (Prime.MidN)
    Draw()


def Draw():
    x = [Prime.ECS, Prime.MidE, Prime.ECE]
    y = [Prime.NCS, Prime.MidN, Prime.NCE]
    plt.plot(x, y)
    plt.xlabel('Eastings')
    plt.ylabel('Northings')
    plt.title('Line')
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
    plt.show()



#def Origin():
#    Prime.EFO = Prime.ECS - Prime.ECE
#    Prime.NFO = Prime.NCS - Prime.NCE
#    print(Prime.EFO)
#    print(Prime.NFO)

def Retry():
    YN = input('Y/N? -->')
    if YN == 'Y' or YN == 'y':
        NewLine()
    else:
        quit()

print(5/2)
NewLine()
