#!/bin/bash

cd /home/pi/MakerGarden
python3 daily_report.py
git add .
git commit -m "daily push"
git push

