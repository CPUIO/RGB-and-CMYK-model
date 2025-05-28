import sys
import json

def main():
	if sys.argv[1] == "rgb":
		cmyk = json.loads(sys.argv[2].replace("(", "[").replace(")", "]"))
		rgb = "#"
		for i in range(3):
			ii = hex(int(255*(1-(cmyk[i]/100))*(1-(cmyk[3]/100))))[2:]
			rgb += "0"*(2-len(ii))+ii
		print(rgb)

	elif sys.argv[1] == "cmyk":
		rgb = sys.argv[2]
		cmy = []
		for i in range(1,6,2):
			cmy.append(int(rgb[i:i+2],16)/255)
		black = 1 - max(cmy)
		if black == 1:
			cmyk = (0,0,0,100)
		else:
			cmyk = ( round((1 - cmy[0] - black) / (1 - black) * 100),
			round((1 - cmy[1] - black) / (1 - black) * 100),
			round((1 - cmy[2] - black) / (1 - black) * 100),
			round(black * 100))

		print(cmyk)
	else:
		print("Введён неправильный флаг преобразования!")
		exit(1)

if __name__=="__main__":
	main()
