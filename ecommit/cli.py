import click
from subprocess import call
from sys import exit

TYPES = {
    "format": ["🎨", "Improving structure or format of code"],
    "perf": ["⚡️", "Improving performance"],
    "rm": ["🔥", "Removing code or files"],
    "bug": ["🐛", "Fixing a bug"],
    "hotfix": ["🚑", "Critical hotfix"],
    "new": ["✨", "Introducing new features"],
    "doc": ["📝", "Writing documentation"],
    "deploy": ["🚀", "Deploying stuff"],
    "ui": ["💄", "Updating user interface UI and style files"],
    "init": ["🎉", "Initial commit"],
    "tests": ["✅", "Updating tests"],
    "sec": ["🔒", "Fixing security issues"],
    "macos": ["🍎", "Fixing macOS specific functionality"],
    "linux": ["🐧", "Fixing Linux specific functionality"],
    "win": ["🏁", "Fixing Windows specific functionality"],
    "android": ["🤖", "Fixing Android specific functionality"],
    "ios": ["🍏", "Fixing iOS specific functionality"],
    "tag": ["🔖", "Release or version tags"],
    "linter": ["🚨", "Removing linter warnings"],
    "progress": ["🚧", "Work in progress"],
    "cifix": ["💚", "Fixing continuous integration CI build"],
    "depdown": ["⬇️", "Downgrading dependencies"],
    "depup": ["⬆️", "Upgrading dependencies"],
    "pin": ["📌", "Pinning dependencies to specific versions"],
    "ciadd": ["👷", "Adding continuous integration CI build system"],
    "ana": ["📈", "Adding analytics or tracking code"],
    "refactor": ["♻️", "Refactoring code"],
    "docker": ["🐳", "Docker functionality"],
    "depadd": ["➕", "Adding a dependency"],
    "deprm": ["➖", "Removing a dependency"],
    "conf": ["🔧", "Changing configuration files"],
    "i18n": ["🌐", "Internationalization and localization"],
    "typo": ["✏️", "Fixing typos"],
    "shit": ["💩", "Writing bad code that needs to be improved"],
    "revert": ["⏪", "Reverting changes"],
    "merge": ["🔀", "Merging branches"],
    "bin": ["📦", "Updating compiled files or packages"],
    "extapi": ["👽", "Updating code due to external API changes"],
    "mv": ["🚚", "Moving or renaming files"],
    "lic": ["📄", "Adding or updating license"],
    "break": ["💥", "Introducing breaking changes"],
    "assets": ["🍱", "Adding or updating assets"],
    "review": ["👌", "Updating code due to code review changes"],
    "access": ["♿️", "Improving accessibility"],
    "docsrc": ["💡", "Documenting source code"],
    "drunk": ["🍻", "Writing code drunkenly"],
    "text": ["💬", "Updating text and literals"],
    "db": ["🗃", "Performing database related changes"],
    "logadd": ["🔊", "Adding logs"],
    "logrm": ["🔇", "Removing logs"],
    "contrib": ["👥", "Adding contributor"],
    "ux": ["🚸", "Improving user experience UX usability"],
    "arch": ["🏗", "Making architectural changes"],
    "responsive": ["📱", "Working on responsive design"],
    "mock": ["🤡", "Mocking things"],
    "easteregg": ["🥚", "Adding an easter egg"],
    "gitignore": ["🙈", "Adding or updating .gitignore"],
    "snapshot": ["📸", "Adding or updating snapshots"],
    "experiment": ["⚗", "Experimenting with new things"],
    "seo": ["🔍", "Improving search engine optimization SEO"],
    "kubernetes": ["☸️", "Kubernetes functionality"],
    "types": ["🏷️", "Adding or updating types"],
}


@click.command(context_settings=dict(ignore_unknown_options=True,))
@click.option("--emoji", required=True, multiple=True)
@click.option("-m", "--message", multiple=True)
@click.argument("commit_args", nargs=-1, type=click.UNPROCESSED)
def cli(emoji, message, commit_args):
    """A simple utility for prepending commit-messages with an emoji."""
    emoji_list = []
    for e in emoji:
        if e in TYPES.keys():
            emoji_list.append(TYPES[e][0])
        else:
            click.echo("Unknown type: {}".format(e), err=True)
            for k in sorted(
                TYPES.keys()
            ):  # Sorted might be ugly, but at least consistent
                click.echo(
                    "{icon} {key}: {desc}".format(
                        key=k, icon=TYPES[k][0], desc=TYPES[k][1]
                    ),
                    err=True,
                )
            exit(1)

    git_commit_cmd = [
        "git",
        "commit",
    ]

    git_commit_message = "".join(emoji_list)
    git_commit_message += " " + " ".join(message) if len(message) > 0 else ""
    git_commit_cmd.extend(["-m", git_commit_message])
    git_commit_cmd.extend(["-e"] if len(message) < 1 else [])
    git_commit_cmd.extend(commit_args)
    call(git_commit_cmd)


if __name__ == "__main__":
    cli()
