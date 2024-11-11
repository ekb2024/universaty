import unittest
from runner_and_tournament import Tournament,Runner

class RunnerTest(unittest.TestCase):
    @unittest.skipIf(Runner.is_frozen, "test 12_3 walk")
    def test_walk(self):
        self.obj = Runner('')
        for i in range(10):
           self.obj.walk()
        self.assertEqual(self.obj.distance,50)

    @unittest.skipIf(Runner.is_frozen, "test 12_3 run")
    def test_run(self):
        self.obj = Runner('')
        for i in range(10):
           self.obj.run()
        self.assertEqual(self.obj.distance,100)

    @unittest.skipIf(Runner.is_frozen, "test 12_3 test_challenge")
    def test_challenge(self):
        self.obj1 = Runner('')
        self.obj2 = Runner('')
        for i in range(10):
            self.obj1.walk()
            self.obj2.run()
        self.assertNotEqual(self.obj1.distance, self.obj2.distance)


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн',10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)
    def tearDown(self):
         for i in self.all_results.keys():
             self.all_results[i] = str(self.all_results[i])
         print(self.all_results)

    @unittest.skipIf(Tournament.is_frozen,"test 12_3 test_1  Тесты в этом кейсе заморожены")
    def test_1(self):
            self.test = Tournament(90, self.runner_1, self.runner_3)
            self.all_results.update(dict(self.test.start()))
            self.assertTrue(self.all_results[len(self.all_results)], self.runner_1)

    @unittest.skipIf(Tournament.is_frozen, "test 12_3 test_2  Тесты в этом кейсе заморожены")
    def test_2(self):
        self.test = Tournament(90,  self.runner_2, self.runner_3)
        self.all_results.update(dict(self.test.start()))
        self.assertTrue(self.all_results[len(self.all_results)], self.runner_2)

    @unittest.skipIf(Tournament.is_frozen, "test 12_3 test_3  Тесты в этом кейсе заморожены")
    def test_3(self):
        self.test = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update(self.test.start())
        self.assertTrue(self.all_results[len(self.all_results)], self.runner_3)

