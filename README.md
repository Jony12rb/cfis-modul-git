# cfis-modul-git

# Introduction

In this exercise, you will start to use `git rebase`, one of git's most powerful features. Rebase can be used for:

- Rewriting history
- Merging branches
- Squashing commits
- Splitting commits
- Cherry-picking commits
- Changing commit messages and order
- Fixing merge conflicts
- and much more!

Only a few of these options will be used in this exercise. The goal is to get familiar with the basic usage of `git rebase` and to understand how it works. You will also learn how to use `git rebase` to clean up your commit history, which is usually useful.

*ATTENTION:* This repository is public, which means that rebasing a really, _really_, bad idea. We are doing this for educational purposes only. In a real-world scenario, you should never rebase a public branch. If you want to learn more about this, check out the [Git documentation](https://git-scm.com/docs/git-rebase).

# Exercise

In this branch, you can see, among others, the following commits (from oldest to newest):

- `Add program to print data.`
- `add data`
- `Fix bug in code.`

There are a few thing that are wrong with this commit history:

- The second commit is not orthographically correct. It should be `Add data.`. 
- The last commit fixes a bug that should not exist in the first place. It should be removed from the history.
- It does not make sense to have a program that print data without having data to print. We should reorder the commits so that the data is added before the program is added.

Your task is to learn how to do all of this using `git rebase`. 