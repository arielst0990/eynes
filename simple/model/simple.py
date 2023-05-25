import random  # import the random module to generate random ages

# define function to generate a list of people with random ages
def generate_people_list():
    people_list = []   # create an empty list to store people
    for i in range(10):   # iterate 10 times
        person = {   # create a dictionary to represent a person
            'id': i + 1,   # assign each person an ID number starting from 1
            'age': random.randint(1, 100)   # generate a random age between 1 and 100
        }
        people_list.append(person)   # add the person to the list
    return people_list   # return the completed list of people


# define function to order a list of people by age
def order_people_list(people_list):
    ordered_list = sorted(people_list, key=lambda x: x['age'], reverse=True)
    # sort the list of people by age in descending order, using a lambda function as the sorting key
    # which returns the value of the 'age' key in each dictionary
    youngest_person_id = ordered_list[-1]['id']   # get the ID of the person with the lowest age (at the end of the sorted list)
    oldest_person_id = ordered_list[0]['id']   # get the ID of the person with the highest age (at the beginning of the sorted list)

    print("ID of the youngest person:", youngest_person_id)   # print the ID of the youngest person
    print("ID of the oldest person:", oldest_person_id)   # print the ID of the oldest person

    return ordered_list   # return the ordered list of people


# generate a list of people with random ages
people = generate_people_list()

# order the list of people by age and print the results
ordered_people = order_people_list(people)
print("List:", ordered_people)
