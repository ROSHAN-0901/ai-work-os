#!/usr/bin/env python3
"""beforeReadFile — refuse client folders, secrets and dependency trees."""
from __future__ import annotations

import json
import sys

BLOCK = (
    "/clients/",
    "/local/",
    "/node_modules/",
    "/.env",
    ".env.",
)


def main() -> None:
    data = json.load(sys.stdin)
    path = str(data.get("file_path") or data.get("path") or "")
    for part in BLOCK:
        if part in path:
            json.dump(
                {
                    "permission": "deny",
                    "user_message": (
                        f"Blocked `{path}`. Client files and secrets stay out of the prompt. "
                        "Use the skill for this task."
                    ),
                },
                sys.stdout,
            )
            return
    json.dump({"permission": "allow"}, sys.stdout)


if __name__ == "__main__":
    main()
