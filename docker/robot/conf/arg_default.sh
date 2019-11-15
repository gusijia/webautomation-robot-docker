#!/bin/bash
# this file holds the conjoint arguments of all robot jobs.

echo -e "
--variablefile  $ROBOT_HOME/conf/var_default.py
--loglevel      INFO
--pythonpath    $ROBOT_HOME/lib
--pythonpath    $ROBOT_HOME/res
--extension     robot

# Adds a timestamp to all output files.
# --timestampoutputs

# import other file to overwrite this
# --argumentfile <file>
"
