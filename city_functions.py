def form_city_country(city,country,population=''):
    """ prints in specific format """
    if population:
        format = f"{city}, {country} - population {population}"
    else:
        format = f"{city}, {country}."
    return format.title()

#ct_cnt = form_city_country(city = 'Santiago', country = 'chile', population = 50000)
#print(ct_cnt)
