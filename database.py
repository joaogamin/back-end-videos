from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db():
	inspector = db.inspect(db.engine)
	tables = inspector.get_table_names()

	if not tables:
		db.create_all()
		db.session.commit()
		print("Database tables created successfully!")
	else:
		print("Tables already exist. No action needed.")
