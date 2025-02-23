# Проверяет, существует ли переданная команда
command_exists() {
  command -v "$@" >/dev/null 2>&1
}

command_exists git || {
fmt_error "git is not installed"
exit 1
}


if ! command_exists zsh; then
echo "${FMT_YELLOW}Zsh is not installed.${FMT_RESET} Please install zsh first."
exit 1
fi
