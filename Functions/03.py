def save_players(**kwargs): # Позволяет передавать сколько угодно ключ/значений
    for k, v in kwargs.items():
        print(k, v)

save_players(y = 23, sd = 2346)
