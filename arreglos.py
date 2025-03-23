from flask import Flask 
app=Flask(__name__)
import numpy as np

@app.route("/")
def HolaFlask():
    return "<h1> ¡Hola  Flask! </h1> <hr>"
##creamos otra ruta realizamos el siguiente ejemplo
##3:)  programa que cre arreglos con valores aleatorios
## importamos la libreria numpy si no existe la instalamos com:


@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")

def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglos=np.random.randint(valores,size=columnas)
    else:
        arreglos=np.random.randint(valores,size=(filas,columnas))
        
    return f"<h1>el arreglo aleatorio es : {arreglos}</h1> <hr>"    

if __name__=='__main__':
    app.run(debug=True)
