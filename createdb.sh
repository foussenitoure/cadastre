#!/usr/bin/env bash
psql;
CREATE database gisconsultingdb;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE gisconsultingdb TO myprojectuser;
\c gisconsultingdb;
CREATE EXTENSION postgis;
\q