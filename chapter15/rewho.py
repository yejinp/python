#!/usr/bin/env python

from re import split
from os import popen

f = popen('who', 'r')
for eachLine in f.readlines():
    print split('\s\s+|\t', eachLine.strip())

f.close()
