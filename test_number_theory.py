import unittest
from src.number_theory import is_prime,gcd_euclid,fibonacci
class TestNumberTheory(unittest.TestCase):
    def test_primes(self):
        self.assertEqual([n for n in range(20) if is_prime(n)],[2,3,5,7,11,13,17,19])
    def test_gcd(self):
        self.assertEqual(gcd_euclid(54,24),6)
        self.assertEqual(gcd_euclid(-15,0),15)
    def test_fibonacci(self):
        self.assertEqual(fibonacci(10),55)
        with self.assertRaises(ValueError): fibonacci(-1)
if __name__=='__main__': unittest.main()
