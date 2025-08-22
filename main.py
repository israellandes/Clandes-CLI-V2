#!/usr/bin/env python3
"""
Clandes-CLI-V2: Minimal, focused AI agent
One workflow, done perfectly.
"""

import sys
from pathlib import Path

def main():
    """Entry point for the focused agent"""
    print("Clandes-CLI-V2: Starting from scratch")
    print("\nAvailable models:")
    print("1. Qwen2.5-7B-Instruct (4.4GB) - Fast, efficient")
    print("2. Qwen2.5-Coder-32B (19GB) - Powerful, specialized for code")
    
    models_dir = Path(__file__).parent / "models"
    if models_dir.exists():
        model_files = list(models_dir.glob("*.gguf"))
        print(f"\n✓ Found {len(model_files)} models ready to use")
    
    print("\nNext: Build one robust workflow with enforced contracts")
    return 0

if __name__ == "__main__":
    sys.exit(main())