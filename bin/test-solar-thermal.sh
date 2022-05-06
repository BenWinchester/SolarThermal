#!/usr/bin/env bash
########################################################################################
# test-solar-thermal.sh - Runs a series of tests across the system.                    #
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################

echo "Running test suite: black, mypy, pylint and pytest."

# Black formatter.
echo -e "Running black...\e[0m"
python3.7 -m black src || echo -e "\e[1m\033[91mBlack failed.\e[0m"
echo -e "\e[1mBlack formatter done, see above for details.\e[0m\n"

# Mypy type checker.
echo -e "\e[1mRunning mypy...\e[0m"
python3.7 -m mypy src || echo -e "\e[1m\033[91mMypy failed.\e[0m"
echo -e "\e[1mMypy done, see above for details.\e[0m\n"

# Pylint linter.
echo -e "\e[1mRunning pylint...\e[0m"
python3.7 -m pylint src || echo -e "\e[1m\033[91mPylint failed.\e[0m"
echo -e "\e[1mPylint done, see above for details.\e[0m\n"

# YAML linter.
echo -e "\e[1mRunning yamllint...\e[0m"
yamllint -c .yamllint-config.yaml src/ || echo -e "\e[1m\033[91mYamllint failed.\e[0m"
echo -e "\e[1mYamllint done, see above for details.\e[0m\n"

# Automated Python test suite.
echo -e "\e[1mRunning pytest...\e[0m"
python3.7 -m pytest src || if [ $? != 5 ] ; then
    echo -e "\e[1m\033[91mPytest failed\e[0m\n"
fi
echo -e "\e[1mTest suite complete: see above stdout for details.\e[0m"
