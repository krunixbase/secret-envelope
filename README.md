# secret-envelope

Reference-grade format and tooling for storing secret shares without leaking structure or intent.

## Scope

This repository defines a minimal “envelope” structure for storing secret shares (e.g., produced by Shamir Secret Sharing) together with explicit metadata and validation rules.

## Non-goals

- Secret generation or recovery
- Secret share aggregation
- Encryption, key management, or backups
- Network features or remote storage

## Status

Early stage. Interfaces may change until v1.0.0.
