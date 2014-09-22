#!/usr/bin/env python

# Maltego transform for getting the robots.txt file from websites

from MaltegoTransform import *
import requests

m = MaltegoTransform()
m.parseArguments(sys.argv)

website = m.getVar('fqdn')
port = m.getVar('ports')
port = port.split(',')
ssl = m.getVar('website.ssl-enabled')
robots = []

print website


try:
  for c in port:
    if ssl == 'true':
      r = requests.get('https://' + website + ':' + str(c) + '/robots.txt')
      if r.status_code == 200:
        robots = str(r.text).split('\n')
        for i in robots:
          m.addEntity('maltego.Phrase', i)
      else:
        m.addUIMessage("No Robots.txt found..")
    else:
      r = requests.get('http://' + website + ':' + str(c) + '/robots.txt')
      if r.status_code == 200:
        robots = str(r.text).split('\n')
        for i in robots:
          m.addEntity('maltego.Phrase', i)
      else:
        m.addUIMessage("No Robots.txt found..")
except Exception as e:
  m.addUIMessage(str(e))

m.returnOutput()


