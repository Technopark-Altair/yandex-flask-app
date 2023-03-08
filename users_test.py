from requests import get, post, delete
from pprint import pprint


api_url = 'http://localhost:8080/api/v2'

pprint(get(f'{api_url}/users').json())
# pprint(get(f'{api_url}/users/4').json())

# pprint(get(f'{api_url}/users/asd').text)
# новости с id = 999 нет в базе

# pprint(post(f'{api_url}/users').json())
#
# pprint(post(f'{api_url}/users',
#            json={'name': 'Заголовок'}).json())
# #
# pprint(post(f'{api_url}/users',
#            json={'name': 'Misha',
#                  'about': 'Human',
#                  'email': 'misha@mail.ru',
#                  'password': 'misha12345',
#                  'password_again': 'misha12345'
#                  }).json())

# pprint(delete(f'{api_url}/users/2').json())
# # новости с id = 999 нет в базе
#
pprint(delete(f'{api_url}/users/5').json())