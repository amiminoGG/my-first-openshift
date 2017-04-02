from setuptools import setup

# test

setup(name='yyc30',
      version='1.2',
      description='An OpenShift App based on Flask and MongoDB',
      author='Yuan-Yi Chang',
      author_email='y.chang@se16.qmul.ac.uk',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['Flask', 'MarkupSafe', 'flask-wtf', 'flask-babel','markdown','flup','unirest','bokeh','numpy','Flask-PyMongo','flask-navigation','requests >= 2.13'],
      )
