## Show the working tree status
```
git
```

## Viewing the commit history (press 'q' to exit)
```
git log
```

## Viewing the source tree (press 'q' to exit)
```
git log --color --graph --all --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

## Adding a remote
```
git add <remote name> <remote url>
```

## Develope workflow:
```
git checkout master
git pull --rebase origin master
git checkout -b <new-branch>
# modify something & commit
git push <remote name> <branch-name>
# open PR
```
> why we use 'git pull --rebase'
> 1. https://ihower.tw/blog/archives/3843
> 2. https://stackoverflow.com/questions/2472254/when-should-i-use-git-pull-rebase