class Page():
    def __init__(self, name, title=None, path=None):
        """
        Create a new Vue.js page (i.e. a view).

        >>> page = Page('Home', 'Home Page', '/home')
        >>> page.name
        'Home'

        >>> page.title
        'Home Page'

        >>> page.path
        '/home'

        Parameters
        ----------
        name : str
            The internal name of the page, used in Python code.
        title : str, optional
            The title of the page, used in the browser tab. Defaults to the name if not provided.
        path : str, optional
            The URL path of the page. Defaults to the name if not provided.
        """
        self.name = name
        self.title = title if title else name # TODO: Add title support
        self.components = []

        self.path = path if path else name.lower().replace(' ', '-') # 'Testing 123' -> 'testing-123'
        self.path = f'/{self.path}'
        self.filename = f'{self.name}.vue'

    def add(self, component):
        self.components.append(component)
        return self
