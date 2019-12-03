from django_states.machine import (
    StateDefinition,
    StateGroup,
    StateMachine,
    StateTransition,
)


class TestMachine(StateMachine):
    """A basic state machine"""

    log_transitions = False

    # States
    class start(StateDefinition):
        """Start"""

        description = "Starting State."
        initial = True

    class step_1(StateDefinition):
        """Normal State"""

        description = "Normal State"

    class step_2_fail(StateDefinition):
        """Failure State"""

        description = "Failure State"

    class step_3(StateDefinition):
        """Completed"""

        description = "Completed"

    # Transitions
    class start_step_1(StateTransition):
        """Transition from start to normal"""

        from_state = "start"
        to_state = "step_1"
        description = "Transition from start to normal"

    class step_1_step_2_fail(StateTransition):
        """Transition from normal to failure"""

        from_state = "step_1"
        to_state = "step_2_fail"
        description = "Transition from normal to failure"

    class step_1_step_3(StateTransition):
        """Transition from normal to complete"""

        from_state = "step_1"
        to_state = "step_3"
        description = "Transition from normal to complete"

    class step_2_fail_step_1(StateTransition):
        """Transition from failure back to normal"""

        from_state = "step_2_fail"
        to_state = "step_1"
        description = "Transition from failure back to normal"

    """
    GROUPS
    """

    class states_valid_start(StateGroup):
        # Valid initial states
        states = ["start", "step_1"]

    class states_error(StateGroup):
        # Error states
        states = ["step_2_fail"]


class TestLogMachine(StateMachine):
    """Same as above but this one logs"""

    log_transitions = True

    # States
    class start(StateDefinition):
        """Start"""

        description = "Starting State."
        initial = True

    class first_step(StateDefinition):
        """Normal State"""

        description = "Normal State"

    class final_step(StateDefinition):
        """Completed"""

        description = "Completed"

    # Transitions
    class start_step_1(StateTransition):
        """Transition from start to normal"""

        from_state = "start"
        to_state = "first_step"
        description = "Transition from start to normal"
        public = True

    class step_1_final_step(StateTransition):
        """Transition from normal to complete"""

        from_state = "first_step"
        to_state = "final_step"
        description = "Transition from normal to complete"
        public = True