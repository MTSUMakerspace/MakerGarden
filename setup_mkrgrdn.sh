#!/bin/bash

# Be sure to do sudo apt update and sudo apt install before running script

sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
cp /home/pi/grdnPI/ipconfifiles/dhcpcd.conf /etc/
cp /home/pi/grdnPI/ipconfifiles/hostname /etc/
cp /home/pi/grdnPI/ipconfifiles/hosts /etc/
sudo systemctl enable ssh
sudo systemctl start ssh
sudo reboot
