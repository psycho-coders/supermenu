from pkg.models import db


class Menu:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def get(self):
        doc_ref = db.collection('menu').document(f'{self.id}')
        doc = doc_ref.get()
        self.data = doc.to_dict()

    def create(self):
        doc_ref = db.collection('menu').document(f'{self.id}')
        doc_ref.set({
            'data': self.data,
        })

    def delete():
        pass
