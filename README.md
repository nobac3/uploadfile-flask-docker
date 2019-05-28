# Flask, Dockerfile & Docker-compose.yaml

## Flask 

#### 1 - start virtual env: 

    cd upload-to-s3-master
    source env/bin/activate
    
#### 2 - start app

    python app/app.py

## Dockerfile

#### 1 - create machine 

    docker-machine create --driver virtualbox default
    docker-machine env default
    $ eval "$(docker-machine env default)"

#### 2 - build image 

    docker build -t group-c/flask-app .

#### 3 - run the container

    docker run --name upload-file-project -p 8030:8030 group-c/flask-app

#### 4 - delete all images 

    docker rmi  $(docker images)

#### 5 - delete all containers

    docker rm -vf $(docker ps -a -q)
    
#### 6 - remove container 

    docker rm -f upload-file-project

## Docker-compose 

#### 1 - create image

    docker build -t group-c/flask-app .     
    docker build -t group-c/flask-app -e S3_ACCESS_KEY="AKIAJHV54AGZJ5KFR46A" -e S3_SECRET_ACCESS_KEY="LdH3xRt+uqfG0ncvkk8vaxzyrEAAStBrnOdSTv/a" .



#### 2 - docker-compose 

    docker-compose up

## Secure your AWS access code


#### 1 - local

    export S3_ACCESS_KEY="WRITE_YOUR_ACCESS_KEY_HERE"
    export S3_SECRET_ACCESS_KEY="WRITE_YOUR_S3_SECRET_ACCESS_KEY_HERE"

#### 2 - DOCKER 

    docker run --name upload-file-project -p 8030:8030 -e S3_ACCESS_KEY="WRITE_YOUR_ACCESS_KEY_HERE" -e S3_SECRET_ACCESS_KEY="WRITE_YOUR_S3_SECRET_ACCESS_KEY_HERE" group-c/flask-app