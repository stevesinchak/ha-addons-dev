import sys, getopt

device = ""
address = ""
broker = ""
port = 1883
mqtt_user = ""
mqtt_pass = ""
discovery_prefix = "homeassistant"
prefix = 'vantagepro'
unit_system = "Metric"
alt_windspeed_uom = False
hass_configured = False
log_level = 'notice'
interval = 30
new_sensor_used = False
windrose8 = False
availability_topic = f"{discovery_prefix}/sensor/{prefix}/Status/state"

qc_cold_temp = -100
qc_hot_temp = 200

try:
    opts, args = getopt.getopt(sys.argv[1:], ":d:a:b:P:u:p:I:s:i:nl:kw:c:t:",["device=","address=","broker=","port=","user=","password=","prefix=","system=","interval=","new_sensor", "log_level=", "alt_windspeed_uom", "windrose8", "qc_cold_temp=", "qc_hot_temp="])
except getopt.GetoptError:
    print('vantagepro2mqtt.py [-d <device>|-a <address>] -b <broker>[-P <port>][-u <user>][-p <password>][-I <prefix>][-s <system>][-i <interval][-l <loglevel>][-n][-k][-w][-c <qccoldtemp>][-t <qchottemp>]')
    sys.exit(2)
for opt, arg in opts:
    logger.debug(f"{opt}={arg}")
    if opt in ('-d',"--device"):
        if arg != 'null':
            device = arg
    elif opt in ("-a", "--address"):
        if arg != 'null':
            address = arg
    elif opt in ("-b", "--broker"):
        broker = arg
    elif opt in ("-P", "--port"):
        port = int(arg)
    elif opt in ("-u", "--user"):
        mqtt_user = arg
    elif opt in ("-p", "--password"):
        mqtt_pass = arg
    elif opt in ("-I", "--prefix"):
        discovery_prefix = arg
    elif opt in ("-s", "--system"):
        unit_system = arg
    elif opt in ("-i", "--interval"):
        interval = int(arg)
    elif opt in ("-n", "--new_sensor"):
        new_sensor_used = True
    elif opt in ("-l", "--log_level"):
        log_level = arg
    elif opt in ("-k", "--alt_windspeed_uom"):
        alt_windspeed_uom = True
    elif opt in ("-w", "--windrose8"):
        windrose8 = True
    elif opt in ("-c", "--qc_cold_temp"):
        qc_cold_temp = int(arg)
    elif opt in ("-t", "--qc_hot_temp"):
        qc_hot_temp = int(arg)
