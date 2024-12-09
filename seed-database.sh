#!/bin/bash

# Obtener el ID del contenedor de la base de datos
CONTAINER_ID=$(docker compose ps -q bakugan-db)

if [ -z "$CONTAINER_ID" ]; then
    echo "Error: No se encontró el contenedor de la base de datos"
    exit 1
fi

echo "Ejecutando script seed.sql..."
docker compose exec -T bakugan-db mysql -ubakugan -pbakugan bakugan < api/bakugan/seed.sql

if [ $? -eq 0 ]; then
    echo "Base de datos inicializada exitosamente!"
else
    echo "Error al inicializar la base de datos"
    exit 1
fi