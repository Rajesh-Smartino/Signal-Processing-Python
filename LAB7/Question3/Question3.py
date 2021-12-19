import math

class NewComplex():
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        return "{} {} i{}".format(self.real, '-' if self.imaginary < 0 else '+', abs(self.imaginary))
    
    def __add__(self, second_object):
        return NewComplex(self.real + second_object.real, self.imaginary + second_object.imaginary)
    
    def __mul__(self, second_object):
        real_real = self.real * second_object.real
        real_img = self.real * second_object.imaginary
        img_real = second_object.real * self.imaginary
        img_img = second_object.imaginary * self.imaginary
        return NewComplex(real_real - img_img, real_img + img_real)
    
    def __le__(self, second_object):
        n1 = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        n2 = math.sqrt(second_object.real ** 2 + second_object.imaginary ** 2)
        return n1 <= n2
    
    def __lt__(self, second_object):
        n1 = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        n2 = math.sqrt(second_object.real ** 2 + second_object.imaginary ** 2)
        return n1 < n2
    
    def __ge__(self, second_object):
        n1 = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        n2 = math.sqrt(second_object.real ** 2 + second_object.imaginary ** 2)
        return n1 >= n2
    
    def __gt__(self, second_object):
        n1 = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        n2 = math.sqrt(second_object.real ** 2 + second_object.imaginary ** 2)
        return n1 > n2
        
        
u = NewComplex(9, -3)
v = NewComplex(0, 1)
print('------------ Input Complex Numbers ------------')
print('a = {}\nb = {}'.format(u, v))
print('\n------------ Addition of Complex Numbers ------------\n')
w = u + v
print(w)

print('\n------------ Multiplication of Complex Numbers ------------\n')
w = u * v
print(w)

print('\n------------ Complex Numbers Comparison by Modulus ------------')
print('------------ Less than equal to ------------')
print(u <= v)
print('------------ Less than ------------')
print(u < v)
print('------------ Greater than equal to ------------')
print(u >= v)
print('------------ Greater than ------------')
print(u > v)