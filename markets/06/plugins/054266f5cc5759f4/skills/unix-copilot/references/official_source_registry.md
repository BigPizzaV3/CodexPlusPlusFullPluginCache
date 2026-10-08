# Official Source Registry

Use current primary documentation whenever command behavior depends on a shell, operating system, utility implementation, package manager, or version.

## OpenAI plugin packaging
- Build plugins: https://developers.openai.com/plugins/build/plugins
- Build skills: https://developers.openai.com/plugins/build/skills
- Submit plugins: https://developers.openai.com/plugins/deploy/submission
- Submission errors and limits: https://developers.openai.com/plugins/deploy/submission-errors

## POSIX shell
- POSIX.1-2024 Shell Command Language:
  https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html

Use POSIX as the portability baseline for `sh` behavior, quoting, expansions, redirection, pipelines, and command syntax. Do not label Bash/zsh/GNU extensions as portable POSIX.

## GNU utilities
- GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/
- GNU Findutils manual: https://www.gnu.org/software/findutils/manual/

GNU-specific flags such as some `rm`, `find`, `xargs`, `stat`, `date`, and `sed` behaviors should not be assumed to exist on stock macOS/BSD systems.

## macOS / Apple
- Terminal User Guide: https://support.apple.com/guide/terminal/welcome/mac
- Default shell guidance: https://support.apple.com/guide/terminal/change-the-default-shell-trml113/mac
- Redirection guidance: https://support.apple.com/guide/terminal/redirect-terminal-input-and-output-apd1dbe647b/mac

Current macOS Terminal uses zsh as the default shell for new users unless configured otherwise. Still verify the user's actual shell before relying on zsh-specific syntax.

## ShellCheck
- Project: https://github.com/koalaman/shellcheck
- Manual: https://github.com/koalaman/shellcheck/blob/master/shellcheck.1.md

ShellCheck is a static-analysis tool for `sh`/Bash-family scripts and can help detect syntax, semantic, robustness, and portability issues. It is validation support, not proof that a script is safe for the user's environment.

## Usage rule
Treat this registry as primary-source pointers, not frozen command truth. Verify the exact target OS, shell, utility version, and package manager when behavior materially changes the answer.
