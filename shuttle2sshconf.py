#!/usr/bin/env python
import json
import re
import argparse
import sys
from os.path import expanduser

def is_host(array):
	if array.has_key('cmd') and array.has_key('name'):
		return True

def extracts_host_from(_hash):
	for element in _hash.iteritems():
		key, array = element
		for a in array:
			if is_host(a):
				print convert_array_to_ssh_config_syntax(a)
			else:
				extracts_host_from(a)
	return 

def ssh_target(string):
	return string.split('@')

def convert_array_to_ssh_config_syntax(array):
	user = ""
	host = ""
	parser = argparse.ArgumentParser(prog = 'ssh')
	parser.add_argument('target', type=ssh_target )
	parser.add_argument('-i',dest='key')
	args = parser.parse_args(array['cmd'].split()[1:])
	user, host = args.target
	syntax = ""
	syntax += "Host %s:\n" % array['name']
	syntax += "\tHostname %s\n" % host
	syntax += "\tUser %s\n" % user
	if args.key:
		syntax += "\tIdentityFile %s\n" % args.key
	return syntax

home = expanduser("~")
p = argparse.ArgumentParser()
p.add_argument('-c', '--conf', help="Shuttle configuration file", default='%s/.shuttle.json' % home)
args = p.parse_args() 

try:
	json_data = open(args.conf).read()
except IOError as e:
	print e
	sys.exit(1)
	
try:
	conf = json.loads(json_data)
except ValueError as e:
	print e
	exit(2)

extracts_host_from(conf['hosts'].pop())
