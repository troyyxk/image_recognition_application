#!/usr/bin/env bash

BASE_DIR=$(pwd)

echo "Which role does this machine play?"
echo "[1] Server"
echo "[2] Worker"

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
  echo "hello"

else
  echo "Input invalid! Aborted!"

fi