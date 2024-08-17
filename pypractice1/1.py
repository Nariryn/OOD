print(' *** Wind classification ***')
x = input('Enter wind speed (km/h) : ')
speed = float(x)
if speed<0:
    print('!!!Wrong value can\'t classify.')
elif 0 <=speed < 52:
    print('Wind classification is Breeze.')
elif 52 <= speed  < 56:
    print('Wind classification is Depression.')
elif 56 <= speed  < 102:
    print('Wind classification is Tropical Storm.')   
elif 102 <= speed  < 203:
    print('Wind classification is Typhoon.')
elif speed  >= 209:
    print('Wind classification is Super Typhoon.')