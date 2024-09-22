from flask import Flask, render_template, request, redirect, url_for, flash
import poo

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # La clave para manejar los mensajes flash

# Variables con el usuario y la contraseña que deben coincidir con lo que quiero
usuario = "empleado"
contraseña = "$uper4utos#"

# Lista de autos
lista = []

@app.route('/')  # Ruta raíz
def home():
    return redirect(url_for('login'))  # Redirigir al login

@app.route('/opciones')  # Ruta de opciones
def opciones():
    return render_template('opciones.html')

@app.route('/login', methods=['GET', 'POST'])  # Ruta login
def login():
    if request.method == 'POST':  # Si se envía un POST
        user = request.form['username']
        password = request.form['password']
        
        # Verificar si el usuario y la contraseña coinciden con los valores predefinidos
        if user == usuario and password == contraseña:
            return redirect(url_for('opciones'))  # Redirigir a opciones
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@app.route('/logout')  # Ruta logout
def logout():
    return redirect(url_for('login'))

@app.route('/agregar', methods=['GET', 'POST'])  # Ruta agregar
def agregar():
    if request.method == 'POST':
        id = request.form['id']
        marca = request.form['marca']
        modelo = request.form['modelo']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        imagen = request.form['imagen']
        
        # Agregar el auto a la lista
        lista.append(poo.auto(id, marca, modelo, descripcion, precio, cantidad, imagen))
        return redirect(url_for('opciones'))
    
    return render_template('agregar.html')

@app.route('/listar')  # Ruta listar
def listar():
    return render_template('listar.html', lista=lista)  # Pasar la lista a la plantilla listar.html

if __name__ == '__main__':
    app.run(debug=True)
