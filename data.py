ADMIN_ACCOUNT = {
    'username': 'admin',
    'password': 'Admin.123',
}

# boundary
BOUNDARY_TESTCASE = {
    'test 1': 0,
    'test 2': 1,
    'test 3': 2,
    'test 4': 5000,
    'test 5': 9999,
    'test 6': 10000,
    'test 7': 10001,
}

BOUNDARY_EXPECT = {
    'test 1': 'Some settings were not changed due to an error.',
    'test 2': 'Changes saved',
    'test 3': 'Changes saved',
    'test 4': 'Changes saved',
    'test 5': 'Changes saved',
    'test 6': 'Changes saved',
    'test 7': 'Some settings were not changed due to an error.',
}

# equivalent classs
EQUIVALENT_CLASS_DATA = {
    'username': 'taikhoan.1',
    'password': 'Matkhau.1',
    'first name': 'A1',
    'surname': 'Bùi',
    'email': 'taikhoan.1@gmail.com'
}

EQUIVALENT_CLASS_TESTCASE = {
    'test 1': {'current': 'Matkhau',
               'new password': 'Matkhau.2', 'confirm': 'Matkhau.2'},
    'test 2': {'current': 'Matkhau.1',
               'new password': 'Matkhau.', 'confirm': 'Matkhau.'},
    'test 3': {'current': 'Matkhau.1',
                          'new password': 'Matkhau1', 'confirm': 'Matkhau1'},
    'test 4': {'current': 'Matkhau.1',
                          'new password': 'MATKHAU.1', 'confirm': 'MATKHAU.1'},
    'test 5': {'current': 'Matkhau.1',
                          'new password': 'matkhau.1', 'confirm': 'matkhau.1'},
    'test 6': {'current': 'Matkhau.1',
                          'new password': '123456', 'confirm': '123456'},
    'test 7': {'current': 'Matkhau.1',
               'new password': 'mMatkhau.2', 'confirm': 'Matkhau'},
}

EQUIVALENT_CLASS_EXCEPT = {
    'test 1': 'Invalid login, please try again',
    'test 2': 'Passwords must have at least 1 digit(s).',
    'test 3': 'The password must have at least 1 special character(s) such as as *, -, or #.',
    'test 4': 'Passwords must have at least 1 lower case letter(s).',
    'test 5': 'Passwords must have at least 1 upper case letter(s).',
    'test 6': '''Passwords must be at least 8 characters long.
Passwords must have at least 1 lower case letter(s).
Passwords must have at least 1 upper case letter(s).
The password must have at least 1 special character(s) such as as *, -, or #.''',
    'test 7': 'These passwords do not match'
}


# decision table
DECISION_TABLE_DATA = {
    'course': {'full name': 'Môn 4', 'short name': 'Môn 4'},
    'events': [
        {
            'name': 'project 1',
            'allow submission': {'day': 23, 'month': 11, 'year': 2022},
            'due date': {'day': 24, 'month': 11, 'year': 2022},
            'topic': 1,
        },
        {
            'name': 'project 2',
            'topic': 2,
        },
        {
            'name': 'project 3',
            'due date': {'day': 25, 'month': 12, 'year': 2022},
            'remind': {'day': 26, 'month': 12, 'year': 2022},
            'topic': 3,
        },
        {
            'name': 'project 4',
            'due date': {'day': 2, 'month': 2, 'year': 2023},
            'remind': {'day': 3, 'month': 2, 'year': 2023},
            'topic': 4,
        },
        {
            'name': 'project 5',
            'due date': {'day': 2, 'month': 5, 'year': 2023},
            'remind': {'day': 3, 'month': 5, 'year': 2023},
            'topic': 4,
        },
    ]
}

DECISION_TABLE_TESTCASE = {
    'test 1': {'filter': 'All', 'sort': 'Sort by dates'},
    'test 2': {'filter': 'Overdue', 'sort': 'Sort by dates'},
    'test 3': {'filter': 'Next 7 days', 'sort': 'Sort by dates'},
    'test 4': {'filter': 'Next 30 days', 'sort': 'Sort by dates'},
    'test 5': {'filter': 'Next 3 months', 'sort': 'Sort by dates'},
    'test 6': {'filter': 'Next 6 months', 'sort': 'Sort by dates'},
    'test 7': {'filter': 'All', 'sort': 'Sort by courses'},
    'test 8': {'filter': 'Overdue', 'sort': 'Sort by courses'},
    'test 9': {'filter': 'Next 7 days', 'sort': 'Sort by courses'},
    'test 10': {'filter': 'Next 30 days', 'sort': 'Sort by courses'},
    'test 11': {'filter': 'Next 3 months', 'sort': 'Sort by courses'},
    'test 12': {'filter': 'Next 6 months', 'sort': 'Sort by courses'},
}

DECISION_TABLE_EXPECT = {
    'test 1': ['project 1', 'project 2', 'project 3', 'project 4', 'project 5'],
    'test 2': ['project 1'],
    'test 3': ['project 2'],
    'test 4': ['project 2', 'project 3'],
    'test 5': ['project 2', 'project 3', 'project 4'],
    'test 6': ['project 2', 'project 3', 'project 4', 'project 5'],
    'test 7': ['project 1', 'project 2', 'project 3', 'project 4', 'project 5'],
    'test 8': ['project 1'],
    'test 9': ['project 2'],
    'test 10': ['project 2', 'project 3'],
    'test 11': ['project 2', 'project 3', 'project 4'],
    'test 12': ['project 2', 'project 3', 'project 4', 'project 5'],
}


# usecase 1
USECASE1_DATA = {
    'course 1': {'full name': 'Môn 1', 'short name': 'Môn 1'},
    'course 2': {'full name': 'Môn 2', 'short name': 'Môn 2'},
}

USECASE1_EXPECT = {
    'test 1': 'Môn 1',
    'test 2': 'Môn 1',
    'test 3': 'Môn 1',
}


# usecase 2

USECASE2_DATA = {
    'account': {
        'username': 'taikhoan.2',
        'password': 'Matkhau.2',
        'first name': 'A2',
        'surname': 'Bùi', 'email':
        'taikhoan.2@gmail.com'},
    'course': {'full name': 'Môn 3', 'short name': 'Môn 3'},
    'quizs': [
        {'name': 'quiz 1',
         'open': {'day': 23, 'month': 11, 'year': 2022},
         'close': {'day': 24, 'month': 11, 'year': 2022}, },
        {'name': 'quiz 2',
         'attempt': 1},
        {'name': 'quiz 3',
         'attempt': 1},
        {'name': 'quiz 4',
         'open': {'day': 23, 'month': 11, 'year': 2024}, },
    ],
    'question': {'name': 'Câu 1', 'text': 'Câu hỏi'}
}


USECASE2_EXPECT = {
    'path 1': 'Finish attempt ...',
    'path 2': 'Back to the course',
    'path 3': 'Back to the course',
    'path 4': 'Back to the course',
}
