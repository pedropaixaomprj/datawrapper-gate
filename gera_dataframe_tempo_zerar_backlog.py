# Criando coluna extra "TEMA_CONSIDERADO" (tema usado para previsão antes da correção)

# Aqui futuramente trocar por leitura no banco
# Solução temporária
df = pd.read_csv('C:\\Users\\pedro.paixao\\Desktop\\Pedro\\PrevisaoTempoFila\\Transformacao\\Resultados\\previsao_fila_admitidos.csv')

# Initialize an empty column for 'TEMA_CONSIDERADO'
df['TEMA_CONSIDERADO'] = None

# Iterate through the DataFrame to fill 'TEMA_CONSIDERADO'
row_index = 0

while row_index < len(df):
    
    # Get the current row's themes
    temas_pos_fila = df.loc[row_index, 'TEMAS_POS_FILA']

    # Split the themes and sort them alphabetically
    themes_positions = [theme[:-4].rstrip() for theme in temas_pos_fila.split(',')]
    sorted_themes = sorted(themes_positions)

    # Get all the times this exact temas_pos_fila was repeated
    repeated_rows = df.loc[df.TEMAS_POS_FILA == temas_pos_fila]
    index_repeated_rows = repeated_rows.index.to_list()
    
    # Fill in 'TEMA_CONSIDERADO' for each repeated row
    for i in range(len(index_repeated_rows)):
        
        index_to_be_changed = index_repeated_rows[i]
        theme_to_be_changed = sorted_themes[i]
        
        if pd.isna(df.loc[index_to_be_changed, 'TEMA_CONSIDERADO']):
            df.loc[index_to_be_changed, 'TEMA_CONSIDERADO'] = theme_to_be_changed
    
    row_index += 1

# Display the updated DataFrame
df[['SEI', 'TEMAS', 'TEMAS_POS_FILA', 'TEMA_CONSIDERADO', 'PREVISAO_PROD']] .to_csv('..\\Resultados\\previsao_fila_admitidos_com_tema_considerado.csv', index=False)

previsao_zerar_backlog = df.groupby('TEMA_CONSIDERADO')[['PREVISAO_PROD_ANTES_CORRECAO','PREVISAO_PROD']].max().reset_index()

# Salva na mesma pasta
previsao_zerar_backlog.to_csv(
    '.tempo_previsto_zerar_backlog_novoalgoritmo.csv', index=False)
