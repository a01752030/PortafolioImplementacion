import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols




# Datos de rendimiento
data = {
    "Género": ["Chico"]*18 + ["Chica"]*18,
    "Método": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
               1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
    "Rendimiento": [10, 7, 9, 9, 9, 10, 5, 7, 6, 6, 8, 4, 2, 6, 3, 5, 5, 3,
                    9, 7, 8, 8, 10, 6, 8, 3, 5, 6, 2, 6, 1, 4, 3]
}

df = pd.DataFrame(data)

# Modelo ANOVA
modelo = ols('Rendimiento ~ C(Género) + C(Método) + C(Género):C(Método)', data=df).fit()
anova_table = sm.stats.anova_lm(modelo, typ=2)

print(anova_table)