#!/usr/bin/evn python3

import sqlite3
# create table temperature (id integer,tempfloat,datetext);
#sensorID = 1;
#type = 'door';
#zone = 'kitchen';
dbconnect = sqlite3.connect("lab4_p4.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
dbconnect.commit();
cursor.execute('SELECT * FROM sensors WHERE zone = "kitchen"');
for row in cursor:
	print(row['sensorID'], row['type'], row['zone']);
cursor.execute('SELECT * FROM sensors WHERE type = "door"');
for row in cursor:
        print(row['sensorID'], row['type'], row['zone']);
dbconnect.close();

