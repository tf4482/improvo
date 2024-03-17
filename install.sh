#!/bin/sh

CYAN=$'\e[0;36m'
NC='\033[0m'

printf "${CYAN}Setting up virtual environment...${NC}\n"
python -m venv myenv

printf "${CYAN}Activating virtual environment...${NC}\n"
source myenv/Scripts/activate

printf "${CYAN}Installing Django...${NC}\n"
pip install django

printf "${CYAN}Installing other requirements...${NC}\n"
pip install -r requirements.txt

printf "${CYAN}Creating database...${NC}\n"
python manage.py migrate

printf "${CYAN}Setting up admin...${NC}\n"
python manage.py createsuperuser --username admin --email mail@example.com

printf "${CYAN}Done! You can now run the server by executing 'run.sh'. Your admin username is 'admin'.${NC}\n"
