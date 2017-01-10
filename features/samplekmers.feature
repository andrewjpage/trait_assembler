Feature: Running KMC over a bunch of samples and putting the results in separate directories

  @capture
  Scenario: We want to see the samplekmers task in the overall help text with no options
    Given we want to see the samplekmers task
    When I run "trait_assembler"
    Then the command output should contain "Create a KMC database"
    And it should pass
	
  @capture     
  Scenario: We want to see the samplekmers task in the overall help text with minus h
    Given we want to see the version
    When I run "trait_assembler -h"
    Then the command output should contain "Create a KMC database"
    And it should pass
	
  @capture
  Scenario: We want to see the help text for the samplekmers task
    Given we want to see the version
    When I run "trait_assembler samplekmers"
    Then the command output should contain " "
    And it should pass
    