FROM postgres:10.3-alpine

ADD setupdb.sql /docker-entrypoint-initdb.d

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

EXPOSE 5432