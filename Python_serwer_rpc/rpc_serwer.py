 # -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import MySQLdb

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8001),
                            requestHandler=RequestHandler,
                            allow_none=True)
server.register_introspection_functions()


#trzeba napisać 4 metody pobieranie Book_object_all, book_object_get, category_object_all, category_object_get


#sqlalchemy
    
def add_book(title,autor,slug,text,price,quantity):
    sql = "INSERT INTO books_book (title,slug,text,autor,price,quantity)" \
       "VALUES (%s,%s,%s,%s,%s,%s )"
    try:
        db = MySQLdb.connect("db4free.net", "ksiegarnia", "tas_projekt", "tasksiegarnia")
        cursor = db.cursor()
        cursor.execute(sql,(title,slug,text,autor,price,quantity))
        db.commit()
        print "Dodałem książke"
        return "TRUE"  
    except:
        print "Nie dodałem książki. Błąd"
        return "FALSE"        
        db.rollback()
    finally:
        cursor.close()
        db.close()
    
        
def delete_book(id):
    sql = "DELETE FROM books_book WHERE id=%s"
    try:
        db = MySQLdb.connect("db4free.net", "ksiegarnia", "tas_projekt", "tasksiegarnia")
        cursor = db.cursor()
        cursor.execute(sql,(id,))
        db.commit()
        print "Usunąlem książke"
        return "TRUE"  
    except:
        print "Nie udało się usunąć książki. Błąd"
        return "FALSE"     
    finally:
        cursor.close()
        db.close()

def add_category(name):
    sql = "INSERT INTO books_category (name) VALUES (%s)"
    try:
        db = MySQLdb.connect("db4free.net", "ksiegarnia", "tas_projekt", "tasksiegarnia")
        cursor = db.cursor()
        cursor.execute(sql,(name,))
        db.commit()
        print "Dodałem kategorie"
        return "TRUE"  
    except:
        print "Nie dodałem kategorii. Błąd"
        return "FALSE"     
        db.rollback()
    finally:
        cursor.close()
        db.close()

		
def update_book(title,autor,slug,text,price,quantity,id):
    sql = "UPDATE books_book SET title=%s, autor=%s, slug=%s, text=%s, price=%s, quantity=%s WHERE id=%s"
    
    try:
        db = MySQLdb.connect("db4free.net", "ksiegarnia", "tas_projekt", "tasksiegarnia")
        cursor = db.cursor()
        cursor.execute(sql,(title,autor,slug,text,price,quantity,id,))
        print "Edytowałem"
        return "TRUE"  
    except:
        print "Nie udało się zedytować książki. Błąd"
        return "FALSE"     
        db.rollback()
    finally:
        cursor.close()
        db.close()		
		

server.register_function(add_book)
server.register_function(delete_book)
server.register_function(add_category)
server.register_function(update_book)
server.serve_forever()
