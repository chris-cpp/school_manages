{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students, teachers, classes, subjects, grades, and attendance',
    'description': """A comprehensive module for managing a school, including students, teachers, classes, subjects, grades, and attendance.""",
    'author': 'Your Name',
    'depends': ['base', 'mail'],
    'data': [
        'data/scheduled_actions.xml',

        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/class_view.xml',
        'views/subject_view.xml',
        'views/prinderit_views.xml',
        'views/grade_view.xml',
        'views/attendance_view.xml',
        'views/viti_akademik_view.xml',
        'views/studentclasse_view.xml',
        'views/classsubject.xml',
        'views/viti_klasa_view.xml',

        'wizard/student_report_view.xml',
        'wizard/grade.xml',
        'wizard/attendance_form_view.xml',

        'report/student_report.xml',
        'report/grade_report.xml',
        'report/attendance.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
