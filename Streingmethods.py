#extract the character 

hello="Ghimire"



print(hello[2])

date = "2026-09-7"
print(date[ :4])


#extract MOnth

print(date[5:7])

Messydata= "968-Maria, ( D@t@ Engineer );; 27y  "
print(len(Messydata))
name= "Maria"
role = "Data Engineer" 
age=27

Cleandata =( Messydata.replace("-"," ").replace("968","name:").replace ("-"," ").replace(","," |").replace("(","role:")
.replace("@","a").replace(")"," ").replace (";;","| age:").replace("y "," " ))
print(len(Cleandata))
Cleandatas=Cleandata.lower().strip()
print(len(Cleandatas))

