import string

oldstr ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new = ""
for i in oldstr:
    if i >= 'a' and i <= 'x':
        new += chr(ord(i) + 2)
    elif i >= 'y' and i <= 'z':
        new += chr(ord(i) - 24)
    else:
        new += i
print new

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
tran = string.maketrans(intab,outtab)
print string.translate("map",tran,"");

