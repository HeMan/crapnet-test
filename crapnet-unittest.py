#! /usr/bin/python

import unittest

from xmlrpclib import ServerProxy, Error

# server = ServerProxy("http://localhost:8000") # local server
server = ServerProxy("http://192.168.128.1/cgi-bin/crapnet/wrapper.lua")
#server = ServerProxy("http://192.168.128.1/cgi-bin/crapnet/do.lua")
#server = ServerProxy("http://192.168.128.1/cgi-bin/crapnet/cgitest.lua")

print server.hello()


