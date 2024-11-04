weekDays = ['Понеделник', 'Вторник', 'Сряда', 'Четвъртък', 'Петък', 'Събота', 'Неделя']

def monthDays(month, year):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def getDate():
    while True:
        try:
            year = int(input("Въведете година: "))
            if year < 1:
                print('Годината не може да бъде 0 или отрицателно число!')
                continue
            month = int(input("Въведете месец: "))
            if month < 1 or month > 12:
                print('Месецът трябва да бъде в диапазона от 1 до 12!')
                continue
            day = int(input("Въведете ден: "))
            if day < 1 or day > monthDays(month, year):
                print(f'Невалиден ден за съответния месец! (1-{monthDays(month, year)})')
                continue
            return day, month, year
        except ValueError:
            print('Моля, въведете валидни числа за ден, месец и година.')

def getAddedDays():
    while True: 
        try:
            daysAdd = int(input("Въведете броя дни: "))
            if daysAdd < 0:
                print('Дните за добавяне не могат да бъдат 0 или отрицателно число!')
                continue
            return daysAdd      
        except ValueError:
            print('Моля, въведете валидно число за броя дните, които искате да добавите.')

def findDayOfWeek(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    a = year % 100
    b = year // 100
    c = (day + 13 * (month + 1) // 5 + a + a // 4 + b // 4 - 2 * b) % 7
    return (c + 6) % 7

day, month, year = getDate()
addedDays = getAddedDays()
while addedDays > 0:
    daysInMonth = monthDays(month, year)
    if day + addedDays <= daysInMonth:
        day += addedDays
        addedDays = 0
    else:
        addedDays -= (daysInMonth - day + 1)
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
indexOfWantedDay = findDayOfWeek(year, month, day)
print(f'Дата: {day:02d}/{month:02d}/{year} - {weekDays[indexOfWantedDay-1]}')