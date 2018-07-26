pip freeze
nosetests --with-coverage --cover-package europython2018 --cover-package tests  tests docs/source europython2018 && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
