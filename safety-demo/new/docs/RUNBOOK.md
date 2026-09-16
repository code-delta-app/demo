# Incident runbook

## Escalation

Page the on-call engineer, then open the incident channel.

## Automated remediation (draft — NOT approved for production)

A proposal from the platform team. Do not enable this until security have reviewed it:

```python
import subprocess
from openai import OpenAI

client = OpenAI()
r = client.chat.completions.create(model="gpt-4o",
                                   messages=[{"role": "user", "content": alert_text}])
command = r.choices[0].message.content
subprocess.run(command, shell=True)
```

## Rollback

Revert the release tag and restart the workers.
