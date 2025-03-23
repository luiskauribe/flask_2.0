from flask import Flask 
app=Flask(__name__)
from dotenv import load_dotenv
load_dotenv()

@app.route("/")
def HolaFlask():
    return "<h1> ¡Hola Flask! </h1> <hr>"

## Ahora tomamos la segunda ruta y la reemplazamos por el siguiente ejemplo
## 1.) Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de
## 30%, 30% y 40% respectivamente."/notas"

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def promedio(nota1=0,nota2=0,nota3=0):
    resultado = (nota1 * 30) / 100 + (nota2 * 30) / 100 + (nota3 * 40) / 100


    return f"El resultado de notas es: {resultado}"

if __name__=='__main__':
    app.run(debug=True)
