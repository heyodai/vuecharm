import dagwood
import subprocess
import os
from jinja2 import Environment, PackageLoader
from .page import Page

class VueApp():
    def __init__(self):
        self.log = dagwood.assemble() # TODO: Move this to __init__.py
        
        self.components = []
        self.pages = []
        self.assets = [] # TODO: Add asset support

        self.api = None # TODO: Add API support
        self.store = None # TODO: Add Vuex support

        self.jinja = Environment(loader=PackageLoader('vuecharm', 'templates'))

    def compile(self):
        """
        Convert to Vue.js code and prepare for distribution
        """
        self.transpile()

        # Install dependencies
        subprocess.run(["npm", "install"])

        # Build the app
        subprocess.run(["npm", "run", "build"])

    def transpile(self, path: str = 'src'):
        """
        Convert stored pages and components into Vue.js code
        """
        # Build the main
        os.makedirs(path, exist_ok=True)
        with open('src/main.js', 'w') as f:
            f.write(self.build_main())

        # Build the app
        with open(f'{path}/App.vue', 'w') as f:
            f.write(self.build_app())

        # Build the routes
        with open(f'{path}/router.js', 'w') as f:
            f.write(self.build_routes())

        # Build the pages
        os.makedirs(f'{path}/views', exist_ok=True)
        for page in self.pages:
            with open(f'src/views/{page.filename}', 'w') as f:
                f.write(self.build_page(page))

    def build_routes(self) -> str: # TODO: Should we have a stricter return type?
        """
        Build the routes for the Vue.js app
        """
        # Assemble the routes
        routes = {}
        for page in self.pages: # TODO: Add error checking for duplicate paths, no pages, etc.
            routes[page] = f"""{{ 
                path: '{page.path}', 
                component: {page.name},
                name: '{page.name}'
                filename: '{page.filename}'
            }}"""

        # Load the template
        template = self.jinja.get_template('router.j2')

        # Render the template
        rendered_template = template.render(routes=routes)
        return rendered_template
    
    def build_app(self):
        """
        Build the app for the Vue.js app
        """
        # Load the template
        template = self.jinja.get_template('app.j2')

        # Render the template
        rendered_template = template.render(components=self.components)
        return rendered_template

    def build_main(self):
        """
        Build the main for the Vue.js app
        """
        # Load the template
        template = self.jinja.get_template('main.j2')

        # Render the template
        rendered_template = template.render(components=self.components)
        return rendered_template

    def build_page(self, page: Page) -> str: 
        """
        Build a page (i.e. a view) for the Vue.js app
        """
        # Load the template
        template = self.jinja.get_template('page.j2')

        # Render the template
        rendered_template = template.render(page=page)
        return rendered_template
    