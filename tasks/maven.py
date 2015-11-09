#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess 

proc =subprocess.Popen(['mvn', 'clean', 'install', '-U'], stdout=subprocess.PIPE)
outs, err = proc.communicate()

print (outs.decode('ascii'))
