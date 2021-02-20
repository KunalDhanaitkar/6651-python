# Assignment 4 - (Program 4) - Program to generate a shorten URL.
# Name: Kunal Dhanaitkar
# UNH ID: 00722835
# Major: Computer Science
# Course: 6651-02; Introduction to Script Programming/Python.
# Submitted to: Professor Gulnora Nurmotova

# Module to generate pseudo-random numbers
import random

# URL to convert to a shorten URL.
url = input("Enter the URL: ")

# Declaring class which contains 2 functions. A function to generate a shoten url. Another to use that shorten url to get back the original url.
class url_short:

    # Function to convert the long URL into a bunch of random numbers and add it to a base url.
    def shorten_url(self, longUrl: str) -> str:
        self.urls = {}    # Behaves like a database.
        x = random.randint(0, 1000000000)
        if x not in self.urls:
            self.urls[x] = longUrl
        else:
            x = random.randit(1000000000, 10000000000000)
            self.urls[x] = longUrl
        shortened_url = "http://encryptedurl.com/" + str(x)
        return shortened_url

    # Function which receives the encrypted url and converts it to the original url.
    def original_url(self, shortUrl: str) -> str:
        return self.urls[int(shortUrl[24:])]

# Calling the class we defined earlier.
url_short = url_short()
print("The Original URL: ", url)
print("The shortened URL = ", url_short.shorten_url(url))
print("Decrypting the shortened url to get the original url: ",url_short.original_url(url_short.shorten_url(url)))

"""

Comparing all the Methods that can generate a Short URL.

 1) uuid - UUID is 36 characters. it is way too long for the intended usage i.e., think about putting the url into Twitter. UUID is already 1/4 into 140 chars limit. It generates ids that are unique across every table, every database and every server. It generates IDs anywhere, instead of having to roundtrip to the database. However, it is a bit cumbersome to debug.

 2) timestamp - If we use the timestamp, then we are limiting the characters we can use for generating the shortel URL from 26+10(letters and digits) to 10(digits only), thus the length of the shorter URL will have to be longer comppared to a URL shortener algorithm that uses both letter and numbers, for the same total number of URL conversions. It just gives a way to generate unique encoding withouth random numbers as time always changes. It has a high collision ratio.

 3) MD5 hash - This hash function accepts sequence of bytes and returns 128 bit hash value, usually used to check data integrity but has security issues. Its fast and presents a extremely low collision ratio but it is mainly used to check data integrity only.

 4) Random method - This program uses randint to map each url to a random integer 1 and 10^10. It is not an optimal solution for real world problems. This program produces a random string using rand function for short URL. It checks to make sure the number hasn't been used already. If it has been used already, it finds another random integer between 1 and 10^10.

"""