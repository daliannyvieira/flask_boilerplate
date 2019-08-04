dbhost = ''
dbport = ''
dbdatabase = ''
dbuser = ''
dbpass = ''

export FLASK_APP=start.py
export DATABASE_URI=mysql+pymysql://$(dbuser):$(dbpass)@$(dbhost):$(dbport)/$(dbdatabase)
export APPLICATION_ENVIRONMENT=development

server:
	python3 -m start