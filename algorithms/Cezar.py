import time

from Crypto.Random import random

from algorithms.algorithm_interface import AlgorithmInterface

class result:
    def __init__(self):
        iterations = 0
        decrypted_text = ''
        msg = ''

class CezarAdapter(AlgorithmInterface):
    def __init__(self):
        self.algorithm = CezarClass()

    def encrypt(self, text):

        # key = 3
        key = random.randint(1, 25)

        return self.algorithm.szyfruj(text, key)

    def decrypt(self, encrypted_text, key):
        print(encrypted_text)
        encrypted_text = encrypted_text.decode('utf-8')
        key = int.from_bytes(key, 'big')
        print('tu', key)
        return self.algorithm.szyfruj(encrypted_text, -key)

    def brute_force(self, encrypted_text, original):
        return self.algorithm.bruteForce(encrypted_text, original)

    def frequency_analysis(self, encrypted_text):
        return self.algorithm.frequency_analysis_cezar(encrypted_text)


class CezarClass:
    def szyfruj(self, napis, klucz):
        print('szyfruj', napis, klucz)
        szyfrogram = ""
        for i in napis:
            if i == ' ':
                szyfrogram += i
            else:
                litera = klucz + ord(i)
                if litera > ord('z'):
                    litera -= 26
                elif litera < ord('a'):
                    litera += 26
                szyfrogram += chr(litera)
        return szyfrogram, klucz

    def bruteForce(self, napis, original):

        start_time = time.time()
        for i in range(1, 26):
            decrypted_text = self.szyfruj(napis, -i)
            if decrypted_text[0].replace(' ', '').lower() == original.replace(' ', '').lower():
                end_time = time.time()
                key = i
                msg = "Znaleziono klucz: " + str(key) + " Oryginalny tekst: " + decrypted_text[0] + " Złamano w " + str(
                    end_time - start_time) + " sekund"
                result = {
                    'iterations': i,
                    'decrypted_text': decrypted_text[0],
                    'msg': msg
                }
                return result

    def frequency_analysis_cezar(self, cipher_text):
        start_time = time.time()
        max_time = 300
        attempts = 0

        freq_polish = {'a': 8.91, 'b': 1.47, 'c': 3.96, 'd': 3.25, 'e': 7.66, 'f': 0.3, 'g': 1.42, 'h': 1.08, 'i': 8.21,
                       'j': 2.28, 'k': 3.51, 'l': 2.1, 'm': 2.8, 'n': 5.52, 'o': 7.75, 'p': 3.13, 'q': 0.14, 'r': 4.69,
                       's': 4.32, 't': 3.98, 'u': 2.5, 'v': 0.04, 'w': 4.65, 'x': 0.02, 'y': 3.76, 'z': 5.64}

        try:
            freq_cipher = {}
            for letter in cipher_text:
                if letter in freq_cipher:
                    freq_cipher[letter] += 1
                else:
                    freq_cipher[letter] = 1

                if time.time() - start_time > max_time:
                    msg = f"Nie udało się złamać po: {attempts} prób"
                    return msg

                attempts += 1

            diff_freq = {}
            for letter in freq_cipher:
                diff_freq[letter] = abs(freq_cipher[letter] - freq_polish.get(letter, 0))

            min_diff_letter = min(diff_freq, key=diff_freq.get)

            shift = ord(min_diff_letter) - ord('e')

            decrypted_text = self.szyfruj(cipher_text, -shift)

            end_time = time.time()
            time_elapsed = end_time - start_time

            msg = "Znaleziono przesunięcie: " + str(
                shift) + " Oryginalny tekst: " + decrypted_text + " Złamano w " + str(time_elapsed) + " sekund"

            return msg, decrypted_text, shift
        except Exception as e:
            raise e
