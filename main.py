#SENDING A POST REQUEST:        curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/ -d '{"ingredients":"chicken, tomatoes"}'

#SAMPLE PAYLOAD:                
#                   [
#                     {
#                       "ingredients": "chicken, mint, garlic, cucumber, tzatziki, shallot", 
#                       "linkToWebsite": "http://www.recipezaar.com/Chicken-Tzatziki-246418", 
#                       "picture": "http://img.recipepuppy.com/299622.jpg", 
#                       "title": "Chicken Tzatziki"
#                      }
#                    ]

from flask import Flask, request,json, jsonify
import requests
from recipeGenerator import listOfRecipe

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def api_root():
  if request.headers['Content-Type'] =='application/json':
    ingredients = request.json 

    return jsonify(listOfRecipe(ingredients['ingredients']))
  
if __name__ == '__main__':
  app.run()

  
