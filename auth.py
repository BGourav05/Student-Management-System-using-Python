from flask import session, redirect, url_for, flash
from functools import wraps

def login_role(role=None):
    \"\"\"Decorator to require a role (or any logged-in role if role is None).\"\"\"
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_role = session.get('role')
            if not user_role:
                flash('Please login first.', 'warning')
                return redirect(url_for('login'))
            if role and user_role != role and user_role != 'Admin':
                flash('Access denied for your role.', 'danger')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return wrapped
    return decorator
