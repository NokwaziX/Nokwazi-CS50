'''
In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).


'''

def main():
    time = input('What is the time? ')

    time_float = convert(time)

    if time_float >= 7 and time_float <= 8:
        print ('breakfast time')
    elif time_float >= 12 and time_float <= 13:
        print('lunch time')
    elif time_float >= 18 and time_float <= 19:
        print('dinner time')


def convert(time):
    hours, mins = time.split(':') #find a colon in the string/input ans split string into 2 parts. 1st value(left)= hours and 2nd value(right)= mins
    hours_int, mins_int = int(hours), int(mins) #convert the entire thing to a float by converting the string to integers

    time_float = hours_int + mins_int / 60 #  to convert mins to hours? Divide hour by 60
    return time_float


if __name__ == "__main__":
    main()
