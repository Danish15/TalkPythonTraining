def main()
	print_the_header
	code = input('What zipcode do you want the weather for (97201)? ')
	print(code)

def print_the_header():
	print("------------------------------------")
	print("				WEATHER APP			   ")
	print("------------------------------------")


def get_html_from_web(zipcode):
	url = 'http"//www.wunderground.com/weather-forecast/{}'.format(zipcode)
	requests



if __name__ == '__main__':
	main()
