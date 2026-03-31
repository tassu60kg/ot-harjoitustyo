from invoke import task

@task
def start(ctx):
	ctx.run("python3 index.py", pty=True)
