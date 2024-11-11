import unittest
import tests_12_2,tests_12_1

tests_12_1_ = unittest.TestSuite()
tests_12_1_.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
tests_12_2_ = unittest.TestSuite()
tests_12_2_.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runn = unittest.TextTestRunner( verbosity=2.)
runn.run(tests_12_1_)
runn.run(tests_12_2_)


