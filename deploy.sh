#!/usr/bin/env bash

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, verion 2 ONLY.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ==== Check user and environment ====
function check_user() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "[\e[92mOK\e[39m] Not running as root"
    else
        echo -e "[\e[33mWARNING\e[39m] You really shouldn't be running this as root..."
    fi
}

# ==== Check compatibility ====
function check_compat() {

    # Check for ostype
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo -e "[\e[92mOK\e[39m] gnu/linux os detected"
        os="linux"
    else
        echo -e "[\e[31mERROR\e[39m] Sorry, non Gnu/Linux OS are not supported"
        os="$OSTYPE"
    fi

    # Check for Distribution
    distro=$(lsb_release -is)

    if [[ $distro == "Debian" ]]; then
        echo -e "[\e[92mOK\e[39m] Debian based distribution detected"
        distro="debased"
    elif [[ $distro == "Ubuntu" ]]; then
        echo -e "[\e[92mOK\e[39m] Debian based distribution detected"
        distro="debased"
    else
        echo -e "[\e[31mERROR\e[39m] Non debian distros are not supported!"
        distro="$(lsb_release -is)"
    fi

    if [[ $os == "linux" && $distro == "debased"  ]]; then
        echo -e "[\e[92mOK\e[39m] No platform errors were found."
    else
        echo -e "[\e[31mERROR\e[39m] There was a problem with either your OS
being $os or your distribution being $distro, cannot proceed."
        exit 1;
    fi
}

# ==== Check for Dependencies ====
function check_deps() {
    for name in python3 pipenv
    do
        [[ $(which $name 2>/dev/null) ]] || { echo -en "[\e[31mERROR\e[39m] $name was not found";deps=1; }
    done
    [[ $deps -ne 1 ]] && echo -e "[\e[92mOK\e[39m] All dependencies are installed." || { echo -en "\nInstall the missing dependencies and rerun this script\n";exit 1; }
}

# ==== Main function ====
function main() {
    clear
    echo -e "\e[34mhttps://upvent.codes\e[39m deployment script - UpVent Codes 2021"
    echo "------------------------------------------------------------------"
    echo "Checking running user and privileges"
    echo "------------------------------------------------------------------"
    check_user;
    echo "------------------------------------------------------------------"
    echo "Checking for compatibility [OS and Distribution]"
    echo "------------------------------------------------------------------"
    check_compat;
    echo "------------------------------------------------------------------"
    echo "Checking if all dependencies are installed"
    echo "------------------------------------------------------------------"
    check_deps;
}

# Run script
main;
