try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
from project.constants import BASE_URL

TODOS_URL = urljoin(BASE_URL, 'todos')

class TodoManager(object):
    
    def get_todos(self):
        response = requests.get(TODOS_URL)
        if response.ok:
            return response
        else:
            return None

    def get_uncompleted_todos(self):
        response = self.get_todos()
        if response is None:
            return []
        else:
            todos = response.json()
            return [todo for todo in todos if todo.get('completed') == False]
