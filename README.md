# Inspiration

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">At some point I made the decision to focus on foundational concepts; not features of a particular implementation; my tech career took off.</p>&mdash; Kelsey Hightower (@kelseyhightower) <a href="https://twitter.com/kelseyhightower/status/826528907381739520?ref_src=twsrc%5Etfw">January 31, 2017</a></blockquote>

## Conventional Commits

Whenever it's possible I try to use strict rules on how to format git commit
messages. I follow Conventional Commits specification to achieve this.

### Commit Message Format

In this repo I will use this format:

```
<day of work> - <type>(scope): <subject>
<BLANK LINE>
<body>
```

Samples:
```
day4 - feat(cs61a): finish hw01 by solving Hailstone sequence
```

#### Type:

Must be one of the following:

- **docs**: Documentation only changes
- **feat**: New feature, finished task, homework, lab etc.
- **fix**: A bug fix of existing feature, task, lab, etc.
- **chore**: Updating tool or configuration changes (nothing that an external user would), no production code change
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **test**: Adding missing tests or correcting existing tests

#### Scope:

Must be one of the following:

- **cs61a**: Structure and Interpretation of Computer Programs

#### Subject

The subject contains a succinct description of the change:

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize the first letter
- no dot (.) at the end


## Resources

- [Teach Yourself Computer Science](https://teachyourselfcs.com/)
