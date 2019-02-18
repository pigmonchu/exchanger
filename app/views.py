from app import app
from flask import render_template, request, redirect, url_for
import psycopg2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nuevacompra', methods=['GET', 'POST'])
def nuevacompra():
    if request.method == 'GET':
        return render_template('nuevacompra.html')
    else:
        dbParams = app.config['DATABASE']
        conn = psycopg2.connect(host=dbParams['host'], port=dbParams['port'], dbname=dbParams['dbname'], user=dbParams['dbuser'], password=dbParams['password'])
        cur = conn.cursor()
        query = """INSERT INTO movimientos (fecha_hora, descripcion, moneda_comprada, cantidad_comprada, moneda_pagada, cantidad_pagada)
                               VALUES ('{} {}:00.000000', '{}', '{}', {}, '{}', {});"""
        f = request.form
        query = query.format(f['fecha'], f['hora'], f['descripcion'], f['monedaComprada'], f['cantidadComprada'], f['monedaPagada'], f['cantidadPagada'])

        cur.execute(query)

        conn.commit()

        conn.close()

        return redirect(url_for('index'))
