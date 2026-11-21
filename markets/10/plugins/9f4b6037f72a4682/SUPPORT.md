# FifthRow LCM support

LCM stands for Large Consulting Model, FifthRow's consulting-agent platform.

Contact **support@fifthrow.com** for connection, account, workflow, research or data-deletion questions. Include the client name/version, operation ID, approximate time and a nonconfidential description of the problem. Never send passwords, access tokens, OAuth client secrets or private customer documents.

## Connection

Connect `https://mcp.fifthrow.com/lcm/v1` as a remote Streamable HTTP MCP server and sign in through the browser OAuth flow. Refresh the client's tool catalog after server changes. If access expires or is revoked, reconnect through the client's connection settings. A company administrator may need to enable custom integrations.

## Background research

Research and App building can take several minutes; a multi-step App can take substantially longer. Keep the accepted operation ID. A timeout while monitoring does not mean the research stopped, and starting the same task again may duplicate work. Card progress is an approximate time estimate plus observed status, not a promised deadline. Native background Tasks, cards and automatic assistant continuation depend on the client.

## Results and sources

Long reports use lossless pages. The assistant can retrieve the original body through `read_run_output` or `read_document`, following continuation and version fields. The card displays all platform-returned sources and inspectable report details. Ask for a sourced explanation of the scope you need; summaries do not establish that every page was read.

## Data boundaries

Company workflows use the signed-in account's permissions. Answers questions and results enter a globally shared library; never submit confidential company content, private documents or personal records. Read [the privacy policy](https://www.fifthrow.com/privacy-policy) and [terms](https://www.fifthrow.com/terms-of-service). Contact support for account-specific deletion/export questions.

Directory availability and client feature support vary. A locally installed plugin does not imply that the public directory has approved or published it.
