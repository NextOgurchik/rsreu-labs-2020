import math

class Color:
    """Дескриптор для изображений в RGB формате"""
    def __set_name__(self, owner, name):
        self.__name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
 
    def __set__(self, instance, value):
        if isinstance(value, int) and value >= 0 and value <= 255:
            instance.__dict__[self.__name] = value
        else:
            raise Exception('Числа должны быть в диапозоне от 0 до 255')

class RGB:
    """Изображение в RGB формате"""
    Red = Color()
    Green = Color()
    Blue = Color()

    def __init__(self, red = 0, green = 0, blue = 0):
            self.Red = red
            self.Green = green
            self.Blue = blue
    
    cmyk_scale = 100

    def tocmyk(self):
        """Перевод RBG в CMYK"""
        cmyk_scale = 100
        if (self.Red == 0) and (self.Green == 0) and (self.Blue == 0):
            return 0, 0, 0, cmyk_scale
        c = 1 - self.Red / 255.
        m = 1 - self.Green / 255.
        y = 1 - self.Blue / 255.
        min_cmy = min(c, m, y)
        c = (c - min_cmy) / (1 - min_cmy)
        m = (m - min_cmy) / (1 - min_cmy)
        y = (y - min_cmy) / (1 - min_cmy)
        k = min_cmy
        return f"({int(c * cmyk_scale)},{int(m * cmyk_scale)},{int(y * cmyk_scale)},{int(k * cmyk_scale)})"

    def __add__(self, other):
        return RGB(self.Red + other.Red, self.Green + other.Green, self.Blue + other.Blue)

    def __sub__(self, other):
        return RGB(self.Red - other.Red, self.Green - other.Green, self.Blue - other.Blue)

    def __str__(self):
        return f"({self.Red},{self.Green},{self.Blue})"

    def __lt__(self, other):
        return math.sqrt(self.Red ** 2 + self.Green ** 2 + self.Blue ** 2) < math.sqrt(other.Red ** 2 + other.Green ** 2 + other.Blue ** 2)

    def __le__(self, other):
        return math.sqrt(self.Red ** 2 + self.Green ** 2 + self.Blue ** 2) <= math.sqrt(other.Red ** 2 + other.Green ** 2 + other.Blue ** 2)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        return math.sqrt(self.Red ** 2 + self.Green ** 2 + self.Blue ** 2) >= math.sqrt(other.Red ** 2 + other.Green ** 2 + other.Blue ** 2)

    def __eq__(self, other):
        return math.sqrt(self.Red ** 2 + self.Green ** 2 + self.Blue ** 2) == math.sqrt(other.Red ** 2 + other.Green ** 2 + other.Blue ** 2)

    def __ne__(self, other):
        return not self.__eq__(other)

rgb = RGB(0,0,100)
rgb2 = RGB(0,0,100)
print(rgb)
print(rgb2)
# print(rgb + rgb2)
# print(rgb2 - rgb)
print(rgb >= rgb2)
print(rgb < rgb2)
print(rgb.tocmyk())
