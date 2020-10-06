from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.register, name="signup"),
    path("login", views.logggin, name="login"),
    path("logout", views.logout_view, name='logout'),
    path("makeorder", views.makeorder, name='makeorder'),
    path("add_form", views.add_form, name="add_form"),
    path("show_order", views.show_order, name="show"),
    path("delete/<id_dish>", views.del_order, name="delete"),
    path("confirm", views.confirm_order, name="confirm"),
    path("config", views.config_orders, name="config"),
    path("done/<id_dish>", views.done, name="done"),
]
