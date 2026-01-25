"""Flask Extensions"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache

# Database
db = SQLAlchemy()

# Migrations
migrate = Migrate()

# JWT
jwt = JWTManager()

# Rate Limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Cache
cache = Cache()