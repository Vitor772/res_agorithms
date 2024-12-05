import matplotlib.pyplot as plt
import pandas as pd
from xlrd import colname

# Carregar os dados do arquivo Excel (ajuste o skiprows conforme necessário)
df = pd.read_excel("API_NY.GDP.MKTP.CD_DS2_en_excel_v2_43.xls", skiprows=3)

# Filtrar os dados de China e Estados Unidos
colnuna_china = df.loc[df["Country Name"] == "China", "1960":"2023"]
coluna_usa = df.loc[df["Country Name"] == "United States", "1960":"2023"]

# Certifique-se de que as séries estejam no formato correto
gdp_china = coluna_china.values.flatten()
gdp_usa = coluna_usa.values.flatten()

# Anos correspondentes para os dados
anos_china = list(range(1960, 1960 + len(gdp_china)))
anos_usa = list(range(1960, 1960 + len(gdp_usa)))

# Remover valores NaN (caso existam)
anos_china_validos = [ano for ano, gdp in zip(anos_china, gdp_china) if not pd.isna(gdp)]
gdp_china_validos = [gdp for gdp in gdp_china if not pd.isna(gdp)]

anos_usa_validos = [ano for ano, gdp in zip(anos_usa, gdp_usa) if not pd.isna(gdp)]
gdp_usa_validos = [gdp for gdp in gdp_usa if not pd.isna(gdp)]

# Plotar os dados
plt.figure(figsize=(10, 6))
plt.plot(anos_china_validos, gdp_china_validos, marker="o", label="China")
plt.plot(anos_usa_validos, gdp_usa_validos, marker="o", label="United States")
plt.title("Evolução do PIB de China e Estados Unidos (1960-2023)")
plt.xlabel("Ano")
plt.ylabel("PIB (US$)")
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar o layout para evitar cortes
plt.show()
