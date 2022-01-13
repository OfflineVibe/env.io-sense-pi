#!/usr/bin/python
import sys

# Helper Functions

# Reading Temperature from Sensor
def get_temperature(sensor, precision):
    tempfile = open("/sys/bus/w1/devices/" + sensor + "/w1_slave")
    inhalt = tempfile.read()
    tempfile.close()
    tempdata = inhalt.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    return round(temperature, precision)

# Wrapper for env.io POST-payload
def wrap_envio_data(data):
    api_object = {
        "measurements": data
    }
    return api_object

def killme(var):
    sys.exit('Missing environment variable \"' + var + '\"')