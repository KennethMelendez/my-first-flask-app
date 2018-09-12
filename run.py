# run.py

# configuring our run.py to start the flask server

from app import app

if __name__ == '__main__':
    app.run()



    """
    In order to run flask use these commands
    set FLASK_APP=run.py
    $ flask run
    """