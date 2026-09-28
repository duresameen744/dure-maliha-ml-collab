# Contributing

## Branching model
Work flows one way: short-lived branches -> dev -> staging -> main. Only main is production.
Nobody pushes directly to dev, staging or main. Everything goes through a reviewed pull request.

| Branch | Purpose | Created from | Merges into |
|---|---|---|---|
| main | Released, tagged models only | - | - |
| staging | Release candidate | main | main |
| dev | Integration of finished work | staging | staging |
| feat/<name> | Features and pipeline changes | dev | dev |
| data/<name> | Dataset updates tracked with DVC | dev | dev |
| exp/<member>-<idea> | Experiments; never merged directly | dev | nothing (cherry-pick the winner into a feat/ branch) |
| fix/<name> | Urgent fix to production | main | main, then back into dev |

Feature, data and fix branches are deleted after merge. Rebase on dev often.

## Commit messages (Conventional Commits)
Format: `type: short description`

Types we use: feat, fix, data, exp, docs, chore, test, ci.
Examples: `feat: add scaling step`, `data: remove duplicate rows`, `exp: try max_depth=8`.

## Merge strategy
PRs into dev are **squash-merged**: one commit per PR keeps dev history clean.
The PR title must follow the commit convention because it becomes the commit message.

## Pull requests
- Every PR is reviewed by the other teammate, who must fill in the review checklist.
- The reviewer checks out the branch and runs it at least once for PRs that change the pipeline.
- Each member authors at least 2 merged PRs and reviews at least 2.
- Never commit on behalf of another teammate.

## Data and models
- Data and model files are tracked with DVC, never with Git.
- Always run `dvc push` before `git push` if data or models changed.
- Never commit secrets or DVC remote credentials. Keep them in `.dvc/config.local` or environment variables.

## Experiments
- Run experiments only on committed code, so the logged commit SHA matches the code.
- Set seeds everywhere randomness occurs.
