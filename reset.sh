#!/bin/sh

LRED=$'\e[1;91m'
NC='\033[0m'

printf "${LRED}Deleting virtual environment...\n${NC}"
rm -rf myenv

printf "${LRED}Deleting database...\n${NC}"
rm db.sqlite3

printf "${LRED}Deleting migration files...\n${NC}"
rm -f ./*.pyc
rm -rf migrations

printf "${LRED}Deactivating virtual environment...\n${NC}"
deactivate
