# This is a fork based on the deprecated Vantage Pro to MQTT Home Assistant Addon

Before being deprecated, version 1.0.15 was originally located at [https://github.com/MarcoGos/ha-addons/tree/master/addon-vantagepro2mqtt](https://github.com/MarcoGos/ha-addons/tree/master/addon-vantagepro2mqtt) by [Marco Gosselink](https://github.com/MarcoGos).  The developer moved their focus to a different implementation no longer leveraging MQTT.  

For those interested in a MQTT-based solution, this fork, which is tracked as version 2, is actively maintained with various bug fixes and enhancements. 

## Enhancements in Version 2

- Fix: Negative temperatures are now handled correctly fixing an unsigned integer bug in the pyvantage library.
- New: User-configurable temperature and wind speed quality control settings. Ignore measurements outside of the allowed range to prevent reporting bad data. For example, temperature readings above 150 degrees F typically would indicate a measurement error and should not be reported. 

# Reference copy of Version 1 README

[https://github.com/MarcoGos/ha-addons/blob/master/addon-vantagepro2mqtt/README.md](https://github.com/MarcoGos/ha-addons/blob/master/addon-vantagepro2mqtt/README.md)

# Home Assistant Add-on: Vantage Pro to MQTT

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

Acquiring data from a Davis Vantage weather station using the pyvantagepro software. Either use a serial port or use an ip adress to connect to your device. Tested with the Vantage Pro 2 combined with a Davis WeatherLink 6510SER serial port data logger (connected via a ser2usb converter to the ha server) and with a Vantage Vue combined with a WeatherLink IP. Probably works with the WeatherLink 6510USB as well. Other models unsure. Please leave a note if model is working.

### The following models should work:

- Vantage Pro
- Vantage Pro 2 (Rev B)
- Weather Envoy
- Vantage Vue

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg