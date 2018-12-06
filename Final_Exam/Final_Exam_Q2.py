
import quine_mccluskey
from tabulate import tabulate
import re
import sys

def read_file(filename):
	with open(filename) as f:
		lines = f.readlines()

	tt_vars = lines[0].strip().split('\t') + ["out"]

	tt = []
	for i in range(len(lines)-1):
		tt.append(lines[i+1].strip().split("\t"))

	return [tt_vars, tt]

def get_minterms(tt):
	minterms = []
	for r in tt:
		if r[-1] == '1':
			# print("Binary:", "".join(r[:-1]))
			conv_bin_2_int = int("".join(r[:-1]), 2)
			# print("Int:   ", conv_bin_2_int)
			minterms.append(conv_bin_2_int)

	return minterms



fn =  sys.argv[1]

variables, truth_table = read_file(fn)
print("\nTruth table from '{filename}' :".format(filename=fn))
print(tabulate(truth_table, headers=variables))

minterms = get_minterms(truth_table)

expression = quine_mccluskey.boolean_reduction(variables[:-1], minterms)

print("\nExpression:", expression)

# Remove all characters that are not alphabets from expression
# to determine how many components there will be in output file
regex = re.compile('[^a-zA-Z]')
number_of_components = len(regex.sub('', expression))

expression = list(filter(None, expression.split(" ")))

output_file = ""

print("output file:", output_file)

node = 1

for i, element in enumerate(expression):
        if "'" in element:
                expression[i] = "!" + expression[i].replace("'", "")

        if expression[i] != "+":
                output_file += expression[i] + "\t" + str(node) + "\t" + str(node+1) + "\n"

        if i < len(expression)-1:
                if expression[i+1] == "+":
                        node += 1

output_file = output_file.replace("1", "0").replace(str(node+1), "1")

output_file = str(number_of_components) + "\n" + output_file

print()
print(output_file)

# Write output file
if ".bool" in fn:
	output_fn = fn.replace(".bool", ".cir")
elif ".txt" in fn:
	output_fn = fn.replace(".txt", ".cir")

print("Writing data to:", output_fn)

with open(output_fn, 'w') as f:
        f.write(output_file)




