#!/usr/bin/env python3

device_name = input("Введите имя устройства: ") 
feature = input("Введите параметр устройства: ")
#a = device_name

london_co = { 
        'r1': {
             'location': '21 New Globe Walk',
             'vendor': 'Cisco',
             'model': '4451',
             'ios': '15.4',
             'ip': '10.255.0.1'
            },
        'r2': {
             'location': '21 New Globe Walk',
             'vendor': 'Cisco',
             'model': '4451',
             'ios': '15.4',
             'ip': '10.255.0.2'
            },
         'sw1': {
             'location': '21 New Globe Walk',
             'vendor': 'Cisco',
             'model': '3850',
             'ios': '3.6.XE',
             'ip': '10.255.0.101',
             'vlans': '10,20,30',
             'routing': True
    }
}


#device_name = input("Введите имя устройства: ")
#a = device_name
print('\n' + '-' * 30)  
print(london_co[device_name][feature])

