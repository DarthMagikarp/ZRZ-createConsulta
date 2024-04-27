# chat conversation
import json
import pymysql
import requests
import http.client
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")
    print("REQUEST: "+str(request.json))

    try:
        cursor = connection.cursor()

        id_alumno = str(request.json['id_alumno'])
        motivo_consulta = str(request.json['motivo_consulta'])
        descripcion_sintomatologia = str(request.json['descripcion_sintomatologia'])
        atenciones_previas = str(request.json['atenciones_previas'])
        antecedentes_familiares = str(request.json['antecedentes_familiares'])
        expectativas = str(request.json['expectativas'])
        impresion_diagnostica = str(request.json['impresion_diagnostica'])
        acuerdos = str(request.json['acuerdos'])
        observaciones = str(request.json['observaciones'])
        fecha = str(request.json['fecha'])
        numero_sesion = str(request.json['numero_sesion'])
        
        sql_insertar = 'INSERT INTO '+DB_DDBB+'.consulta'+'''
                        (id_alumno,motivo_consulta,descripcion_sintomatologia,atenciones_previas,antecedentes_familiares,expectativas,impresion_diagnostica,acuerdos,observaciones,fecha,numero_sesion)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        '''
        print('INSERT:'+sql_insertar)
        print(id_alumno,motivo_consulta,descripcion_sintomatologia,atenciones_previas,antecedentes_familiares,expectativas,impresion_diagnostica,acuerdos,observaciones,fecha,numero_sesion)
        cursor.execute(sql_insertar,(profesional_id, alumno_id, fecha, hora, estado, modalidad, campus, notas, motivo, como, derivado_desde, tratamiento, diagnostico_previo))
        connection.commit()

        retorno = {
                "estado":True,
                "detalle":"success!!"
            }

    except Exception as e:
        print('Error: '+ str(e))
        retorno = {
            "estado":False,
            "detalle":"fail!!"
        }
    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')