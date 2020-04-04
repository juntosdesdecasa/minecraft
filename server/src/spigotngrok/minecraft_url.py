#!/bin/python
# -*- coding: iso-8859-15 -*-

import subprocess
import json
import sys
from urlparse import urlparse

line = subprocess.check_output(["/usr/bin/curl", "http://127.0.0.1:4040/api/tunnels"], shell=False)
ngrokstatus = json.loads(line)
ngrokurl = urlparse(ngrokstatus["tunnels"][0]["public_url"])

print (u"Tu servidor de minecraft es accesible en esta direccion: %s" % (ngrokurl.netloc))
