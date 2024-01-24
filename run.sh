#!/bin/bash

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