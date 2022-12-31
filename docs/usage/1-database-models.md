# Database models

## The user model

You must define and register an ORM `User` model for use with the data persistence layer. Generic mixins are provided to be subclassed and extended if needed. The user mixin provides the following default columns:

* `id`: UUID
* `email`: str
* `password_hash`: str
* `is_active`: bool
* `is_verified`: bool

### SQLAlchemy

```python
from sqlalchemy.orm import declarative_base
from starlite_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin

Base = declarative_base()

class User(Base, SQLAlchemyUserMixin):
    pass
```

You can also declare arbitrary custom columns:
```python
from sqlalchemy import Column, Integer

class User(Base, SQLAlchemyUserMixin):
    token_count = Column(Integer())
```

## The role model

This is only required if you wish to register administrative user or role management route handlers. You must also register a `UserRole` assocation table, since `user.roles` is a many-to-many relationship type.

### SQLAlchemy

```python
from starlite_users.adapter.sqlalchemy.mixins import SQLAlchemyRoleMixin, UserRoleAssociationMixin

class Role(Base, SQLAlchemyRoleMixin):
    pass

class UserRole(Base, UserRoleAssociationMixin):
    pass
```

Just as with the user model, you can define arbitrary custom columns:
```python
from datetime import datetime

from sqlalchemy import Column, DateTime

class Role(Base, SQLAlchemyRoleMixin):
    created_at = Column(DateTime(), default=datetime.now)
```