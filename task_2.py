print("UNITS CONVERION FOR ENERGY")
print("Available units joules,kilojoule,megajoules")
conversion1=input("from:")
conversion2=input("to:")
energy=float(input("enter number:"))

if conversion1=="joules" and conversion2=="joules":
    print("converted value:",energy*1)
elif conversion1=="joules" and conversion2=="kilojoules":
    print("converted value:",energy/1000)
elif conversion1=="joules" and conversion2=="megajoules":
    print("converted value:",energy/1000000)
elif conversion1=="kilojoules" and conversion2=="joules":
    print("converted value:",energy*1000)
elif conversion1=="kilojoules" and conversion2=="kilojoules":
    print("converted value:",energy*1)
elif conversion1=="kilojoules"and conversion2=="megajoules":
    print("converted value:",energy/1000)
elif conversion1=="megajoules" and conversion2=="joules":
    print("converted value:",energy*1000000)
elif conversion1=="megajoules" and conversion2=="kilojoules":
    print("converted value:",energy*1000)
elif conversion1=="megajoules" and conversion2=="megajoules":
    print("converteed value:",energy*1)
else:
    print("invalid units")
