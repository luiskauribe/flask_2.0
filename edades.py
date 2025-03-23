from flask import Flask 
app=Flask(__name__)


@app.route("/")
def HolaFlask():
    return "<h1> ¡Hola  Flask! </h1> <hr>"

## Ahora tomamos la tercera ruta y la remplazamos por el siguiente ejemplo
##2:) un programa que al capturar la edad de una persona diga que si es:
##   menor de edad (menor a 18 años)
##   adulto ( Mayor o igual a 18 años y menor a 65 años)
##   jubilado ( Mayor o igual a 65 años)

@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad< 18:
        r = "menor de edad"
    elif 18 <= edad < 65:
        r = "adulto"
    else:
        r = "jubilado"
    return f"<h1> La persona es : {r} </h1> <hr>"

    

if __name__=='__main__':
    app.run(debug=True)
