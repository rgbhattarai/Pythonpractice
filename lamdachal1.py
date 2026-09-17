# Keep name of students only starting with letter M

Students =[['Maria', 85],
            ['Kumar', 90],
            ['Max', 70]] 


print(list((filter(lambda row: row [0].startswith('M'),Students))))