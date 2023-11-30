# Importando las librerías necesarias
from flask import Flask, render_template, request

# Creando la aplicación Flask
app = Flask(__name__)

# Definiendo la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Definiendo la ruta para el ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            edad = int(request.form['edad'])
            tarros = int(request.form['tarros'])
            
            total_sin_descuento = tarros * 9000
            descuento = 0.15 if 18 <= edad <= 30 else 0.25 if edad > 30 else 0
            total_con_descuento = total_sin_descuento * (1 - descuento)
            
            resultado = {
                'nombre': nombre,
                'total_sin_descuento': total_sin_descuento,
                'descuento': descuento,
                'total_con_descuento': total_con_descuento
            }
        except (KeyError, ValueError):
            error = "Error: Asegúrate de completar todos los campos correctamente."

    return render_template('ejercicio1.html', resultado=resultado, error=error)

# Definiendo la ruta para el ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        usuarios = {'juan': 'admin', 'pepe': 'user'}
        
        if usuario in usuarios and usuarios[usuario] == password:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
    
    return render_template('ejercicio2.html', mensaje=mensaje)

# Ejecutando la aplicación
if __name__ == '__main__':
    app.run(debug=True)
