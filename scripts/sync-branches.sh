#!/usr/bin/env bash
set -euo pipefail

PUSH=false
if [ "${1:-}" = "--push" ]; then
  PUSH=true
fi

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "main" ]; then
  echo "Error: run this script from 'main' (currently on '$CURRENT_BRANCH')." >&2
  exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
  echo "Error: working tree is not clean. Commit or stash changes first." >&2
  exit 1
fi

SHORT_HEAD=$(git rev-parse --short HEAD)

for lang in it en-gb fr de; do
  if [ ! -d "locales/${lang}" ]; then
    echo "Skipping missing locales/${lang}"
    continue
  fi

  tree=$(git rev-parse "HEAD:locales/${lang}")
  msg="chore(${lang}): sync ${lang} package from main (${SHORT_HEAD})"

  if git show-ref --verify --quiet "refs/heads/${lang}"; then
    parent=$(git rev-parse "refs/heads/${lang}")
    parent_tree=$(git rev-parse "${parent}^{tree}")
    if [ "${tree}" = "${parent_tree}" ]; then
      echo "Branch '${lang}' is already up to date."
      continue
    fi
    commit=$(git commit-tree "${tree}" -p "${parent}" -m "${msg}")
  else
    commit=$(git commit-tree "${tree}" -m "${msg}")
  fi

  git update-ref "refs/heads/${lang}" "${commit}"
  echo "Updated local branch '${lang}' -> ${commit}"

  if [ "$PUSH" = true ]; then
    git push origin "refs/heads/${lang}:refs/heads/${lang}"
    echo "Pushed '${lang}' to origin."
  fi
done
