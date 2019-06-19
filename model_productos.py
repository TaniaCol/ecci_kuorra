import web
import config

db = config.db


def get_all_productos():
    try:
        return db.select('productos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_productos(id_producto):
    try:
        return db.select('productos', where='id_producto=$id_producto', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_productos(id_producto):
    try:
        return db.delete('productos', where='id_producto=$id_producto', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_productos(productos,precio,existencias):
    try:
        return db.insert('productos',productos=productos,
precio=precio,
existencias=existencias)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_productos(id_producto,productos,precio,existencias):
    try:
        return db.update('productos',id_producto=id_producto,
productos=productos,
precio=precio,
existencias=existencias,
                  where='id_producto=$id_producto',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
