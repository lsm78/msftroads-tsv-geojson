#convert microsoft roads .tsv file to .geojson file
import re

#read tsv file
with open("file.tsv", r) as tsvfile:
	with open("file.geojson", w) as geojsonfile:
		for line in tsvfile:
			#Delete everything before the first curly brace
			filecontent = re.sub(r'^.*?{', '{', line)

			#Write line to a new text file
			geojsonfile.write(fileContent)

print("geojson file is ready")