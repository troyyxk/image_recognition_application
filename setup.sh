#!/usr/bin/env bash

BASE_DIR=$(pwd)

echo "Which role does this machine play?"
echo "[1] Server"
echo "[2] Worker"

read role

if [ $role = "1" ]; then

  sudo apt-get update
  sudo apt-get install -y python3-pip libjpeg8-dev zlib1g-dev nginx

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

  sudo systemctl restart nginx

elif [ $role = "2" ]; then
  echo "hello"
fi