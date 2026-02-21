# PIC - Publisher in Chief

**Quick Reference Brief**

---

## What Is This?

AI-assisted manuscript editorial review system using Claude to perform deep chapter-by-chapter analysis following professional publishing methodology.

---

## Key Files

| File | Purpose |
|------|---------|
| **PUBLISHER_IN_CHIEF.md** | Full editorial methodology & role definition |
| **working_notes.md** | Cumulative manuscript analysis (108KB) |
| **Ch##_critique.md** | Individual chapter critiques |
| **status/COMPLETED.md** | Progress tracking |

---

## Quick Commands

```bash
# View status
python3 tools/read_status.py

# Add status entry
python3 tools/save_status.py

# View editorial brief
cat PUBLISHER_IN_CHIEF.md

# Check progress
git log --oneline
```

---

## Current Progress

- ✅ Chapters 1-7 critiqued
- ✅ Detailed Model 7 edits for Ch01
- ✅ Comprehensive notes for Ch01-03
- 🚧 Ongoing chapter-by-chapter review

---

## Editorial Approach

**Role:** Seasoned publishing professional (30 years experience)
**Focus:** Commercial viability + literary excellence
**Philosophy:** "You are not here to be encouraging. You are here to be right."

---

## Review Framework

Each chapter covers:
- Narrative Arc
- Character Development
- Voice & Style
- Commercial Viability
- Technical Craft
- Strategic Recommendations

---

## Workflow

1. Load context (PUBLISHER_IN_CHIEF.md + working_notes.md)
2. Read chapter
3. Perform analysis
4. Write critique
5. Update working notes
6. Save status
7. Commit to git

---

## Repository

**GitHub:** https://github.com/SilverWizardAI/PIC
**Organization:** Silver Wizard Software
**License:** MIT

---

**See README.md for full documentation.**
