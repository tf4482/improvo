@echo off

echo Deactivating virtual environment...
call myenv\Scripts\deactivate

echo Deleting virtual environment...
rd /s /q myenv

echo Deleting database...
del db.sqlite3

echo Deleting migration files...
del /s /q *.pyc
rd /s /q migrations

echo Reset completed!
