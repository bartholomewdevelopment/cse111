
interest_year = int(input('Enter the year of interest: '))

max_life = -1
min_life = 999999999
max_life_country = 0
max_life_year = 0
min_life_country = 0
min_life_year = 0
sum_interest_year_life = 0
count_interest_life = 0
max_country_year = ''
max_life_y = -1
min_life_y = 99999999
min_country_year = ''
with open('life-expectancy.csv') as file:

    next(file)
    for row in file:
        clean = row.strip()
        data = row.strip().split(',')
        country = data[0]  
        year = int(data[2])
        life = float(data[3])
        if life > max_life:
            max_life = life
            max_life_country = country
            max_life_year = year
        if life < min_life:
            min_life = life 
            min_life_country = country
            min_life_year = year
        if year == interest_year:
            sum_interest_year_life += life
            count_interest_life += 1
            average_life_year = sum_interest_year_life / count_interest_life
            if life > max_life_y:
                max_life_y = life
                max_country_year = country
            if life < min_life_y:
                min_life_y = life
                min_country_year = country

print()        
print(f'The overall max life expectancy is: {max_life} from {max_life_country} in {max_life_year}')
print(f'The overall min life expectancy is: {min_life} from {min_life_country} in {min_life_year}')
print()
print(f'For the year {interest_year}:')
print(f'The average life expectancy across all countries was {average_life_year:.2f}')
print(f'The max life expectancy was in {max_country_year} with {max_life_y}')
print(f'The min life expectancy was in {min_country_year} with {min_life_y}')




    