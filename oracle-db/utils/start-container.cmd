podman container stop oracle-db
podman container rm oracle-db
podman run -d --name oracle-db -p 1521:1521 --net oradb-network  -v c:\volumes\oradata:/opt/oracle/oradata    container-registry.oracle.com/database/free:latest
