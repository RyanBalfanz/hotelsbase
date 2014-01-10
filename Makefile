db:
	sqlite3 hotelsbase.db < init_db.sql
	echo "BEGIN;" `cat hotelsbase.sql` "END;" | sqlite3 hotelsbase.db

all: db
