class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        if hour < 0 or minute < 0 or second < 0: #Clearly when we get abs form, it doesen't nessesary but possibly someone wants to just use our class ...
            raise ValueError('You entered some negative(invalid) value but we correct it. (get it positive)')
        self.hour = abs(hour)
        self.minute = abs(minute)
        self.second = abs(second)
    def __repr__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __add__(self, other):
        if isinstance(other, Time):
            return self.time_increment(other)
        else:
            return self.second_increment(other)
    def __sub__(self, other):
        if isinstance(other, Time):
            return self.time_decrement(other)
        else:
            return self.second_decrement(other)
    def second_decrement(self, seconds):
        seconds -= self.time_to_second()
        while seconds < 0:
            self.minute -= 1
            self.second += 60
        return self.second_to_time(seconds)
    def time_decrement(self, other):
        seconds = self.time_to_second() - other.time_to_second()
        return self.second_to_time(seconds)
    def second_increment(self, seconds):
        seconds += self.time_to_second()
        return self.second_to_time(seconds)
    def time_increment(self, other):
        seconds = self.time_to_second() + other.time_to_second()
        return self.second_to_time(seconds)
    def second_to_time(self, seconds):
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)
        return self
    def time_to_second(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
def menu():
    print("""All your choices are :
    1. Add
    2. Subtract
    3. Make seconds to time format(hour:minute:day)
    4. make time format to seconds
    5. Exit program
    """
def get_time_foramt():
    hour = abs(int(input('Please enter an hour of your time : ')))
    minute = abs(int(input('Please enter an minute of your time : ')))
    second = abs(int(input('Please enter an second of your time : ')))
    return hour, minute, second


def main():
    while True:
        menu()
        choice = abs(int(input('Please Take a Choice: ')))
        if choice == 1:
            print('Please enter numbers for your first time format : ')
            hour, minute, second = get_time_foramt()
            time1 = Time(hour, minute, second)
            print('Enter for Second Time: ')
            hour, minute, second = get_time_foramt()
            time2 = Time(hour, minute, second)
            print('It\s : ', time1 + time2)
        elif choice == 2:
            print('Enter for First Time: ')
            hour, minute, second = get_time_foramt()
            time1 = Time(hour, minute, second)
            print('Enter for Second Time: ')
            hour, minute, second = get_time_foramt()
            time2 = Time(hour, minute, second)
            print('It\s : ', time1 - time2)
        elif choice == 3:
            s = abs(int(input('Please enter your seconds value to vonvert to time format : ')))
            obj = Time(second = s)
            print('It\s : ', obj.second_to_time(s))
        elif choice == 4:
            print('Please enter in time format to convert to the seconds : ')
            hour, minute, second = get_time_foramt()
            obj = Time(hour, minute, second)
            print('It\s : ', obj.time_to_second())
        elif choice == 5:
            print('Tnx for using this program ... Have good time ;)')
            exit()
        else:
            print('Please choose your choice in range that we said!')
if __name__ == '__main__':
    main()