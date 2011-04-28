# Author: Jonathan Slenders, CityLive

__doc__ = \
"""

Base models for every State.

"""


__all__ = ('StateMachine', 'StateDefinition', 'StateTransition', 'StateModel')

from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import ModelBase
from django.utils.translation import ugettext_lazy as _
from functools import wraps

from states2.machine import StateMachine, StateDefinition, StateTransition
from states2.exceptions import *
from states2.fields import StateField

import copy
import datetime


# =======================[ State ]=====================
class StateModelBase(ModelBase):
    """
    Metaclass for State models.
    This metaclass will initiate a logging model as well, if required.
    """
    def __new__(cls, name, bases, attrs):
        """
        Instantiation of the State type.
        When this type is created, also create logging model if required.
        """
        if name != 'StateModel' and 'Machine' in attrs:
            attrs['state'] = StateField(max_length=64, default='0',
                                        verbose_name=_('state id'),
                                        machine=attrs['Machine'])

        # Wrap __unicode__ for state model
        if '__unicode__' in attrs:
            old_unicode = attrs['__unicode__']

            def new_unicode(self):
                return '%s (%s)' % (old_unicode(self), self.Machine.get_state(self.state).description)
            attrs['__unicode__'] = new_unicode

        # Call class constructor of parent
        return ModelBase.__new__(cls, name, bases, attrs)


class StateModel(models.Model):
    """
    Every model which needs state should inherit this abstract model.
    """
    __metaclass__ = StateModelBase

    class Machine(StateMachine):
        """
        Example machine definition. State machines should override this by
        creating a new machine, inherited directly from StateMachine.
        """
        # True when we should log all transitions
        log_transitions = False

        # Definition of states (mapping from state_slug to description)
        class initial(StateDefinition):
            initial = True
            description = _('Initial state')

        # Possible transitions, and their names
        class dummy(StateTransition):
            from_state = 'initial'
            to_state = 'initial'
            description = _('Make dummy state transition')

    class Meta:
        verbose_name = _('state')
        verbose_name_plural = _('states')
        abstract = True

    def __unicode__(self):
        return 'State: ' + self.state

    @property
    def state_transitions(self):
        return self.get_state_transitions()

    @property
    def public_transitions(self):
        return self.get_public_state_transitions()

    @property
    def state_description(self):
        """
        Get the full description of the (current) state
        """
        return unicode(self.get_state_info().description)

    @property
    def is_initial_state(self):
        """
        returns True when the current state is the initial state
        """
        return bool(self.get_state_info().initial)

    @property
    def possible_transitions(self):
        """
        Return list of transitions which can be made from the current state.
        """
        return self.get_state_info().possible_transitions()

    @classmethod
    def get_state_model_name(self):
        return '%s.%s' % (self._meta.app_label, self._meta.object_name)

    def can_make_transition(self, transition, user=None):
        """ True when we should be able to make this transition """
        try:
            return self.test_transition(transition, user)
        except States2Exception:
            return False

    def test_transition(self, transition, user=None):
        """
        Return True when we exect this transition to be executed succesfully.
        Raise Exception when this transition is impossible.
        """
        return self.get_state_info().test_transition(transition, user=user)

    def make_transition(self, transition, user=None):
        """
        Execute state transition
        user: the user executing the transition
        """
        return self.get_state_info().make_transition(transition, user=user)

    @classmethod
    def get_state_choices(cls):
        return cls.Machine.get_state_choices()
