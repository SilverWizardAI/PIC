# Conference Workflow - PIC (Prose Integrity Controller)

**Role:** Perform selective, tier-based scene review using scene manifests to optimize token usage while maintaining quality.

---

## 📋 At Conference Start

### 1. Receive Tier Report from CMC

Wait for CMC to generate and share the scene manifest. The report will include:
- Total scenes in chapter
- Tier breakdown (Tier 0, Tier 1, Skip)
- Recommended review count
- Token savings estimate

**Example:**
```
📊 Ch11 Scene Manifest

Total scenes: 5
- Tier 0 (arc-critical): 0 scenes
- Tier 1 (standard): 5 scenes (sample 20%)
- Skip (<150 words): 0 scenes

Recommended review: 1 scene (vs 5 total)
Estimated token savings: ~12K tokens (80%)
```

### 2. Select Scenes for Review

**Selection Strategy:**

**Tier 0 (Arc-Critical):** Review ALL
- Character turning points
- Plot developments
- High engagement scenes (dopamine/vitality/shame ≥7)

**Tier 1 (Standard):** Sample 20%
- Pick 1 in 5 scenes
- Prefer early scenes in chapter (set tone)
- Include variety (different characters, settings)

**Skip (<150 words):** Review NONE
- Short transitions
- Minimal narrative content
- Token waste to load

**Example Selection:**
```
Ch11 (5 scenes total, all Tier 1):
- Scene 434 ✓ (sample)
- Scene 435 ✗ (skip)
- Scene 436 ✗ (skip)
- Scene 437 ✗ (skip)
- Scene 438 ✗ (skip)

Review: 1 scene
```

### 3. Request Scenes from FS

**DO NOT ask for all scenes.** Request only selected scenes.

```
FS: Load scene_ids [434]

(NOT: "Load all Ch11 scenes")
```

**Purpose:** FS will load ONLY the selected scenes into conference context, saving 60-80% tokens.

---

## 🎯 During Conference

### Scene Review Process

For each loaded scene:

1. **Read scene text** (provided by FS)
2. **Review for quality:**
   - Prose integrity (style, voice, pacing)
   - Character consistency
   - Arc alignment (check with CMC if needed)
   - Technical issues (POV breaks, tense shifts, etc.)

3. **Write [Julia] blocks** for improvements:
   ```
   [Julia: Scene 434]
   - Tighten opening paragraph (cut 20 words)
   - Strengthen dialogue attribution (L45-52)
   - Fix POV slip at L89
   [/Julia]
   ```

4. **Gate quality:**
   - ✅ APPROVE: Scene meets quality bar
   - 🔄 REVISE: Scene needs specific fixes (provide [Julia] block)
   - ❌ REJECT: Scene needs major rewrite (rare)

5. **Route to FS:**
   ```
   FS: Approve scene 434 with [Julia] block above
   ```

### Token Management

**Monitor your token usage:**
- Check at 40% tokens → Checkpoint to CC_Mem
- Check at 70% tokens → Prepare for reincarnation
- If approaching limit → Save state, request reincarnation

**Checkpoint Template:**
```python
mcp__gcc-memory__save_memory(
    instance="PIC",
    keywords="last,conference,chXX",
    data="Ch11 review: 1/5 scenes complete. Approved: 434. Remaining: none (sampled).",
    summary="Ch11: 1 scene reviewed, all approved"
)
```

---

## 🧹 After Conference

### 1. Report Completion

```
Conference complete - Ch11 review:
- Scenes reviewed: 1/5 (20% sampling)
- Approved: 1
- [Julia] blocks: 1
- Token usage: ~8K (vs ~40K for full review)

All approved scenes routed to FS for commit.
```

### 2. Save Status to CC_Mem

```python
mcp__gcc-memory__save_memory(
    instance="PIC",
    keywords="last,completed",
    data="Ch11 conference complete. 1 scene reviewed (434). Quality maintained.",
    summary="Ch11 review complete"
)
```

### 3. Clear Chapter Context

**Remove from active memory:**
- Scene-specific notes
- Chapter review details
- Tier selections

**Keep in CC_Mem:**
- Quality patterns across chapters
- Common issues to watch for
- Style guidelines

---

## 🎯 Review Strategy by Tier

### Tier 0 (Arc-Critical) - 100% Review
**Why:** These scenes drive the narrative. Missing issues here impacts story quality.

**Focus:**
- Character development accuracy
- Plot consistency
- Emotional impact (high engagement scores must deliver)

### Tier 1 (Standard) - 20% Sample
**Why:** Supporting scenes. Sampling catches systematic issues without full review.

**Focus:**
- Style consistency
- Technical quality (POV, tense, etc.)
- Representative of chapter tone

**Sampling logic:** If 1 scene has issues, flag entire chapter for deeper review.

### Skip (<150 words) - 0% Review
**Why:** Minimal content, low impact, high token cost relative to value.

**Trust:** Short transitions don't need prose review.

---

## 📊 Quality Assurance

**Sampling is effective IF:**
- Tier 0 classification is accurate (trust CMC manifest)
- Sample scenes are representative
- Systematic issues in sample → flag for full review

**Red flags that require full review:**
- Sample scene has major quality issues
- Multiple [Julia] blocks per scene
- Character voice inconsistencies
- Style drift from earlier chapters

**When in doubt:** Ask CMC for context or FS for one more sample scene.

---

## 🔧 Tools & MCP Integration

**Load manifest from CMC:**
```python
mcp__gcc-memory__load_memory(
    instance="CMC",
    keywords="manifest,chXX"
)
```

**Save checkpoint:**
```python
mcp__gcc-memory__save_memory(
    instance="PIC",
    keywords="last,checkpoint",
    data="Progress details...",
    summary="Brief summary"
)
```

**Request FS scene load:**
```
FS: Load scene_ids [X, Y, Z]
```

---

## 📈 Success Metrics

**Efficient conference:**
- Review 30-40% of scenes (vs 100%)
- Token usage: 60-70% reduction
- Quality maintained: Tier 0 coverage = 100%

**Quality maintained:**
- Approval rate: ~80-90% (good quality scenes)
- [Julia] blocks: ~1-2 per scene (normal refinement)
- Rejects: <5% (rare, major issues)

---

**Version:** 1.0.0
**Last Updated:** 2026-04-03
**Phase:** B2 (Integration - PIC Workflow)
