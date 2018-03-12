
from flask_script import Manager
from csrf_demo import app
from exts import db
from flask_migrate import Migrate,MigrateCommand
from models import User

manager = Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)


if __name__ == "__main__":
	manager.run()

