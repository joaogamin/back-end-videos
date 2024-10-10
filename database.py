from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(database: SQLAlchemy):
	inspector = database.inspect(database.engine)
	tables = inspector.get_table_names()

	if not tables:
		database.create_all()
		database.session.commit()
		print("Database tables created successfully!")
	else:
		print("Tables already exist. No action needed.")
