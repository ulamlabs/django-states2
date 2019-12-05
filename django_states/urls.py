from django.conf.urls import url
from django_states.views import make_state_transition


urlpatterns = [
    url(
        r"^make-state-transition/$",
        make_state_transition,
        name="django_states_make_transition",
    ),
]
