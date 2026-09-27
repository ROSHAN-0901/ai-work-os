# 1. Work router

Cursor is where the job runs. The router is a folder, not a prompt I retype.

## The problem

The same kinds of jobs come back every week. A factor question. A disclosure section. A questionnaire. Without a router I was pasting last week's explanation into a new chat, and sometimes a whole workbook with it.

## What I set up

- **Skill.** One markdown playbook per job. The agent loads that file and not the others. See `.cursor/skills/`.
- **Agent.** A short brief that points at one skill. See `.cursor/agents/`.
- **Hook.** `.cursor/hooks/before_read_guard.py` runs before a file is read. It refuses `clients/`, `local/` and env files, so a client workbook cannot wander into the prompt.
- **Task.** `.cursor/MASTER_RULEBOOK.md` maps an ask to exactly one skill.

Claude does the draft inside Cursor. I do not keep a second copy of the method in a chat window.

## What changed

The start of the week is no longer an explanation. It is a task id. The private book has more rows than the three in this repo. Same rule: one row, one skill.
