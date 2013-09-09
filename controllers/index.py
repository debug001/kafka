import sys
sys.path.insert(0, '../')

from bottle import route, run, static_file, request
from bottle import jinja2_template as template
import simplejson
from kafka.server_stats import Server_stats
import re

@route('/')
def index():
    return template('templates/index')


@route('/server_status')
def server_status():
    return template('templates/server_status')



@route('/api/server_status')
def get_attr():
    data = {"topic":[]}

    ss = Server_stats()
    for row in ss.get()['SocketServerStats']:
        row = row.strip()
        data["topic"].append({"name":row, "now":99})


    #return "Ext.data.JsonP.callback1(%s)" % data

    temp = """
{
"topic": [
{ "name":"test1", "now": 55, "lastm": 34, "lasth": 99 },
{ "name":"test2", "now": 55, "lastm": 34, "lasth": 99 }
]
}
"""

    return data



@route('/api/server_status/<attribute>')
def ss_attr(attribute):
    result = {}
    if attribute == 'ProduceRequestsPerSecond':
        result['ss'] = {}
        result['ss'][date]
        print result
#        result['ss'].append({"date":"15:10", "value":35})
#    return simplejson.dump(result)
    return ""


    



