import requests


def main(): 
	fi = open("in.txt", "r")
	fo = open("out.txt", "a+")
	if fi.mode == 'r':
		lines = fi.readlines()
		for line in lines:
			try:
				url = "https://www.apple.com" + line.rstrip()
				print(url)
				r = requests.head(url)
				print(r.status_code)
				if r.status_code == 200:
					fo.write(url + "\n")
			except requests.ConnectionError:
				print("Failed to connect")
		fi.close()


if __name__ == "__main__":
	main()
