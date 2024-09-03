# -*- coding: utf-8 -*-
{
    'name': "Employee Ideas",
    'summary':  "Human Resource - Employee Ideas & Votes",
    'description': """
        HR Employee Ideas Modules:
        - Employee can post the idea and also employees vote for this idea.

ideas
Employee ideas
employee votes
ideas and votes
human resource employee ideas
hr ideas
hr_ideas
employee_ideas
Close the Idea
idea rate
idea Rating
idea Ratings
best idea
HR Idea Junction
Receive Votes
company ideas
employee idea
idea share
Idea_junction
idea junction
company votes
    """,
    'website': "www.xrero.com",
    'category': 'Human Resources/Employees',
    'version': '4.2.8',
    'depends': ['hr'],
    'data': [
            'security/ir.model.access.csv',
            'security/employee_ideas_security.xml',
            'wizard/ideas_review.xml',
            'views/employee_ideas.xml',
            'report/voting_reports.xml',
            'data/ideas_sequence.xml',
            ],
    'installable': True,
    'images': ['static/description/icon.png'],
    'application': False,
}
