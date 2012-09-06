#! /usr/bin/python

import unittest

from xmlrpclib import ServerProxy, Error, Fault

XMLRPCURL="http://192.168.128.1/cgi-bin/crapnet/wrapper.lua"

allpresets={'2G': {'latency': 100, 'bandwidth': 3000}, '3G': {'latency': 80, 'bandwidth': 7000}}

verbose=True
verbose=False

class TestCrapnet(unittest.TestCase):

    def setUp(self):
        self.server = ServerProxy(XMLRPCURL,verbose=verbose)

    def test_hello(self):
        self.assertEqual(self.server.hello(),"Hello world")

    def test_reset(self):
        self.assertEqual(self.server.reset(),"Reseted")

    def test_getpresets(self):
        self.assertEqual(self.server.getpresets(),allpresets)

    def test_tcversion(self):
        tcversion=self.server.tcversion()
        self.assertNotEqual(tcversion,0)

if __name__ == '__main__':
    unittest.main()
