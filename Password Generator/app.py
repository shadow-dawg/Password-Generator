from flask import Flask, render_template, request
import random

app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

@app.route('/', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        nr_letters = int(request.form['letters'])
        nr_symbols = int(request.form['symbols'])
        nr_numbers = int(request.form['numbers'])
        
        password_list = []

        for char in range(nr_letters):
            password_list.append(random.choice(letters))

        for char in range(nr_numbers):
            password_list.append(random.choice(numbers))

        for char in range(nr_symbols):
            password_list.append(random.choice(symbols))

        random.shuffle(password_list)

        password = "".join(password_list)
        return render_template('index.html', password=password)

    return render_template('index.html', password="")

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/