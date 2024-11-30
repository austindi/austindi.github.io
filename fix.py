import json 

with open('presentation_v1.json', 'r') as file:
    data = json.load(file)

#for i in data[ 'oral' a] ):
for i in  range(len(  data[ 'oral' ] ) ) :
    del  data[ 'oral' ][ i ][ 'authors' ] 

with open('pp.json', 'w') as file:
    json.dump(data, file, indent=4)

