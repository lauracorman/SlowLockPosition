# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 11:30:31 2015

@author: tempo
"""
import ConfigParser
config = ConfigParser.RawConfigParser()

config.add_section('Lumenera camera 1')
config.set('Lumenera camera 1','exposureTime','0.312')
config.set('Lumenera camera 1','gain','1')

config.add_section('Princeton camera 1')
config.set('Princeton camera 1','exposureTime','0.312')
config.set('Princeton camera 1','gain','1')

with open('configFileTest.cfg','w') as configfile:
    config.write(configfile)

