# DWDS-MCP-Artefact
# AfCFTA RoO — DWDS & MCP Prototype

Artefact for 7005SCN Individual Research Project.
Author: Obonganwan Akpabio (SID: 16742655)

## Contents
- `mcp_server.py` — MCP server exposing Rule Reserve as discoverable AI tools
- `rules/` — DWDS IOR-format rule files for Article 8A and Article 10
- `test-data/` — sample product documents used for validation

## Note on Rule Reserve / Rule Taker
This project reuses the open-source Rule Reserve/Rule Taker components
maintained by the Xalgorithms Alliance:
https://gitlab.com/xalgorithms-alliance/rule-networking-software/prod-impl

A parser fix (Section 4.10 of the report) was applied locally to
`parser.rs` to resolve a silent assertion-parsing defect. 
