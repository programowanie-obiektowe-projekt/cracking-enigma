import unittest
from algorithms.Cezar import CezarAdapter, CezarClass

class TestCezar(unittest.TestCase):
    def test_encrypt(self):
        plaintext = "hello"
        key = 3
        expected_ciphertext = "khoor"
        algorithm = CezarClass()
        self.assertEqual(algorithm.szyfruj(plaintext, key)[0], expected_ciphertext)

    def test_decrypt(self):
        ciphertext = "khoor"
        key = 3
        expected_plaintext = "hello"
        algorithm = CezarClass()
        self.assertEqual(algorithm.szyfruj(ciphertext, -key)[0], expected_plaintext)

    def test_brute_force(self):
        ciphertext = "khoor"
        original = "hello"
        algorithm = CezarClass()
        self.assertEqual(algorithm.bruteForce(ciphertext, original)['status'], "Udało się złamać szyfr")

if __name__ == '__main__':
    unittest.main()