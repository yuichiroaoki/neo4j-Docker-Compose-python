FROM neo4j:latest
COPY import/*.csv import/
COPY script/import_csv.sh import_csv.sh
ENV EXTENSION_SCRIPT=import_csv.sh
ENV NEO4J_AUTH=neo4j/password
CMD [ "neo4j" ]