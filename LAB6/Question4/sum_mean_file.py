

with open('/Users/rajeshr/Desktop/input_b') as file:
    inp = file.read()

lines = inp.split('\n')

for l in lines:
    add = 0
    vals = l.split()
    for n in vals:
        try:
            add += int(n)
        except ValueError:
            pass
    print('SUM:', add, end=', ')
    try:
        print('MEAN:', add/len(vals))
    except ZeroDivisionError:
        print('MEAN:', 0)
        
    print()