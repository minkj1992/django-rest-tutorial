# zsh .code 명령어 

`~/.zshrc`
```sh
# for VS code code command
code () { VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $* ;
```