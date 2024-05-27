import ast
from flask import Flask, render_template, request, session, send_file

from algorithms.algorithm_factory import AlgorithmFactory
from file_reading_strategy import FileHandler, ReadAsBytesStrategy, ReadAsStringStrategy

app = Flask(__name__)
app.secret_key = 'very_secret_key_tajne_haslo'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/encrypt')
def index():  # put application's code here
    return render_template('encrypt.html')


@app.route('/submit', methods=['POST'])
def submit():
    selected_algorithm = request.form.get('select')
    file = request.files.get('file')
    file_content = file.read()
    if selected_algorithm != 'Szyfr cezara':
        file_content = ast.literal_eval(file_content.decode('utf-8'))

    key = request.files.get('key')
    key = key.read() if key else None

    action = request.form.get('action')
    print(action)
    if action == 'Odszyfruj':
        decrypt_file(selected_algorithm, file_content, key)
        return render_template('decryption_success.html')

    elif action == 'użyj brutalnej siły':
        return render_template('brute_force.html', result=brute_force(selected_algorithm, file_content))

    elif action == 'użyj ataku statystycznego':
        return "Frequency attack not implemented yet"

    return "invalid action"


@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.html')


@app.route('/encrypt_succesfull', methods=['POST'])
def encrypt():
    selected_algorithm = request.form.get('select')
    file = request.files.get('file')

    # strategy pattern
    strategy_mapping = {
        "AES": ReadAsBytesStrategy(),
        "Szyfr cezara": ReadAsStringStrategy(),
        "DES3": ReadAsBytesStrategy(),
    }

    strategy = strategy_mapping[selected_algorithm]

    file_handler = FileHandler(strategy)
    file_content = file_handler.handle_file(file)

    session['file_content'] = file_content

    # Factory pattern
    algorithm = AlgorithmFactory.create_algorithm(selected_algorithm)

    encrypted_text = algorithm.encrypt(text=file_content)

    with open('encrypted_text.txt', 'w') as f:
        f.write(str(encrypted_text[0]))
    if selected_algorithm == 'Szyfr cezara':
        with open('key.txt', 'wb') as f:
            f.write((encrypted_text[1]).to_bytes((encrypted_text[1].bit_length() + 7) // 8, 'big'))

    else:
        print(encrypted_text[1], type(encrypted_text[1]))
        with open('key.txt', 'wb') as f:
            f.write(encrypted_text[1])
        pass

    session['encrypted_text'] = 'encrypted_text.txt'
    session['key'] = 'key.txt'

    return render_template('encrption_success.html')


@app.route('/decrypt', methods=['POST'])
def decrypt_file(selected_algorithm, file_content, key):

    # Factory pattern
    algorithm = AlgorithmFactory.create_algorithm(selected_algorithm)
    decrypted_text = algorithm.decrypt(file_content, key)

    filename = 'decrypted_text.txt'
    with open(filename, 'w') as f:
        if selected_algorithm == 'Szyfr cezara':
            f.write(decrypted_text[0])
        else:
            f.write(decrypted_text)

    session['decrypted_text'] = filename

    return render_template('decryption_success.html')


@app.route('/bruteForce')
def brute_force(selected_algorithm, file_content):

    # Factory pattern
    algorithm = AlgorithmFactory.create_algorithm(selected_algorithm)
    result = algorithm.brute_force(file_content.decode('utf-8'), original=session.get('file_content'))

    return result

@app.route('/download-<file_type>')
def download(file_type):
    if file_type not in ['encrypted_text', 'key', 'decrypted_text']:
        return "Invalid file type"
    filename = session.get(file_type)
    if filename is None:
        return "No file to download"

    return send_file(filename, as_attachment=True)

@app.route('/crack')
def crack():
    return render_template('crack.html')


if __name__ == '__main__':
    app.run(port=6900)
