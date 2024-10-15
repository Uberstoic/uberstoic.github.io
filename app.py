from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

valid_key = "secret123"  # Ключ для входа

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    key = request.form['key']
    if key == valid_key:
        flash('Успешный вход!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Неверный ключ. Попробуйте снова.', 'danger')
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
