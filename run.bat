@echo off

if exist myenv\Scripts\activate (
    echo Virtual environment found. Starting server...
    call myenv\Scripts\activate
    echo --------------------------------------------------------------------------------------------------------------------------------------
    echo Keep in mind, after closing the server, you'll have to deactivate the virtual enviroment by yourself by running 'voff' or 'deactivate'
    echo --------------------------------------------------------------------------------------------------------------------------------------
    python manage.py runserver
) else (
    echo Virtual environment not found. Please run the installation script first.
)
