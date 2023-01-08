from pkg.models import db


class Menu:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def get(self):
        doc = db.collection(u'menu').where(u'id', u'==', self.id)
        if doc.exists:    
            self.data = doc.get().to_dict()
        else: self.data = dict()

    def create(self):
        doc_ref = db.collection(u'menu').document(f'{self.id}')
        doc_ref.set({
            u'data': self.data,
        })

    def delete():
        pass
