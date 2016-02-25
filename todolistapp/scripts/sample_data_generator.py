"""
Creates test data
************************************WARNING************************************
Many of the unit tests depend on data set in this script. Always
run the unit tests (python manage.py test) after making any changes to this
data!!
************************************WARNING************************************
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))

from todolistapp import models as models

def run():
    """
    Create basic sample data
    """
    print('Creating Person')

if __name__ == "__main__":
    run()
