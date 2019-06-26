#!/usr/bin/env python

vvod = input("Введите ip адрес в формате ip/mask: ")

vvod.split("/")
ip = vvod.split("/")[0]
mask = vvod.split("/")[1]

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
ip_split = ip.split(".")

a = ip_split[0]
b = ip_split[1]
c = ip_split[2]
d = ip_split[3]

oct1 = int(a)
oct2 = int(b)
oct3 = int(c)
oct4 = int(d)

mask_split = mask_output.split(".")

a_m = mask_split[0]
b_m = mask_split[1]
c_m = mask_split[2]
d_m = mask_split[3]

m1 = int(a_m)
m2 = int(b_m)
m3 = int(c_m)
m4 = int(d_m)

print(f'''
     IP address:

     {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}

     {oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}

     Mask:

     /{mask}

     {m1:<8} {m2:<8} {m3:<8} {m4:<8}

     {m1:<08b} {m2:<08b} {m3:<08b} {m4:<08b}

      ''')


