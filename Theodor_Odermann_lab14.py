def get_number_values(file_name):
	number_values = []
	with open(file_name, "r") as file:
		for line in file:
			try:
				number_values.append(float(line.strip()))
			except ValueError:
				pass
	return number_values
	
def find_min(values, current_min=float('inf'), index=0):
	if index == len(values):
		return current_min
	else:
		if values[index] < current_min:
			current_min = values[index]
		return find_min(values, current_min, index + 1)

def find_max(values, current_max=float('-inf'), index=0):
	if index == len(values):
		return current_max
	else:
		if values[index] > current_max:
			current_max = values[index]
		return find_max(values, current_max, index + 1)

def extrema(values, include_min=True, include_max=True):
	result = []
	if include_min == True:
		min_val = find_min(values)
		result.append(min_val)
	if include_max == True:
		max_val = find_max(values)
		result.append(max_val)
	return result
	
file_name = "randomValues.txt"
numeric_values = get_number_values(file_name)
extrema_max = extrema(numeric_values, False, True)
extrema_min = extrema(numeric_values, True, False)

print("Minimum:", extrema_min)
print("Maximum:", extrema_max)

	
