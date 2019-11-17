#!/bin/bash
# this file holds the arguments of all robot jobs.

echo -e "
--variablefile  $ROBOT_HOME/conf/var_default.py
--loglevel      INFO
--pythonpath    $ROBOT_HOME/lib
--pythonpath    $ROBOT_HOME/res
--extension     robot
--outputdir     $LOG_DIR
--debugfile     $LOG_DIR/debugfile.txt
--report        NONE

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
