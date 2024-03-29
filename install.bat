@echo off

echo Setting up virtual environment...
python -m venv myenv

echo Activating virtual environment...
call myenv\Scripts\activate

echo Installing Django...
pip install django

echo Installing other requirements...
pip install -r requirements.txt

echo Installing Tailwind CSS...
python manage.py tailwind install

echo Building application...
python manage.py tailwind build

echo Creating database...
python manage.py migrate

echo Setting up admin...
python manage.py createsuperuser --username admin --email mail@example.com

echo Done! You can now run the server by executing 'run.bat'. Your admin username is 'admin'.
