  
#!/bin/sh

set -e

function create_user_and_database() {
	local database=$1
	echo "  Creating user and database '$database'"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	    CREATE DATABASE $database;
	    GRANT ALL PRIVILEGES ON DATABASE $database TO $POSTGRES_USER;
	EOSQL
}

function create_extensions_postgis() {
	local database=$1
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname="$database" <<-'EOSQL'
		CREATE EXTENSION IF NOT EXISTS postgis;
		CREATE EXTENSION IF NOT EXISTS postgis_topology;
		CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
		CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder;
	EOSQL
}
echo "Multiple database creation requested:"

DATABASE_LIST=("${DB_NAME}" "${TEST_DB_NAME}")

for db in ${DATABASE_LIST[@]}; do
	create_user_and_database $db
	create_extensions_postgis $db
done 
echo "Multiple databases created"
