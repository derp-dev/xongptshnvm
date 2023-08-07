class ClientModel:
    def __init__(self):
        self.code_snippet = None
        self.execution_result = None
        self.error = None

    def update_code_snippet(self, code_snippet):
        self.code_snippet = code_snippet

    def update_execution_result(self, execution_result):
        self.execution_result = execution_result

    def update_error(self, error):
        self.error = error

    def get_code_snippet(self):
        return self.code_snippet

    def get_execution_result(self):
        return self.execution_result

    def get_error(self):
        return self.error