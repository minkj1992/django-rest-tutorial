# zsh와 pyenv를 통한 python 버전 충돌

[참고자료](https://lhy.kr/configuring-the-python-development-environment-with-pyenv-and-virtualenv)


## zsh .code 명령어 

~/.zshrc
```sh
# for VS code code command
code () { VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $* ;
```