from behave import *
from behave4cmd0 import command_steps,command_shell
from hamcrest import assert_that, matches_regexp
import os

command_shell.Command.COMMAND_MAP["trait_assembler"] = os.path.normpath("{0}/scripts/trait_assembler".format(os.path.join(os.path.dirname(__file__), "../..")))

@given(u'we want to see the version')
def step(context):
    pass

@then(u'the output should contain a version number')
def step_command_output_should_contain_text(context):
    assert_that(context.command_result.output, matches_regexp('\d+\.\d+\.\d+'))


