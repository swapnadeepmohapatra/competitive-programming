def hcf(wbc, rbc):
    return wbc if (rbc == 0) else hcf(rbc, wbc % rbc)


redC = 5000000
whiteC = 8000

factor = hcf(redC, whiteC)

whiteR = int(whiteC / factor)
redR = int(redC / factor)

print('Aspect Ration: ', whiteR, ' : ', redR)
