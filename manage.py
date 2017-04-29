#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line
    sys.path[0]='/Users/scofieldyu/yu/myproject/'
    sys.path.append('/Users/scofieldyu/yu/myproject/tmitter')
    sys.path.append('/Users/scofieldyu/yu/myproject/tmitter/utils')
    sys.path.append('/Users/scofieldyu/yu/myproject/tmitter/mvc')
    sys.path.append('/Users/scofieldyu/yu/myproject/tmitter/venv/lib/python2.7/site-packages/PIL')
    #print sys.path
    execute_from_command_line(sys.argv)
