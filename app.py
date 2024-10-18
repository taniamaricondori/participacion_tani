from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__, static_folder='static')
app.secret_key = 'tu_secreto_aqui'  # Cambia esta clave a una más segura en un entorno de producción

# Usuarios de ejemplo (en un entorno real, usarías una base de datos)
users = {
    "admin": "password123",
    "user1": "mypassword",
    "Tania": "tania12345"
}

@app.route('/')
def home():
    # Redirigir al usuario a la página de inicio de sesión si no está autenticado
    if 'username' in session:
        return redirect(url_for('bienvenida'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificación de credenciales
        if username in users and users[username] == password:
            session['username'] = username
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('bienvenida'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')

@app.route('/bienvenida')
def bienvenida():
    # Verificar si el usuario está autenticado
    if 'username' in session:
        username = session['username']
        return render_template('bienvenida.html', username=username)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Eliminar la sesión del usuario
    session.pop('username', None)
    flash('Cierre de sesión exitoso', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
