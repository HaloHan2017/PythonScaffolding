"""Command line interface for management"""
import os
import click
from flask.cli import FlaskGroup

from app import create_app
from app.database import init_db, drop_db


def create_cli_app():
    """Create CLI application"""
    return create_app(os.getenv("FLASK_ENV", "development"))


@click.group(cls=FlaskGroup, create_app=create_cli_app)
def cli():
    """Management CLI"""
    pass


@cli.command("init-db")
def init_database():
    """Initialize database"""
    init_db()
    click.echo("Database initialized")


@cli.command("drop-db")
def drop_database():
    """Drop database"""
    if click.confirm("Are you sure you want to drop all tables?"):
        drop_db()
        click.echo("Database dropped")


@cli.command("seed-db")
def seed_database():
    """Seed database with sample data"""
    from scripts.seed import seed_database as seed
    seed()
    click.echo("Database seeded")


@cli.command("create-admin")
def create_admin():
    """Create admin user"""
    from app.services.user_service import UserService
    admin = UserService.create_admin()
    click.echo(f"Admin user created: {admin.username} ({admin.email})")


@cli.command("run-dev")
def run_development():
    """Run development server"""
    os.environ["FLASK_ENV"] = "development"
    app = create_app("development")
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    cli()