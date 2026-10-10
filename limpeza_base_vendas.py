
import pandas as pd
import numpy as np

# 1. Ler a base original
df = pd.read_csv("vendas_sujas.csv", dtype=str)

print("BASE ORIGINAL")
print(df.to_string(index=False))
print("\nTotal de linhas:", len(df))

# 2. Remover espaços extras dos textos
for coluna in df.select_dtypes(include="str").columns:
    df[coluna] = df[coluna].str.strip()

# 3. Transformar campos vazios em valores ausentes
df = df.replace(r"^\s*$", np.nan, regex=True)

# 4. Remover pedidos duplicados
df = df.drop_duplicates(
    subset="pedido_id",
    keep="first"
).copy()

# 5. Converter preços brasileiros para números
df["preco_unitario"] = (
    df["preco_unitario"]
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
)

df["preco_unitario"] = pd.to_numeric(
    df["preco_unitario"],
    errors="coerce"
)

# 6. Converter quantidades para números
df["quantidade"] = pd.to_numeric(
    df["quantidade"],
    errors="coerce"
)

# 7. Converter datas
df["data"] = pd.to_datetime(
    df["data"],
    format="%d/%m/%Y",
    errors="coerce"
)

# 8. Identificar problemas nos registros
def identificar_problemas(linha):
    problemas = []

    if pd.isna(linha["cliente"]):
        problemas.append("Cliente ausente")

    if pd.isna(linha["data"]):
        problemas.append("Data inválida")

    if pd.isna(linha["quantidade"]):
        problemas.append("Quantidade ausente")
    elif linha["quantidade"] <= 0:
        problemas.append("Quantidade deve ser maior que zero")

    if pd.isna(linha["preco_unitario"]):
        problemas.append("Preço ausente ou inválido")
    elif linha["preco_unitario"] <= 0:
        problemas.append("Preço deve ser maior que zero")

    if not problemas:
        return "OK"

    return "; ".join(problemas)


df["motivo_revisao"] = df.apply(
    identificar_problemas,
    axis=1
)

# 9. Calcular o faturamento
df["faturamento"] = (
    df["quantidade"] * df["preco_unitario"]
)

# 10. Separar vendas válidas e registros pendentes
vendas_limpas = df[
    df["motivo_revisao"] == "OK"
].copy()

vendas_revisar = df[
    df["motivo_revisao"] != "OK"
].copy()

# 11. Exportar os arquivos CSV
vendas_limpas.to_csv(
    "vendas_limpas.csv",
    index=False,
    encoding="utf-8-sig"
)

vendas_revisar.to_csv(
    "vendas_para_revisar.csv",
    index=False,
    encoding="utf-8-sig"
)

# 12. Mostrar resumo da limpeza
print("\nRESUMO DA LIMPEZA")
print("Registros após remover duplicatas:", len(df))
print("Vendas válidas:", len(vendas_limpas))
print("Registros para revisar:", len(vendas_revisar))

faturamento_total = vendas_limpas["faturamento"].sum()

print(
    f"Faturamento válido: R$ {faturamento_total:.2f}"
)

# 13. Mostrar vendas válidas
print("\nVENDAS VÁLIDAS")

print(
    vendas_limpas[
        [
            "pedido_id",
            "cliente",
            "produto",
            "quantidade",
            "preco_unitario",
            "faturamento",
        ]
    ].to_string(index=False)
)

# 14. Mostrar registros que precisam de revisão
print("\nREGISTROS PARA REVISAR")

print(
    vendas_revisar[
        [
            "pedido_id",
            "cliente",
            "produto",
            "motivo_revisao",
        ]
    ].to_string(index=False)
)

print("\nArquivos exportados:")
print("- vendas_limpas.csv")
print("- vendas_para_revisar.csv")
print("\nLimpeza concluída!")
