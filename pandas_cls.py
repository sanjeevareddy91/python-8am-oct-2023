# Pandas -- pip install pandas


# filteration
# analysis of data 

import pandas 

# data = ["Ramesh","Suresh","Mahesh","venkatesh",'rajesh','subash','vignesh']

# info = pandas.DataFrame(data)

# print(info)

# print(type(info))

# dict1 = {
#     "teams":["CSK","RCB","MI","LSG"],
#     "players":["Dhoni","Kohli","Rohit","Rahul"]
# }

# info = pandas.DataFrame(dict1)

# print(info)

# print(type(info))

# read_csv
# read_excel
# read_json
csv_data = pandas.read_csv('sample_data.csv')

# print(csv_data)

# print(csv_data.loc[0:2]) # row based access.

# print(csv_data.loc[[0,1,4]])

# print(csv_data['name']) # column based access

# print(csv_data)

info = csv_data[csv_data['city']=='Hyderabad']

print(info)

# info.to_csv("filtered_data.csv",index=False)

info.to_excel('sample.xlsx',index=False)

info.to_json('sample_info.json',index=False,indent=4,orient='records')