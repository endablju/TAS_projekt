from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import MySQLdb

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8001),
                            requestHandler=RequestHandler,
                            allow_none=True)
server.register_introspection_functions()

    
def add_book(title,autor,slug,text,price,quantity):
    sql = "INSERT INTO books_book (title,slug,text,autor,price,quantity)" \
       "VALUES (%s,%s,%s,%s,%s,%s )"
    try:
        db = MySQLdb.connect("db4free.net", "ksiegarnia", "tas_projekt", "tasksiegarnia")
        cursor = db.cursor()
        cursor.execute(sql,(title,slug,text,autor,price,quantity))
        db.commit()
        print "1"
    except:
        print "0"
        db.rollback()
    finally:
        cursor.close()
        db.close()
        



server.register_function(add_book)
server.serve_forever()
