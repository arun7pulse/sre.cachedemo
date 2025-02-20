#!/bin/bash

if($1){


# Dcoker Compose Build 
docker-compose up -d --build --remove-orphans


# docker compose -f docker_devcompose.yaml up -d



# Load Redis sample data. 
redis-cli -h localhost -p 6379 < ./seed_scripts/import_users.redis

}
# Docker Compose Down. 
docker-compose down --volumes 

