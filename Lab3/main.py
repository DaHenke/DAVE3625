# New imports
from faker import Faker
import pandas as pd
from faker.providers.credit_card import Provider as CreditCardProvider # Add credit cards to faker

# 1. Faker Create a dataframe with 100 fake persons
fake = Faker(['no_NO']) # Create a faker with norwegian names and structures

df = pd.DataFrame(columns=['Navn', 'Adresse', 'PersonNr', 'CreditCard', 'ipv4'])

for i in range(100):
    row = fake.name(), fake.address(), fake.ssn(), fake.credit_card_number(), fake.ipv4()
    df.loc[i]=row

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(df.head(10))

# 2. Anonymization
textArray = []
for i in range(10):
    row=df.loc[i]
    name = row[0]
    adress = row[1]
    ssn = row[2]
    cc = row[3]
    textArray.append(f'Hi, my name is {name}. I wonder if you deliver to {adress}. My credit card nr is {cc} and my ssn is {ssn}')

for i in range(10):
    print(textArray[i])


