# Выведите в браузер текущее время.

#  На главной странице создайте несколько кнопок, по нажатию на которые пользователю будет показываться или
#  текущая дата, или текущее время.

import datetime
import cherrypy
import random
import string


def current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return str(current_time)


def current_date():
    today = datetime.date.today()
    return str(today)


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>DATE OR TIME</head>
          <body>
            <form method="get" action="generate_time">
              <input type="text" value="time" name="length" />
              <button type="submit">Get time!</button>
            </form>
            <form method="get" action="generate_date">
              <input type="text" value="date" name="length" />
              <button type="submit">Get date!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate_time(self, length=8):
        return current_time()

    @cherrypy.expose
    def generate_date(self, length=8):
        return current_date()


class DateTime(object):
    @cherrypy.expose
    def index(self):
        return current_time()


cherrypy.quickstart(StringGenerator())
