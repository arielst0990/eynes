# importing the necessary modules
import unittest
import sys
from unittest.mock import patch
sys.path.append("simple/model")
from simple import generate_people_list, order_people_list


# creating TestGeneratePeopleList class to test method which creates list of people and return a list
class TestGeneratePeopleList(unittest.TestCase):
    
    # testing the length of generated people list
    def test_list_length(self):
        people = generate_people_list()
        self.assertEqual(len(people), 10)

    # testing all ages in list are between 1 to 100
    def test_valid_age_range(self):
        people = generate_people_list()
        for person in people:
            self.assertGreaterEqual(person['age'], 1)
            self.assertLessEqual(person['age'], 100)


# creating TestOrderPeopleList class to test method which orders the list of people by age
class TestOrderPeopleList(unittest.TestCase):

    # defining people data for testing
    def setUp(self):
        self.people = [
            {'id': 1, 'age': 10},
            {'id': 2, 'age': 30},
            {'id': 3, 'age': 20},
            {'id': 4, 'age': 50}
        ]

    # testing if list is ordered based on age in descending order
    def test_ordering(self):
        ordered_people = order_people_list(self.people)
        self.assertNotEqual(ordered_people, self.people)
        self.assertEqual(len(ordered_people), len(self.people))
        for i in range(len(ordered_people) - 1):
            self.assertGreaterEqual(ordered_people[i]['age'], ordered_people[i+1]['age'])

    # testing if the ordering works correctly with people having similar age
    def test_same_age_ordering(self):
        self.people.append({'id': 5, 'age': 30})
        ordered_people = order_people_list(self.people)
        self.assertEqual(ordered_people[1]['id'], 2)
        self.assertEqual(ordered_people[2]['id'], 5)

    # testing if the print statements display correct data
    @patch('builtins.print')
    def test_output(self, mock_print):
        ordered_people = order_people_list(self.people)
        youngest_person_id = ordered_people[-1]['id']
        oldest_person_id = ordered_people[0]['id']
        expected_output = [
            'ID of the youngest person:'.format(youngest_person_id),
            'ID of the oldest person:'.format(oldest_person_id),
        ]
        for call_args, call_kwargs in mock_print.call_args_list:
            self.assertIn(call_args[0], expected_output)

    # testing if input list is not modified by the method
    def test_input_not_modified(self):
        input_copy = self.people.copy()
        order_people_list(self.people)
        self.assertEqual(input_copy, self.people)


# running all the tests in this module
if __name__ == '__main__':
    unittest.main()
