import requests  # importing requests for accessing API
import random 
import tkinter as tk
from PIL import Image, ImageTk
import io


def get_country_flags():
    
    with open('countries.txt', 'r') as file:    #allowed countries from txt file
        allowedCountries = {line.strip() for line in file if line.strip()}

    name_corrections = {
        "Cape Verde": "Cabo Verde",
        "Ivory Coast": "Côte d'Ivoire",
        "Gambia": "The Gambia",
        "São Tomé and Príncipe": "Sao Tome and Principe"
    }

    url = "https://restcountries.com/v3.1/all"  # URL for the RestCountries API containing all country data
    getCountries = requests.get(url)
    
    if getCountries.status_code == 200:  # Successful request, returned data correctly

        countriesData = getCountries.json()  # Using JSON to convert data into Python data structure for simpler readability

        flags = {}
        foundCountries = set()  # Using a set to keep track of countries in the txt file found in the API data

        for country in countriesData:

            commonName = country['name']['common']

            
            if commonName in name_corrections: # Applying name corrections
                commonName = name_corrections[commonName]

            if 'flags' in country and commonName in allowedCountries:

                flag_url = country['flags']['png']  #retreiving flags image links as png
                flags[commonName] = flag_url    #storing flags url in dictionary with country name as key
                foundCountries.add(commonName)

        missingCountries = allowedCountries - foundCountries #used for determing which countries are missing from the API list, or have different names
                                                             
        return flags, missingCountries

    else:
        print("Data was not collected from RestCountries API.")
        return {}

flagsAndLinks, missingCountry = get_country_flags()
 
#print("Num of countries:", len(flagsAndLinks)) #to check all countries present


#CREATING THE GUI USING TKINTER

correct_country_name = ""

def display_random_flag():

    global correct_country_name, submission_locked

    country_name = random.choice(list(flagsAndLinks.keys()))    # picking random country and getting its URL
    flag_url = flagsAndLinks[country_name]
    correct_country_name = country_name

    response = requests.get(flag_url)  # fetching the image from the URL
    
    img = Image.open(io.BytesIO(response.content)) #response outputs a byte string, processes the binary stream into an image
    img = img.resize((400, 250), Image.Resampling.LANCZOS)  # Resizing with LANCZOS
    img_tk = ImageTk.PhotoImage(img)  # Convert the image for tkinter

    flag_label.config(image=img_tk)
    flag_label.image = img_tk  # Keep a reference to avoid garbage collection
    
    entry_box.grid(row=2, pady=10)
    submit_button.grid(row=3, pady=10)

    next_flag_button.grid_remove() # Hide the "Next Flag" button

    country_label.config(text="")
    
    submission_locked = False #to prevent enter key from being spammed

def submit_answer():

    global submission_locked

    if submission_locked:
        return  # Ignore further submissions if already submitted to prevent spamming

    user_text = entry_box.get().strip() # Retrieve the user's answer from the entry box

    if user_text.lower() == correct_country_name.lower():
        country_label.config(text=f"Correct! The country is {correct_country_name}")
    else:
        country_label.config(text=f"Incorrect. The country was {correct_country_name}")

    entry_box.delete(0, tk.END)

    submission_locked = True

    entry_box.grid_remove()
    submit_button.grid_remove()

    next_flag_button.grid(row=4, pady=20)

def on_enter_key(event):
    submit_answer()

def on_space_key(event):
    display_random_flag()  # Call display_random_flag when space is pressed


# Set up the main application window
root = tk.Tk()
root.title("Country Flag Quiz")

# Create labels for flag and country name
flag_label = tk.Label(root, font=("Helvetica", 16), text="Press 'Show Flag' to start")
flag_label.grid(row=0, pady=20)

country_label = tk.Label(root, font=("Helvetica", 16))
country_label.grid(row=1, pady=20)

# Entry box for user's answer
entry_box = tk.Entry(root, font=("Helvetica", 16), width=30)

entry_box.bind("<Return>", on_enter_key) 

submit_button = tk.Button(root, text="Submit Answer, (enter)", command=submit_answer, font=("Helvetica", 14))

next_flag_button = tk.Button(root, text="Show Next Flag, (space bar)", command=display_random_flag, font=("Helvetica", 14))

next_flag_button.bind("<space>", on_space_key)

display_random_flag() #display flag when launched

root.mainloop() 