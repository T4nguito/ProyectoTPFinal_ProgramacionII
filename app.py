from flask import Flask, jsonify, Response, request
import json 
from http import HTTPStatus

app= Flask(__name__)

with open ("peliculas.json", encoding="utf-8") as archivo_json:
    datos = json.load(archivo_json)

with open ("users.json") as archivos_json:
   users = json.load(archivo_json)
    
@app.route("/")
def home():
    return "/"

@app.route("/usuarios", methods = ["GET"])
def devolver_usuario():
    return jsonify(users)

@app.route("/peliculas", methods = ["GET"])
def devolver_peliculas():
    return jsonify(datos)

@app.route("/usuarios/<id>", methods = ["GET"])
def devolver_usuario(id):
    lista_encontrados=[]    
    id_int = int(id)
    for i in users:
        for usuario in users[i]:
            if usuario["id"] == id_int:
                lista_encontrados.append(usuario)
    print(lista_encontrados)
    return Response("{]", status= HTTPStatus.NOT_FOUND)

@app.route("/agregar/pelicula", method = ["POST"])
def agregar_pelicula():
    #Recibir datos del cliente
    datos_cliente = request.get_json()
    #id?
    if (("titulo" in datos_cliente) and ("anio" in datos_cliente) and ("director" in datos_cliente) and ("genero" in datos_cliente) and ("actores" in datos_cliente) and ("sipnosis" in datos_cliente) and ("imagen" in datos_cliente)):
        datos[0]["peliculas"].append({
            "titulo" : datos_cliente["titulo"],
            "anio" : datos_cliente["anio"],
            "director" : datos_cliente["director"],
            "genero" : datos_cliente["genero"],
            "actores": datos_cliente["actores"],
            "sipnosis" : datos_cliente["sipnosis"],
            "imagen" : datos_cliente["imagen"]
            })
        return Response(datos_cliente["titulo"], status= HTTPStatus.OK)
    else:
        return Response("{}", status= HTTPStatus.BAD_REQUEST)

@app.route("/actualizar/pelicula", methods = ["PUT"])
def actualizar_datos_pelicula():
    datos_cliente = request.get_json()
    if (("titulo" in datos_cliente) and ("anio" in datos_cliente) and ("genero" in datos_cliente)):
        for pelicula in datos[0]["peliculas"]:
            if ((pelicula["titulo"] == datos_cliente["titulo"]) and (pelicula["anio"] == datos_cliente["anio"]) and (pelicula["genero"] in datos_cliente["genero"])):
                print("ok")
        return Response(status= HTTPStatus.OK)
    else:
        return Response("{}", status= HTTPStatus.BAD_REQUEST)


