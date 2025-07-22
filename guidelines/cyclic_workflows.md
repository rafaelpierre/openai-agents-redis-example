### Implementing Cyclic Workflows with OpenAI Agents SDK

You **can implement cyclic (repetitive, looping) workflows** using the OpenAI Agents SDK. The core of the SDK is built around the concept of an “agent loop,” which is designed to repeatedly call tools, send results back to the model, and continue this process until a final result is achieved or specific stop criteria are met[^1_1][^1_2][^1_3][^1_4].

#### How the Agent Loop Works

- **Loop Execution:** When you trigger an agent run, the SDK manages a cycle where the agent:
    - Calls tools based on instructions and context.
    - Interprets results from tools.
    - Updates its state/history.
    - Decides whether to continue looping, hand off to another agent, or produce a final output.
- **Stopping Criteria:** The loop continues until:
    - The agent returns a clearly defined final output.
    - A handoff is triggered to route the workflow to another agent.
    - A guardrail (safety, validation, or max turn limit) halts execution[^1_1][^1_2][^1_3].


#### Features Facilitating Cyclic Workflows

- **Handoffs:** Allow complex workflows where multiple agents coordinate, delegate, and even return control to a main orchestrator—enabling not just cycles within a single agent but loops across multiple agents[^1_2][^1_5].
- **Guardrails:** You can set safety checks or limits for iterations (such as a max turns parameter) to avoid infinite loops or unwanted behavior[^1_6].
- **State Management:** The SDK automatically maintains the agent’s conversation or task state throughout the loop, which supports multi-step, iterative workflows[^1_1][^1_3].
- **Tracing:** Built-in tracing allows you to visualize and debug these loops and identify where cyclic processes occur or terminate[^1_1][^1_3].


#### Typical Patterns Enabled

- **Iterative Task Execution:** Agents can repeatedly apply tools or strategies, such as iterative code review, document editing, or process optimization, until success or a stopping rule is met.
- **Multi-Agent Coordination:** You can implement orchestrator patterns where control is passed back and forth between agents (for example, review and revision cycles in content generation)[^1_2][^1_5].
- **LLM Feedback Loops:** It's possible to set up workflows where outputs are generated and iteratively improved based on feedback, forming an intelligent cycle for refining results[^1_2].


#### Example: Simplified Flow

1. Agent receives an initial input.
2. Agent processes input and potentially calls tools.
3. If more work is needed:
    - Tool results are appended to state/history, and the agent runs another cycle.
    - Optionally, control can be handed off and then returned for further cycles.
4. The loop terminates on final output or when a guardrail is tripped (e.g., max iterations)[^1_1][^1_6][^1_3].

#### Summary Table: Key SDK Capabilities for Cyclic Workflows

| Feature | Supports Cyclic Workflows? | Notes |
| :-- | :--: | :-- |
| Agent Loop | Yes | Automatic looping until completion |
| Handoffs | Yes | Enables multi-agent cycles |
| Guardrails | Yes | Prevents infinite or undesired loops |
| State Management | Yes | Maintains workflow context across cycles |
| Tracing | Yes | Debug and inspect loop behavior |

**In conclusion:** The OpenAI Agents SDK explicitly supports and encourages the implementation of cyclic workflows, both within single agents and across multi-agent orchestrations. This is managed via the agent loop, handoff logic, and built-in safeguards, making it suitable for advanced iterative AI-driven applications[^1_1][^1_2][^1_3].

<div style="text-align: center">⁂</div>

[^1_1]: https://composio.dev/blog/openai-agents-sdk-vs-langgraph-vs-autogen-vs-crewai

[^1_2]: https://blog.agen.cy/p/openai-agents-sdk-a-comprehensive

[^1_3]: https://openai.github.io/openai-agents-python/

[^1_4]: https://platform.openai.com/docs/guides/agents-sdk

[^1_5]: https://pkg.go.dev/github.com/pontus-devoteam/agent-sdk-go/examples/openai_advanced_workflow

[^1_6]: https://www.npmjs.com/package/@openai/agents

[^1_7]: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf

[^1_8]: https://humanloop.com/blog/openai-agents-sdk

[^1_9]: https://www.linkedin.com/posts/shehroz-hanif-60441727a_openai-agentssdk-agentloop-activity-7329979541735497728--SqB

[^1_10]: https://openai.com/index/new-tools-for-building-agents/

[^1_11]: https://openai.github.io/openai-agents-js/guides/quickstart/

[^1_12]: https://www.reddit.com/r/LangChain/comments/1g1pkki/openais_new_framework_for_agents_why_is_langgraph/

[^1_13]: https://dev.to/ivor/openais-agent-building-guide-summary-56jg

[^1_14]: https://sdtimes.com/ai/openai-reveals-responses-api-agents-sdk-for-building-agentic-experiences/

[^1_15]: https://www.youtube.com/watch?v=DvlGKovbMu0\&vl=fr

[^1_16]: https://openai.github.io/openai-agents-python/running_agents/

[^1_17]: https://www.linkedin.com/posts/imvinayc_4-key-lessons-after-building-with-the-openai-activity-7350720769397542912-R2xa

[^1_18]: https://community.openai.com/t/agents-sdk-modifying-messages-array-mid-loop-during-a-single-run/1247114

[^1_19]: https://www.youtube.com/watch?v=eA9heVJqtq8

[^1_20]: https://community.openai.com/t/sharing-an-agentic-workflow-to-build-vertical-agents-with-openai-agents-sdk/1180989


---

## Cyclic Handoffs and Controlled Iteration in OpenAI Agents SDK

You can set up two agents that hand off control to each other with the OpenAI Agents SDK, and it is possible to control how many times each agent is handed off control, but this requires explicit workflow management.

### How Agent Handoffs Work

- **Handoffs** let one agent delegate the entire conversation or task to another, transferring full control between agents.
- Handoffs are defined using the `handoffs` parameter or via a `handoff()` function that allows adding custom logic, input filters, and callbacks[^2_1][^2_2][^2_3].


### Two Agents Handing Off to Each Other

- You can configure both agents to list each other in their respective `handoffs` parameter, enabling each to delegate back to the other as required[^2_2].
- This creates the potential for cyclic or iterative workflows if each agent's instructions or handoff logic is set up accordingly.


### Controlling Handoff Count (Iteration Limit)

- While SDK handoffs natively allow transfer of control, **iteration limits or "handoff counts" are not intrinsic SDK features**. Instead, you must manage limits using one of these approaches:
    - **Custom Guardrails**: Use SDK mechanisms (or your own code) to count handoffs by tracking state, and enforce a maximum by instructing agents to stop or change behavior when the limit is reached.
    - **on_handoff Callback**: The `on_handoff` callback feature can be used to increment a counter or check a condition with each handoff event. If the limit is reached, you could halt further handoffs or direct the agent to produce a final output instead[^2_1][^2_4].
    - **History and Input Filtering**: Input filters can be used to propagate custom state or counters through each agent’s context, letting you communicate and check local "handoff count" state at each step[^2_1][^2_3][^2_4].
    - **Prompt Engineering**: You can instruct each agent to only hand off a limited number of times using careful prompting, though this is less robust than code-level guardrails.


#### Example Pattern

| Component | Functionality |
| :-- | :-- |
| Agent A | Handoff to Agent B, checks or updates a counter |
| Agent B | Handoff to Agent A, checks or updates a counter |
| on_handoff | Custom callback to increment/check iteration |
| Guardrails | Code or SDK-enforced max turn/handoff limit |

If each agent's code or prompt is configured properly, you can enforce "no more than N handoffs between agents" by stopping or producing output when the allowed number is reached.

### Limitations and Recommendations

- There is no single built-in `max_handoffs` parameter; controlling the loop count is always a matter of custom logic.
- Use the SDK’s `on_handoff` and history state to propagate and enforce limits reliably; avoid relying solely on AI instructions when enforcing strict iteration limits[^2_1][^2_4].
- Careful design prevents infinite recursion and keeps agent cycles controlled and explainable.

**Summary:**
You can configure two agents in the OpenAI Agents SDK to hand off to each other and, with careful use of callbacks, input filters, or state tracking, strictly control how many times each agent is handed off control[^2_1][^2_4][^2_2].

<div style="text-align: center">⁂</div>

[^2_1]: https://openai.github.io/openai-agents-python/handoffs/

[^2_2]: https://blog.arcade.dev/openai-agents-sdk-how-to-build-a-multi-agent-system-for-gmail-and-slack

[^2_3]: https://openai.github.io/openai-agents-js/guides/handoffs/

[^2_4]: https://www.geeky-gadgets.com/openai-agents-sdk-guide/

[^2_5]: https://openai.github.io/openai-agents-js/openai/agents/functions/handoff/

[^2_6]: https://www.youtube.com/watch?v=LuarehusOWU

[^2_7]: https://cookbook.openai.com/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration

[^2_8]: https://www.linkedin.com/pulse/understanding-handoffs-vs-agents-as-tools-openais-agents-majid-sheikh-cvxgf

[^2_9]: https://github.com/openai/openai-agents-python/issues/256

[^2_10]: https://apidog.com/blog/how-to-use-openai-agents-sdk/

[^2_11]: https://www.linkedin.com/pulse/guide-build-openai-agents-sdk-multi-agent-sales-team-hai-nghiem-gcnle

[^2_12]: https://openai.github.io/openai-agents-python/ref/handoffs/

[^2_13]: https://hexdocs.pm/openai_agents/OpenAI.Agents.Handoff.html

[^2_14]: https://www.siddharthbharath.com/openai-agents-sdk/

[^2_15]: https://cookbook.openai.com/examples/agents_sdk/dispute_agent

[^2_16]: https://learn.microsoft.com/en-us/azure/databricks/mlflow3/genai/tracing/integrations/openai-agent

[^2_17]: https://github.com/openai/openai-agents-python/issues/123

[^2_18]: https://community.openai.com/t/openai-agents-sdk-handoffs-cant-iterate-am-i-right/1235072

[^2_19]: https://www.linkedin.com/pulse/openai-agents-sdk-step-by-step-guide-building-your-first-hai-nghiem-oouwc

[^2_20]: https://openai.com/index/new-tools-for-building-agents/


---

## Limiting Handoff Counts Per Agent in OpenAI Agents SDK

The OpenAI Agents SDK does not offer a dedicated built-in parameter (such as `max_handoffs`) to directly limit the handoff count **per agent**. However, you can achieve this type of control using the SDK’s flexibility with callbacks, state, and tool customization.

### Approaches to Limit Handoffs for Each Agent

#### 1. Custom State Tracking

- Use a shared state object (such as a dictionary or an input payload) to record how many times each agent has been handed control.
- Pass this state with each handoff, and increment a per-agent counter.
- Agents check the counter on each invocation and avoid further handoffs or switch behavior once their individual handoff count limit is reached[^3_1][^3_2].


#### 2. `on_handoff` Callback

- Leverage the `on_handoff` callback when configuring a handoff.
- Increment a persistent counter associated with the specific agent each time control is handed off.
- If the count meets or exceeds the desired limit, alter the workflow—block further handoffs, issue a final output, or reroute the conversation[^3_1][^3_2].


#### 3. Input Filtering and Guardrails

- Use input filters to inject and propagate per-agent handoff counters through the workflow as part of agent context.
- Create "guardrails" in your logic or within each agent’s instructions to check the counter and enforce handoff limits at runtime[^3_1][^3_3][^3_2].


#### 4. Prompt Engineering (Not Robust)

- Instruct agents via explicit prompt instructions, e.g., “You may only hand off to Agent B three times.” However, this method is more vulnerable to LLM unpredictability and should be complemented with programmatic guards[^3_2].


### Example Pattern (Python-Style Pseudocode)

```python
state = {"AgentA_handoffs": 0, "AgentB_handoffs": 0}

def agent_a_on_handoff(ctx):
    state["AgentA_handoffs"] += 1
    if state["AgentA_handoffs"] >= MAX_AGENT_A_HANDOFFS:
        # Block or reroute further handoffs

def agent_b_on_handoff(ctx):
    state["AgentB_handoffs"] += 1
    if state["AgentB_handoffs"] >= MAX_AGENT_B_HANDOFFS:
        # Block or reroute further handoffs

AgentA = Agent(name="A", handoffs=[handoff(B, on_handoff=agent_a_on_handoff)])
AgentB = Agent(name="B", handoffs=[handoff(A, on_handoff=agent_b_on_handoff)])
```

You would expand this to pass state via the agent context or input filters[^3_1][^3_2].

### Summary Table

| Method | Granular Per-Agent Control? | Notes |
| :-- | :--: | :-- |
| State Tracking | Yes | Most flexible, explicit per-agent logic |
| on_handoff Callback | Yes | Directly count per agent |
| Input Filter/Guardrail | Yes | Propagates limits through agent context |
| Prompt Engineering | No* | Unreliable—supplement with other methods |

(*) Prompting alone is not recommended for strict enforcement.

### Key Points

- You **must manage per-agent handoff limits in your own code**, using state or callback mechanisms—SDK does not do this for you automatically.
- Use the `on_handoff` callback and/or input filters to enforce and propagate these limits[^3_1][^3_2].
- Always update and check state each time a handoff occurs for fine-grained control over each agent’s maximum allowed participations.

This pattern is robust for enforcing workflow boundaries, preventing infinite loops, or implementing custom cyclic collaboration logic within agentic applications[^3_1][^3_2].

**References:**
[^3_1] Handoffs - OpenAI Agents SDK
[^3_3] Running agents | OpenAI Agents SDK - GitHub Pages
[^3_2] OpenAI Agents SDK Handoffs Tutorial for Smarter AI Collaboration

<div style="text-align: center">⁂</div>

[^3_1]: https://openai.github.io/openai-agents-python/handoffs/

[^3_2]: https://www.geeky-gadgets.com/openai-agents-sdk-guide/

[^3_3]: https://openai.github.io/openai-agents-js/guides/running-agents/

[^3_4]: https://cookbook.openai.com/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration

[^3_5]: https://www.siddharthbharath.com/openai-agents-sdk/

[^3_6]: https://hexdocs.pm/openai_agents/OpenAI.Agents.Handoff.html

[^3_7]: https://developer.mamezou-tech.com/en/blogs/2025/03/23/openai-agents-sdk-intro/

[^3_8]: https://www.youtube.com/watch?v=LuarehusOWU

[^3_9]: https://apidog.com/blog/how-to-use-openai-agents-sdk/

[^3_10]: https://github.com/openai/openai-agents-python/issues/256

[^3_11]: https://community.openai.com/t/agents-sdk-looping-handoffs/1256231

[^3_12]: https://towardsdatascience.com/build-multi-agent-apps-with-openais-agent-sdk/

[^3_13]: https://openai.github.io/openai-agents-python/ref/run/

[^3_14]: https://pub.towardsai.net/openais-agent-sdk-f58dfec89f5b

[^3_15]: https://openai.github.io/openai-agents-js/openai/agents/classes/usage/

[^3_16]: https://openai.github.io/openai-agents-python/ref/handoffs/

[^3_17]: https://www.aibusinessasia.com/en/p/how-openai-agents-sdk-can-automate-91-of-your-work/

[^3_18]: https://www.npmjs.com/package/@openai/agents

[^3_19]: https://openai.github.io/openai-agents-js/openai/agents-core/classes/handoff/

[^3_20]: https://community.openai.com/t/agents-sdk-handoffs-tools-across-multiple-agents/1213811


---

## Example: `on_handoff` Callback with State Management for Handoff Counting

To keep track of how many times an agent is invoked via handoff within a specific conversation or session using the OpenAI Agents SDK, use a combination of the optional `on_handoff` callback and a shared state object (such as a dictionary or custom context). Below is a Python-style example based on the SDK’s callback API.

### 1. Define Shared State

You’ll need a state container to persist data between handoffs. This is typically injected into each agent’s run context or stored globally for the session.

```python
# Shared state per session (could be stored in a DB or session object)
conversation_state = {
    "agent_X_handoff_count": 0
}
```


### 2. Create the Callback

The `on_handoff` function receives the run context (often a `RunContextWrapper`) and, if needed, any structured input data for the handoff. You would increment your count here:

```python
from agents import handoff, Agent, RunContextWrapper

async def on_handoff_count_x(ctx: RunContextWrapper):
    # Increment the per-session counter
    if "agent_X_handoff_count" not in ctx.session_state:
        ctx.session_state["agent_X_handoff_count"] = 0
    ctx.session_state["agent_X_handoff_count"] += 1

    print(f"Agent X handoff count for this session: {ctx.session_state['agent_X_handoff_count']}")
    # Optional: enforce a maximum or take action if a limit is reached
    # if ctx.session_state["agent_X_handoff_count"] > MAX_HANDOFFS:
    #     raise Exception("Max handoffs reached for Agent X")
```

**Note:** The `session_state` is a suggested attribute; adapt based on your SDK version and how you pass/run context.

### 3. Attach Callback to Handoff

Wrap your agent handoff using the `handoff()` helper and provide the callback:

```python
agent_X = Agent(name="Agent X", ...)
agent_Y = Agent(name="Agent Y", handoffs=[
    handoff(agent=agent_X, on_handoff=on_handoff_count_x)
])
```

When Agent Y hands off to Agent X, the callback executes and updates the count.

### 4. Access or Act on the State

Anywhere in the workflow, you can read (or enforce limits using) the current per-session handoff count:

```python
current_count = ctx.session_state.get("agent_X_handoff_count", 0)
if current_count >= 5:
    # Block further handoffs, alert, or change behavior.
    ...
```


### Summary Table: What Happens

| Step | What Occurs | Where |
| :-- | :-- | :-- |
| 1 | State object created per session | Outside agents |
| 2 | Callback increments state on handoff | `on_handoff` |
| 3 | Handoff wired up with callback | Agent definition |
| 4 | State checked to enforce logic/limits | Callback or agent |

**References:**
SDK documentation on handoffs, callbacks, and state[^4_1][^4_2][^4_3].

- The SDK lets you define `on_handoff` callbacks for custom per-agent logic at each handoff[^4_1][^4_2].
- Use the run/session context to persist and update per-conversation state, such as handoff counts[^4_1][^4_2][^4_3].

This approach ensures accurate, session-specific tracking and granular control of agent invocation in complex workflows.

<div style="text-align: center">⁂</div>

[^4_1]: https://openai.github.io/openai-agents-python/handoffs/

[^4_2]: https://www.datacamp.com/tutorial/openai-agents-sdk-tutorial

[^4_3]: https://www.linkedin.com/pulse/guide-build-openai-agents-sdk-multi-agent-sales-team-hai-nghiem-gcnle

[^4_4]: https://openai.github.io/openai-agents-js/guides/handoffs/

[^4_5]: https://www.youtube.com/watch?v=LuarehusOWU

[^4_6]: https://codesignal.com/learn/courses/coordinating-openai-agents-workflows-in-python/lessons/customizing-agent-handoffs-with-validation-and-callbacks

[^4_7]: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/state.html

[^4_8]: https://blog.agen.cy/p/openai-agents-sdk-a-comprehensive

[^4_9]: https://cookbook.openai.com/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration

[^4_10]: https://openai.github.io/openai-agents-python/

[^4_11]: https://github.com/openai/openai-agents-python/issues/69

[^4_12]: https://www.geeky-gadgets.com/openai-agents-sdk-guide/

[^4_13]: https://openai.github.io/openai-agents-python/agents/

[^4_14]: https://github.com/openai/openai-agents-python/issues/256

[^4_15]: https://openai.com/index/new-tools-for-building-agents/

[^4_16]: https://www.marktechpost.com/2025/07/14/tracing-openai-agent-responses-using-mlflow/

[^4_17]: https://community.openai.com/t/fun-with-agents-simple-example-of-an-agent-hand-off/1142697

[^4_18]: https://www.linkedin.com/pulse/openai-agent-sdk-adding-state-data-toagents-dennis-layton-o7syc

[^4_19]: https://www.npmjs.com/package/@openai/agents

[^4_20]: https://velog.io/@jieun9851/OpenAI-Agent-SDK-Handoff-란

