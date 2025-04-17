# cfis-modul-git

# Exercise

The objective of this exercise is to get familiar with the `git stash` command. In a nutshell, you will learn how to use `git stash` to temporarily save changes in your working directory without committing them. This is useful when you need to switch branches or pull changes from a remote repository but don't want to commit your current changes yet.

# Instructions

First, write some text in the file called `Foo.txt`, but do not commit it. Then, try to switch to the `stashing\bar` branch. You will see that you cannot switch branches because you have uncommitted changes. To solve this, you will need to use the `git stash` command like this:

```bash
git stash 
```

Which is a shorter way of saying:

```bash
git stash push
```
This command will save your changes in a "stash" and allow you to switch branches. A stash is a temporary storage area for changes that you don't want to commit yet. You can think of it as a shelf where you can put your unfinished work until you're ready to deal with it. It is different from a commit because it doesn't create a permanent record in the repository's history. Instead, it allows you to save your changes temporarily and come back to them later.
After stashing your changes, you can switch to the `stashing\bar` branch. Once you are on the `stashing\bar` branch, you can do some work (add text, files, whatever you want), and then come back to the `stashing\main` branch. After that, you can apply the stashed changes to the `stashing\main` branch. To do this, you will need to use the `git stash apply` command like this:

```bash
git stash apply
```

or, if you want to delete the stash, you can use:

```bash
git stash pop
```
This command will apply the changes from the stash to your working directory and remove the stash from the stash list. If you want to keep the stash after applying it, you can use `git stash apply` instead of `git stash pop`. This way, you can apply the changes without removing them from the stash list.