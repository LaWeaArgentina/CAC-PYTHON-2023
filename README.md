# presupuestar  
Sistema para Crear Presupuesto Rodaje Audiovisual

## requirements

- install docker  
- install docker-compose
- install flask
- install python

## get start

1. clone repository

```bash 
git clone https://github.com/LaWeaArgentina/CAC-PYTHON-2023.git
```

2. create .env file

```bash 
cp .env.dist .env
```

3. install python packages

```bash 
pip install -r requirements.txt
```

4. start database

```bash 
docker-compose up -d
```

5. start flask app

```bash 
python3 app.py
```

