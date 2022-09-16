def check_weather(temperature):
    if temperature < 0:
        return 'На улице холодно'
    elif temperature >= 15 and temperature < 25:
        return 'На улице тепло'
    return 'Не работает'

print(check_weather(-1)) # На улице холодно
print(check_weather(8)) # На улице прохладно
print(check_weather(21)) # На улице тепло
print(check_weather(32)) # На улице жарко