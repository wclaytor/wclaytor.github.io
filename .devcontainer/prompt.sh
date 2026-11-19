#!/usr/bin/env bash
# prompt.sh - a custom Bash prompt that shortens long Git branch names.
#
# Install (once after each container rebuild):
#   bash .devcontainer/prompt.sh
#   This adds one line to ~/.bashrc that loads this file in every new shell.
#   Running it again does nothing if the line is already there.
#
# Try different options:
#   1. Comment or uncomment lines in the OPTIONS section below.
#   2. Open a new terminal, or run: source .devcontainer/prompt.sh
#
# Default result:
#   ubuntu ➜ /workspaces/job-tracker (102-update-dashboard...) $

# --- Install mode: the script was run, not sourced -----------------------------
if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    script_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
    if grep -qF "$script_path" ~/.bashrc 2>/dev/null; then
        echo "✅ ~/.bashrc already loads $script_path"
    else
        printf '\n# Custom prompt (see %s)\n[ -f "%s" ] && source "%s"\n' \
            "$script_path" "$script_path" "$script_path" >> ~/.bashrc
        echo "✅ Added prompt to ~/.bashrc. Open a new terminal to see it."
    fi
    exit 0
fi

# Clear options from any earlier load, so a commented-out line really turns off.
unset PROMPT_BRANCH_MAX PROMPT_BRANCH_STYLE PROMPT_THEME PROMPT_DIR_STYLE \
      PROMPT_TWO_LINE PROMPT_SYMBOL PROMPT_DURATION_MIN "${!PROMPT_SHOW_@}"

# ================================== OPTIONS ===================================
# Lines that start with "#" are off. Remove the "#" to turn an option on.

# --- Branch name ---
PROMPT_BRANCH_MAX=20            # Shorten branch names longer than this. 0 = never shorten.
PROMPT_BRANCH_STYLE=end         # end:    (102-update-dashboard...)
# PROMPT_BRANCH_STYLE=middle    # middle: (102-update...anban-view)

# --- Git details ---
# PROMPT_SHOW_DIRTY=1           # ✗  you have uncommitted or untracked changes
# PROMPT_SHOW_AHEAD_BEHIND=1    # ↑2 ↓1  commits ahead of / behind the remote branch
# PROMPT_SHOW_STASH=1           # ≡3  number of stashed changes

# --- Context ---
PROMPT_SHOW_USER=1              # ubuntu (or @your-github-name in Codespaces)
# PROMPT_SHOW_TIME=1            # 14:05:32  when the prompt appeared
# PROMPT_SHOW_EXIT_CODE=1       # ✘ 1  exit code of the last command, only when it failed
# PROMPT_SHOW_DURATION=1        # took 1m 12s  for slow commands
PROMPT_DURATION_MIN=2           #   ...that ran at least this many seconds
# PROMPT_SHOW_VENV=1            # (.venv)  active Python virtual environment

# --- Layout ---
PROMPT_DIRTRIM=4                # Show at most this many folders, e.g. .../docs/notes/2026/11
# PROMPT_DIR_STYLE=repo         # Show the path from the repo root: job-tracker/docs/notes
# PROMPT_TWO_LINE=1             # Type commands on a second line, below the details
PROMPT_SYMBOL='$'               # The character before your cursor
# PROMPT_SYMBOL='❯'
# PROMPT_SYMBOL='λ'

# --- Colours ---
PROMPT_THEME=devcontainer       # The standard dev container colours
# PROMPT_THEME=ocean            # Blues and greens
# PROMPT_THEME=sunset           # Oranges and purples
# PROMPT_THEME=mono             # No colour
# ================================ END OPTIONS =================================

# Wraps a colour code so Bash does not count it as visible text.
__prompt_color() { [[ "$PROMPT_THEME" == mono ]] && return; printf '\001\033[%sm\002' "$1"; }

__prompt_theme() {
    local user dir branch extra
    case "$PROMPT_THEME" in
        ocean)  user='0;32' dir='1;36' branch='1;34' extra='0;37' ;;
        sunset) user='0;33' dir='1;35' branch='1;33' extra='0;95' ;;
        *)      user='0;32' dir='1;34' branch='1;31' extra='0;36' ;;
    esac
    __pc_reset=$(__prompt_color 0)
    __pc_user=$(__prompt_color "$user")
    __pc_dir=$(__prompt_color "$dir")
    __pc_branch=$(__prompt_color "$branch")
    __pc_extra=$(__prompt_color "$extra")
    __pc_ok=$(__prompt_color 0)
    __pc_err=$(__prompt_color '1;31')
    __pc_warn=$(__prompt_color '1;33')
    __pc_dim=$(__prompt_color '0;90')
}

# Shortens a branch name to PROMPT_BRANCH_MAX characters plus "...".
__prompt_shorten() {
    local name="$1" max="${PROMPT_BRANCH_MAX:-0}"
    if (( max <= 0 || ${#name} <= max )); then
        printf '%s' "$name"
    elif [[ "$PROMPT_BRANCH_STYLE" == middle ]]; then
        local head=$(( max / 2 )) tail=$(( max - max / 2 ))
        printf '%s...%s' "${name:0:head}" "${name: -tail}"
    else
        printf '%s...' "${name:0:max}"
    fi
}

# Builds the Git part of the prompt, for example: (102-update-dashboard... ✗ ↑1)
__prompt_git() {
    __prompt_git_text=""
    [[ "$(git config --get devcontainers-theme.hide-status 2>/dev/null)" == 1 ]] && return
    [[ "$(git config --get codespaces-theme.hide-status 2>/dev/null)" == 1 ]] && return

    local branch="" dirty="" ahead=0 behind=0 line
    if [[ -n "$PROMPT_SHOW_DIRTY$PROMPT_SHOW_AHEAD_BEHIND" ]]; then
        # One git call gives the branch, ahead/behind counts, and changed files.
        local status
        status="$(git --no-optional-locks status --porcelain=v2 --branch 2>/dev/null)" || return
        while IFS= read -r line; do
            case "$line" in
                '# branch.head '*) branch="${line#\# branch.head }" ;;
                '# branch.ab '*)   read -r _ _ ahead behind <<< "$line"
                                   ahead="${ahead#+}" behind="${behind#-}" ;;
                '#'*) ;;
                *) dirty=1 ;;
            esac
        done <<< "$status"
        [[ "$branch" == "(detached)" ]] && branch="$(git rev-parse --short HEAD 2>/dev/null)"
    else
        branch="$(git --no-optional-locks symbolic-ref --short HEAD 2>/dev/null \
               || git --no-optional-locks rev-parse --short HEAD 2>/dev/null)"
    fi
    [[ -z "$branch" ]] && return

    local text="${__pc_extra}(${__pc_branch}$(__prompt_shorten "$branch")"
    [[ -n "$PROMPT_SHOW_DIRTY" && -n "$dirty" ]] && text+=" ${__pc_warn}✗"
    if [[ -n "$PROMPT_SHOW_AHEAD_BEHIND" ]]; then
        (( ahead > 0 ))  && text+=" ${__pc_extra}↑${ahead}"
        (( behind > 0 )) && text+=" ${__pc_extra}↓${behind}"
    fi
    if [[ -n "$PROMPT_SHOW_STASH" ]]; then
        local stashes
        stashes="$(git --no-optional-locks stash list 2>/dev/null | wc -l)"
        (( stashes > 0 )) && text+=" ${__pc_extra}≡${stashes}"
    fi
    __prompt_git_text="${text}${__pc_extra})${__pc_reset} "
}

# Formats seconds as "45s", "1m 12s", or "2h 5m".
__prompt_duration() {
    local s="$1"
    if (( s >= 3600 )); then printf '%dh %dm' $(( s / 3600 )) $(( s % 3600 / 60 ))
    elif (( s >= 60 )); then printf '%dm %ds' $(( s / 60 )) $(( s % 60 ))
    else printf '%ds' "$s"
    fi
}

# Runs before each prompt and rebuilds PS1.
__prompt_build() {
    local exit_code=$?
    __prompt_theme

    # Text that comes from outside (branch, folder, venv names) goes into
    # variables that PS1 refers to by name, so Bash never runs it as code.
    __prompt_git_text="" __prompt_info="" __prompt_dir=""
    __prompt_git

    if [[ -n "$PROMPT_SHOW_EXIT_CODE" ]] && (( exit_code != 0 )); then
        __prompt_info+="${__pc_err}✘ ${exit_code}${__pc_reset} "
    fi
    if [[ -n "$PROMPT_SHOW_DURATION" && -n "$__prompt_start" ]]; then
        local took=$(( SECONDS - __prompt_start ))
        (( took >= ${PROMPT_DURATION_MIN:-2} )) &&
            __prompt_info+="${__pc_dim}took $(__prompt_duration "$took")${__pc_reset} "
    fi
    unset __prompt_start

    if [[ "$PROMPT_DIR_STYLE" == repo ]]; then
        local top
        top="$(git rev-parse --show-toplevel 2>/dev/null)"
        [[ -n "$top" ]] && __prompt_dir="${top##*/}${PWD#"$top"}"
    fi

    local ps=""
    [[ -n "$PROMPT_SHOW_TIME" ]] && ps+="${__pc_dim}\t${__pc_reset} "
    if [[ -n "$PROMPT_SHOW_VENV" && -n "$VIRTUAL_ENV" ]]; then
        __prompt_venv="(${VIRTUAL_ENV##*/}) "
        ps+="${__pc_extra}\${__prompt_venv}${__pc_reset}"
    fi
    if [[ -n "$PROMPT_SHOW_USER" ]]; then
        if [[ -n "${GITHUB_USER:-}" ]]; then ps+="${__pc_user}@${GITHUB_USER} "
        else ps+="${__pc_user}\u "
        fi
    fi
    # The arrow turns red when the last command failed.
    if (( exit_code != 0 )); then ps+="${__pc_err}➜ " ; else ps+="${__pc_ok}➜ "; fi
    if [[ -n "$__prompt_dir" ]]; then ps+="${__pc_dir}\${__prompt_dir} "
    else ps+="${__pc_dir}\w "
    fi
    ps+="\${__prompt_git_text}\${__prompt_info}${__pc_reset}"

    if [[ -n "$PROMPT_TWO_LINE" ]]; then
        ps+="\n${__pc_dim}╰─${__pc_reset}"
    fi
    PS1="${ps}${PROMPT_SYMBOL:-\$} "
}

# Apply the options.
[[ -n "$PROMPT_SHOW_VENV" ]] && export VIRTUAL_ENV_DISABLE_PROMPT=1

# Record when each command starts, for PROMPT_SHOW_DURATION. PS0 is shown just
# before a command runs; this expands to nothing but sets __prompt_start.
if [[ -n "$PROMPT_SHOW_DURATION" ]]; then
    # Bash skips the arithmetic if __prompt_noop is unset, so set it to "".
    __prompt_noop=""
    PS0='${__prompt_noop:0:$((__prompt_start=SECONDS, 0))}'
elif [[ "$PS0" == *__prompt_start* ]]; then
    PS0=""
fi

# Run __prompt_build first, so it sees the real exit code. Add it only once.
if [[ "$PROMPT_COMMAND" != *__prompt_build* ]]; then
    PROMPT_COMMAND="__prompt_build${PROMPT_COMMAND:+; $PROMPT_COMMAND}"
fi
