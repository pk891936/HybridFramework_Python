
print('******program to plot a simple bar chart*********')
import pandas as pd
import matplotlib.pyplot as plt

data = [['E001', 'M', 34,123,'Normal', 350],
        ['E002', 'F', 40,113,'WEIGHT', 450],
        ['E003', 'F', 37,129,'Normal', 320],
        ['E004', 'M', 30,143,'Normal', 350],
        ['E005', 'F', 44,129,'AVERAGE', 550],
        ['E006', 'M', 36,165,'OVERWEIGHT', 250],
        ['E007', 'M', 32,93,'Normal', 500],
        ['E008', 'F', 26,137,'Normal', 850]]

df = pd.DataFrame(data, columns=['EMPID','Gender','Age','Sales','BMI','Income'])
df.plot.bar()
plt.bar(df['Age'], df['Sales'])
plt.xlabel('Age')
plt.ylabel('Sales')
plt.show()