import matlab.engine
import sys

eng = matlab.engine.start_matlab()

def magic(n):
	m = eng.magic(int(n))
	print(m)

if __name__ == "__main__":
	magic(sys.argv[1])