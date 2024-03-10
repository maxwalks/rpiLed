#!/bin/bash

# Config files
sudo cp config/52-usb.rules /etc/udev/rules.d/

# Add permitted users to dialout group
sudo usermod -a -G dialout $USER

# Install tools needed
sudo apt install git apache2 libapache2-mod-wsgi-py3 pip virtualenv uhubctl

# Config files
sudo rm /etc/apache2/sites-available/000-default.conf
sudo cp config/000-default.conf /etc/apache2/sites-available/

# Navigate to the specified directory
cd /var/www/html

# Remove the existing index.html file
sudo rm index.html

# Install Flask using pip
sudo pip install flask

# Clone the Git repository
sudo git clone https://github.com/maxwalks/rpiLed.git

# Navigate to the cloned repository
cd rpiLed

# Create a virtual environment
sudo virtualenv venv

# Reboot System
echo "Rebooting System..."
sleep 5
sudo reboot