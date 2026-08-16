capitals = {
    'France': 'Paris',
    'Spain': 'Madrid',
    'Italy': 'Rome',
    'Germany': 'Berlin',
    'Portugal': 'Lisbon'
    }

# Nested lists in a dictionary
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
    }

# Nested dictionaries
travel_log = {
    'France': {
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
        },
    'Germany': {
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
        }
}
# Accessing nested dictionaries
print(travel_log['France']['cities_visited'])  # Output: ['Paris', 'Lille', 'Dijon']
print(travel_log['Germany']['total_visits'])  # Output: 5
print(travel_log['Germany']['cities_visited'][1])  # Output: 'Hamburg'