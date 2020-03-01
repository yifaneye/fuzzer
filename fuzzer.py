import requests


def main(): 
	fo = open("edu.txt", "a+")
	for i in range(100000, 10000000):
		try:
			url = "https://www.apple.com/au_edu_" + str(i) + "/shop"
			r = requests.head(url)
			print(url + " " + str(r.status_code))
			if r.status_code != 404:
				fo.write(url + "\n")
		except requests.ConnectionError:  # print("Failed to connect")
			continue


if __name__ == "__main__":
	main()
