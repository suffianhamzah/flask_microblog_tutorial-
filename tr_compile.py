#!/home/suffian/Envs/microblog_tutoriak/bin/python

import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\[ybabel'
else:
    pybabel = '/home/suffian/Envs/microblog_tutoriak/bin/pybabel'
os.system(pybabel + ' compile -d app/translations')
