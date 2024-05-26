import time
def szyfruj(napis, klucz):
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
    return szyfrogram
def bruteForce(napis, original):
    start_time = time.time()
    for i in range(1, 26):
        decrypted_text = szyfruj(napis, -i)
        if decrypted_text.replace(' ', '').lower() == original.replace(' ', '').lower():
            end_time = time.time()
            key = i
            msg = "Znaleziono klucz: " + str(key) + " Oryginalny tekst: " + decrypted_text + " Złamano w " + str(end_time - start_time) + " sekund"
            return i, decrypted_text, msg

def frequency_analysis_cezar(cipher_text):
    start_time = time.time()
    max_time = 300
    attempts = 0

    freq_polish = {'a': 8.91, 'b': 1.47, 'c': 3.96, 'd': 3.25, 'e': 7.66, 'f': 0.3, 'g': 1.42, 'h': 1.08, 'i': 8.21, 'j': 2.28, 'k': 3.51, 'l': 2.1, 'm': 2.8, 'n': 5.52, 'o': 7.75, 'p': 3.13, 'q': 0.14, 'r': 4.69, 's': 4.32, 't': 3.98, 'u': 2.5, 'v': 0.04, 'w': 4.65, 'x': 0.02, 'y': 3.76, 'z': 5.64}

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

        decrypted_text = szyfruj(cipher_text, -shift)

        end_time = time.time()
        time_elapsed = end_time - start_time

        msg = "Znaleziono przesunięcie: " + str(shift) + " Oryginalny tekst: " + decrypted_text + " Złamano w " + str(time_elapsed) + " sekund"

        return msg, decrypted_text, shift
    except Exception as e:
        raise e
def main():
    napis = input("Podaj napis do zaszyfrowania: ")
    klucz = int(input("Podaj klucz: "))
    szyfrogram = szyfruj(napis, klucz)
    print("Zaszyfrowany napis:", szyfrogram)

    bruteForce(szyfrogram, napis)

if __name__ == "__main__":
    main()