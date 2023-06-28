import pandas as pd
import formatacao
import os

INPUT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')
CAMINHO_INPUT = os.path.join(INPUT_PATH, 'input.xlsx')

df_output = pd.read_excel(CAMINHO_INPUT)

df_output['valor_juros'] = formatacao.preencher_valores_nulos(df_output['valor_juros'])
df_output['valor_face'] = df_output['valor_principal'] + df_output['valor_juros']

for index, row in df_output.iterrows():
    df_output.loc[index,'advogado_documento'] = formatacao.formatar_cpf_cnpj(row['advogado_documento'])
    df_output.loc[index,'documento_credor'] = formatacao.formatar_cpf_cnpj(row['documento_credor'])
    df_output.loc[index,'numero_processo'] = formatacao.formatar_precatorio_processo(row['numero_processo'])
    df_output.loc[index,'numero_precatorio'] = formatacao.formatar_precatorio_processo(row['numero_precatorio'])
    df_output.loc[index,'url_arquivo_oficio'] = row['numero_precatorio'] + '.pdf'
    df_output.loc[index,'data_liquidacao'] = formatacao.formatar_data(row['data_liquidacao'])
    df_output.loc[index,'data_autuacao'] = formatacao.formatar_data(row['data_autuacao'])
    df_output.loc[index,'data_transito_conhecimento'] = formatacao.formatar_data(row['data_transito_conhecimento'])
    df_output.loc[index,'data_transito_execucao'] = formatacao.formatar_data(row['data_transito_execucao'])
    row['advogado_nome'] = str(row['advogado_nome']).replace('- ASSOCIADOS', 'ASSOCIADOS')
    if row['advogado_nome'] is not None and str(row['advogado_nome']) != 'nan':
        row['advogado_nome'] = row['advogado_nome'].split('-')
        df_output.loc[index,'advogado_nome'] = row['advogado_nome'][0]
        df_output.loc[index,'advogado_oab'] = row['advogado_nome'][1] 

for excluir_termos in formatacao.LISTA_TERMOS_EXCLUIR:
    df_output['nome_credor'] = df_output['nome_credor'].replace(excluir_termos,'', regex=True)

df_output.to_excel(f'{OUTPUT_PATH}\\output_tratado.xlsx', engine='xlsxwriter', index=False)
print('Output_tratado gerado com sucesso!')