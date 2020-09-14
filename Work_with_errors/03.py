class TupoiDebil(Exception): # Так пишется кастомная ошибка
    """Are you mad bro?"""

def bigger_than_one(x):
    if x <= 0:
        raise TupoiDebil("Are you mad bro?")

print(bigger_than_one(0))
