#!/usr/bin/env python3


access_template = ['switchport mode access',
                  'switchport access vlan {}',
                  'switchport nonegotiate',
                  'spanning-tree portfast',
                  'spanning-tree bpduguard enable']


intf = input("Введите номер интерфейса: ")
vlan = input("Введите номер влана: ")
print([intf, vlan])

access_str = '\n'.join(access_template)
print("interface {}".format(intf))
print(access_str.format(vlan))

