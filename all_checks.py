#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """ Returns True if computer is rebooting"""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        """ checks for reboot pending """
        print('pending reboot')
        sys.exit(1)
    print('everything ok')
    sys.exit(0)

main()
