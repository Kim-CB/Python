# Day 16 - Intermediate - Object Oriented Programming (OOP) 

# from turtle import Screen, Turtle

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.align = "l"
# table.add_rows(
#     [
#         ["Pikachu", "Eletric+"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"]
#     ]
# )
# print(table)
# Made some "web scraping with PrettyTable"
from bs4 import BeautifulSoup
from html_poke import html_doc
from prettytable import PrettyTable

# 1. Initializae the BeatifulSoup parser and PrettyTable
soup = BeautifulSoup(html_doc,'html.parser')
table = PrettyTable()

# 2. Set up the table headers and alignment
table.field_names = ["#", "Pokemon Name", "Type(s)", "Total Stats"]
table.align = "l"

# 3. Ask the user what type they want to search for
# .strip() removes accidental spaces, and .title() ensures it matches the HTML ("fire" becomes "Fire")
request_type = input("What type of Pokemon do you want to see? (e.g., Fire, Water, Grass) ").strip().title()

# 4. Find the main pokedex table and isolate all the rows (<tr>) in the body (<tbody>)
pokedex_table = soup.find('table', id='pokedex')
rows = pokedex_table.find('tbody').find_all('tr')

found = False

# 5. Loop through every row to extract the data
for row in rows:
    # Get all the cells (<td>) in the current row
    cells = row.find_all('td')

    # Extract the ID and Name
    poke_id = cells[0].find('span', class_='infocard-cell-data').text.strip()
    poke_name = cells[1].find('a', class_='ent-name').text.strip()

    # Extract the types. Since some Pokemon have two types, we find all 'a' tags with the class 'type-icon'
    type_tags = cells[2].find_all('a', class_='type-icon')
    poke_types = [t.text.strip() for t in type_tags]

    # 6. Check if the user's request type is in the Pokemon's list of types
    if request_type in poke_types:
        total_stats = cells[3].text.strip()
        # Add the matching Pokemon to the PrettyTable
        table.add_row([poke_id, poke_name, ", ".join(poke_types), total_stats])
        found = True

# 7. Print the results
if found:
    print(f"\nHere are the {request_type}-type Pokemon from Generation 1: ")
    print(table)
else:
    print(f"\nSorry, no Pokemon found with the type '{request_type}'. Make sure you spelled it correctly!")