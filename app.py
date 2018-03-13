
import psycopg2

# connect
conn = psycopg2.connect(dbname="buss", user="ag3125", password="sd8sdpsf", host="pgserver.mah.se")

	    while True:
		welcome()
        menu()
        user_choice = input("Ditt val: ")
        if user_choice == "1":
            register()
        elif user_choice == "2":
            book_trip()
        elif user_choice == "3":
            search()
        elif user_choice == "4":
            print("Hejdå!")
            break
        else:
            print("Du valde inte ett korrekt alternativ, försök igen")

def welcome():
	print(*******)
	print("Välkommen till Mörtfors buss bokningssystem!")
	print(*******)

def menu():
    print("")
    print("Meny")
    print("****")
    print("1. Registrera dig som kund")
    print("2. Boka resa")
    print("3. Sök resa")
    print("4. Avsluta")

def register():
	name = input("Ange ditt namn: ")
	adress = input("Ange din adress: ")
	epost = input("Ange din epostadress: ")
	telefonnummer = input("Ange ditt telefonnummer: ")

	cursor = conn.cursor()
	cursor.execute("insert into kund values (%s, %s, %s, %s)", (name, adress, epost, telefonnummer))
	conn.commit()

def book_trip():
	pass

def search():
	depart = input("Vilken stad vill du åka ifrån? ")
	arrive = input("Vilken stad vill du åka till? ")

	cursor = conn.cursor

register()
