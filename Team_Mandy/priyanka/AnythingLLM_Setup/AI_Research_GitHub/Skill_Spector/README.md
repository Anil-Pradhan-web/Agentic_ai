\# Skill Spector



\## Overview



Skill Spector is a lightweight security scanner designed to analyze AI agent skills and identify potentially dangerous code patterns before execution.



It helps in checking downloaded AI skills for suspicious behavior and generates a vulnerability report.



\## Objective



The main objectives of Skill Spector are:



\- Analyze AI agent skills before execution

\- Detect potentially unsafe code patterns

\- Identify security risks in downloaded skills

\- Generate a vulnerability report for review



\## Features



\- File-based skill scanning

\- Detection of suspicious code patterns

\- Automated vulnerability report generation

\- Lightweight Python-based implementation



\## Detected Risk Patterns



The scanner checks for commonly risky patterns:



\- `subprocess`

\- `os.system`

\- `eval()`

\- `exec()`

\- `password`

\- `private\_key`

\- `secret`

\- `token`

\- `api\_key`



\## Project Structure



```

Skill\_Spector/

│

├── scanner.py

├── vulnerability\_report.md

├── skills/

│   └── test\_skill.py

├── README.md

└── venv/

```



\## Installation



Create a virtual environment:



```bash

python -m venv venv

```



Activate the environment:



Windows:



```bash

venv\\Scripts\\activate

```



\## Usage



Run the vulnerability scanner:



```bash

python scanner.py

```



After scanning, the tool generates:



```

vulnerability\_report.md

```



\## Testing



A sample skill file was created to test the scanner.



The scanner successfully detected the following risky patterns:



\- `subprocess`

\- `os.system`

\- `password`



Example vulnerability report:



```

\## skills\\test\_skill.py



\- Possible risky pattern found: subprocess

\- Possible risky pattern found: os.system

\- Possible risky pattern found: password

```



\## Future Improvements



\- Integration with OpenClaw/ClawHub skill repositories

\- Automatic skill downloading and scanning

\- Dependency vulnerability checking

\- Sandbox-based skill execution testing

\- Advanced AI-based threat detection



\## Conclusion



Skill Spector provides a basic security layer for AI agent ecosystems by identifying potentially harmful code patterns before executing external skills.

