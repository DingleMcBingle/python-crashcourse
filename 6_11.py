cities = {
    'Altoona': {
        'country':'USA',
        'population': '40k',
        'fact':'railroad boom town',
    },

    'Pittsburgh': {
        'country': 'USA',
        'population':'300k',
        'fact':'city of steel',
    },

    'Philadelphia': {
        'country': 'USA',
        'population': '1.6m',
        'fact': 'city of brotherly love',
    }
}

for name, info in cities.items():
    print("\nCity name: " + name)
    location = (info['country'])
    population = (info['population'])
    fun_fact = (info['fact'])

    print("\tLocation: " + location)
    print("\tPopulation: " + population)
    print("\tFun fact: " + fun_fact)