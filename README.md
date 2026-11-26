# Data QA Validador

Projeto de validação automatizada de migração de dados, focado em garantir a qualidade dos dados entre uma base antiga e uma base nova.

## Objetivo
Simular um cenário real de migração de dados e criar um script em Python que detecta automaticamente inconsistências.

## O que o validador verifica
- Diferença na quantidade de linhas entre as bases
- Valores nulos na base nova
- Linhas duplicadas
- Alterações indevidas em métricas críticas (ROI)

## Tecnologias
- Python
- Pandas
- Openpyxl

## Como executar
1. Instale as dependências: pip install pandas openpyxl
2. Gere a base nova simulada: python gerar_base_nova.py
3. Execute o validador: python validador.py

## Resultado
O script gera um arquivo relatorio_validacao.xlsx com 3 abas:
- Resumo: Visão geral da validação
- Valores_Nulos: Detalhamento dos dados faltantes
- Comparacao_ROI: Comparativo da métrica antes e depois

## Autor
Projeto desenvolvido para estudos de Data Quality Assurance.