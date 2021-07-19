#!/bin/bash

# just a mock version of what our hc update should look like

# take the cli args to indicate pass or fail
pf="mock_upgrade"

echo "Beginning verification for mock_upgrade"

if [ $# -eq 0 ] ; then
    echo "$pf: No fail arg provided, defaulting to pass (0)"
    exit 0
fi

if [ "$1" == "fail" ];
then 
    echo "$pf: verify FAILED (exiting with 1)"
    exit 1
else
    echo "$pf: verify PASSED (exiting with 0)"
    exit 0
fi
