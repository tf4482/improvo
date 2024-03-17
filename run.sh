#!/bin/bash

if [ -e myenv/Scripts/activate ]; then

    LYELLOW=$'\e[1;93m'
    LGREEN=$'\e[1;92m'
    NC='\033[0m'

    echo "Virtual environment found. Starting server..."
    source myenv/Scripts/activate
    printf "\n${LYELLOW}--------------------------------------------------------------------"
    printf "\n${LGREEN}Keep in mind, after closing the server, you'll have to deactivate"
    printf "\nthe virtual enviroment by yourself by running 'deactivate'"
    printf "\n${LYELLOW}--------------------------------------------------------------------${NC}\n"
    python manage.py runserver

else

    echo "Virtual environment not found. Please run the installation script first."

fi
