from bottle import route, run
 
from controllers.index import *

@route('<path:path>')
def server_static(path):
    return static_file(path, root='/www/kafka-webconsole/public/')



if __name__ == '__main__':
    run(host='0.0.0.0',port=8888,reloader=True)
