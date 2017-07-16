import os, sys, json
from py2neo import Graph

__config_file_path__ = os.path.abspath( os.path.join(os.path.dirname(__file__), "config.json" )


class medical_db:

    def __init__(self, conf = {}):
        if conf == {}:
            with open(config_file) as fp:
                self.conf = json.load(fp=fp)
        else:
            self.conf = conf
        self.start()       #start db

    def start(self):
        conf = self.conf
        self.graph = Graph( host = conf['host'], user= conf['user'], password = conf['password'] )

    def query(self, query):
        return self.graph.run(query).data()

    def get_list_by_type(self, type = 'disease', attrib = ['standard_name']):
        '''
            return cursors
        '''
        attrib_str = ", ".join([ "a." + a for a in attrib])
        sql = "MATCH (a:{0} RETURN {1} )".format(type, attrib_str)
        return self.graph.run(sql)

    def query_disease_info(self,  key = 'standard_name', value = ''):
        '''
            query_disease_info by id
        '''
        return self.graph.find_one(label="disease", property_key=key, property_value = value)
