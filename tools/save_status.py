#!/usr/bin/env python3
"""
Save PIC Status

Interactive tool to add new entries to the status log.

Usage:
    python3 tools/save_status.py

Will prompt for:
- Session title
- Summary
- Changes made
- Next steps (optional)
"""

import sys
from pathlib import Path
from datetime import datetime

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
STATUS_FILE = PROJECT_ROOT / "status" / "COMPLETED.md"


def get_multiline_input(prompt):
    """Get multiline input from user."""
    print(f"\n{prompt}")
    print("(Enter a blank line to finish)")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return '\n'.join(lines)


def create_status_entry():
    """Create a new status entry interactively."""
    print("\n" + "="*60)
    print("NEW STATUS ENTRY")
    print("="*60)

    # Get session info
    title = input("\nSession title: ").strip()
    if not title:
        print("❌ Title required")
        return None

    status = input("Status (✅ COMPLETE / 🚧 IN PROGRESS / ⏸️ PAUSED): ").strip()
    if not status:
        status = "🚧 IN PROGRESS"

    summary = get_multiline_input("\nSummary (what was accomplished):")
    if not summary:
        print("❌ Summary required")
        return None

    changes = get_multiline_input("\nChanges made (files, sections, etc.):")
    next_steps = get_multiline_input("\nNext steps (optional):")

    # Build entry
    today = datetime.now().strftime('%Y-%m-%d')
    entry = f"""
## {title} - {today}

**Date:** {today}
**Status:** {status}

### Summary

{summary}

### Changes Made

{changes}
"""

    if next_steps:
        entry += f"""
### Next Steps

{next_steps}
"""

    entry += "\n---\n"

    return entry


def save_status_entry(entry):
    """Insert entry at the top of the status file."""
    if not STATUS_FILE.exists():
        print(f"❌ Status file not found: {STATUS_FILE}")
        return False

    content = STATUS_FILE.read_text()
    lines = content.split('\n')

    # Find where to insert (after header and last updated)
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.startswith('---') and i > 0:
            insert_pos = i + 1
            break

    # Update "Last Updated" timestamp
    for i, line in enumerate(lines):
        if line.startswith('**Last Updated:**'):
            lines[i] = f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}"
            break

    # Insert new entry
    lines.insert(insert_pos, entry)

    # Write back
    STATUS_FILE.write_text('\n'.join(lines))
    return True


def main():
    """Main entry point."""
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return 0

    print("\n" + "="*60)
    print("PIC STATUS UPDATER")
    print("="*60)

    entry = create_status_entry()
    if not entry:
        return 1

    print("\n" + "="*60)
    print("PREVIEW")
    print("="*60)
    print(entry)

    confirm = input("\nSave this entry? (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ Cancelled")
        return 0

    if save_status_entry(entry):
        print(f"\n✅ Status entry saved to {STATUS_FILE}")
        return 0
    else:
        print("\n❌ Failed to save entry")
        return 1


if __name__ == "__main__":
    sys.exit(main())
