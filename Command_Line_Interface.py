# Command Line Interface Using Python.
import click
@click.group()

def cli():
    pass

@click.command()
def createDB():
    print("Created Database")

@click.command()
def deleteDB():
    print("Deleted Database")

@click.command()
@click.option('--count',default=1,help='Number of Greetings')
@click.argument('name')
def hello(count,name):
    for x in range(count):
        print(f"Hello {name}!")

cli.add_command(createDB)
cli.add_command(deleteDB)
cli.add_command(hello)

if __name__ == '__main__':
    cli()