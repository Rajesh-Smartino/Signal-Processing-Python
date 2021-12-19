import numpy as np

class Polynomial():
    """poly: [(1, 4), (3, 6), (2, 2)]: x^4 + 3x^6 + 2x^2"""
    
    def __init__(self, poly):
        self.poly = poly
        
    def __str__(self):
        f_string = ""
        for i in self.poly:
            s = "{}X^{}".format(i[0], i[1])
            f_string = "{} {} {}".format(f_string, '+' if i[0] > 0 else '-', s)
            
        return f_string
        
    def __add__(self, second_object):
        
        added = self.poly + second_object.poly
        dictionary = {}
        for idx in range(len(added)):
            if added[idx][1] in dictionary:
                dictionary[added[idx][1]] += added[idx][0]
            else:
                dictionary[added[idx][1]] = added[idx][0]
                    
        return [(dictionary[key], key) for key in dictionary.keys()]
    
    def __call__(self):
        return self.poly
    
    def numpy_root(self):
        """np.roots takes a list: f the polynomial is x^2 +3x^1 + 1, then the array will be [1, 3, 1]"""
        max_val = max([i[1] for i in self.poly])
        arr = [0 for i in range(max_val + 1)]
        for i in self.poly:
            arr[max_val - i[1]] = i[0]
            
        return np.roots(arr)
        
u = Polynomial([(1, 4), (3, 6), (2, 2)])
v = Polynomial([(1, 4), (3, 6), (2, 2)])

print('\n---------- Addition of Polynomials ----------\n')
print(u+v)
print('\n---------- Call Method ----------')
print(u())
print('\n---------- Show Polynomial ----------')
print(u)
print('\n---------- Roots Addition of Polynomials ----------')
print(u.numpy_root())
print('\n')