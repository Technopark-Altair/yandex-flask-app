from requests import get, post, delete
from pprint import pprint


api_url = 'http://localhost:8080/api/v2'

pprint(get(f'{api_url}/news').json())
# pprint(get(f'{api_url}/news/1').json())

# pprint(get(f'{api_url}/news/asd').text)
# новости с id = 999 нет в базе

# pprint(post(f'{api_url}/news').json())
#
# pprint(post(f'{api_url}/news',
#            json={'title': 'Заголовок'}).json())
# #
# pprint(post(f'{api_url}/news',
#            json={'title': 'Заголовок 2',
#                  'content': 'Текст новости',
#                  'is_published': False,
#                  'user_id': 1,
#                  'is_private': False}).json())

# pprint(delete(f'{api_url}/news/2').json())
# # новости с id = 999 нет в базе
#
# pprint(delete(f'{api_url}/news/2').json())