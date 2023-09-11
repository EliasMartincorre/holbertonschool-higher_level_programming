import db
from models import Producto

def run():
    pass

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()