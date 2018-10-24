from models.models import Items
from models.db import Session


class DataItems(Items):
    @staticmethod
    def load_data_all():
        items = Session.query(Items).all()
        datas = []
        for item in items:
            datas.append({
                "id": str(item.id),
                "datetime": item.datetime,
                "title": item.title,
                "context": item.context,
                "finish": item.finish,
                "status": item.status
            })
        return datas

    @staticmethod
    def load_data_by_status(status):
        items = Session.query(Items).filter(Items.status == status).all()
        datas = []
        for item in items:
            datas.append({
                "id": str(item.id),
                "datetime": item.datetime,
                "title": item.title,
                "context": item.context,
                "finish": item.finish
            })
        return datas

    @staticmethod
    def load_data_by_id(id):
        items = Session.query(Items).filter(Items.id == id).all()
        datas = []
        for item in items:
            datas.append({
                "id": str(item.id),
                "datetime": item.datetime,
                "title": item.title,
                "context": item.context,
                "status": item.status
            })
        return datas

    @staticmethod
    def modify_data(item):
        db_item = Session.query(Items).filter(Items.id == item["id"]).first()
        db_item.datetime = item["datetime"]
        db_item.title = item["title"]
        db_item.context = item["context"]
        Session.commit()

    def modify_status(id, status, finish=None):
        db_item = Session.query(Items).filter(Items.id == id).first()
        db_item.status = status
        if finish is not None:
            db_item.finish = finish
        Session.commit()

    @staticmethod
    def add_data(**kwargs):
        Session.add(Items(
            datetime = kwargs['datetime'],
            title = kwargs['title'],
            context =kwargs['context'],
            status = kwargs['status']
        ))
        Session.commit()

    @staticmethod
    def delete_data(id):
        Session.query(Items).filter(Items.id == id).delete()
        Session.commit()
