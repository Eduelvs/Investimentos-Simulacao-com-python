from decimal import Decimal, getcontext
import pandas as pd

# Precisão de casas decimais
getcontext().prec = 12

# Função para calcular valor futuro com aportes mensais e capital acumulado anterior
def calcular_valor_futuro(aporte_mensal, meses, juros_mensal, valor_presente=0):
    i = Decimal(juros_mensal)
    n = Decimal(meses)
    pmt = Decimal(aporte_mensal)
    vp = Decimal(valor_presente)

    if i == 0:
        fv = pmt * n + vp
    else:
        fv = pmt * ((1 + i)**n - 1) / i + vp * (1 + i)**n

    return round(fv, 2)

# Taxa de juros mensal
juros_mensal = Decimal("0.008")  # 0,8% a.m

#"Financiamento":         [3000, 3000, 3000, 0],
# Dados: categoria → aportes mensais por etapa
planos = {

    "Meta":                  [3000, 4200, 6000, 10000],
    "Fundo de Emergência":  [1000, 1600, 3000, 3000],
    "Filho":                 [0, 0, 1000, 1000],
}

# Períodos em meses para cada etapa
periodos = [36, 48, 72, 132]  # 1–3 anos, 4–7, 8–12, 13–23

# Cálculo acumulado por etapa
resultados = {categoria: [] for categoria in planos}
for categoria, aportes in planos.items():
    acumulado = Decimal("0")
    for i, aporte in enumerate(aportes):
        meses = periodos[i]
        acumulado = calcular_valor_futuro(aporte, meses, juros_mensal, valor_presente=acumulado)
        resultados[categoria].append(acumulado)

# Criar DataFrame para exibir
df_resultados = pd.DataFrame(resultados, index=["1–3 anos", "4–7 anos", "8–12 anos", "13–23 anos"]).T
df_resultados["Valor Final"] = df_resultados["13–23 anos"]
print(df_resultados)
