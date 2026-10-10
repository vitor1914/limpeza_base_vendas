# Limpeza de Base de Vendas com Pandas e NumPy

## Sobre o projeto

Projeto de análise e preparação de dados desenvolvido em Python para simular uma demanda real de tratamento de uma base comercial.

O objetivo é transformar dados de vendas desorganizados em arquivos estruturados, identificando inconsistências e separando registros válidos daqueles que precisam de revisão.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- CSV
- Git e GitHub

## Etapas desenvolvidas

1. Importação da base de vendas.
2. Remoção de espaços extras e tratamento de campos vazios.
3. Identificação e remoção de pedidos duplicados.
4. Conversão de preços brasileiros para valores numéricos.
5. Conversão de quantidades e datas.
6. Validação de registros e identificação de inconsistências.
7. Cálculo do faturamento por venda.
8. Exportação dos resultados em arquivos CSV.

## Resultados

A base de exemplo contém 10 registros originais.

Após a remoção de uma duplicata, restaram 9 registros:

- 5 vendas válidas.
- 4 registros encaminhados para revisão.
- R$ 7.490,00 de faturamento calculado sobre as vendas válidas.

## Arquivos gerados

- `vendas_limpas.csv`: contém os registros aprovados pelas regras de validação.
- `vendas_para_revisar.csv`: contém os registros com inconsistências.
- `limpeza_base_vendas.py`: script responsável pelo processo de limpeza.
- `vendas_sujas.csv`: base original utilizada no projeto.

## Como executar

1. Instale Python 3.
2. Instale as bibliotecas:

   `python -m pip install pandas numpy`

3. Execute o script:

   `python limpeza_base_vendas.py`

## Aprendizados

Este projeto demonstra conhecimentos iniciais de manipulação de dados, tratamento de valores ausentes, remoção de duplicatas, conversão de tipos, validação de informações e exportação de dados.

## Observação

Os dados são fictícios e foram criados exclusivamente para fins de estudo e demonstração.