
# Select count(*) from customer where ID is Null 

tables= ['Cutomer','orders','products','prices']
columns = ['ID','Creation date']

for t in tables:
    for c in columns:
        print (f'Select count(*) From {t} where {c} IS NULL;')