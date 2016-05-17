# App 5: Weather client app

![image](app-5-screenshot.png)

If you want to try this yourself, try to build the interactive app above. 

The WHITE text is output from the program. The YELLOW input is what the users types.

This application will ask the user for their zip code. Then you will use this zip code, the requests and beautiful soup 4 PyPI packages to download a weather web page, scrape out the relevant info and display it back on the console.

Key concepts introduced
=================

**Python Package Index (PyPI)**

[https://pypi.python.org/pypi](https://pypi.python.org/pypi)

**pip**

    pip3 list
    pip3 install requests

**Requests package**

Quick start: [http://docs.python-requests.org/en/master/user/quickstart/](http://docs.python-requests.org/en/master/user/quickstart/)

**Beautiful soup package**

Quick start: [http://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

**tuples**

    # Create a tuple
    m = (22.5, 44.234, 19.02, 'strong')

**namedtuples**

    import collections
    
    # Define a named tuple 'type'
    Measurement = collections.namedtuple('Measurement', 
        long=19.02, quality='strong')