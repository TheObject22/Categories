category_file = open("hazards.tsv", "r")
lines = category_file.readlines()
categories = {'category': ['Unique_Sub_Categories']}
a_category = ""
b_subcategory = ""

for line in lines:
	a_category = line[:line.find('\t')]
	b_subcategory = line[line.find('\t'):line.find('\n')]

	a_category = a_category.lower()
	b_subcategory = b_subcategory.strip()
	b_subcategory = b_subcategory.lower()
	if a_category in categories:
		if b_subcategory not in categories[a_category]:
			categories[a_category].append(b_subcategory)
	else:
		categories[a_category] = [b_subcategory]

sortedKeys = []
for key in categories:
	sortedKeys.append(key)
	sortedKeys = sorted(sortedKeys)

largest_subcat_count= 0
largest_subcat = ""
for g in sortedKeys:
	print g, len(categories[g]), "\n"
	if largest_subcat_count < len(categories[g]):
		largest_subcat = g
		largest_subcat_count = len(categories[g])

print "Most Unique sub-categories: ", largest_subcat,"\n","Sub-Categories (Sorted Alphabetically): ",sorted(categories[largest_subcat])

	
	
