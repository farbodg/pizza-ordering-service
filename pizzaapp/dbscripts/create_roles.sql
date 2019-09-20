CREATE DATABASE pizza;

CREATE USER pizzauser WITH PASSWORD 'ilovepizza';

ALTER ROLE pizzauser SET client_encoding TO 'utf8';
ALTER ROLE pizzauser SET default_transaction_isolation TO 'read committed';
ALTER ROLE pizzauser SET timezone TO 'UTC';
ALTER USER pizzauser CREATEDB;

GRANT ALL PRIVILEGES ON DATABASE pizza TO pizzauser;