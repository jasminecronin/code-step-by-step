print('This program calculates y coordinates for a line.')
m = int(input('Enter slope (m): '))
b = int(input('Enter intercept (b): '))
x = int(input('Enter x: '))
while x != -1:
    y = m * x + b
    print('f(' + str(x) + ') = ' + str(y))
    x = int(input('Enter x: '))
