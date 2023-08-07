import requests
from client.client_model import ClientModel
from client.client_view import ClientView
from client.client_controller import ClientController

class Client:
    def __init__(self, server_url):
        self.server_url = server_url
        self.model = ClientModel()
        self.view = ClientView()
        self.controller = ClientController(self.model, self.view)
