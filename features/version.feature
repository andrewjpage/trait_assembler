Feature: Getting the version number

  @capture
  Scenario: We want to see the version task in the overall help text with no options
    Given we want to see the version
      When I run "trait_assembler"
      Then the command output should contain "Print version and exit"
	
  @capture     
  Scenario: We want to see the version task in the overall help text with minus h
    Given we want to see the version
      When I run "trait_assembler -h"
      Then the command output should contain "Print version and exit"
	
  @capture
  Scenario: We want the version number
    Given we want to see the version
      When I run "trait_assembler version"
      Then the output should contain a version number