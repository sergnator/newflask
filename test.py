from Flask_new_class import Server
import copy

server = Server()

need_href = ['/index', '/login', '/registration', '/posts']
functions = []
for href in need_href:
    server.add_method(href, lambda: href[1:], endpoint=href[1:])
    functions.append(copy.deepcopy(lambda: href[1:]))

for f in functions:
    print(f())
server.run()
