import mysql.connector as mc

conn = mc.connect(
	host="localhost",
	user="root",
	password="connect",
)
c = conn.cursor()


def showDatabases():
	c.execute("show databases")
	fetch = c.fetchall()
	print(fetch)


def dropDatabase():
	c.execute("DROP DATABASE menagerie")


def createDatabase():
	c.execute("CREATE DATABASE menagerie")


def createPetTable():
	c.execute("CREATE TABLE pet \
	         (              \
	            name varchar(20),\
	            owner varchar(20),\
	            species varchar(20),\
	            sex char(1), \
	            birth date, \
	            death date \
	          )"
	          )


def readData():
	c.execute("describe pet")
	pet_table = c.fetchall()
	for i in pet_table:
		print(i)


def database():
	c.execute("USE menagerie")


def insertIntoPet():
	c.execute('INSERT INTO pet VALUES \
	          ("Fluffy","Harold", "cat", "f", "1993-02-04", NULL), \
	          ("Claws", "Gwen", "cat", "m", "1994-03-17", NULL), \
	            ("Buffy", "Harold", "dog", "f", "1989-05-13", NULL),\
	             ("Fang", "Benny", "dog", "m", "1990-08-27", NULL),\
	             ("Bowser", "Diane", "dog", "m", "1979-08-31", "1995-05-29"),\
				("Chirpy", "Gwen", "bird", "f", "1998-09-11", NULL),\
				("Whistler", "Gwen", "bird", NULL, "1997-12-09", NULL), \
				("Slim", "Benny", "snake", "m", "1996-04-29", NULL), \
				("Puffball", "Diane", "hamster", "f", "1999-03-30", NULL)'
	          )


def readPet():
	c.execute("SELECT * FROM pet")
	pet_table = c.fetchall()
	for i in pet_table:
		print(i)


def returnFemaleDog():
	c.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog'")
	fetch = c.fetchall()
	print(fetch)


def nameBirth():
	c.execute("SELECT name, birth FROM pet")
	fetch = c.fetchall()
	for i in fetch:
		print(i)


def petsOwner():
	c.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner ")
	fetch = c.fetchall()
	for i in fetch:
		print(i)


def petNameBirthMonth():
	c.execute("SELECT name, birth, MONTH(birth) FROM pet")
	fetch = c.fetchall()
	for i in fetch:
		print(i)


if __name__ == '__main__':
	database()
	insertIntoPet()
	petNameBirthMonth()

