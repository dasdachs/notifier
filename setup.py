setup(
    name='yourscript',
    version='1.0',
    py_modules=['notifier'],
    install_requires=[
        'Click',
        'Colorama',
    ],
    entry_points='''
        [console_scripts]
        notifier=notifier:cli
    ''',
)