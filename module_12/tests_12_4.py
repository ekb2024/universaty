import unittest
import logging
from  rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
          self.obj = Runner("fabio",-2)
          for i in range(10):
             self.obj.walk()
          self.assertEqual(self.obj.distance,50)
          logging.info('test_walk выполнен успешно', exc_info=True)
        except ValueError:
           logging.warning('Неверная скорость для Runner ', exc_info=True)

    def test_run(self):
        try:
          self.obj = Runner(45)
          for i in range(10):
            self.obj.run()
          self.assertEqual(self.obj.distance,100)
          logging.info('test_run выполнен успешно', exc_info=True)
        except TypeError:
           logging.warning('Неверный тип данных для объекта Runner ', exc_info=True)

#runner = RunnerTest()


logging.basicConfig(level=logging.INFO,filename='runner_tests.log',filemode='w',encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
