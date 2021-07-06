#!/usr/bin/env bash

# ==== Check compatibility ====
function check_compat() {

    # Check for ostype
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo -e "[\e[92mOK\e[39m] Gnu/Linux OS detected"
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
    echo "TODO"
}

# ==== Main function ====
function main() {
    clear
    echo -e "\e[34mhttps://upvent.codes\e[39m deployment script - UpVent Codes 2021"
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
