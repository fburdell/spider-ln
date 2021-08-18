# LinkedIn Scraper 

In learning about industry, I liked to learn about people. This is a simple LinkedIn spider that retrieves education and work history. It accepts three arguments : ```-n``` : number of profiles to find, ```-k``` : keywords with which to search profiles, and ```-g``` : accepting ```hless``` or ```head``` as arguments to indicate to the program to run WebBrowswer with or without head.

	 $ python3 spider.py -n 5 -k "financial analyst" -g hless 
	 $ ls out/
	 financial-analyst.csv

