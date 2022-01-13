# env.io Sense-Client for Raspberry Pi (Docker Container)
This container is pushing temperatures measured on your Raspberry Pi on either env.io or adafruit.io
Please make sure that your user has sufficient privileges to read the value of your sensor.

## Environment Variables
Please set up environment variables before starting your Docker-Container.

| name          | required   | description |
|:----          |:--------   | -----------:|
| `SERVICE`     | true       | either `envio` or `adafruit`
| `HOST`        | envio-only | REST-URL for posting content
| `APIKEY`      | true       | API key used for authentication
| `USER`        | true       | Username for your Service
| `FEED`        | true       | Name of Sensor or Feed at service
| `SENSOR`      | true       | 1-Wire ID of sensor 
| `PRECISION`   | false      | Default: `1`. Number of digits after comma for measurements
| `TIMEOUT`     | false      | Default: `120`. Time in seconds between measurements
| `PACKAGESIZE` | envio-only | Default: `5`. Number of Measurements collected before sending

default values for `TIMEOUT` and `PACKAGESIZE` are meeting the maximum abilities of the adafruit.io free tier. Changing them might result in error responses by their API.

## Installation
Please consider using docker-compose for a proper overview on your environment variables. A dockerfile example is listed below:

```
version: '3.9'

services:
  envio-sense-pi:
    build:
      context: .
    environment:
      - SERVICE=envio
      - HOST=https://example.com/api/v1
      - APIKEY=
      - USER=
      - FEED=
      - SENSOR=
    restart: unless-stopped
```

After making the configuration, build your Container.

```
docker-compose up --build
```

## Changelog

### 0.0.3
- Added support for adafruit.io

### 0.0.2
- Added environment variables

### 0.0.1
- Added env.io support


## Todo

### Network Fail Check
Check Network once every x Minutes.
If it is offline, first, turn on an LED. Second, store data locally. At restart, send an email to a backup plan.

### AWS API Validation
