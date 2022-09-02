#!/usr/bin/env bash
import os
from pygments.lexers import python
import manage

python3 manage.py dumpdata --format=json contacts > /Users/foussenytoure/Documents/ProjectPycharm/douniyasoba/tmp/$(date +"%Y%m%d_%H:%M:%S")_data.json;
psql -U postgres;
drop database gisconsultingdb;
create database gisconsultingdb;
create user myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE gisconsultingdb TO myprojectuser;
\c gisconsultingdb;
create extension postgis;
CREATE EXTENSION postgis_topology;
python3 manage.py makemigrations;
python3 manage.py migrate;
python3 manage.py createsuperuser;
python3 manage.py loaddata  /Users/foussenytoure/Documents/ProjectPycharm/douniyasoba/tmpp/$(current +"%Y%m%d_%H:%M:%S")_data.json
