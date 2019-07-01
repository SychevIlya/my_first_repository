#!/usr/bin/env python 

vvod = input("Введите ip адрес в формате ip/mask: ")

a = vvod.split("/")
ip = a[0]
mask = a[1]

mask_dict = {
        "20": "255.255.224.0",
        "21": "255.255.248.0",
        "22": "255.255.252.0",
        "23": "255.255.254.0",
        "24": "255.255.255.0",
        "25": "255.255.255.128",
        "26": "255.255.255.192",
        "27": "255.255.255.224",
        "28": "255.255.255.248",
}

mask_output = mask_dict[mask]

mask_split = mask_output.split(".")

a_m = int(mask_split[0])
b_m = int(mask_split[1])
c_m = int(mask_split[2])
d_m = int(mask_split[3])

ip_split = ip.split(".")

oct1 = int(ip_split[0])
oct2 = int(ip_split[1])
oct3 = int(ip_split[2])
oct4 = int(ip_split[3])

net1 = a_m & oct1
net2 = b_m & oct2
net3 = c_m & oct3
net4 = d_m & oct4


print(f'''
    IP address:\n
    {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}\n
    {oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}\n
    Mask:\n
    /{mask}\n
    {a_m:<8} {b_m:<8} {c_m:<8} {d_m:<8}\n
    Network:\n
    {net1:<8} {net2:<8} {net3:<8} {net4:<8}\n
    {net1:08b} {net2:08b} {net3:08b} {net4:08b}\n
    ''')

