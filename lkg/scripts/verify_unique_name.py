
import os
import time
import logging
from datetime import datetime

log = logging.getLogger(__name__)

unique_test_name = os.environ.get("unique_name")

def run(context):
    context.verify(grep=unique_test_name)
    #context.verify(grep="Test Run")