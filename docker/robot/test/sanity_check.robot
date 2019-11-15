*** Variables ***

*** Settings ***
Library  SanityCheck

*** Test Cases ***

| Ping all machines should succeed
| | [Template] | Ping machine should succeed
| | se-hub
| | se-node-ch
