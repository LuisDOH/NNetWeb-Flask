from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/respuesta',methods=["GET","POST"])
def respuesta():
    if request.method == "GET":
        return inicio()
    elif request.method == "POST":
        nombre  = request.form.get("Nombre")
        nombre = nombre.lower()
        usuario = request.form.get("Usuario")
        clave   = request.form.get("Clave")
        print(nombre)

        if nombre == "luis":
            return f'''El nombre: {nombre} ya esta registrado. </br>
                    Por favor verifique la informacion.
                    </br>
                    <a href = "/registro"> Volver a formulario </a>
                    '''
        else:
            return f'''Se han obtenido los datos para {nombre}:
                        </br>
                        Usuario: {usuario}
                        </br>
                        Clave: {clave}

                        <a href = "/registro"> Volver a formulario </a>
                    '''



if __name__ == '__main__':
    app.run(debug = True, port = 3000)
