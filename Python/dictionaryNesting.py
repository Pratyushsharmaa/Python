# nesting dictionary in a dictionary

travel_log_dict = {
  'India': {'cities_visited': ['Delhi', 'Mumbai', 'Bangalore'], 'total_visits':5},
  'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits':12},
}
print (travel_log_dict)

# nesting dictionary in a list

travel_log_list = [
  {
    'country': 'India',
    'cities_visited': ['Delhi', 'Mumbai', 'Bangalore'],
    'total_visits':5
  },
  {
    'country': 'France',
    'cities_visited': ['Paris', 'Lille', 'Dijon'],
    'total_visits':12,
  }
]

print(travel_log_list)
