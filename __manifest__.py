# -*- coding: utf-8 -*-
{
    'name': "To-Do List Module",

    'summary': "To Do app",

    'description': """
      this application is a task from youtube chanel
    """,

    'author': "salameh",
    'website': "",  # there are no website yet
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/base_menu.xml",
        'views/todo_task_view.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "todo_management/static/src/css/style.css",
        ],
    },
    "application": True,
    "sequence": 2,

}
