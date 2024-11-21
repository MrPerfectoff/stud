import logging
import unittest
from runnerTest import Runner

logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    filemode='w',  # Убедитесь, что используете filemode
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Test Runner", -5)  # Передаем отрицательное значение speed
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(12345, 5)  # Передаем некорректный тип name (должно быть строкой)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

if __name__ == "__main__":
    unittest.main()