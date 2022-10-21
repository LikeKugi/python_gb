import cherrypy


class Calc(object):
    @cherrypy.expose
    def index(self):
        with open('index.html',encoding='utf-8') as index:
            return index.read()

    @cherrypy.expose()
    def calc(self, f_value, s_value, op_value):
        return str(eval(f'{f_value} {op_value} {s_value}'))


if __name__ == '__main__':
    cherrypy.quickstart(Calc(), '/')
