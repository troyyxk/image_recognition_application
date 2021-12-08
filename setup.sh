#!/usr/bin/env bash

BASE_DIR=$(pwd)

echo "Which role does this machine play?"
echo "[1] Server - Serves HTML files, Django backend and RabbitMQ"
echo "[2] Worker - Runs GoogleNet"

read role

if [ $role = "1" ]; then

  sudo apt-get update
  sudo apt-get install -y python3-pip libjpeg8-dev zlib1g-dev nginx
  sudo apt-get install -y ca-certificates curl gnupg lsb-release

  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  echo "Installing docker..."
  sudo apt-get update
  sudo apt-get install -y docker-ce docker-ce-cli containerd.io

  echo "Installing Django and Dependencies..."
  sudo pip3 install django pillow celery

  cd $BASE_DIR/back_end/back_end

  echo "Initializing Database..."
  python3 manage.py migrate

  echo "Setting up superuser..."
  python3 manage.py createsuperuser

  echo "Running Django Server..."
  nohup python3 manage.py runserver 0.0.0.0:28000 &

  echo "Copying frontend html files..."
  cd $BASE_DIR/front_end/image_recognition_frontend
  sudo cp -R build /var/www/html/

  sudo cp $BASE_DIR/server.conf /etc/nginx/sites-enabled/
  sudo rm /etc/nginx/sites-enabled/default

  echo "Reload nginx server..."
  sudo systemctl restart nginx

  echo "Starting RabbitMQ..."
  sudo docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management


elif [ $role = "2" ]; then

  echo "Installing dependencies..."
  sudo apt-get update
  sudo apt-get install -y python3-pip libjpeg8-dev zlib1g-dev nginx
  pip3 install setuptools
  pip3 install wheel celery
  pip3 install torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
  pip3 install requests

  echo "Starting Celery Worker..."
  cd $BASE_DIR/celery_worker
  nohup celery -A tasks worker --loglevel=INFO &

else
  echo "Input invalid! Aborted!"
fi