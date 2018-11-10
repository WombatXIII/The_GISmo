def ll():
        llen = float(input('Laid length--->'))
        dlen = float(input('Digi length--->'))
        tol_p = 5
        tol_m = 2
        tol_md = (tol_m * 2)
        tol_mneg = tol_m - tol_md
        threshold = 40
        if llen >= threshold:
            dif = (llen/dlen)*100
            if dif > (100-tol_p):
                blue = ('Too short, not within '+str(tol_p)+'%')
            if dif >= (100-tol_p) and dif <= (100+tol_p):
                blue = ('Within Tollerance of '+str(tol_p)+'%')
            if dif > (100+tol_p):
                blue = ('Too long, not wihtin '+str(tol_p)+'%')
        if llen < threshold:
            dif = llen-dlen
            if dif > tol_m:
                blue = ('Too short')
            if dif < tol_m and dif > tol_mneg:
                blue = ('Within Tollerance')
            if dif < tol_mneg:
                blue = ('Too long')
            else:
                blue = ('No god damn clue')

        print(blue)
        again()


def again():
        print('Again?')
        yn = str(input('Y/N?'))
        if yn == 'Y' or yn == 'y' or yn == 'yes':
                ll()
        if yn == 'N' or yn == 'n' or yn == 'no':
                quit()
        if yn == 'report':
                report()
        if yn == 'perams':
                perams()
        else:
                again()


def report():
    print('laid length'+str(llen))
    print('digi length'+str(dlen))
    print('tol_p'+str(tol+p))
    print('tol_m'+str(tol_m))
    print('tol_md'+str(tol_md))
    print('tol_mneg'+str(tol_mneg))
    again()


def perams():
    print('Please define the folllowing; (standard given in brackets)')
    threshold = float(input('What is the percentage threshold? (40m) ---> '))
    tol_p = float(input('Percentage tollaerance above threshold (5%) --->'))
    tol_m = float(input('meter tollerance below threshold (2m) --->'))
    again()


ll()
