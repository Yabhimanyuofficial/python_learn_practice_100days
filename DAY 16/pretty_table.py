from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["SL No.", "Pokemon Name", "Power"]
table.add_rows(
    [
        [1, "Balbasaur", "Poison"],
        [2, "Charmander", "Fire"],
        [3, "Squirtle", "Water"],
        [4, "Metapod", "Bug"],
        [5, "Blastoise", "Water"],
        [6, "Rattata", "Normal"],
        [7, "Arbok", "Poison"],
        [8, "Pikachu", "Electric"],
    ]
)
print(table)