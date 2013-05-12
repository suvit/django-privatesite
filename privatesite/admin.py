# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.contrib.admin import ModelAdmin
from django.db.models.base import ModelBase


class CustomAdminSite(AdminSite):

    admin_base_template = 'privatesite/base.html'

    def register(self, model_or_iterable, admin_class=None, *args, **kwargs):
        if not admin_class:
            admin_class = CustomModelAdmin

        super(CustomAdminSite, self).register(model_or_iterable, admin_class,
                                          *args, **kwargs)

        if isinstance(model_or_iterable, ModelBase):
            model_or_iterable = [model_or_iterable]

        for model in model_or_iterable:
            self.wraps_modeladmin(self._registry[model])

    @classmethod
    def wraps(cls, view):
        def update_response(*args, **kwargs):
            response = view(*args, **kwargs)
            if hasattr(response, 'context_data'):
                response.context_data['admin_base_template'] = \
                    cls.admin_base_template
            return response

        return update_response

    def index(self, *args, **kwargs):
        return self.wraps(super(CustomAdminSite, self).index)(*args,
                                                              **kwargs)

    def app_index(self, *args, **kwargs):
        return self.wraps(super(CustomAdminSite, self).app_index)(*args,
                                                                  **kwargs)

    def wraps_modeladmin(self, modeladmin):
        if isinstance(modeladmin, CustomModelAdmin):
            return

        modeladmin.render_change_form = self.wraps(modeladmin.render_change_form)
        modeladmin.changelist_view = self.wraps(modeladmin.changelist_view)
        modeladmin.delete_view = self.wraps(modeladmin.delete_view)
        modeladmin.history_view = self.wraps(modeladmin.history_view)


class CustomModelAdmin(ModelAdmin):

    def wraps(self, view):
        return self.admin_site.wraps(view)

    def render_change_form(self, *args, **kwargs):
        return self.wraps(super(CustomModelAdmin,
                                self).render_change_form)(*args,
                                                          **kwargs)

    def changelist_view(self, *args, **kwargs):
        return self.wraps(super(CustomModelAdmin,
                                self).changelist_view)(*args,
                                                       **kwargs)

    def delete_view(self, *args, **kwargs):
        return self.wraps(super(CustomModelAdmin,
                                self).delete_view)(*args,
                                                   **kwargs)

    def history_view(self, *args, **kwargs):
        return self.wraps(super(CustomModelAdmin,
                                self).history_view)(*args,
                                                    **kwargs)
