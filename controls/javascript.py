import json
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot
from controls.items import DataItems


def decorator_format_result_for_js(func):
    def format_result_for_js(data):
        context = func(data)
        return json.dumps({
            "status": 200 if context is not None else 500,
            "context": context
        })
    return format_result_for_js


class JsHandler(QObject):
    @pyqtSlot(str, str, result=str)
    def channel(self, url, data):
        url = url.replace("/", "_")
        print(url)
        func = getattr(self, url)
        return func(data)

    @staticmethod
    @decorator_format_result_for_js
    def interface_data_load_all(data):
        items = DataItems.load_data_all()
        datas = []
        for item in items:
            print(item)
            datas.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "context": item.get("context"),
                "done": item.get("status") == "done"
            })
        return json.dumps(datas)

    @staticmethod
    @decorator_format_result_for_js
    def interface_data_modify(data):
        item = json.loads(data)
        id = item.get("id")
        status = item.get("status")
        DataItems.modify_status(id, status)
        return ""

    @staticmethod
    @decorator_format_result_for_js
    def interface_data_add(data):
        item = json.loads(data)
        title = item.get("title")
        DataItems.add_data(datetime="", title=title, context="", status="todo")
        return ""

    @staticmethod
    @decorator_format_result_for_js
    def interface_data_delete(data):
        item = json.loads(data)
        id = item.get("id")
        DataItems.delete_data(id)
        return ""
