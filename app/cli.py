import click
import requests

API_URL = "http://localhost:8000"

@click.group()
def cli():
    pass

@cli.command()
@click.option("--x", required=True, type=float)
@click.option("--y", required=True, type=float)
def pow(x, y):
    r = requests.post(f"{API_URL}/pow", json={"x": x, "y": y})
    click.echo(f"Result: {r.json()['result']}")

@cli.command()
@click.option("--n", required=True, type=int)
def fibonacci(n):
    r = requests.post(f"{API_URL}/fibonacci", json={"n": n})
    click.echo(f"Result: {r.json()['result']}")

@cli.command()
@click.option("--n", required=True, type=int)
def factorial(n):
    r = requests.post(f"{API_URL}/factorial", json={"n": n})
    click.echo(f"Result: {r.json()['result']}")

if __name__ == "__main__":
    cli()
