import pandas as pd

data = {'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
        'Blood Sugar Level': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125,
                              130, 135, 140, 145],
        'Product': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D',
                    'D', 'D', 'E', 'E']}

df = pd.DataFrame(data)

print(df)