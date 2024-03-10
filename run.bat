@echo off

if exist myenv\Scripts\activate (
    echo Virtual environment found. Starting server...
    call myenv\Scripts\activate
    python manage.py runserver
) else (
    echo Virtual environment not found. Please run the installation script first.
)
