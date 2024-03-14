from app import create_app
from flask_script import Manager, Server
import psycopg2, tempfile

db_fd, db_path = tempfile.mkstemp()
# Creating app instance
app = create_app('development',{
        'TESTING': True,
        'DATABASE': db_path,
    })
   

manager = Manager(app)
manager.add_command('server',Server)



@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run()