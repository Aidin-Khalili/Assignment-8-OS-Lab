class complex_Nums:
    def __init__(self, real_part, imaginary_part = 0.0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
    def __repr__(self):
        return str(self.real_part) + ' + (' + str(self.imaginary_part) + ') i'
    def __add__(self, other):
        real_part = self.real_part + other.real_part
        imaginary_part = self.imaginary_part + other.imaginary_part
        return complex_Nums(real_part, imaginary_part)
    def __mul__(self, other):
        real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary_part = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return complex_Nums(real_part, imaginary_part)
    def __sub__(self, other):
        real_part = self.real_part - other.real_part
        imaginary_part = self.imaginary_part - other.imaginary_part
        return complex_Nums(real_part, imaginary_part)
def menu():
    print("""All your choices are :
        1. Add
        2. Multiplication
        3. Subtract
        4. Exit
        """)
def get_complex_num():
    real_part = int(input('Plesae enter your real_part of your complex number : '))
    imaginary_part = int(input('Plesae enter your imaginary_part of your complex number : '))
    return real_part, imaginary_part



def main():
    print('Please enter these part for your first complex number : ')
    real_part, imaginary_part = get_complex_num()
    complex_number1 = complex_Nums(real_part, imaginary_part)
    print('Please enter these part for your second complex number : ')
    real_part, imaginary_part = get_complex_num()
    complex_number2 = complex_Nums(real_part, imaginary_part)
    while True:
        menu()
        choice = abs(int(input('Please choose one choice : ')))
        if choice == 1:
            print('It\'s : ', complex_number1 + complex_number2)
        elif choice == 2:
            print('It\'s : ', complex_number1 * complex_number2)
        elif choice == 3:
            print('It\'s : ', complex_number1 - complex_number2)
        elif choice == 4:
            print('Thanks for using our program ... have good tim ;)')
            exit()
        else:
            print('You have entered incorrectly number ... please choose between range that we said.')
if __name__ == '__main__':
    main()