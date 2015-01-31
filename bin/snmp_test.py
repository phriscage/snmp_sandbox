#!/usr/bin/python2.7
import netsnmp

class Snmp(object):
    """ encapsulate snmp as a class """
    
    def __init__(self):
        """ instatiate the object """
        self.community = 'public'
        self.dest_host = 'localhost'
        self.version = 2 # must be an integer
        try:
            self.session = netsnmp.Session(DestHost=self.dest_host, 
                Version=self.version, Community=self.community)
            #self.session.UseNumeric = 1 # OID numerci
            self.session.UseSprintValue = 1
        except Exception, error:
            print error
            raise error
    
    def get(self, oid):
        """ get the values for a given host and oid """
        vars = netsnmp.VarList(netsnmp.Varbind(oid)) # must be a list
        #res = netsnmp.snmpgetbulk(1, oid, Version=version, DestHost=dest_host, community=community)
        res = self.session.get(vars)
        if res:
            #print res
            for var in vars:
                print "%s.%s = %s: %s" % (var.tag, var.iid, var.type, var.val)
        else:
            return None

    def getbulk(self, oid):
        """ get the values for a given host and oid """
        vars = netsnmp.VarList(netsnmp.Varbind(oid)) # must be a list
        #res = netsnmp.snmpgetbulk(1, oid, Version=version, DestHost=dest_host, community=community)
        res = self.session.getbulk(0, 100, vars)
        if res:
            #print res
            for var in vars:
                print "%s.%s = %s: %s" % (var.tag, var.iid, var.type, var.val)
        else:
            return None

    def walk(self, oid):
        """ get the values for a given host and oid """
        vars = netsnmp.VarList(netsnmp.Varbind(oid)) # must be a list
        #res = netsnmp.snmpgetbulk(1, oid, Version=version, DestHost=dest_host, community=community)
        res = self.session.walk(vars)
        if res:
            #print res
            for var in vars:
                print "%s.%s = %s: %s" % (var.tag, var.iid, var.type, var.val)
        else:
            return None

if __name__ == '__main__':
    snmp = Snmp()
    #snmp.get('sysDescr.0')
    #snmp.getbulk('.1.3.6.1.2.1.1.1')
    #snmp.walk('.1.3.6.1.2.1.1')
    #snmp.walk('ipRouteTable')
    #snmp.getbulk('ifTable')
    snmp.getbulk('ifTable')

