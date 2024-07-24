# Using PythonAnywhere API to reload the web app without using the web interface

import requests
import datosconexion as dt

response = requests.post(f'https://www.pythonanywhere.com/api/v0/user/{dt.username}/webapps/{dt.domain_name}/reload/', headers={'Authorization': f'Token {dt.api_token}'})

if response.status_code == 200:
    print('reloaded OK')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))