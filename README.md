# MyCart

## To run this application:


> Requirement: docker

### Run following commands:

```
docker build -t mycart:latest .
docker run -ti mycart:latest
```

or 

### just pull the image from docker hub:

`docker run -ti imaskm/mycart`

or

### to run locally, checkout the project, go to project directory and

```
export PYTHONPATH="$PYTHONPATH:$PWD"
export DB_PATH=$PWD/mycart.db
#install pip3 modules
pip3 install -r requirements.txt

# create tables and admin user
python3 mycart/scripts/init.py
#Run application
python3 mycart/main.py

```

#### Add cateogry,products using admin user:

username - admin
password - admin

then use app to create other users and perform different operations.

### To run the tests:

```
coverage run -m unittest discover tests/
coverage report -m
```


