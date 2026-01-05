
# import json 
# data = '{"name": "John", "age": 30}'
# parsed_data = json.loads(data)
# print(parsed_data)

import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 40]
plt.plot(x, y)
plt.show()

import requests
response = requests.get('https://api.github.com')
print(response.status_code)

from bs4 import BeautifulSoup
import requests
page = requests.get("https://example.com")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.text) 


