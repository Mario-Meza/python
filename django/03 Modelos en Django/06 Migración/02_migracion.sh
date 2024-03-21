# crear migración
python3 manage.py makemigrations

# migrar a base de datos
python3 manage.py migrate

# revisar sql
# python3 manage.py sqlmigrate app 0001_initial
python3 manage.py sqlmigrate holamundo 0001_initial