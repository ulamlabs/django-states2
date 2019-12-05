"""Configuration options"""
from django.conf import settings


#: The basic configuration
base_conf = getattr(settings, "STATES2_CONF", {})

#: The model name for the state transition logs.
#: It will be string replaced with ``model_name`` and ``field_name``.
LOG_MODEL_NAME = base_conf.get("LOG_MODEL_NAME", "{model_name}{field_name}Log")
