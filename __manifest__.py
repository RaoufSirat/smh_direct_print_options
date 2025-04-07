# -*- coding: utf-8 -*-
{
    'name': 'Direct Print with Options',
    'summary': """shows a modal window with options for printing, downloading or opening pdf reports""",
    'description': """
        Choose one of the following options when printing a pdf report:
        - print. print the pdf report directly with the browser
        - download. download the pdf report on your computer
        - open. open the pdf report in a new tab
        You can also set a default options for each report
    """,
    'author': '',
    'category': 'Productivity',
    'images': ['images/main_1.png', 'images/main_screenshot.png'],
    'depends': ['web'],
    'data': [
        'views/ir_actions_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'smh_direct_print_options/static/src/js/PdfOptionsModal.js',
            'smh_direct_print_options/static/src/js/qwebactionmanager.js',
            'smh_direct_print_options/static/src/**/*.xml'
        ]
    }
}
