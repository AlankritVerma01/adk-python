# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .tool_context import ToolContext


# TODO: make this internal, since user doesn't need to use this tool directly.
def transfer_to_agent(agent_name: str, tool_context: ToolContext):
  """Transfer the current conversation to another agent.

  This tool hands off control of the conversation to a different agent by
  setting `tool_context.actions.transfer_to_agent`. It accepts exactly two
  parameters and will ignore any others. Parameters such as `query`, 
  `temperature`, etc. belong in the LLM prompt, not here.

  Args:
    agent_name (str): The name of the agent to transfer control to.
    tool_context (ToolContext): The current tool‐context whose
      `actions.transfer_to_agent` field will be set.

  Returns:
    None
  """
  tool_context.actions.transfer_to_agent = agent_name
