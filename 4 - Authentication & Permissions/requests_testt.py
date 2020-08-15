import requests
# import json

data = {"title": "Criando titulo novo", "linenos": "false", "language": "python", "style": "autumn"}

f = requests.post('http://127.0.0.1:8000/snippets/', json=data, auth=('admin', 'admin'))

print(f.json())
