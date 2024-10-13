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

def display_random_flag():
    
    country_name = random.choice(list(flagsAndLinks.keys()))    # picking random country and getting its URL
    flag_url = flagsAndLinks[country_name]

    response = requests.get(flag_url)  # fetching the image from the URL
    
    img = Image.open(io.BytesIO(response.content)) #response outputs a byte string, processes the binary stream into an image
    img = img.resize((400, 250), Image.Resampling.LANCZOS)  # Resizing with LANCZOS
    img_tk = ImageTk.PhotoImage(img)  # Convert the image for tkinter

    flag_label.config(image=img_tk)
    flag_label.image = img_tk  # Keep a reference to avoid garbage collection
    country_label.config(text=country_name)

# Set up the main application window
root = tk.Tk()
root.title("Random Country Flag")

# Create labels for flag and country name
flag_label = tk.Label(root)
flag_label.pack(pady=20)

country_label = tk.Label(root, font=("Helvetica", 16))
country_label.pack(pady=20)

# Button to show a random flag
show_button = tk.Button(root, text="Show Random Flag", command=display_random_flag)
show_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()