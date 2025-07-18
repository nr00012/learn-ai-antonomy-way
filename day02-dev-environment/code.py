# Day 02 – Verify Your Python Environment

import sys
import platform

def show_env_info():
    print("✅ Python Version:", sys.version)
    print("💻 Platform:", platform.system(), platform.release())

if __name__ == "__main__":
    show_env_info()
