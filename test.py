from Flask_new_class import Server
server = Server()
need_href = ['/login', '/registration', '/posts']
server.easy_setup(need_href, templates={'dat': 'Слава Путину'})
server.run()
