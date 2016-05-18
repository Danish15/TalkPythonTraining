import requests
import bs4

def main():
	print_the_header
	code = input('What zipcode do you want the weather for (97201)? ')
	html = get_html_from_web(code)

	get_weather_from_html(html)


def print_the_header():
	print("------------------------------------")
	print("				WEATHER APP			   ")
	print("------------------------------------")


def get_html_from_web(zipcode):
	url = 'http:"//www.wunderground.com/weather-forecast/{}'.format(zipcode)
	response = requests.get(url)
	#print(response.text[0:250])

	return response.txt

def get_weather_from_html(html):
	soup = bs4.BeautifulSoup(html, 'html.parser')
	print(soup)




if __name__ == '__main__':
	main()
