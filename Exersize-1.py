from math import gcd

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        #Checking type of input & raise it if it's not correct type.
        if not isinstance(numerator, int):
            raise TypeError('You have to enter numerator as an integer not other types!')
        if (not isinstance(denominator, int)):
            raise TypeError('You have to enter denominator as an integer not other types!')
        #Checking denominator for being non-zero that is impossible.
        if denominator == 0:
            raise ZeroDivisionError('The Denominator can\'t be zero.')
        self.numerator= numerator
        self.denominator= denominator
    #To reduce or we can say make it as fraction that is the most simple that it can be.
    def reduce(self, fraction):
        d = gcd(fraction.numerator, fraction.denominator)
        fraction.numerator, fraction.denominator = fraction.numerator/ d, fraction.denominator/ d
        return fraction
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)
    def __add__(self, other):
        numerator= self.get_numerator() * other.get_denominator() + other.get_numerator() * self.get_denominator()
        denominator= self.get_denominator() * other.get_denominator()
        return self.reduce(Fraction(numerator, denominator))
    def __sub__(self, other):
        numerator= self.get_numerator() * other.get_denominator() - other.get_numerator() * self.get_denominator()
        denominator= self.get_denominator() * other.get_denominator()
        return self.reduce(Fraction(numerator, denominator))
    def __mul__(self, other):
        if self.numerator == 0 or other.numerator == 0:
            return 0
        else:
            numerator = self.get_numerator() * other.get_numerator()
            denominator = self.get_denominator() * other.get_denominator()
            return self.reduce(Fraction(numerator, denominator))
    def __truediv__(self, other):
        if self.numerator == 0:
            return 0
        else:
            numerator = self.get_numerator() * other.get_denominator()
            denominator = self.get_denominator() * other.get_numerator()
            return self.reduce(Fraction(numerator, denominator))
def show_menu():
    print("""All your choices :
    1. Add 
    2. Subtract
    3. Multiplication
    4. Division  
    5. Exit
    """)
def get_fraction():
    numerator = int(input('Please enter numerator of your fraction : '))
    denominator = int(input('Please enter denominator of your fraction : '))
    return numerator, denominator
    
    
    
def main():
    print('Please enter your First Fraction nums : ')
    numerator, denominator = get_fraction()
    fraction1 = Fraction(numerator, denominator)
    print('Enter for Second Fraction: ')
    numerator, denominator = get_fraction()
    fraction2 = Fraction(numerator, denominator)
    while True:
        show_menu()
        choice = abs(int(input('Please choose one above choice : ')))
        if choice == 1:
            print('It is : ', fraction1 + fraction2)
        elif choice == 2:
            print('It is : ', fraction1 - fraction2)
        elif choice == 3:
            print('It is : ', fraction1 * fraction2)
        elif choice == 4:
            print('It is : ', fraction1 / fraction2)
        elif choice == 5:
            print('Tnx for using this program ... have good time ;) ')
            exit()
        else:
            print('Please choose number in our range.')
if __name__ == '__main__':
    main()