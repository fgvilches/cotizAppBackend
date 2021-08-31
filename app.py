from flask import Flask, request, render_template 
from gencoti import genCotizacion, uploadOverleaf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    uf_dia = request.form['uf_dia']
    uf_dia = int(uf_dia)
    cliente_name = request.form['cliente_name']
    cliente_name = cliente_name.upper()
    cliente_dir = request.form['cliente_dir']
    cliente_dir = cliente_dir.upper()
    cliente_telefono = request.form['cliente_telefono']
    tipo_prod = request.form['tipo_prod']

    sector = request.form['sector']

    capacidad = request.form['capacidad']

    valor_n_inmediata = request.form['valor_n_inmediata']


    valor_compr_ant = request.form['valor_compr_ant']


    dscto_contado  = request.form['dscto_contado']


    dscto_otro_num = request.form['dscto_otro_num']


    dscto_otro_razon = request.form['dscto_otro_razon']
    dscto_otro_razon = dscto_otro_razon.upper()

    total = request.form['total']

    pie = request.form['pie']

    restriccion =  request.form['restriccion']

    uf_por_dia =  request.form['uf_por_dia']

    mantencion_anual =  request.form['mantencion_anual']

    mantencion_perpetua =  request.form['mantencion_anual']

    arancel_sep =  request.form['arancel_sep']

    n_cuotas = request.form['n_cuotas']

    valor_cuota = request.form['valor_cuota']
    genCotizacion(uf_dia, cliente_name, cliente_dir,cliente_telefono,tipo_prod,sector,capacidad,valor_n_inmediata,valor_compr_ant, dscto_contado, dscto_otro_num, dscto_otro_razon,total,pie, restriccion, uf_por_dia, mantencion_anual, mantencion_perpetua, arancel_sep, n_cuotas,valor_cuota)
    uploadOverleaf()
    return "Archivo generado y abierto en una nueva ventana."


if __name__ == "__main__":
    app.run()