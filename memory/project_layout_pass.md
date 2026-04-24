---
name: Paragraph Layout Pass — Manuscript Cleanup
description: Workflow for semantic paragraph reformatting of the full Forbidden Spice manuscript using CMC-built tools
type: project
---

PIC runs a paragraph layout pass on the full manuscript using two tools built by CMC.

**Why:** Word/PDF conversion produces chapters with poor paragraph layout — either walls of text (multiple beats crammed together) or over-fragmented micro-paragraphs. Needs LLM semantic analysis to fix.

**How to apply:** When started for this task, loop through scenes using the get/save tools CMC built, applying the rules below to each scene.

## Tool workflow
- Get tool: fetches one scene at a time from the manuscript DB
- Save tool: writes the cleaned text back (separate column, original preserved)
- Loop until all scenes processed

## Layout rules
1. **Strip trailing/multiple spaces** — any runs of spaces before a line ending, collapse mid-line double-spaces to single
2. **Paragraphs stay as one long unwrapped line** — Word wraps them; do not add soft wraps
3. **One blank line between paragraphs**
4. **Split** paragraphs that contain multiple distinct beats (action shift, emotional register change, new focus)
5. **Merge** paragraphs that are the same beat split arbitrarily — especially orphaned one-liners that are direct qualifications or continuations of the sentence above
6. **Do NOT change words** — no edits beyond whitespace and paragraph boundaries

## What NOT to merge
- Deliberately short paragraphs used for punch/emphasis (e.g. "He always does." / "He had no idea.")
- Sofia's clipped voice fragments — they are intentional register, not accidents
- Dialogue exchanges — each speaker gets their own paragraph
- [Sofia]...[/Sofia] blocks are preserved as-is structurally

## ✅ PASS COMPLETE — 2026-04-24

All 183 scenes processed through C6_PIC_Cleaned. Ch08 was pre-done (C6_PDF_Cleanup).

**Fixes applied during the pass:**
- Ch09 S6: Removed duplicate [Sofia] block created by normalization pass
- Ch09 S9: Pronoun fix inside [Sofia] block ("around her" → "around me")
- Ch09 multiple: "Zurich" → "Zürich" (missing umlaut)
- Ch11 S1: "Carole ." → "Carole." (extra space); `---` separator fix
- Ch11 S2: `---` separator concatenated to text — fixed
- Ch02 S1: "Ans with that" → "And with that" (typo in [Sofia] block)
- Ch01 S2: "Her orgasm" → "her orgasm" (spurious capital)
- Ch13 S8: 3 collapsed paragraphs split into 10 semantic paragraphs
- Ch03–Ch13: Re-paragraphing throughout where normalization collapsed multiple beats

**Remaining fix (pre-publish):**
- Ch05 S2: "Benoit" → "Laurent" (single word, body text contradicts scene heading) — **still needs fixing**
- Ch15 S11: "2:09" → "2:05" in [Sofia] block (timeline inconsistency with Suite 1247) — **fixed by Steve 2026-04-24**

**Next step:** CMC to regenerate EPUB + print PDF from database (C6_PIC_Cleaned versions), then final layout check and KDP upload.
