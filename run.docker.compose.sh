#!/bin/bash
# Dcoker Compose Build 
docker-compose up -d --build --remove-orphans
# Docker Compose Down. 
docker-compose down --volumes 

# Load Redis sample data. 
redis-cli -h localhost -p 6379 < ./seed_scripts/import_users.redis
