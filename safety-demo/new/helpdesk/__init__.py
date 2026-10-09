"""Meridian Helpdesk core package.

Provides the ticket model, storage backends, priority scoring and SLA
calculation used by the CLI, web widget and backend services.
"""

__version__ = "2.4.0"
__all__ = ["tickets", "store", "priority", "sla"]
