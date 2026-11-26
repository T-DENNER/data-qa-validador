import pandas as pd

print("Iniciando validação...\n")

# Carrega as duas bases
antiga = pd.read_csv('data/base_antiga.csv')
nova = pd.read_csv('data/base_nova.csv')

# 1. Compara quantidade de linhas
print(f"Base antiga: {len(antiga)} linhas")
print(f"Base nova: {len(nova)} linhas")
if len(antiga) != len(nova):
    print("ALERTA: Quantidade de linhas diferente!\n")

# 2. Verifica nulos na base nova
nulos = nova.isnull().sum()
print("Valores nulos na base nova:")
print(nulos[nulos > 0])
print()

# 3. Verifica duplicados
duplicados = nova.duplicated().sum()
print(f"Linhas duplicadas na base nova: {duplicados}\n")

# 4. Compara o ROI (pega as primeiras 5 linhas que a gente alterou)
print("Comparando ROI das 5 primeiras campanhas:")
comparacao = pd.DataFrame({
    'campanha': antiga['nome'].head(5),
    'roi_antigo': antiga['roi'].head(5),
    'roi_novo': nova['roi'].head(5)
})
print(comparacao)

print("\nValidação finalizada!")


with pd.ExcelWriter('relatorio_validacao.xlsx') as writer:
    # Aba 1: Resumo
    resumo = pd.DataFrame({
        'Metrica': ['Linhas base antiga', 'Linhas base nova', 'Duplicados na nova'],
        'Valor': [len(antiga), len(nova), duplicados]
    })
    resumo.to_excel(writer, sheet_name='Resumo', index=False)
    
    # Aba 2: Nulos
    nulos.to_excel(writer, sheet_name='Valores_Nulos')
    
    # Aba 3: Comparação ROI
    comparacao.to_excel(writer, sheet_name='Comparacao_ROI', index=False)

print("\nRelatório 'relatorio_validacao.xlsx' gerado com sucesso!")