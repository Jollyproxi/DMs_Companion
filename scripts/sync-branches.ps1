<#
.SYNOPSIS
    Publishes each folder under locales/<lang>/ to its standalone orphan branch (it, en-gb, fr, de).
.DESCRIPTION
    Run from the main branch with a clean working tree. Each language branch receives the exact
    contents of locales/<lang>/ at its root without sharing commit history with main or other languages.
#>
[CmdletBinding()]
param(
    [string[]]$Languages = @('it', 'en-gb', 'fr', 'de'),
    [switch]$Push
)

$ErrorActionPreference = 'Stop'

$currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
if ($currentBranch -ne 'main') {
    throw "Please run this script from 'main' (currently on '$currentBranch')."
}

$dirty = git status --porcelain
if ($dirty) {
    throw "Working tree is not clean. Commit or stash changes on 'main' before syncing branches."
}

$shortHead = (git rev-parse --short HEAD).Trim()

foreach ($lang in $Languages) {
    $localePath = "locales/$lang"
    if (-not (Test-Path $localePath)) {
        Write-Warning "Skipping missing directory: $localePath"
        continue
    }

    $tree = (git rev-parse "HEAD:$localePath").Trim()
    $msg = "chore($lang): sync $lang package from main ($shortHead)"

    $existingRef = $null
    git show-ref --verify --quiet "refs/heads/$lang"
    if ($LASTEXITCODE -eq 0) {
        $existingRef = (git rev-parse "refs/heads/$lang").Trim()
        $existingTree = (git rev-parse "$existingRef^{tree}").Trim()
        if ($tree -eq $existingTree) {
            Write-Host "Branch '$lang' is already up to date."
            continue
        }
        $commit = (git commit-tree $tree -p $existingRef -m $msg).Trim()
    } else {
        $commit = (git commit-tree $tree -m $msg).Trim()
    }

    git update-ref "refs/heads/$lang" $commit
    Write-Host "Updated local branch '$lang' -> $commit"

    if ($Push) {
        git push origin "refs/heads/${lang}:refs/heads/${lang}"
        Write-Host "Pushed '$lang' to origin."
    }
}
