import unittest
import runner


#unittest.TestCase
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.obj = runner.Runner('')
        for i in range(10):
           self.obj.walk()
        self.assertEqual(self.obj.distance,50)

    def test_run(self):
        self.obj = runner.Runner('')
        for i in range(10):
           self.obj.run()
        self.assertEqual(self.obj.distance,100)


    def test_challenge(self):
        self.obj1 = runner.Runner('')
        self.obj2 = runner.Runner('')
        for i in range(10):
            self.obj1.walk()
            self.obj2.run()
        self.assertNotEqual(self.obj1.distance, self.obj2.distance)

test = RunnerTest()
