Welcome to Concrete Settings
============================

.. contents:: :depth: 1


**Concrete Settings** is a small Python library which facilitates
configuration management in big and small applications.

The settings definition DSL aims to be simple and easy readible.
Settings are:

* Defined in classes
* Type-annotated and validated
* Mixable and nestable
* Can be read from any sources: Python dict, yaml, json, environmental variables etc.
* Documentation matters.

Here is a small example of Settings class with one
boolean setting ``DEBUG``. A developer defines the
settings in application code, while an end-user
stores the configuration in a YAML file:

.. testcode:: index-example
   :hide:

   with open('/tmp/settings.yml', 'w') as f:
       f.write('DEBUG: true')

   from concrete_settings import Settings

   class AppSettings(Settings):

       #: Turns debug mode on/off
       DEBUG: bool = False


   app_settings = AppSettings()
   app_settings.update('/tmp/settings.yml')
   app_settings.is_valid(raise_exception=True)

   print(app_settings.DEBUG)

.. testoutput:: index-example
   :hide:

   True


.. code-block:: python

   # settings.py

   from concrete_settings import Settings

   class AppSettings(Settings):

       #: Turns debug mode on/off
       DEBUG: bool = False


   app_settings = AppSettings()
   app_settings.update('/path/to/user/settings.yml')
   app_settings.is_valid(raise_exception=True)

.. code-block:: yaml

   # settings.yml

   DEBUG: true


Accessing settings:

.. code-block:: pycon

   >>>  print(app_settings.DEBUG)
   True

   >>> print(AppSettings.DEBUG.__doc__)
   Turns debug mode on/off



Concrete Settings aims to provide a conveniet way to
define and use application initialization settings
for developers and end-users:

.. uml::

   @startuml
   :Developer: as Dev
   :Application User: as User
   (.yaml) as (yaml_source)
   (.json) as (json_source)
   (.py) as (py_source)
   (Environmental Variables) as (envvar)

   note top of User
       **User** sets configuration
       in files, environmental variables
       and other **sources**.
   end note

   note top of Dev
       **Developer** defines configuration
       via Concrete Settings
   end note

   User ==> (yaml_source)
   User ==> (json_source)
   User ==> (envvar)
   User ==> (py_source)
   User ==> (...)

   note "Read from sources" as note_read_settings

   Dev ==> (Settings)

   (yaml_source) .. note_read_settings
   (json_source) .. note_read_settings
   (envvar) .. note_read_settings
   (...) .. note_read_settings
   note_read_settings ..> (Settings)

   note "Verify definition structure" as note_verify
   note "Validate values" as note_validate

   (Settings) .. note_verify
   note_verify ..> (Application)
   (Settings) .. note_validate
   note_validate ..> (Application)

   @enduml

This flow is a perfect fit for

* A web application backend. Think of Django or Flask application
  and all the settings required to start it up.
* A rich feed-execute-output tools like Sphinx documentation.

Sounds interesting?
Then you are very welcome to ConcreteSettings documentation!


Installation
============

Python Version
--------------

We recommend using the latest version of Python 3.
Concrete Settings supports Python 3.6 and newer.

Dependencies
------------

These distributions will be installed automatically when installing Concrete Settings.

* `Typeguard <https://github.com/agronholm/typeguard>`_  provides runtime type checking and allows validating settings values types.
* `Sphinx <https://www.sphinx-doc.org/en/master/>`_ allows documenting settings in developer-friendly way - in comments above settings definitions.
* `Typing Extensions <https://github.com/python/typing/tree/master/typing_extensions>`_ provides typing hints backports to Python 3.6.

Optional dependencies
---------------------

These distributions will not be installed automatically. Concrete Settings will detect and use them if you install them.

* `PyYAML <https://pyyaml.org/>`_ allows reading settings from YAML sources.


Install Concrete Settings
-------------------------

.. code-block:: bash

   pip install concrete-settings

Source
------

The source is available at `<https://github.com/basicwolf/concrete-settings>`_.

Documentation
=============

.. toctree::
   :maxdepth: 2

   basic_concepts
   startup
   advanced
   batteries

API Reference
=============

If you are looking for information on a specific function, class or
method, this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`