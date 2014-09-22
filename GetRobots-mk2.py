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

try:
  for c in port:
    if ssl == 'true':
      url = 'https://' + website + ':' + str(c) + '/robots.txt'
      r = requests.get(url)
      if r.status_code == 200:
        robots = str(r.text).split('\n')
        for i in robots:
          ent = m.addEntity('maltego.Phrase', i)
          ent.addAdditionalFields("url","Original URL",True,url)
      else:
        m.addUIMessage("No Robots.txt found..")
    else:
      url = 'http://' + website + ':' + str(c) + '/robots.txt'
      r = requests.get(url)
      if r.status_code == 200:
        robots = str(r.text).split('\n')
        for i in robots:
          ent = m.addEntity('maltego.Phrase', i)
          ent.addAdditionalFields("url","Original URL",True,url)
      else:
        m.addUIMessage("No Robots.txt found..")
except Exception as e:
  m.addUIMessage(str(e))

m.returnOutput()


