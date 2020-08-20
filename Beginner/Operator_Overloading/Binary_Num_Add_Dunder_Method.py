
class bnum:

    """
    A class called bnum that is binary number that takes a decimal
    number as an input and outputs the binary representation of that decimal number in the form of a
    list.
    a. Create a function show() which displays the binary representation of the decimal number.
    b. Create a __add__() function that adds two binum objects.
    c. Create a val() function that returns the decimal representation of the above added binary
    numbers.
    """

    def __init__(self,x):
        self.d = x

    def show(self):
        self.b = bin(self.d)
        print (self.b[2:])

    def __add__(self,other):
        add = self.d + other.d
        return bnum(add)

    def val(self):
        print(int(self.b,2))
        # Converting Binary to int we need to supply int(binary_with_0b,2)


X= bnum(10)
X.show()
Y= bnum(16)
Y.show()
Z=X+Y
Z.show()
Z.val()    


def f(y):
    return la+y

la=10
print(f(20))
