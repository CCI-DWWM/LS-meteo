from database import get_connection
import sys



def get_city(codePostal):
    db = get_connection()

    mycursor = db.cursor()

    mycursor.execute(f"SELECT nom_de_la_commune FROM code_postal WHERE code_postal = {codePostal}")

    myresult = mycursor.fetchone()[0]

    return myresult