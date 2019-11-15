#!/bin/bash

source $CONF_DIR/arg_default.sh

echo -e "
# --doc           This is an example (where "special characters" are ok!)
# --loglevel      INFO
--outputdir     $LOG_DIR
--debugfile     $LOG_DIR/debugfile.txt
--variablefile  $ROBOT_HOME/conf/var_linux_gc.py

# Selects the test cases by name
# --test <name>
# Selects the test suites by name
# --suite <name>

# --include <tag>
# --exclude <tag>

# test cases path
$ROBOT_HOME/test/sanity_check.robot
$ROBOT_HOME/test/web_regression.robot
"
