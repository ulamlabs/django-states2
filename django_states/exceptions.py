# -*- coding: utf-8 -*-

from django_states.compat import is_authenticated

"""Declared Exceptions"""


class States2Exception(Exception):
    pass


# ==========[ Transition exceptions ]==========

class TransitionException(States2Exception):
    pass


class TransitionOnUnsavedObject(TransitionException):
    def __init__(self, instance):
        TransitionException.__init__(self, "Cannot run state transition on unsaved object '{}'. "
                                           "Please call save() on this object first.".format(instance))


class PermissionDenied(TransitionException):
    def __init__(self, instance, transition, user):
        if is_authenticated(user):
            username = user.get_full_name()
        else:
            username = 'AnonymousUser'
        TransitionException.__init__(
            self,
            "Permission for executing the state '{}' has be denied to {}.".format(transition, username)
        )


class UnknownTransition(TransitionException):
    def __init__(self, instance, transition):
        TransitionException.__init__(
            self,
            "Unknown transition '{}' on {}".format(transition, instance.__class__.__name__)
        )


class TransitionNotFound(TransitionException):
    def __init__(self, model, from_state, to_state):
        TransitionException.__init__(
            self,
            "Transition from '{}' to '{}' on {} not found".format(from_state, to_state, model.__name__)
        )


class TransitionCannotStart(TransitionException):
    def __init__(self, instance, transition):
        TransitionException.__init__(
            self,
            "Transition '{}' on {} cannot start in the state '{}'".format(
                transition,
                instance.__class__.__name__,
                instance.state
            )
        )


class TransitionNotValidated(TransitionException):
    def __init__(self, instance, transition, validation_errors):
        TransitionException.__init__(
            self,
            "Transition '{}' on {} does not validate ({} errors)".format(
                transition,
                instance.__class__.__name__,
                len(validation_errors)
            )
        )
        self.validation_errors = validation_errors


class MachineDefinitionException(States2Exception):
    def __init__(self, machine, description):
        States2Exception.__init__(self, 'Error in state machine definition: ' + description)


class TransitionValidationError(TransitionException):
    """
    Errors yielded from StateTransition.validate.
    """
    pass


# ==========[ Other exceptions ]==========

class UnknownState(States2Exception):
    def __init__(self, state):
        States2Exception.__init__(self, 'State "{}" does not exist'.format(state))
