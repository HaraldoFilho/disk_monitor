# Disk Monitor for Raspberry Pi

This is a script to monitor the disk usage of a Raspberry Pi. It sends warning e-mails when the usage is above a threshold level and remove logs and reboot the device if above a critical level.

## Installation

To run, the script requires **_Python 3_**, a user **_pi_** configured in the system and the packages **_mailutils_** and **_ssmtp_** installed and configured.

To install the script, login as **_pi_** and execute the following commands: 

```
cd /home/pi
git clone https://github.com/HaraldoFilho/disk_monitor.git
cd disk_monitor
./install.sh
```

The file _/etc/sudoers_ will be automatically opened for edit. Add the following line to it:

```
root   ALL=(ALL) NOPASSWD: /sbin/reboot
```

This will permit that the device can be rebooted without asking for a password.

## Configuration

There are two configuration files with default values that can be modified by the user:

### _config.py_

```
# Parameters:

# MON_PERIOD     : Number of seconds the usage is read. 
# MON_INTERVAL   : Number of seconds the usage is checked. 
# USAGE_THRESOLD : Value in usage percent on that a warning e-mail is sent if temperature is above it.
# USAGE_CRITICAL : Value in usage percent on that log files are removed and the device is rebooted.
# MSG_CRITICAL   : An additional message when the usage is critical.

MON_PERIOD       = 1
MON_INTERVAL     = 600
USAGE_THRESHOLD  = 80
USAGE_CRITICAL   = 90
```

### _mail.py_

```
# Parameters:

# FROM           : Sender's e-mail address.
# TO             : Recipient's e-mail address.
# USAGE_HIGH     : Message when the disk usage is above the threshold.
# USAGE_NORMAL   : Message when the disk usage is back to normal.
# USAGE_CRITICAL : Message when the disk usage is above the critical level.
# MSG_CRITICAL   : Additional message when the disk is above the critical level.

FROM             = ""
TO               = ""
USAGE_HIGH       = "Disk usage is too high!"
USAGE_NORMAL     = "Disk usage is back to normal"
USAGE_CRITICAL   = "DISK USAGE IS CRITICALLY HIGH!!!"
MSG_CRITICAL     = "Some log files were removed and the system rebooted trying to free some space."
```

## Usage

Just reboot the device and the script will run in background.


