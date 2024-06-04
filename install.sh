#!/bin/bash

cp files/mail mail.py
sudo cp files/disk-mon /etc/init.d/
sudo update-rc.d disk-mon defaults
