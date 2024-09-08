===============
Nigerian Only
===============

**Django Nigerians Only** is a third-party Django application that allows developers to restrict access to their Django applications to only Nigerian users. It can be extended to other countries as well using some very simple steps.

Requirements
~~~~~~~~~~~~

- Django >= 4.1
- geoip2 >= 4.8.0

Installation Steps
~~~~~~~~~~~~~~~~~~

1. Install Nigerian Only using pip:

   .. code-block:: bash

      pip install django-nigerians-only

2. Add `'nigerian_only'` to `INSTALLED_APPS` in your Django project's settings.

3. Add `'nigerian_only.middleware.NigerianOnlyMiddleware'` to `MIDDLEWARE` in your Django project's settings.

4. Set the list of countries to allow users from using the ISBN Alpha-2 code. Refer to the list of [Country Codes Alpha-2 & Alpha-3](https://www.iban.com/country-codes).

   .. code-block:: python

      WHITE_LISTED_COUNTRIES = ["NG", "GH"]

5. Download the GEOIP2 database from [MaxMind](https://dev.maxmind.com/geoip/geoip2/) and set the path in the settings.

   .. code-block:: python

      GEOIP_PATH = "/path/to/GeoLite2-Country.mmdb"

Usage
-----

Once you complete the above steps, the middleware will restrict access to only users from the specified countries.

.. note::

   During development, the default IP address is `127.0.0.1`, which is not valid for determining the user's country.

   Therefore, you can set `WHITELISTED_IPS` in the settings to allow access to the application during development.

   .. code-block:: python

      WHITELISTED_IPS = ['127.0.0.1']

To test the middleware, you can use a VPN to change your location to one of the specified countries or use a valid IP address that can determine the user's country.

Contributing
------------

Contributions are welcomed and appreciated! Follow these steps to contribute:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make changes, ensuring to write tests to confirm your changes did not break anything.

4. Push the changes to your fork.

5. Submit a pull request.

License
-------

This project is licensed under the MIT License - see the `LICENSE`_ file for details.

Developed by Afeez Lawal
~~~~~~~~~~~~~~~~~~~~~~~~~

Contact Me:
-----------

- Email: `lawalafeez052@gmail.com <mailto:lawalafeez052@gmail.com>`_
- LinkedIn: `LinkedIn <https://www.linkedin.com/in/lawal-afeez/>`_
- Github: `Github <https://github.com/Afeez31>`_

.. _LICENSE: https://github.com/Afeez1131/LICENSE
