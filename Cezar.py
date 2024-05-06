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
    start_time = time.time()  # Zapisz czas startu
    for i in range(1, 26):
        decrypted_text = szyfruj(napis, -i)
        if decrypted_text.replace(' ', '').lower() == original.replace(' ', '').lower():  # Dodano .lower()
            end_time = time.time()  # Zapisz czas zakończenia
            print("Klucz:", i, "Tekst:", decrypted_text)
            print(f"Złamano w {end_time - start_time} sekund")
            return
def main():
    napis = input("Podaj napis do zaszyfrowania: ")
    klucz = int(input("Podaj klucz: "))
    szyfrogram = szyfruj(napis, klucz)
    print("Zaszyfrowany napis:", szyfrogram)

    bruteForce(szyfrogram, napis)

if __name__ == "__main__":
    main()