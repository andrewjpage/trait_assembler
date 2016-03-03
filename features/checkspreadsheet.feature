Feature: Check an input spreadsheet is valid

  @capture
  Scenario: We want to see the checkspreadsheet task in the overall help text with no options
    Given we want to check a spreadsheet
    When I run "trait_assembler"
    Then the command output should contain "checkspreadsheet"
      
  @capture
  Scenario: We run checkspreadsheet without any input files
    Given we want to check a spreadsheet
    When I run "trait_assembler checkspreadsheet"
    Then the command output should contain "error: the following arguments are required: input_spreadsheet_filename"
    And it should fail
    
  @capture
  Scenario: We pass in a valid input file
    Given we want to check a spreadsheet
    When I run "trait_assembler checkspreadsheet ../features/data/one_single_ended.csv"
    Then the command output should contain "Valid file"
    And it should pass
    
  @capture
  Scenario: We pass in a file which doesnt exist
    Given we want to check a spreadsheet
    When I run "trait_assembler checkspreadsheet file_which_doesnt_exist"
    Then the command output should contain "Invalid file"
    And it should pass