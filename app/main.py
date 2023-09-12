#!/usr/bin/env python
""" Start App """
import os
def main():
    os.environ.setdefault('APP_SETTINGS_MODULE', 'settings.development')
    from core import start 
    start()

if __name__ == '__main__':
    main()