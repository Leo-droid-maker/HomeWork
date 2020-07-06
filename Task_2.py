def get_person(name, surname, age, year, city, email, tel):
    return f'Name: {name}, Surname: {surname}, Age: {age}, Year: {year}, City: {city}, Email: {email}, Tel.№: {tel}'


print(get_person(name='Max', surname='Davidov', age=34, year='1986', city='Moscow', email='mail@email.com', tel='+79140'))
