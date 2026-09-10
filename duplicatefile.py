# check whether the filename appears more than once

file_list = ['report.csv', 'data.xslx', 'summary.docs', 'report.csv','data.csv']

has_duplicate = len(file_list) != len(set(file_list))

print("Are there duplicates filename?:", has_duplicate)



for file in file_list:
    if file_list.count(file) >1:
        print('duplicate file found:',{file} )
        continue
    else:
        print('no duplicates file found')
        
