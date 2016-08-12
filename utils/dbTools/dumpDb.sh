#!/bin/bash

ssh dissert "mysqldump -u cowrie -p cowrie > cowrie.sql"
scp dissert:/home/yann/cowrie.sql /tmp/
mysql -u root -p cowrie < /tmp/cowrie.sql
