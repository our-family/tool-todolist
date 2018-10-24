from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from controls.javascript import JsHandler
from configures import settings


class MainWindow(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.channel = QWebChannel()
        self.handler = JsHandler()
        self.channel.registerObject('pyjs', self.handler)
        self.page().setWebChannel(self.channel)
        self.load(QUrl("file:///" + settings.HTML_INDEX))
