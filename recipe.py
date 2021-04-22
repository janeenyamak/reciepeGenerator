### This Program will generate the GUI of our application 
### INPUT: List of ingredients
### OUTPUT: A single image

from io import BytesIO
from PIL import Image, ImageTk
import requests
import tkinter as tk
import webbrowser
import random

WINDOW_TITLE = "Recipe App"
WIDTH = 250
HEIGHT = 200

class RecipeApp(object):

    def __init__(self):

        self.window = tk.Tk()
       
        # Auto resize geometry
        self.window.geometry("")
        self.window.configure(bg="#00274C")
        self.window.title(WINDOW_TITLE)

        #Creating a Bar for a user to enter in a list of ingredients 
        self.search_label = tk.Label(self.window, text = "Ingredients:", bg = "#FF7900")
        self.search_label.grid(column = 0, row = 0, padx=5)

        self.search_entry = tk.Entry(master = self.window, width = 40)
        self.search_entry.grid(column = 1, row = 0, padx=5, pady = 10)

        #A button that will then send a POST request to the server 
        self.search_button = tk.Button(self.window, text = "Generate A Recipe", highlightbackground = "#FF7900",
            command = self.search_query)
        self.search_button.grid(column = 2, row = 0, padx = 5)

       
    #This function shall send a POST request to our server and return a list of recipes 
    def search_query(self):

        query = self.search_entry.get()
        print("query, ", query, "\n")
        url = 'http://127.0.0.1:5000/'
        recipes = requests.post(url, json={'ingredients': query})
        recipes = recipes.json()

        #randomly choses a reciepe form the list of reciepes
        recipe = random.choice(recipes)

        #Grab the picture and a link to the website
        if recipe:
            recipeImage = recipe['picture']
            recipeUrl = recipe['linkToWebsite']

        #If No recipe was found
        else:
            # Recipe not found
            recipeImage = "https://www.mageworx.com/blog/wp-content/uploads/2012/06/Page-Not-Found-13.jpg"
            recipeUrl = ""

        #Then print the image and the list of ingredients 
        self.printImage(recipeImage)
        self.getIngredients(recipe)

        #When you click on the "Recipe Link" button, the button will take you to the recipe url
        def openLink():
            webbrowser.open(recipeUrl)

        self.recipeButton = tk.Button(self.window, text = "Recipe Link", highlightbackground = "#FF7900",
            command = openLink)
        self.recipeButton.grid(column = 1, row = 7, pady = 10)

    
    #Image will be displayed on our UI
    def printImage(self, imageUrl):
        #grabs the url
        response = requests.get(imageUrl)
        
        img = Image.open(BytesIO(response.content))
        img = img.resize((WIDTH, HEIGHT))
        image = ImageTk.PhotoImage(img)
        
        holder = tk.Label(self.window, image = image)
        holder.photo = image
        holder.grid(column=1, row=6, pady=10)
    

    #Grabs the set of ingredients from the POST request and displays it in a list 
    def getIngredients(self, recipe):
        ingredients = tk.Text(master = self.window, height = 15, width = 50, bg = "#FF7900")
        ingredients.grid(column=1,row=4, pady = 10)
        ingredients.delete("1.0", tk.END) 

        print('ingredients: ' , ingredients)
        
        #if No Ingredients were found
        if recipe['ingredients'] == None :
            ingredients.insert(tk.END, "No Recipe found for search criteria")
            return
    
        ingredients.insert(tk.END, "\n" + recipe['title'] + "\n")
        for ingredient in recipe['ingredients']:
            ingredients.insert(tk.END, "\n- " + ingredient)

    #Run app until it is closed by user
    def runApp(self):
        self.window.mainloop()
        return
      

# Create App and run the app
if __name__ == "__main__":
    
    recipe = RecipeApp()
    recipe.runApp()
  