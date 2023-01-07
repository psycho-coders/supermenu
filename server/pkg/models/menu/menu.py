from pkg.models import db


class Menu:
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def get():
        pass

    def create(self):
        doc_ref = db.collection(u'menu').document(f'{self.name}')
        doc_ref.set({
            u'data': self.params,
        })

    def delete():
        pass
