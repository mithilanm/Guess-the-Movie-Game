import urllib2
import json
import sys
from random import *

def ask():
    yes=set(["YES","yes","Yes","Y","y"])
    no=set(["NO","no","No","N","n"])
    again=raw_input("Again? (Y or N): ")
    if again in yes:
        main()
    else:
        sys.exit

def main():
    print("Guess the movie based on the descripton")
    movie=findMovie()
    guess(movie)
    ask()
    

def findMovie():
    url='https://api.themoviedb.org/3/trending/movie/day?api_key=f9c489da20f576c7921382713b49e924'
    json_obj=urllib2.urlopen(url)
    data=json.load(json_obj)
    count=0
    movie_list=[]
    description_list=[]
    for item in data['results']:
        count=count+1
        movie_list.append(item['title'])
        description_list.append(item['overview'])
    rand_num=randint(0,count-1)
    rand_title=movie_list[rand_num]
    rand_description=description_list[rand_num]
    print rand_description
    return rand_title

def guess(movie_title):
    guess=raw_input("What movie do you think it is?\n")
    if(guess==movie_title):
        print "Correct, you won!"
    else:
        print "That is incorrect, the movie was "+movie_title

main()
