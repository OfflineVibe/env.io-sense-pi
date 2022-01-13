#!/usr/bin/python
import time
import datetime

class Temperature:

    def __init__(self, temperature):
        currentDate = datetime.datetime.now()
        self.timestamp = int(time.time())
        self.temperature = temperature

    def get_json(self):
        return vars(self)
