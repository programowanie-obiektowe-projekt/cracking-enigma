import unittest
from Crypto.Random import get_random_bytes
from algorithms.AES import AESAdapter

class TestAESAdapter(unittest.TestCase):
    def setUp(self):
        self.aes_adapter = AESAdapter()

    def test_encrypt_returns_encrypted_data_and_key(self):
        text = b"Hello, World!"
        encrypted_data, key = self.aes_adapter.encrypt(text)
        self.assertIsNotNone(encrypted_data)
        self.assertIsNotNone(key)

    def test_decrypt_returns_decrypted_text(self):
        text = b"Hello, World!"
        encrypted_data, key = self.aes_adapter.encrypt(text)
        decrypted_text = self.aes_adapter.decrypt(encrypted_data, key)
        self.assertEqual(text, decrypted_text.encode('utf-8'))

    def test_decrypt_with_wrong_key_raises_error(self):
        text = b"Hello, World!"
        encrypted_data, _ = self.aes_adapter.encrypt(text)
        wrong_key = get_random_bytes(16)
        with self.assertRaises(Exception):
            self.aes_adapter.decrypt(encrypted_data, wrong_key)

    def test_brute_force_returns_dictionary(self):
        text = b"Hello, World!"
        encrypted_data, _ = self.aes_adapter.encrypt(text)
        result = self.aes_adapter.brute_force(encrypted_data, text)
        self.assertIsInstance(result, dict)

    def test_brute_force_dictionary_contains_expected_keys(self):
        text = b"Hello, World!"
        encrypted_data, _ = self.aes_adapter.encrypt(text)
        result = self.aes_adapter.brute_force(encrypted_data, text)
        self.assertIn('msg', result)
        self.assertIn('iterations', result)
        self.assertIn('decrypted_data', result)

    def test_frequency_analysis_returns_dictionary(self):
        text = b"Hello, World!"
        encrypted_data, _ = self.aes_adapter.encrypt(text)
        result = self.aes_adapter.frequency_analysis(encrypted_data)
        self.assertIsInstance(result, dict)

    def test_frequency_analysis_dictionary_contains_expected_keys(self):
        text = b"Hello, World!"
        encrypted_data, _ = self.aes_adapter.encrypt(text)
        result = self.aes_adapter.frequency_analysis(encrypted_data)
        self.assertIn('status', result)
        self.assertIn('decrypted_data', result)

if __name__ == '__main__':
    unittest.main()