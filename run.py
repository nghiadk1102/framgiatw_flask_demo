#!venv/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

from app import app

from app import app as application

if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', debug = True)
