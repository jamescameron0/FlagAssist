#I used this python program to quickly print all the following countries into a txt file
#the txt file was then used to depict which recognized countries were not present in the 
#data extracted from the API

countries = [
    "China", "India", "United States", "Indonesia", "Pakistan", "Brazil", "Nigeria", 
    "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt", 
    "Vietnam", "DR Congo", "Turkey", "Iran", "Germany", "Thailand", "United Kingdom", 
    "France", "Italy", "Tanzania", "South Africa", "Myanmar", "Kenya", "South Korea", 
    "Colombia", "Spain", "Uganda", "Argentina", "Algeria", "Sudan", "Ukraine", "Iraq", 
    "Afghanistan", "Poland", "Canada", "Morocco", "Saudi Arabia", "Uzbekistan", "Peru", 
    "Angola", "Malaysia", "Mozambique", "Ghana", "Yemen", "Nepal", "Venezuela", 
    "Madagascar", "Cameroon", "Côte d'Ivoire", "North Korea", "Australia", "Niger", 
    "Sri Lanka", "Burkina Faso", "Mali", "Romania", "Malawi", "Chile", "Kazakhstan", 
    "Zambia", "Guatemala", "Ecuador", "Syria", "Netherlands", "Senegal", "Cambodia", 
    "Chad", "Somalia", "Zimbabwe", "Guinea", "Rwanda", "Benin", "Burundi", "Tunisia", 
    "Bolivia", "Belgium", "Haiti", "Cuba", "South Sudan", "Dominican Republic", 
    "Czech Republic (Czechia)", "Greece", "Jordan", "Portugal", "Azerbaijan", "Sweden", 
    "Honduras", "United Arab Emirates", "Hungary", "Tajikistan", "Belarus", "Austria", 
    "Papua New Guinea", "Serbia", "Israel", "Switzerland", "Togo", "Sierra Leone", 
    "Laos", "Paraguay", "Bulgaria", "Libya", "Lebanon", "Nicaragua", "Kyrgyzstan", 
    "El Salvador", "Turkmenistan", "Singapore", "Denmark", "Finland", "Congo", 
    "Slovakia", "Norway", "Oman", "State of Palestine", "Costa Rica", "Liberia", 
    "Ireland", "Central African Republic", "New Zealand", "Mauritania", "Panama", 
    "Kuwait", "Croatia", "Moldova", "Georgia", "Eritrea", "Uruguay", "Bosnia and Herzegovina", 
    "Mongolia", "Armenia", "Jamaica", "Qatar", "Albania", "Lithuania", "Namibia", 
    "The Gambia", "Botswana", "Gabon", "Lesotho", "North Macedonia", "Slovenia", 
    "Guinea-Bissau", "Latvia", "Bahrain", "Equatorial Guinea", "Trinidad and Tobago", 
    "Estonia", "Timor-Leste", "Mauritius", "Cyprus", "Eswatini", "Djibouti", "Fiji", 
    "Comoros", "Guyana", "Bhutan", "Solomon Islands", "Montenegro", "Luxembourg", 
    "Suriname", "Cabo Verde", "Micronesia", "Maldives", "Malta", "Brunei", "Belize", 
    "Bahamas", "Iceland", "Vanuatu", "Barbados", "Sao Tome & Principe", "Samoa", 
    "Saint Lucia", "Kiribati", "Grenada", "St. Vincent & Grenadines", "Tonga", 
    "Seychelles", "Antigua and Barbuda", "Andorra", "Dominica", "Marshall Islands", 
    "Saint Kitts & Nevis", "Monaco", "Liechtenstein", "San Marino", "Palau", "Tuvalu", 
    "Nauru", "Holy See"
]

with open('countries.txt', 'w') as file:
    for country in countries:
        file.write(country + '\n')