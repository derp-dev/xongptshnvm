import handlebars


class Handlebars:

    def __init__(self, template):
        self.template = template
        self.variables = {}

    def render(self, **kwargs):
        for key, value in kwargs.items():
            self.variables[key] = value

        return self._render_template()

    def _render_template(self):
        """
        Renders the handlebars template with the given variables.

        :return: The rendered template
        """
        return Template(self.template).render(**self.variables)


def __init__(self, handlebars_object, endpoint, token, data):
    self.handlebars_object = handlebars_object
    self.endpoint = endpoint
    self.token = token
    self.data = data

def encode_curl_post_request(self):
    curl_command = "curl -s -X POST "
    curl_command += f"'{self.endpoint}' "
    curl_command += "--header 'Content-Type: application/json' "
    curl_command += f"--header 'Authorization: Bearer {self.token}' "
    curl_command += "--data '{\"prompt\":\""
    curl_command += self.handlebars_object.render(**self.data)
    curl_command += "', \"max_tokens\": 3000}'"

    # Example usage
    handlebars = Handlebars("This is a message for {{name}}. It was created on {{day}}.",
                            {'name': 'John', 'day': 'Monday'})
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"
    token = "my_secret_token"
    data = {'name': 'Alice', 'day': 'Tuesday'}
    handle_post = HandlePost(handlebars, endpoint, token, data)
    return handle_post.encode_curl_post_request()
