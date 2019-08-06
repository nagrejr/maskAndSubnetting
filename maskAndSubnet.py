iptext=input()
checkclass=iptext[0:3]
cc=int(checkclass)
mask=''
if(cc>0 and cc<224):
    if(cc<128):
        mask="255.0.0.0"
    if(cc>127 and cc<192):
        mask="255.255.0.0"
    if(cc>191):
        mask="255.255.255.0"
print("Mask: ",mask)

networkAddr=""
ipAddrParts=iptext.split(".")
maskParts=mask.split(".")
for i in range(0,4):
    x=int(ipAddrParts[i])
    y=int(maskParts[i])
    z=x & y
    networkAddr=networkAddr + str(z) + "."
print("ADDRESS: "+networkAddr)
