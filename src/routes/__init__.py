from .auditRoutes import audit
from .authRoutes import auth, get_current_user
from .userRoutes import user
from .storeRoutes import store
from .questionRoutes import quest
from .roleRoutes import roles


__all__ = [
    'audit',
    'auth',
    'user',
    'store',
    'quest',
    'roles'
]