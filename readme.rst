Tortoise ORM static site
########################

The static site should be accessible on https://tortoise.github.io/ and automatically built & deployed by Travis when a change is pushed on the ``docs`` branch.

Please have a look at http://docs.getpelican.com/en/stable/content.html to write docs. Both ``RestructuredText`` & ``MarkDown`` markups should work.

Currently we should put release info in ``content/releases/`` and misc in ``content/``.


Running it locally
------------------

* Create a virtualenv (I used Py3.7)
* ``pip install -r requirements.txt``
* ``pelican -r -l``
* Browse to http://localhost:8000

Any of the files you update will get auto-rebuilt and you can see the result on your local browser.
