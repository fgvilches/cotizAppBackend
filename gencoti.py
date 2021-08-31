import os
import platform
import subprocess
import time
import webbrowser
from github import Github
from six.moves import urllib

# Cotizacion recibe uf_dia, cliente_name, cliente_dir, cliente_telefono,tipo_prod 0-3,sector,capacidad 0-2,valor_n_imediata UF, valor_compra_ant,
# dcto_contado %, dcto_otro_num, dscto_otro_razon,total, pie, restriccion, mantencion_anual, mantencion_perpetua, arancel_sep, n_cuotas, valor_cuota

def genCotizacion(uf_dia, cliente_name, cliente_dir,cliente_telefono,tipo_prod,sector,capacidad,valor_n_inmediata,valor_compr_ant, dscto_contado, dscto_otro_num, dscto_otro_razon,total,pie, restriccion, uf_por_dia, mantencion_anual, mantencion_perpetua, arancel_sep, n_cuotas,valor_cuota):
    coti = open('cotis.tex', 'r')
    lineas = coti.readlines()
    timex = str(time.strftime("%d-%m-%Y", time.gmtime()))
    line = r'\textbf{NOMBRE: } ' + str(cliente_name) + r' & \color{white}---------------------------------- & \textbf{VALOR UF: } ' + str(uf_dia) + r'\\' + ' \n'
    lineas[48] = line
    line = r'\textbf{DIRECCION: }' + str(cliente_dir) + r' & \color{white}---------------------------------- &  \textbf{FECHA: }'+ timex +r' \\' + ' \n'
    lineas[49] = line
    line = r'\textbf{TELEFONO: }' + str(cliente_telefono) + r'& \color{white}-------- &  \\' + ' \n'
    lineas[50] = line

    if tipo_prod == 0:
        line = r'\textbf{X} &  &  & \\' + ' \n'
        lineas[73] = line
    elif tipo_prod == 1:
        line = r' & \textbf{X} &  & \\' + ' \n'
        lineas[73] = line
    elif tipo_prod == 2:
        line = r' &  & \textbf{X} & \\' + ' \n'
        lineas[73] = line
    else:
        line = r' &  &  & \textbf{X} \\' + ' \n'
        lineas[73] = line
        
    line = r'    \textbf{' + str(sector) + r'}' + ' \n'
    lineas[81] = line

    if capacidad == 0:
        line = r'\textbf{X} & & \\' + ' \n'
        lineas[90] = line
    elif capacidad == 1:
        line = r' & \textbf{X} & \\' + ' \n'
        lineas[90] = line
    else:
        line = r' & & \textbf{X} \\' + ' \n'
        lineas[90] = line

    line = r'VALOR NECESIDAD INMEDIATA &  & \textbf{UF: } ' + str(valor_n_inmediata) + r' & \textbf{\$: }'+ str(valor_n_inmediata*uf_dia) + r' \\' + ' \n'
    lineas[113] = line
    line = r'\textbf{DESCUENTO COMPRA ANTICIPADA} & & \textbf{UF: }' + str(valor_n_inmediata-valor_compr_ant) + r'& \textbf{\$: }' + str(int(valor_n_inmediata-valor_compr_ant)*uf_dia) + r' \\' + ' \n'
    lineas[115] = line
    line = r'VALOR COMPRA ANTICIPADA &  & \textbf{UF: }' + str(valor_compr_ant) + r'& \textbf{\$: }' + str(valor_compr_ant*uf_dia) + r' \\ ' + ' \n'
    lineas[117] = line
    line = r'\% DESCUENTO PAGO CONTADO &  & \textbf{UF: }'+ str(dscto_contado) + r'& \textbf{\$: }' + str(dscto_contado*uf_dia)  + r' \\ ' +  ' \n'
    lineas[119] = line
    line = r'\% DESCUENTO (OTRO ESPECIFICAR) &' +  str(dscto_otro_razon) + r'& \textbf{UF: }' + str(dscto_otro_num)+ r'& \textbf{\$: }' + str(dscto_otro_num*uf_dia) + r' \\ '  +  ' \n'
    lineas[121] = line
    line = r'TOTAL &  & \textbf{UF: }' + str(total) + r'& \textbf{\$: }' + str(total*uf_dia) + r' \\ ' + ' \n'
    lineas[126] = line
    line = r'\textbf{PIE EFECTIVO / CHEQUE} &  & \textbf{UF: }' + str(pie) + r'& \textbf{\$: }' + str(pie*uf_dia) + r' \\  ' + ' \n'
    lineas[127] = line 
    line = r'SALDO &  & \textbf{UF: }' + str(total - pie) + r' & \textbf{\$: } ' + str(int(total - pie)*uf_dia) + r' \\ ' + ' \n'
    lineas[128] = line
    line = r'DE USO TRADICIONAL  & & ' + str(restriccion) + r' MESES UF ' + str(uf_por_dia) + r' POR DIA \\' + ' \n'
    lineas[146] = line
    line = r'MANTENCION ANUAL &  & ' r'\textbf{UF: }' + str(mantencion_anual) + r'& \textbf{\$: }' + str(mantencion_anual*uf_dia) + r' \\ ' + ' \n'
    lineas[148] = line
    line = r'MANTENCION PERPETUA &  & \textbf{UF: }' + str(mantencion_perpetua) + r' & \textbf{\$: }' + str(mantencion_perpetua*uf_dia) + r' \\ ' + ' \n'
    lineas[150] = line
    line = r'ARANCEL DE SEPULTACION &  & \textbf{UF: } ' + str(arancel_sep) + r'& \textbf{\$: } ' + str(arancel_sep*uf_dia) + r' \\ ' + ' \n'
    lineas[152] = line
    line = r' & \textbf{N° CUOTAS: }' + str(n_cuotas) +  r'& &\textbf{UF: } ' + str(valor_cuota) + r' & \textbf{\$: } ' + str(valor_cuota*uf_dia) + r' \\ ' + ' \n'
    lineas[171] = line

    line = r'' + ' \n'
    time.sleep(2)
    coti = open('cotis.tex', 'w')
    return coti.writelines(lineas)
    #genCotizacion(123,"Felipe Gonzalez","Polonia 2077",991071926,0,203,2,335,235,0,0,'n/a',335,35,2,3,0,0,7,84,2.25)

def uploadOverleaf():
    g = Github("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")

    with open('cotis.tex', 'r') as file:
        content = file.read()

    repo = g.get_user().get_repo('cotis')
    all_files = []

    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

    # Upload to github
    git_prefix = ''
    git_file = git_prefix + 'cotis.tex'
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="master")
        print(git_file + ' CREATED')

    contents = repo.get_contents("cotis.tex")
    file_content = repo.get_contents(urllib.parse.quote(contents.path))
    uri = file_content.download_url

    time.sleep(2)
    final_url = 'https://www.overleaf.com/docs?snip_uri[]=' + str(uri) + '&snip_uri[]=https://github.com/bonatrash/cotis/raw/master/logo.png'
    return webbrowser.open_new(final_url)