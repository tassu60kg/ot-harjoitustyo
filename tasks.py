from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/menu.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)