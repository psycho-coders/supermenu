from pkg.models import db


class Menu:
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def get(self, name):
        doc = db.collection(u'menu').document(u'{name}').format(name=name)
        if doc.exists:    
            return (f'{name} ==> {doc.get().to_dict()}'), 200
        return "Data not found", 404

    def create(self):
        doc_ref = db.collection(u'menu').document(f'{self.name}')
        doc_ref.set({
            u'data': self.params,
        })

    def delete():
        pass
