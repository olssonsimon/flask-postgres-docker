DO
$do$
BEGIN
   IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'flaskapp_db') THEN
      RAISE NOTICE 'Database already exists'; 
   ELSE
      PERFORM dblink_exec('dbname=' || current_database(), 'CREATE DATABASE flaskapp_db');
   END IF;
END
$do$;