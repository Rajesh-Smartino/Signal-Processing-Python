import subprocess
import sys

BINARY = './subprocess'

punc = '!()-[]{};''"":\,<>./?@#$%^&*_~'

if len(sys.argv) != 2:
	print('Usage: <program_name> <input_file>')
	sys.exit(-1)
	
try:
	with open(sys.argv[1]) as file:
		test_str = file.read()
		
		for ele in test_str:
			if ele in punc:
				test_str = test_str.replace(ele, "")
		
		print("The string after filter: \n"+test_str)
		
		words = test_str.split(" ")
		
		for word in words:
			inputstr = word
			foo = inputstr.split()
			for x in foo:
				cmd = BINARY+' '+x.strip()
				subprocess.run(cmd.split())

except FileNotFoundError as fnf_error:
	print(fnf_error)
			