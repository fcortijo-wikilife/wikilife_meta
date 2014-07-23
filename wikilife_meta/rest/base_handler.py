# coding=utf-8

from tornado.web import RequestHandler
from wikilife_utils.parsers.json_parser import JSONParser

"""
Common base handler shared amongst all admin handlers
"""


class BaseHandler(RequestHandler):

    _logger = None

    def initialize(self, services):
        RequestHandler.initialize(self)
        self._services = services
        self._logger = self.settings['logger']

    def success(self, response=None, status_code=200, user_message=None, dev_message=None):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        if user_message is not None:
            self.set_header("X-User-Message", user_message)
        if dev_message is not None:
            self.set_header("X-Dev-Message", dev_message)
        self.write(JSONParser.to_json(response))