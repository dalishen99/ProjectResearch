#!/usr/bin/env python
import sys, getpass, MySQLdb
import re, wget, os

"""
    This script is used to extract Identifiers (username/passwords) from the
    cowrie database (Honeypot) and create two files storing all identifiers
    and all passwords separately. It is useful to extract identifiers from
    binary strings.

    Usage:
    ------
    python extarctMalware.py DATABASE_USERNAME
"""

if len(sys.argv) != 2:
    sys.exit(2)

user = sys.argv[1]
passwd = getpass.getpass()

try:
    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd=passwd,
                         db="cowrie")
except:
    print "Error: DB fail to connect."
    sys.exit()

cur = db.cursor()

req_username = "select distinct username from auth ;"
cur.execute(req_username)
fuser = open("../../collectedData/identifiers/username", 'w')
cpt = 0
for row in cur.fetchall():
    fuser.write(row[0] + '\n')
    cpt += 1
fuser.close()
print "username: " + str(cpt)

req_password = "select distinct password from auth ;"
cur.execute(req_password)
fpassword = open("../../collectedData/identifiers/password", 'w')
cpt = 0
for row in cur.fetchall():
    fpassword.write(row[0] + '\n')
    cpt += 1
fpassword.close()
print "password: " + str(cpt)
