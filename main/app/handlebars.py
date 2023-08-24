class Handlebars:
    def __init__(self, template, variables=None):
        """
        Initializes the Handlebars template with optional variables.

        :param template: The Handlebars template string
        :param variables: Dictionary of variables to be used in rendering the template
        """
        self.template = template
        self.variables = variables or {}

    def render(self):
        """
        Renders the Handlebars template with the given variables.

        :return: The rendered template
        """
        return self._render_template()

    def _render_template(self):
        """
        Renders the handlebars template with the given variables.

        :return: The rendered template
        """
        # Replace placeholders in the template using self.variables
        rendered = self.template
        for key, value in self.variables.items():
            rendered = rendered.replace("{{" + key + "}}", value)
        return rendered

# Example usage
template_string = "Hello, {{name}}! Today is {{day}}."
variables = {"name": "Alice", "day": "Monday"}
handlebars = Handlebars