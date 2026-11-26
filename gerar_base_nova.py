import pandas as pd
import numpy as np

# Carrega sua base real
df = pd.read_csv('data/base_antiga.csv')

# Cria uma cópia pra ser a base nova
df_nova = df.copy()

# INTRODUZ ERROS DE PROPÓSITO (pra testar seu validador)

# 1. Muda o ROI de 5 campanhas
df_nova.loc[0:4, 'roi'] = df_nova.loc[0:4, 'roi'] * 1.5

# 2. Deixa 3 custos como nulo
df_nova.loc[10:12, 'custo'] = np.nan

# 3. Duplica 2 linhas
df_nova = pd.concat([df_nova, df_nova.iloc[20:22]], ignore_index=True)

# 4. Remove 3 campanhas (simula que sumiram)
df_nova = df_nova.drop(df_nova.index[30:33]).reset_index(drop=True)

# Salva a base nova
df_nova.to_csv('data/base_nova.csv', index=False)
print("Base nova criada com sucesso!")
print(f"Base antiga: {len(df)} linhas")
print(f"Base nova: {len(df_nova)} linhas")