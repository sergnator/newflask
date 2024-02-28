import typing
import flask


class Server:
    def __init__(self, ip: str | None = None, port: int | None = None, name=__name__):
        self._app = flask.Flask(name)
        self._ip = ip
        self._port = port
        self._rules = []

    def add_method(self, rule: str, method: callable, **args):
        """Добавляет метод к ссылке"""
        endpoint = args.pop('endpoint', None)
        self._app.add_url_rule(rule=rule, endpoint=endpoint, view_func=method, **args)
        self._rules.append(rule)

    def easy_setup(self, rules: typing.Iterable[str], **args):
        """быстрая настройка сайта"""
        templates = None
        if 'templates' in args:
            templates = args.pop('templates')

        for rule in rules:
            if templates is None:
                self.add_method(rule, lambda param=rule[1:]: flask.render_template(f'{param}.html'),
                                endpoint=rule[1:])
            else:
                self.add_method(rule, lambda param=rule[1:]: flask.render_template(f'{param}.html', **templates),
                                endpoint=rule[1:])

    def get_rules(self):
        return self._rules

    def run(self):
        """Запуск сервера"""
        self._app.run()
