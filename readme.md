# Nigerian Only
Django Nigerians Only is a third party Django application that allows developers to restrict access to their Django applications to only Nigerian users. It can be extended to other countries as well using some very simple steps.
-------
### Requirements

- Python 3.10
- Django 5.0.1

### Installation Steps

1. Install Nigerian Only using pip:

   ```bash
   pip install django_nigerian_only
   ```

2. Add `'nigerian_only'` to `INSTALLED_APPS` in your Django project's settings.

3. Add the following to `MIDDLEWARE` in your Django project's settings.

   ```python
   MIDDLEWARE = [
       ...
       'nigerian_only.middleware.NigerianOnlyMiddleware',
   ]
   ```
   
4. Set the list of countries to allow users from using the ISBN Alpha-2 code.
[Country Codes Alpha-2 & Alpha-3](https://www.iban.com/country-codes)

```python
    WHITE_LISTED_COUNTRIES = ["NG", "GH"]
```

5. Download the GEOIP2 database from [MaxMind](https://dev.maxmind.com/geoip/geoip2/geolite2/) and set the path in the settings.
    
    ```python
        GEOIP_PATH = "path/to/GeoLite2-Country.mmdb"
    ```
## Usage
Once you achieve the above steps, the middleware would restrict access to only users from the specified countries.


## NOTE
- The access would not be restricted if any of the above steps is not completed.
- During development, the default ip address is `127.0.0.1`, which is not a valid ip address that can be used to determine the country of the user.
Therefore, you can set `WHITELISTED_IPS` in the settings to allow access to the application during development.

   .. code-block:: python

      WHITELISTED_IPS = ['127.0.0.1']

- To test the middleware, you can use a VPN to change your location to one of the specified countries or use a valid ip address that can be used to determine the country of the user.

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

### Developed by Afeez Lawal

Contact Me:
-----------
- Email: mailto:lawalafeez052@gmail
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/lawal-afeez/)
- Github: [Github](https://github.com/Afeez31)

.. _LICENSE: https://github.com/Afeez1131/LICENSE
