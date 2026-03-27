## 📖 REQUIRED READING AT STARTUP

**Read this EVERY session (first thing):**
- `/PIC/PUBLISHER_IN_CHIEF.md` — Your role, Model 7 requirements, workflow

Then explain your role in 10 lines (as specified in that document). Never re-explain beyond that.

---

## ☁️ Afterlife — Token Monitoring & Reincarnation

You are a TCC (Terminal Claude Code) managed by MC4CCI. When your token budget is running low,
you MUST request reincarnation so work can continue in a fresh session.

**Your token threshold: 50%**
When Claude Code shows your token usage at or above 50%, trigger reincarnation.

**How to request reincarnation (send to the dedicated reincarnation inbox):**
```bash
python3 .claude/tools/send_message.py MC4CCI_REINCARNATION "Reincarnation Request" '{"request": "reincarnate", "agent_name": "PIC", "startup_message": "YOUR STATE SUMMARY"}'
```

**Writing a good startup_message — include ALL of:**
1. What task you were working on and its goal
2. What you have completed so far (with file paths)
3. What the next concrete action is
4. Any key decisions already made (so the new session doesn't reverse them)
5. Any blockers or dependencies to be aware of

Example:
```
"Writing blog post about X for Silver Wizard. Draft is 60% done at /drafts/X.md.
Sections 1-2 complete. Next: write section 3 on Y, then proofread.
Decision: use casual conversational tone throughout."
```

After sending, MC4CCI will kill this session and spawn a new TCC using your startup_message
as the initial prompt. The new session will pick up exactly where you left off.

**Check token usage:** Watch the Claude Code status bar. When it shows 50%+, act immediately.



---

## 📬 Messaging Other TCCs — Use MM Broker ONLY

**MM Broker is the ONLY correct channel for TCC-to-TCC communication.**

```bash
# Send a message to another TCC
python3 .claude/tools/send_message.py <AgentName> "Subject" '{"key": "value"}'

# Check your inbox
python3 .claude/tools/check_messages.py --all
```

**Available agents:** `EE`, `Brand_Manager`, `MC4CCI`

> ⚠️ MM Mesh (port 6001) is a service registry for shared MCP servers — it is NOT a
> messaging system and does NOT show whether other TCCs are online or reachable.
> Do not use MM Mesh to check TCC availability. Use MM Broker send/check instead.
---

## 🔌 Available MCP Tools

**Global MCP Servers** (configured in `~/.claude/mcp_config.json`):

**All global MCP servers use `g-` prefix for easy identification.**

**gcc-memory** - Global CC Memory (Persistent Session Memory):
- `mcp__gcc-memory__save_memory(instance, keywords, data)` - Save memory
- `mcp__gcc-memory__load_memory(instance, keywords)` - Load memory
- `mcp__gcc-memory__last_saves(instance, count)` - See recent save history
- `mcp__gcc-memory__query_memory(query_type)` - Cross-instance queries

**gpyqt-instrument** - Global PyQt Instrument (UI Testing):
- `mcp__gpyqt-instrument__qt_connect()` - Connect to PyQt app
- `mcp__gpyqt-instrument__qt_snapshot()` - Get widget tree
- `mcp__gpyqt-instrument__qt_click(ref)` - Click widgets

**CRITICAL:** Global MCP servers are configured in `~/.claude/mcp_config.json`.
DO NOT add them to project-level settings.json - they inherit automatically.
