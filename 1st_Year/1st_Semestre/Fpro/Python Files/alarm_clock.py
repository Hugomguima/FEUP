import datetime
now = datetime.datetime.now()
print(now.strftime("%H:%M"))
houreight = now.hour+8
minutethirty = now.minute+30
if houreight>24 :
     houreight = houreight-24
if minutethirty>60:
     minutethirty = minutethirty-60
print(str(houreight)+":"+str(minutethirty))