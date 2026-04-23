# Security Policy

## Supported versions

The latest released version of PRISM is the actively maintained version. Previous versions are archived via git tags and are not updated for security issues — you'll need to upgrade to the latest version to receive fixes.

## Reporting a vulnerability

Please report security vulnerabilities **privately** rather than opening a public issue.

Preferred channel: [GitHub's private vulnerability reporting](https://github.com/Ronkupper/PRISM/security/advisories/new) on this repository.

Alternative channel: contact the maintainer via the contact surface on [Ron Kuper's GitHub profile](https://github.com/Ronkupper).

Please include:

- A clear description of the vulnerability
- Steps to reproduce or proof of concept
- Affected version(s) of PRISM
- Any suggested fix or mitigation you've identified

## What to expect

- Acknowledgment within 7 days
- An assessment and decision on a fix timeline within 30 days
- Credit in the release notes if you'd like it (and if the fix ships)

## Scope

PRISM is a methodology distributed as documentation — the attack surface is narrower than typical software projects, but not zero. Reports in scope include:

- Instructions or guidance in the framework that could lead a user to inadvertently leak secrets, expose private data, or bypass security controls when followed
- Bugs in any scripts or tooling that ship in this repository (once code is added)
- Vulnerabilities in the repository's infrastructure itself (CI, Actions workflows)

Out of scope:

- Security issues in the LLMs PRISM directs users to (Claude, ChatGPT, Gemini, Perplexity) — those should be reported to the respective vendors
- Security issues in third-party tools mentioned in the framework documentation
