import unittest
from runner_and_tournament import Tournament,Runner

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

    def test_1(self):
        self.test = Tournament(90, self.runner_1, self.runner_3)
        self.all_results.update(dict(self.test.start()))
        self.assertTrue(self.all_results[len(self.all_results)], self.runner_1)

    def test_2(self):
        self.test = Tournament(90,  self.runner_2, self.runner_3)
        self.all_results.update(dict(self.test.start()))
        self.assertTrue(self.all_results[len(self.all_results)], self.runner_2)

    def test_3(self):
        self.test = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update(self.test.start())
        self.assertTrue(self.all_results[len(self.all_results)], self.runner_3)



Test = TournamentTest()







