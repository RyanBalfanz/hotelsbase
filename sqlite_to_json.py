import sqlite3


DATABASE = "hotelsbase.db"

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def dump(db, rowFactory=None):
	connection = conn = sqlite3.connect(db)
	if rowFactory:
		connection.row_factory = rowFactory
	c = conn.cursor()
	for row in c.execute("""SELECT * FROM hotels;"""):
		print row

def main(db, format=None):
	rowFactory = None
	if format and format.lower() == "json":
		rowFactory = dict_factory

	dump(db, rowFactory=rowFactory)


if __name__ == '__main__':
	main(DATABASE, format="json")
