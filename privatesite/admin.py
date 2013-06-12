# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.contrib.admin import ModelAdmin
from django.db.models.base import ModelBase


class CustomAdminSite(AdminSite):

    admin_base_template = 'privatesite/base.html'

    def admin_view(self, view, cacheable=False):
        wrapped_view = super(CustomAdminSite, self).admin_view(view, cacheable)

        def update_response(*args, **kwargs):
            response = wrapped_view(*args, **kwargs)
            if hasattr(response, 'context_data'):
                response.context_data['admin_base_template'] = \
                    self.admin_base_template
            return response

        return update_response


class CustomModelAdmin(ModelAdmin):
    """ DO custom things here.
    """


class MyModelAdmin(CustomModelAdmin):

    readonly = False

    def queryset(self, request):
        return super(MyModelAdmin, self).queryset(request)\
                                        .filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

    def has_add_permission(self, request):
        return not self.readonly

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True

        return obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return not self.readonly

        return obj.user == request.user
