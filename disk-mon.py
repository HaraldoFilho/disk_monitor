#!/usr/bin/python3

import os
import time
import config
import mail

from datetime import datetime


### FUNCTIONS ###

def read_disk():
    df = os.popen("df -lh | grep /dev/root").readline()
    usage = df.split()[4].split('%')[0]
    return int(usage)

def get_hostname():
    hostname = os.popen("hostname").readline()
    return hostname.replace("\n", "")

def write_log(usage, level):
    now = datetime.now()
    log = open("/home/pi/disk_monitor/disk_mon.log", "a")
    log.write("[" + datetime.strftime(now, "%d/%m/%y %H:%M:%S") + "] " + str(usage) + " : " + level + "\n")
    log.close

def send_email(email_from, email_to, subject, critical_msg, usage):
    host_name = get_hostname()
    try:
        os.system("echo \"The disk usage is " + str(usage) + "%. \"" + critical_msg + " | mail -s \"" + subject + "\" -A \"/home/pi/disk_monitor/disk_mon.log\" -a From:" + host_name + "\<" + email_from + "\> " + email_to)
    except:
        pass

def remove_log_files():
    os.system("rm -f /var/log/apt/*.log")
    os.system("rm -f /var/log/nginx/*.log")
    os.system("rm -f /var/log/clamav/*.log")
    os.system("rm -f /var/log/supervisor/*.log")
    os.system("rm -f /var/log/*.log")

def reboot_system():
    os.system("sudo umount -a")
    os.system("sudo reboot -h now")


### MAIN ###

disk_ok = True
i = config.MON_INTERVAL + 1

while True:

    usage = read_disk()

    if usage >= config.USAGE_CRITICAL:
        write_log(usage, "CRITICAL")
        send_email(mail.FROM, mail.TO, mail.USAGE_CRITICAL, mail.MSG_CRITICAL, usage)
        remove_log_files()
        reboot_system()
        exit(0)

    if i > config.MON_INTERVAL:
        if usage > config.USAGE_THRESHOLD:
            if disk_ok:
                disk_ok = False
                write_log(usage, "HIGH")
                send_email(mail.FROM, mail.TO , mail.USAGE_HIGH, "", usage)
                i = 1
        else:
            if not disk_ok:
                disk_ok = True
                write_log(occup, "NORMAL")
                send_email(mail.FROM, mail.TO, mail.USAGE_NORMAL, "", usage)
                i = 1

    i += 1
    time.sleep(config.MON_PERIOD)
