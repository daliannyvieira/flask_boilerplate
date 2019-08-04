dbhost = localhost
dbport = 3306
dbdatabase = new_database
dbuser = root
dbpass = 1234

export FLASK_APP=start.py
export DATABASE_URI=mysql+pymysql://$(dbuser):$(dbpass)@$(dbhost):$(dbport)/$(dbdatabase)
export APPLICATION_ENVIRONMENT=development

server:
	python3 -m start