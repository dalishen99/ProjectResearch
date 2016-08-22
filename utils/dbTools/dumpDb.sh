#!/bin/bash

# This script is used to extract the remote cowrie database (honeypot) and
# copy it locally to be re-used.

ssh dissert "mysqldump -u cowrie -p cowrie > cowrie.sql"
scp dissert:/home/yann/cowrie.sql /tmp/
mysql -u root -p cowrie < /tmp/cowrie.sql
