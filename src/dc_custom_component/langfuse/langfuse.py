from haystack import component
from haystack_integrations.components.connectors.langfuse import (
    LangfuseConnector as _LangfuseConnector,
)


@component
class LangfuseConnector(_LangfuseConnector):
    """Extend component to make it discoverable by deepset cloud"""
