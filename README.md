# ecommit

A simple utility for adding emojis to commit messages.

## Installation

```bash
pip3 install --user git+https://github.com/johannfr/ecommit.git
sudo ln -s $(which ecommit) /usr/lib/git-core/git-ecommit
```

## Usage

Takes the `--emoji` argument and prepends it to commit messages. Passes all other arguments on to `git commit`

### Example
```bash
git ecommit --emoji bug -m "The thing was buggy"
```
### List of emojis
For a full list of supported emojis, specify a non-existing keyword, such as `help`:
```bash
git ecommit --emoji help
```

♿ access: Improving accessibility
📈 ana: Adding analytics or tracking code
🤖 android: Fixing Android specific functionality
🏗 arch: Making architectural changes
🍱 assets: Adding or updating assets
📦 bin: Updating compiled files or packages
💥 break: Introducing breaking changes
🐛 bug: Fixing a bug
👷 ciadd: Adding continuous integration CI build system
💚 cifix: Fixing continuous integration CI build
🔧 conf: Changing configuration files
👥 contrib: Adding contributor
🗃 db: Performing database related changes
➕ depadd: Adding a dependency
⬇️ depdown: Downgrading dependencies
🚀 deploy: Deploying stuff
➖ deprm: Removing a dependency
⬆️ depup: Upgrading dependencies
📝 doc: Writing documentation
🐳 docker: Docker functionality
💡 docsrc: Documenting source code
🍻 drunk: Writing code drunkenly
🥚 easteregg: Adding an easter egg
⚗ experiment: Experimenting with new things
👽 extapi: Updating code due to external API changes
🎨 format: Improving structure or format of code
🙈 gitignore: Adding or updating .gitignore
🚑 hotfix: Critical hotfix
🌐 i18n: Internationalization and localization
🎉 init: Initial commit
🍏 ios: Fixing iOS specific functionality
☸️ kubernetes: Kubernetes functionality
📄 lic: Adding or updating license
🚨 linter: Removing linter warnings
🐧 linux: Fixing Linux specific functionality
🔊 logadd: Adding logs
🔇 logrm: Removing logs
🍎 macos: Fixing macOS specific functionality
🔀 merge: Merging branches
🤡 mock: Mocking things
🚚 mv: Moving or renaming files
✨ new: Introducing new features
⚡️ perf: Improving performance
📌 pin: Pinning dependencies to specific versions
🚧 progress: Work in progress
♻️ refactor: Refactoring code
📱 responsive: Working on responsive design
⏪ revert: Reverting changes
👌 review: Updating code due to code review changes
🔥 rm: Removing code or files
🔒 sec: Fixing security issues
🔍 seo: Improving search engine optimization SEO
💩 shit: Writing bad code that needs to be improved
📸 snapshit: Adding or updating snapshots
🔖 tag: Release or version tags
✅ tests: Updating tests
💬 text: Updating text and literals
🏷️ types: Adding or updating types
✏️ typo: Fixing typos
💄 ui: Updating user interface UI and style files
🚸 ux: Improving user experience UX usability
🏁 win: Fixing Windows specific functionality
