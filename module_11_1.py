import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Простой график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('plot.png')
plt.show()



data = pd.read_csv('data.csv')

print(data.describe())

filtered_data = data[data['column_name'] > threshold]
print(filtered_data)