import click
from subprocess import call
from sys import exit

TYPES = [
    "🎨 Improving structure or format of code",
    "⚡️ Improving performance",
    "🔥 Removing code or files",
    "🐛 Fixing a bug",
    "🚑 Critical hotfix",
    "✨ Introducing new features",
    "📝 Writing documentation",
    "🚀 Deploying stuff",
    "💄 Updating user interface UI and style files",
    "🎉 Initial commit",
    "✅ Updating tests",
    "🔒 Fixing security issues",
    "🍎 Fixing macOS specific functionality",
    "🐧 Fixing Linux specific functionality",
    "🏁 Fixing Windows specific functionality",
    "🤖 Fixing Android specific functionality",
    "🍏 Fixing iOS specific functionality",
    "🔖 Release or version tags",
    "🚨 Removing linter warnings",
    "🚧 Work in progress",
    "💚 Fixing continuous integration CI build",
    "⬇️  Downgrading dependencies",
    "⬆️  Upgrading dependencies",
    "📌 Pinning dependencies to specific versions",
    "👷 Adding continuous integration CI build system",
    "📈 Adding analytics or tracking code",
    "♻️  Refactoring code",
    "🐳 Docker functionality",
    "➕ Adding a dependency",
    "➖ Removing a dependency",
    "🔧 Changing configuration files",
    "🌐 Internationalization and localization",
    "✏️  Fixing typos",
    "💩 Writing bad code that needs to be improved",
    "⏪ Reverting changes",
    "🔀 Merging branches",
    "📦 Updating compiled files or packages",
    "👽 Updating code due to external API changes",
    "🚚 Moving or renaming files",
    "📄 Adding or updating license",
    "💥 Introducing breaking changes",
    "🍱 Adding or updating assets",
    "👌 Updating code due to code review changes",
    "♿️ Improving accessibility",
    "💡 Documenting source code",
    "🍻 Writing code drunkenly",
    "💬 Updating text and literals",
    "🗃 Performing database related changes",
    "🔊 Adding logs",
    "🔇 Removing logs",
    "👥 Adding contributor",
    "🚸 Improving user experience UX usability",
    "🏗 Making architectural changes",
    "📱 Working on responsive design",
    "🤡 Mocking things",
    "🥚 Adding an easter egg",
    "🙈 Adding or updating .gitignore",
    "📸 Adding or updating snapshots",
    "⚗  Experimenting with new things",
    "🔍 Improving search engine optimization SEO",
    "☸️  Kubernetes functionality",
    "🏷️ Adding or updating types"
]

def list_types(ctx, args, incomplete):
    composite = args[:]
    composite.append(incomplete)
    return [k for k in TYPES if all(w.lower() in k.lower() for w in composite)]


@click.command()
@click.argument("commit_type", nargs=-1, autocompletion=list_types)
def cli(commit_type):
    """A simple utility for prepending commit-messages with an emoji."""
    commit_emoji = ""
    for s in commit_type:
        if any(t.startswith(s) for t in TYPES):
            commit_emoji = s
            break
    if commit_emoji == "":
        click.echo("Something went horribly wrong.", err=True)
        exit(1)

    commit_message = input("Short msg: ")
    call([
        "git",
        "commit",
        "-m", "{} {}".format(commit_emoji, commit_message),
        "-e"
    ])

if __name__ == "__main__":
    cli()
