# This is a copy of the deprecated HA-Addon Vantage Pro to MQTT

Originally located at [https://github.com/MarcoGos/ha-addons](https://github.com/MarcoGos/ha-addons) by [Marco Gosselink](https://github.com/MarcoGos).

The deprecated version includes a bug that does not handle negative temperatures which has been fixed in this version. This version will be deleted if Marco approves the pull request to include the fix, but that is uncertain per his deprecation announcement. 

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

# MarcoGos's _HASS.IO_ Repository

## About

This is the MarcoGos's _HASS.IO_ add-ons repository.

## Installation

The add-on is installed like any other:

1. Navigate in your Home Assistant frontend to **Supervisor** -> **Add-on Store**.
2. Click 3-dots menu at upper right > **Repositories** and add this repository URL: [https://github.com/MarcoGos/ha-addons](https://github.com/MarcoGos/ha-addons)
3. Scroll down the page to find the new repository "Add-ons from MarcoGos", and click one of the new add-ons.
4. Click <kbd>Install</kbd> and give it a few minutes to finish downloading.
5. Configure at **Configuration** tab or separate file in [**Configuration folder**](https://www.home-assistant.io/getting-started/configuration/) according to the instructions of the selected add-on:

- [GFS Weather Forecast](./addon-gfs_weather_forecast/)

- [Vantage Pro to MQTT](./addon-vantagepro2mqtt) (DEPRECATED, use the Davis Vantage integration: https://github.com/MarcoGos/davis_vantage)
- [GFS Forecast](./addon-gfsforecast) (DEPRECATED, use the GFS Weather Forecast addon)

6. Click <kbd>Start</kbd>, give it a few seconds to spin up.
7. Enjoy.

For troubleshooting use **Log** tab

## Support

Please open an issue here on Github.
