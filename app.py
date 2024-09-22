from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'  #La clave que no sé para qué sirve

# Variables con el usuario y la contraseña que deben coincidir con lo que quiero
usuario = "empleado"
contraseña = "$uper4utos#"


@app.route('/') #La ruta raiz
def home(): #La función que se ejecuta cuando se accede a la ruta raiz
    return redirect(url_for('login')) # Redirigir a la página del login

@app.route('/login', methods=['GET', 'POST']) #La ruta login con los métodos GET y POST
def login():
    if request.method == 'POST': # Si se envió un POST
        user = request.form['username']
        password = request.form['password']
        
        # Verificar si el usuario y la contraseña coinciden con los valores predefinidos
        if user == usuario and password == contraseña:
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@app.route('/logout') #La ruta logout
def logout():
    return redirect(url_for('login')) # Redirige a la página del login

if __name__ == '__main__':
    app.run(debug=True)
