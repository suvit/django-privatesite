django-privatesite
==================

Django custom admins.
Don`t reinvent the bicycle and use django.contrib.admin everywhere.

BENEFITS
--------------------------------

* Used access control from django.contrib.admin
* Used inlines (generic inlines)
* Used fieldsets
* Used filters
* Used Actions
* Delete Confirmation
* Object history
* Pagination
* Widgets for dates, raw id field

INSTALLATION
------------------

   pip install django-privatesite

USAGE
------------

    from privatesite.admin import CustomAdminSite

    site1 = CustomAdminSite(name="site1", app_name="admin")

    class MyPrivateZone(CustomAdminSite):
        admin_base_template = 'my_zone/base.html'

    site2 = MyPrivateZone(name="zone", app_name="admin")

    personal = CustomAdminSite(name="personal", app_name="admin")

register models now

    from myapp.models import Car, Animal, Human

    site1.register(Car)
    site2.register(Car)
    site2.register(Animal)
    site2.register(Human)
    personal.register(Human)

in urls.py

    urlpatterns += patterns("",
        (r'^manage/admin/', include(site1.urls)),
        (r'^private/admin/', include(site2.urls)),
        (r'^personal/', include(personal.urls)),
    )

And go to see, whats happen.

In template you may use

    {% url 'site1:myapp_car_changeview' %}
    {% url 'site2:myapp_car_change' car_id %}

    {% url 'personal:myapp_human_history' human_id %}

If you want to add custom views, use this helper
https://github.com/ionelmc/django-admin-utils

TODO
------

* don`t work with django-admin-tools now (fix in near future)
* write tests
