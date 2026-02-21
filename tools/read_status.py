#!/usr/bin/env python3
"""
Read PIC Status

Quick tool to view current project status and completed work.

Usage:
    python3 tools/read_status.py           # Show recent status
    python3 tools/read_status.py --all     # Show full status
    python3 tools/read_status.py --summary # Show summary only
"""

import sys
from pathlib import Path
from datetime import datetime

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
STATUS_FILE = PROJECT_ROOT / "status" / "COMPLETED.md"


def read_status(mode="recent"):
    """Read and display project status."""
    if not STATUS_FILE.exists():
        print(f"❌ Status file not found: {STATUS_FILE}")
        return 1

    content = STATUS_FILE.read_text()
    lines = content.split('\n')

    if mode == "summary":
        # Show just the header and latest entry
        print('\n'.join(lines[:20]))
    elif mode == "recent":
        # Show header and first 2 entries
        print('\n'.join(lines[:80]))
    else:  # all
        # Show everything
        print(content)

    return 0


def main():
    """Main entry point."""
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return 0

    mode = "recent"
    if "--all" in sys.argv:
        mode = "all"
    elif "--summary" in sys.argv:
        mode = "summary"

    print(f"\n{'='*60}")
    print(f"PIC STATUS - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")

    return read_status(mode)


if __name__ == "__main__":
    sys.exit(main())
