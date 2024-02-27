import flask


class Server:
    def __init__(self, ip: str | None = None, port: int | None = None):
        self.app = flask.Flask(__name__)
        self.ip = ip
        self.port = port

    def add_method(self, rule: str, method: callable, **args):
        """Добавляет метод к ссылке"""
        endpoint = args.pop('endpoint', None)
        self.app.add_url_rule(rule=rule, endpoint=endpoint, view_func=method, **args)

    def run(self):
        """Запуск сервера"""
        self.app.run()
