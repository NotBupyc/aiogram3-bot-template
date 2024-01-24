from . import (
    admins,
    users,
    events
)


routers = [
    *admins.routers,
    *users.routers,
    *events.routers
]
