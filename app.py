from flask import Flask, render_template, request, redirect, url_for, flash
import poo 

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Clave secreta que no sé para qué sirve

# Variables con el usuario y la contraseña
usuario = "empleado"
contraseña = "$uper4utos#"

lista = [] # Lista de autos 

@app.route('/') # Página de inicio
def home():
    return redirect(url_for('login'))  # Redirigir al login

@app.route('/opciones') # Página de opciones
def opciones():
    return render_template('opciones.html') # Mostrar la plantilla de opciones

@app.route('/login', methods=['GET', 'POST']) # Página de login
def login():
    if request.method == 'POST': # Si se envió el formulario
        user = request.form['username'] # Obtener el usuario y la contraseña del formulario
        password = request.form['password'] 
        
        if user == usuario and password == contraseña: #Si el usuario y la contraseña son correctos
            return redirect(url_for('opciones'))  # Redirigir a la página de opciones
        else: # Si no, mensaje de error
            flash('Usuario o contraseña incorrectos', 'error')  # Mensaje de error
    
    return render_template('login.html')    # Mostrar la plantilla de login si se envió un get

@app.route('/logout') #Solo es para redirigir al al inicio
def logout():
    return redirect(url_for('login'))  # Redirigir al login

@app.route('/agregar', methods=['GET', 'POST']) # Página para agregar autos
def agregar(): 
    if request.method == 'POST':
        
        #Obtengo los datos del formulario
        id = request.form['id']
        marca = request.form['marca']
        modelo = request.form['modelo']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        imagen = request.form['imagen']
        
        # Verifico si el auto ya existe en la lista
        for auto in lista:
            if auto.id == id: #Si ya existe
                flash('El auto ya existe', 'error')  # Mostrar mensaje de error
                return redirect(url_for('agregar')) # Redirigir al formulario nuevamente para agregar otro auto si así se desea

        # Agregar el auto a la lista si no existe
        lista.append(poo.auto(id, marca, modelo, descripcion, precio, cantidad, imagen))
        flash('Auto agregado con éxito', 'success')  # Mensaje de éxito
        return redirect(url_for('agregar'))  # Redirigir al formulario nuevamente para agregar otro auto
    
    return render_template('agregar.html')

@app.route('/listar', methods=['GET', 'POST']) # Página para listar autos
def listar():
    if request.method == 'POST': # Si se envió el formulario
        auto_id = request.form['id']  # Obtener el ID del auto a eliminar
        auto_a_eliminar = None # Declaro la variable para guardar el auto a eliminar
        # Buscar el auto en la lista
        for auto in lista:
            if auto.id == auto_id:
                auto_a_eliminar = auto # Guardar el auto a eliminar
                break 
        
        if auto_a_eliminar: # Si se encontró el auto a eliminar
            lista.remove(auto_a_eliminar)  # Elimino el auto de la lista en la posición
            flash(f"El auto con ID {auto_id} ha sido eliminado.", 'success')  # Mensaje de éxito
        else:
            flash(f"No se encontró un auto con ID {auto_id}.", 'error')  # Mensaje de error
        return redirect(url_for('listar'))  # Redirigir a la lista actualizada
    return render_template('listar.html', lista=lista)  # Pasar la lista de autos a la plantilla

if __name__ == '__main__':
    app.run(debug=True)
