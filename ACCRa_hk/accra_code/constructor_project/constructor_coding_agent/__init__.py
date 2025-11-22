"""
Constructor Coding Agent - Responsible for:
- Managing execution sandboxes (Docker)
- Generating test scripts using LLM
- Executing code and capturing outputs
- Extracting visualizations
"""

from .sandbox.sandbox_manager import (
    SandboxManager,
    SandboxType,
    SandboxConfig,
    ExecutionResult,
)

__all__ = [
    "SandboxManager",
    "SandboxType",
    "SandboxConfig",
    "ExecutionResult",
]
