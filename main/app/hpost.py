import handlebars


class HandlePost:
    def __init__(self, handlebars_object, endpoint, token, data):
        self.handlebars_object = handlebars_object
        self.endpoint = endpoint
        self.token = token
        self.data = data

    @handlebars.register_helper
    def encode_curl_post_request(self):
        curl_command = "curl -s -X POST "
        curl_command += f"'{self.endpoint}' "
        curl_command += "--header 'Content-Type: application/json' "
        curl_command += f"--header 'Authorization: Bearer {self.token}' "
        curl_command += "--data '{\"prompt\":\""
        curl_command += self.handlebars_object.render(**self.data)
        curl_command += "', \"max_tokens\": 3000}'"
        return curl_command

# Example usage
handlebars = Handlebars("This is a message for {{name}}. It was created on {{day}}.",
                         {'name': 'John', 'day': 'Monday'})
endpoint = "https://api.openai.com/v1/engines/davinci/completions"
token = "my_secret_token"
data = {'name': 'Alice', 'day': 'Tuesday'}
handle_post = HandlePost(handlebars, endpoint, token, data)
encoded_request = handle_post.encode_curl_post_request()
print(encoded_request)