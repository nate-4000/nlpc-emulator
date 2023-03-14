import ctypes

class int8(ctypes.c_int8):
    """
ever needed 8 bit numbers that dont mess with you?
too scared to touch ctypes?
use this!
works great!
doesnt kill your family! (citation needed)
perfect twos complement!
    """
    def __repr__(self):
        return str(self.value)
    
    def __add__(self, other):
        return int8(self.value + other.value)
    
    def __sub__(self, other):
        return int8(self.value - other.value)
    
    def __mul__(self, other):
        return int8(self.value * other.value)
    
    def __floordiv__(self, other):
        return int8(self.value // other.value)
    
    def __truediv__(self, other):
        return int8(self.value / other.value)
    
    def __mod__(self, other):
        return int8(self.value % other.value)
    
    def __divmod__(self, other):
        return (int8(val) for val in divmod(self.value, other.value))
    
    def __pow__(self, other):
        return int8(pow(self.value, other.value))
    
    def __lshift__(self, other):
        return int8(self.value << other.value)
    
    def __rshift__(self, other):
        return int8(self.value >> other.value)
    
    def __and__(self, other):
        return int8(self.value & other.value)
    
    def __xor__(self, other):
        return int8(self.value ^ other.value)
    
    def __or__(self, other):
        return int8(self.value | other.value)
    
    def __eq__(self, other):
        return int(self) == int(other)
    
    def __neg__(self):
        return int8(-self.value)
    
    def __pos__(self):
        return int8(+self.value)
    
    def __abs__(self):
        return int8(abs(self.value))
    
    def __invert__(self):
        return int8(~self.value)
    
    def __int__(self):
        return self.value