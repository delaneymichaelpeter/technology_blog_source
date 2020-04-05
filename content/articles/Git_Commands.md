Title: GIT Commands
Date: 2020-01-22 10:20
Modified: 2010-01-22 19:30
Tags: linux, git
Slug: goto-git-commands
Authors: Peter Delaney 
Summary: Commands that I use when working with GIT on the command line


## Initialize GIT Project  and send to GitHub
```git
# Initialize your project
git init

# Push project to GitHub
git remote add orgian https://github.com/delaneymichaelpeter/<my-new-project>.git


```


## Create a new Local Branch
```git
# Pull latest from master/branch creating from
git pull

# Create Branch
git checkout -b <name-of-branch>


# List local Branches
git branch

# Checkout an Existing branch
git checkout <name-of-branch>

# Push local branch to Remote Repository
git push orign <name-of-branch> 

```

## Merge Branch to master/branch
```git
# Add any new files to your branch
git add <files>

# Commit your changes to local branch
git commit -m "put comments here"

# Merge back into branch; this will move back to your new branch
git branch <branch-to-merge-to>

# Get latest from remote
git fetch <name-of-remote-branch>

# Merge locally
git  ??????


```







