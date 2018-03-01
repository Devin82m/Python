# Translate
# Devin St. Clair 2018

from string import maketrans

alphabet = "abcdefghijklmnopqrstuvwxyz"
code = "cdefghijklmnopqrstuvwxyzab"

translation = maketrans (alphabet, code)

mess = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print mess.translate(translation)

urlMess = "map"

print urlMess.translate(translation)