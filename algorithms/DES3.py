from Crypto.Random import get_random_bytes
import itertools
import time
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

from algorithms.algorithm_interface import AlgorithmInterface



class DES3Adapter(AlgorithmInterface):
    def __init__(self):
        self.algorithm = DES3Class()

    def encrypt(self, text):
        return self.algorithm.encrypt_DES(text)

    def decrypt(self, encrypted_text, key):
        iv = encrypted_text[:DES.block_size]
        if isinstance(iv, str):
            iv = bytes(iv[2:-1], 'utf-8').decode('unicode_escape', 'ignore').encode(
                    'latin1')
        encrypted_text = encrypted_text[DES.block_size:]
        if isinstance(encrypted_text, str):
            encrypted_text = encrypted_text.encode('latin1')

        return self.algorithm.decrypt_DES(encrypted_text, key, iv)

    def brute_force(self, encrypted_text, original):
        iv = encrypted_text[:DES.block_size]
        return self.algorithm.bruteForce_des(encrypted_text, iv, original)

    def frequency_analysis(self, encrypted_text):
        iv = encrypted_text[:DES.block_size]
        return self.algorithm.frequency_analysis_des(encrypted_text, iv)



class DES3Class:
    def encrypt_DES(self, text):
        key = get_random_bytes(8)
        cipher = DES.new(key, DES.MODE_CFB)
        msg = cipher.iv + cipher.encrypt(text)
        return msg, key,  cipher.iv

    def decrypt_DES(self, encrypted_data, key, iv):
        cipher = DES.new(key, DES.MODE_CFB, iv=iv)
        decrypted_text = cipher.decrypt(encrypted_data)
        return str(decrypted_text, 'utf-8')

    def bruteForce_des(self, encrypted_data, iv, original):
        start_time = time.time()
        max_time = 5
        attempts = 0

        for i in itertools.product(range(256), repeat=8):
            klucz = bytes(i)
            attempts += 1
            cipher = DES.new(klucz, DES.MODE_CFB, iv=iv)
            try:
                decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)
                if original == decrypted_data:
                    return {
                        "msg": f"udało się złamać po: {attempts} prób",
                        "iterations": attempts,
                        'decrypted_data': decrypted_data
                    }
                return
            except ValueError:
                pass

            if time.time() - start_time > max_time:
                return {
                    "msg": f"Nie udało się złamać po: {attempts} prób",
                    "iterations": attempts,
                    'decrypted_data': ''
                }

    def frequency_analysis_des(self, encrypted_data, iv):
        start_time = time.time()
        max_time = 300
        attempts = 0
        freq_polish = {'a': 8.91, 'b': 1.47, 'c': 3.96, 'd': 3.25, 'e': 7.66, 'f': 0.3, 'g': 1.42, 'h': 1.08, 'i': 8.21,
                       'j': 2.28, 'k': 3.51, 'l': 2.1, 'm': 2.8, 'n': 5.52, 'o': 7.75, 'p': 3.13, 'q': 0.14, 'r': 4.69,
                       's': 4.32, 't': 3.98, 'u': 2.5, 'v': 0.04, 'w': 4.65, 'x': 0.02, 'y': 3.76, 'z': 5.64}

        for i in itertools.product(range(256), repeat=8):
            klucz = bytes(i)
            cipher = DES.new(klucz, DES.MODE_CFB, iv=iv)
            try:
                decrypted_data = cipher.decrypt(encrypted_data, )

                freq_decrypted = {}
                for letter in decrypted_data:
                    if letter in freq_decrypted:
                        freq_decrypted[letter] += 1
                    else:
                        freq_decrypted[letter] = 1

                diff_freq = {}
                for letter in freq_decrypted:
                    diff_freq[letter] = abs(freq_decrypted[letter] - freq_polish.get(letter, 0))
                    attempts += 1

                min_diff_letter = min(diff_freq, key=diff_freq.get)

                if diff_freq[min_diff_letter] < 0.01:
                    msg = "Znaleziono klucz: " + str(
                        klucz) + " Oryginalny tekst: " + decrypted_data + " Złamano w " + str(
                        time.time() - start_time) + " sekund"
                    return {
                        "msg": msg,
                        "iterations": attempts,
                        'decrypted_data': decrypted_data
                    }
            except ValueError:
                pass
            if time.time() - start_time > max_time:
                msg = f"Nie udało się złamać po: {attempts} prób"
                return {
                    "msg": msg,
                    "iterations": attempts,
                    'decrypted_data': ''
                }

