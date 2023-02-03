from pkg.models import db


class Menu:
    def __init__(self, creator, name, data=None):
        self.creator = creator
        self.name = name
        self.data = data
        #fgfdbd

    def get(self):
        doc = db \
            .collection('creators') \
            .document(f'{self.creator}') \
            .collection('menu') \
            .document(self.name)
        self.data = doc.get().to_dict()

    def create(self):
        doc = db \
            .collection('creators') \
            .document(self.creator) \
            .collection('menu') \
            .document(self.name)
        doc.set({
            'data': self.data,
        })

    def delete():
        pass


def all(creator):
    res = []
    docs = db \
        .collection('creators') \
        .document(creator) \
        .collection('menu') \
        .get()
    for doc in docs:
        res.append(Menu(creator, doc.id))
    return res
