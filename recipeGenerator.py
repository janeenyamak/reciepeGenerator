
import requests
import json
def listOfRecipe(ingredients):

  results =[]

  #grabs 10 recieps given the following ingridents
  recipes = requests.get("http://www.recipepuppy.com/api/?i={},garlic&p=20".format(ingredients)).content #grabs the data from the specified url
  recipes = recipes.decode('utf-8') #converts bytes to json format
  recipes = json.loads(recipes)
  

  for recipe in recipes['results']:
    newRecipe = {}
    newRecipe['title'] = recipe['title'].rstrip()
    newRecipe['ingredients'] = list(recipe['ingredients'].split(","))
    newRecipe['linkToWebsite'] = recipe['href']
    newRecipe['picture'] = recipe['thumbnail']
    results.append(newRecipe)

  return results