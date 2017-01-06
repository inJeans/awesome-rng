import unittest

from scipy.stats import chisquare
from scipy.stats import kstest

from awesome_rng import init_awesome_rng
from awesome_rng import awesome_rng

NUM_TEST = 1000
TEST_SEED = 1

class TestAwesomeRNG(unittest.TestCase):

    def test_domain(self):
        init_awesome_rng(TEST_SEED)
        rand_list = [awesome_rng() for r in range(NUM_TEST)]

        assert min(rand_list) > 0.
        assert max(rand_list) < 1.

    def test_chi_squared(self):
        init_awesome_rng(TEST_SEED)
        rand_list = [awesome_rng() for r in range(NUM_TEST)]

        _, p = chisquare(rand_list)

        assert p > 0.99

    def test_kolmogorov_smirnov(self):
        init_awesome_rng(TEST_SEED)
        rand_list = [awesome_rng() for r in range(NUM_TEST)]

        D, _ = kstest(rand_list, 'uniform')
        print(D)

        assert D < 0.05
