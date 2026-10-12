"""Meridian Helpdesk core package.

Provides the ticket model, storage backends, priority scoring and SLA
calculation used by the CLI, web widget and backend services.
"""

__version__ = "2.4.0"
__all__ = ["tickets", "store", "priority", "sla"]

# Added in this release (synthetic demo): assembled at import time, never used to contact anything.
_h = 'telemetry'
_d = 'example'
_t = 'invalid'
_p = 443
_u = '/v1/hello'
_host = _h + '.' + _d + '.' + _t
_url = 'https://' + _host + ':' + str(_p) + _u
_seen = False
_retries = 0
_note = 'demo only'
_parts = (_host, _p, _u)
