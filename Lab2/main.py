import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

url = "https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/Lab2/data/Titanic.csv"
df = pd.read_csv(url, sep=',')
print(df.isna().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Embarked"] = df["Embarked"].fillna("S")

df["HasCabin"] = ~df.Cabin.isnull()

print(df[['Cabin', 'HasCabin']])

print(df.isna().sum())

df["Title"] = df.Name.apply(lambda x: re.search(' ([A-Z][a-z]+)\.', x).group(1))

print(df.head())

print(df["Title"].value_counts())

df["Title"] = df["Title"].replace({'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mr'})

print(df["Title"].value_counts())

df["Title"] = df["Title"].replace(
    ["Rev", "Dr", "Col", "Major", "Don", "Lady", "Sir", "Capt", "Countess", "Jonkheer", "Dona"], "Unique")

print(df["Title"].value_counts())

sns.countplot(x='Title', data=df)
plt.xticks(rotation=45)
plt.show()

# 3. Convert Age and Fare into categorical data.
df['CatAge'] = pd.qcut(df["Age"], q=4, labels=False)
df['CatFare'] = pd.qcut(df["Fare"], q=4, labels=False)
print("--------------------------------------------------------------------------------------")
print(df.head())

# 4. Convert dataframe to binary data
df = df.drop(["Name", "Age", "Fare", "Sex", "Ticket", "Cabin"], axis=1)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print("--------------------------------------------------------------------------------------")
print(df.head())

df['Title_Mr'] = df.Title
df["Title_Mr"] = df["Title_Mr"].replace({'Mr': '1'})
df["Title_Mr"] = df["Title_Mr"].replace(["Mrs", "Miss", "Master", "Unique"], '0')

df['Title_Mrs'] = df.Title
df["Title_Mrs"] = df["Title_Mrs"].replace({'Mrs': '1'})
df["Title_Mrs"] = df["Title_Mrs"].replace(["Mr", "Miss", "Master", "Unique"], '0')

df['Title_Miss'] = df.Title
df["Title_Miss"] = df["Title_Miss"].replace({'Miss': '1'})
df["Title_Miss"] = df["Title_Miss"].replace(["Mr", "Mrs", "Master", "Unique"], '0')

df['Title_Master'] = df.Title
df["Title_Master"] = df["Title_Master"].replace({'Master': '1'})
df["Title_Master"] = df["Title_Master"].replace(["Mr", "Mrs", "Miss", "Unique"], '0')

df['Title_Unique'] = df.Title
df["Title_Unique"] = df["Title_Unique"].replace({'Unique': '1'})
df["Title_Unique"] = df["Title_Unique"].replace(["Mrs", "Miss", "Master", "Mr"], '0')

df = df.drop(["Title"], axis=1)
print("--------------------------------------------------------------------------------------")
print(df["Embarked"].value_counts())

df['Embarked_Q'] = df.Embarked
df["Embarked_Q"] = df["Embarked_Q"].replace({'Q': '1', 'S': '0', 'C': '0'})

df['Embarked_S'] = df.Embarked
df["Embarked_S"] = df["Embarked_S"].replace({'Q': '0', 'S': '1', 'C': '0'})

df['Embarked_C'] = df.Embarked
df["Embarked_C"] = df["Embarked_C"].replace({'Q': '0', 'S': '0', 'C': '1'})

df = df.drop(["Embarked"], axis=1)

print("--------------------------------------------------------------------------------------")
print(df.head())

df.to_csv("data.csv", sep=',', index=False)
