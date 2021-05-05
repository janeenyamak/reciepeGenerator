### This Program will generate the GUI of our application 
### INPUT: List of ingredients
### OUTPUT: A single image

#Libraries necessary in order to run our application
from io import BytesIO
from PIL import Image, ImageTk
import requests
import tkinter as tk
import webbrowser
import random

#this will set up the window of our desktop appliction
WINDOW_TITLE = "Recipe App"
WIDTH = 250
HEIGHT = 200

class RecipeApp(object):

    def __init__(self):

        self.window = tk.Tk() #creates the window
       
        # Auto resize geometry
        self.window.geometry("")
        self.window.configure(bg="#00274C")
        self.window.title(WINDOW_TITLE)

        #Creating a Bar for a user to enter in a list of ingredients 
        self.search_label = tk.Label(self.window, text = "Ingredients:", bg = "#FF7900")
        self.search_label.grid(column = 0, row = 0, padx=5) #creates the grid of our window application

        self.search_entry = tk.Entry(master = self.window, width = 40) #this allows the user to enter text
        self.search_entry.grid(column = 1, row = 0, padx=5, pady = 10) # this assigns where the text box will be located on our desktop application

        #A button that will then send a POST request to the server 
        self.search_button = tk.Button(self.window, text = "Generate A Recipe", highlightbackground = "#FF7900",
            command = self.search_query)
        self.search_button.grid(column = 2, row = 0, padx = 5) #this created the search button 

       
    #This function shall send a POST request to our server and return a list of recipes 
    def search_query(self):

        ##this will query the instructions for you
        query = self.search_entry.get()
        print("query, ", query, "\n")
        url = 'http://127.0.0.1:5000/' #this is this localhost that we used to connect to the server
        recipes = requests.post(url, json={'ingredients': query}) #this grabs a json object of our instructions
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

        #This created the Recipe Link Button which allows the user to actually visit the webiste
        self.recipeButton = tk.Button(self.window, text = "Recipe Link", highlightbackground = "#FF7900",
            command = openLink)
        self.recipeButton.grid(column = 1, row = 7, pady = 10) #Assigns the button on the grid our our desktop application

    
    #Image will be displayed on our UI
    def printImage(self, imageUrl):
        #grabs the url
        response = requests.get(imageUrl)
        
        #opens the image, resizes the image and inserts it into our desktop application
        img = Image.open(BytesIO(response.content))
        img = img.resize((WIDTH, HEIGHT))
        image = ImageTk.PhotoImage(img)
        
        #Creates a Label of our image and displays it on our desktop application
        holder = tk.Label(self.window, image = image)
        holder.photo = image
        holder.grid(column=1, row=6, pady=10)
    

    #Grabs the set of ingredients from the POST request and displays it in a list 
    def getIngredients(self, recipe):
        ingredients = tk.Text(master = self.window, height = 15, width = 50, bg = "#FF7900") #This will show the text of ingreidents on the Screen
        ingredients.grid(column=1,row=4, pady = 10) #This aligns the text for you
        ingredients.delete("1.0", tk.END) 

        print('ingredients: ' , ingredients) #displays the ingreidents on the screen
        
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
  