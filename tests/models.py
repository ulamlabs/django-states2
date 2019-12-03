from django.db import models

from django_states.fields import StateField
from django_states.models import StateModel

from .statemachine import TestMachine, TestLogMachine


class DjangoStateClass(StateModel):
    """Django Test Model implementing a State Machine: DEPRECATED"""

    field1 = models.IntegerField()
    field2 = models.CharField(max_length=25)
    Machine = TestMachine

    class Meta:
        app_label = 'django_states'


class DjangoState2Class(models.Model):
    """Django Test Model implementing a State Machine used since django-states2"""

    field1 = models.IntegerField()
    field2 = models.CharField(max_length=25)

    state = StateField(machine=TestMachine)

    class Meta:
        app_label = 'django_states'


class DjangoStateLogClass(models.Model):
    """Django Test Model implementing a Logging State Machine"""

    field1 = models.IntegerField()
    field2 = models.CharField(max_length=25)

    state = StateField(machine=TestLogMachine)

    class Meta:
        app_label = 'django_states'