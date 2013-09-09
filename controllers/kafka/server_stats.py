import os
import re

class Server_stats(object):
    ROOT = os.path.abspath(os.path.dirname(__file__))
    Port = 9999 
    Bean = {
        'SocketServerStats' : [],
        'BrokerAllTopicStat' : [],
        'LogFlushStats' : [],
    }

    
    def __init__(self):
        pass


    def get(self):
        self.Bean = {
            'SocketServerStats' : [],
            'BrokerAllTopicStat' : [],
            'LogFlushStats' : [],
        } 

        for key in self.Bean:
            commond = "java -jar {path}/cmdline-jmxclient-0.10.3.jar - localhost:{port} kafka:type=kafka.{bean} |grep -v Attributes |awk -F: '{{print $1}}' |sed -r 's#^\s+##'".format(
               path = self.ROOT,
               port = self.Port,
               bean = key,
            )

            for attr in os.popen(commond).readlines():
                attr = attr.strip()
                self.Bean[key].append(attr)
        return self.Bean 

    def find(self, beanname):
        result = {}
        blist = self.get()
        for b, f in blist.iteritems():
            if beanname in f:
                result[b] = beanname
        return result

    def load(self, beanname):
        ss = self.find(beanname) 
        commond = "java -jar {path}/cmdline-jmxclient-0.10.3.jar - localhost:{port} kafka:type=kafka.{bean} {func} 2>&1".format(
            path = self.ROOT,
            port = self.Port,
            bean = ss.keys()[0],
            func = ss.values()[0],
    )
        result = os.popen(commond).read()
        result = re.sub("^.*:\s+", "", result)
        result = "%.2f" % float(result)
        return result




#for k, v in Server_stats().get().iteritems():
#    print k,v




