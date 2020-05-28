# my_scripts
Small scripts to automate some stuff from terminal in my computer.

## All python scripts here are available in my terminal
I have included following in my .bash_profile so that all python scripts in this repo are available by first name in my terminal from anywhere.
```
for file in ~/Git/my_scripts/*.py;
do
  alias ${${file##*/}/.py/}="python "$file
done
```
