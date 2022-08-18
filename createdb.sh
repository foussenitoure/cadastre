#!/usr/bin/env bash
#psql
#create database gisconsultingdb;
#CREATE USER myprojectuser WITH PASSWORD 'password';
#ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
#ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
#ALTER ROLE myprojectuser SET timezone TO 'UTC';
#GRANT ALL PRIVILEGES ON DATABASE gisconsultingdb TO myprojectuser;
#\c gisconsultingdb;
#CREATE EXTENSION postgis;
#\q


python manage.py dumpdata --format=json contacts > /Users/toure/PycharmProjects/douniyasoba/tmp/$(date +"%Y%m%d_%H:%M:%S")_data.json;
psql -U postgresql;
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
python manage.py makemigrations;
python manage.py migrate;
python manage.py createsuperuser;
python manage.py loaddata  /Users/toure/PycharmProjects/douniyasoba/tmp/$(current +"%Y%m%d_%H:%M:%S")_data.json
