from datetime import datetime
from pandas import Series

LISTA_TERMOS_EXCLUIR = ['ESPÓLIO DE', 'E OUTROS', 'E OUTRAS', 'E OUTROS(AS)']

def formatar_precatorio_processo(processo_precatorio):
    processo_precatorio = str(processo_precatorio)
    if len(processo_precatorio) != 28:
        processo_precatorio = '{}-{}.{}.{}.{}.{}'.format(processo_precatorio[:7], processo_precatorio[7:9], processo_precatorio[9:13], processo_precatorio[13:14], processo_precatorio[14:16], processo_precatorio[16:])
    return processo_precatorio

def preencher_valores_nulos(coluna_dataframe:Series, valor:int=0):
    coluna_dataframe = coluna_dataframe.fillna(valor)
    return coluna_dataframe
    
def formatar_data(data, formato_data_origem= '%Y-%m-%d' , formato_data_destino = '%d/%m/%Y'):
    if data is not None and str(data) != 'nan':
        datetime_origem = datetime.strptime(str(data), formato_data_origem)
        data_formatada = datetime_origem.strftime(formato_data_destino)
        return data_formatada

def formatar_cpf_cnpj(cpf_cnpj):
    cpf_cnpj_formatado = None
    cpf_cnpj = str(cpf_cnpj)
    if len(cpf_cnpj) < 11:
        cpf_cnpj = cpf_cnpj.zfill(11)
    if len(cpf_cnpj) > 11 and len(cpf_cnpj) < 14:
        cpf_cnpj = cpf_cnpj.zfill(14)
    if len(cpf_cnpj) == 11:
        cpf_cnpj_formatado = '{}.{}.{}-{}'.format(cpf_cnpj[:3], cpf_cnpj[3:6], cpf_cnpj[6:9], cpf_cnpj[9:])
    if len(cpf_cnpj) == 14:
        cpf_cnpj_formatado = "{}.{}.{}/{}-{}".format(cpf_cnpj[0:2], cpf_cnpj[2:5], cpf_cnpj[5:8], cpf_cnpj[8:12], cpf_cnpj[12:14] )
    if cpf_cnpj_formatado == None:
        print(cpf_cnpj)
    return cpf_cnpj_formatado



