import pandas as pd
dados = {
    "Nome":["João","Marta","Ary","Mathues","Michelle"],
    "Idade":[51,37,23,24,33]
}
df = pd.DataFrame(data=dados)
print(df)