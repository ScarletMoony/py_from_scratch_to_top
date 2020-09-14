import unittest # Модуль для юниттеста
import fizz_buzz # Код для юниттеста

class FizzBuzzTest(unittest.TestCase): # Старт теста

    def test_fizz(self):

        number = 6

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'Fizz') # Проверка возврата функции
        
    def test_buzz(self):

        number = 5

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):

        number = 15

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'FizzBuzz')

if __name__ == '__main__': # Проверка как был запущен скрипт
    unittest.main()
