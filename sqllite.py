import sqlite3
conn=sqlite3.connect('OpenSky.db')

c=conn.cursor()
c.execute("""CREATE TABLE DATA2 (
sensorType text, sensorLatitude real,sensorLongitude real,sensorAltitude real,
timeAtServer real, timeAtSensor real, timestamp real, rawMessage text, sensorSerialNumber integer,
RSSIPacket real, RSSIPreamble real, SNR real, confidence real)
""")


conn.commit()
conn.close()