from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  
login_manager = LoginManager(app)


class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password


users = [
    User(1, 'usuario1', 'contrasena1'),
    User(2, 'usuario2', 'contrasena2')
]

# Configuración de Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users if user.id == int(user_id)), None)

# Rutas de la aplicación
@app.route('/')
def home():
    return 'Página de inicio'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((user for user in users if user.username == username and user.password == password), None)

        if user:
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Bienvenido, {current_user.username}'

if __name__ == '__main__':
    app.run(debug=True)
