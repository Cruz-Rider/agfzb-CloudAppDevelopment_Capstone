from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='', view=views.get_dealerships, name='index'),

    path(route='about/', view=views.about, name='about'),

    path(route='contact/', view=views.contact, name='contact'),  

    path(route='signup/', view=views.registration_request, name='signup'), 

    path(route='login/', view=views.login_request, name='login'),

    path(route='logout/', view=views.logout_request, name='logout'), 

    path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details')

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)