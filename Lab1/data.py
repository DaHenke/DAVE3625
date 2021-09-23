import pandas
import numpy
import matplotlib.pyplot as plt
from numpy import int64, int32

url = "stud.csv"

df = pandas.read_csv(url, sep=';')
df.head()

print(df.isna().sum())                                                          # show missing values
df.replace(r'^\s*$', numpy.nan, regex=True)                  # Replace blank values with np.nan values


df.dropna(inplace=True)


df['StudentID'] = df['StudentID'].astype(str).astype(int64)                     # Convert from obj to int
df['Age'] = df['Age'].astype(float).astype(int32)
df['hrsStudy'] = df['hrsStudy'].astype(float).astype(int32)

df.info()

conditions = [(df['FinalGrade'] >= 91) & (df['FinalGrade'] <= 100),
              (df['FinalGrade'] >= 81) & (df['FinalGrade'] <= 90),
              (df['FinalGrade'] >= 71) & (df['FinalGrade'] <= 80),
              (df['FinalGrade'] >= 61) & (df['FinalGrade'] <= 70),
              (df['FinalGrade'] >= 51) & (df['FinalGrade'] <= 60),
              (df['FinalGrade'] < 50),
              (df['FinalGrade'] > 100)
              ]

grades = ['A', 'B', 'C', 'D', 'E', 'F', numpy.nan]

df['GradeLetter'] = numpy.select(conditions, grades)

print(df.head(100))

grade_count = df['GradeLetter'].value_counts(dropna=True).sort_index()
grade_count.plot.bar()
plt.show()
