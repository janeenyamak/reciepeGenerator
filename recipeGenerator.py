
###
### This file parces through the json object that we generated through the Flask application 
### and we store the necessary information we need from it so we can then use it in our Desktop 
### application
###

import requests
import json
def listOfRecipe(ingredients):

  results =[]

  #grabs recieps given the following ingridents
  recipes = requests.get("http://www.recipepuppy.com/api/?i={},garlic&p=20".format(ingredients)).content #grabs the data from the specified url
  recipes = recipes.decode('utf-8') #converts bytes to json format
  recipes = json.loads(recipes) #converts JSON string to a dictionary
  

  #look through the Dictionary and grab the necessary data we need from the API and make our own payload
  for recipe in recipes['results']:
    newRecipe = {} #creates a new dictionary
    #adds the title , ingrideints, the link to the website, and the pictiure to the dictionary object
    newRecipe['title'] = recipe['title'].rstrip()
    newRecipe['ingredients'] = list(recipe['ingredients'].split(","))
    newRecipe['linkToWebsite'] = recipe['href']
    newRecipe['picture'] = recipe['thumbnail']
    #then add to our list of recipes so we can reference it later.
    results.append(newRecipe)

  #return the list of reciepes that we generated
  return results