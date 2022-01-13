#!/usr/bin/python
import requests
import time
import os

# import Temperature class (mainly built for envio, but suits well for adafruit too)
from modules.temperature import Temperature
from modules.helpers import get_temperature, wrap_envio_data, killme

# Load and validate config
config = {}
# FIRST: Fail immediately if required vars are not set
required = ['SERVICE', 'APIKEY', 'USER', 'FEED', 'SENSOR']
for var in required:
    config[var.lower()] = (var in os.environ) and os.environ[var] or killme(var)

# SECOND: Fail for service-specific environment variables
if config['service'] == 'envio':
    config['host'] = ('HOST' in os.environ) and os.environ['HOST'] or killme('HOST')

# THIRD: Variables with default values
config['precision'] = int(os.environ.get('PRECISION', 1))
config['timeout'] = int(os.environ.get('TIMEOUT', 120))
config['packagesize'] = int(os.environ.get('PACKAGESIZE', 1))

# TODO: Do wireless connection check, if connection lost, future led will indicate loss of connection
# Probably making a simple request to a common website, maybe a website that is self hosted, in order to prevent legal claims for bots


if __name__ == "__main__":
    while True:
        
        # Handling envio
        if config['service'] == "envio":
            # Empty dataset
            dataset = []
            # Build url
            url = config['host'] + "/user/" + config['user'] + "/sensor/" + config['feed'] + "/measurement"
            headers = {'X-API-Key': config['apikey']}
            # Now collect data with timeout until size of package is reached
            for i in range(config['packagesize']):
                # Grab current temperature and add to dataset
                measurement = Temperature(get_temperature(config['sensor'], config['precision']))
                dataset.append(measurement.get_json())
                # sleep for seconds configured in timeout
                time.sleep(config['timeout'])
            # Once done collecting, wrap the content and send it
            json = wrap_envio_data(dataset)
            response = requests.post(url, headers=headers, json=json)
            print(vars(response))

        # Handling for adafruit.io    
        elif config['service'] == "adafruit":
            # Build url
            url = "https://io.adafruit.com/api/v2/" + config['user'] + "/feeds/" + config['feed'] + "/data"
            # Grab current temperature
            measurement = get_temperature(config['sensor'], config['precision'])
            # Prepare auth and content
            headers = {'X-AIO-Key': config['apikey'], 'Content-Type': 'application/json'}
            json = {'value': measurement}
            # Send Data to adafruit.io
            response = requests.post(url, headers=headers, json=json)
            print(vars(response))
            # Go to sleep before next measurement
            time.sleep(config['timeout'])
