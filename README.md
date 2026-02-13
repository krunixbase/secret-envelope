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

This project is designed to interoperate with the sealed `shamir` v1.0.0
reference implementation.

The envelope format and tooling are stable in scope, but this repository
is not yet sealed as a reference artifact. Future changes are expected to
be additive and versioned.

