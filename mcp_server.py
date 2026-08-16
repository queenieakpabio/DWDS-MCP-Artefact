import subprocess
import json
import re
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("xalgorithms-rules")

PROD_IMPL_DIR = "/home/obong/prod-impl"

def run_binary(binary: str, args: list[str]) -> str:
    result = subprocess.run(
        [f"{PROD_IMPL_DIR}/target/debug/{binary}"] + args,
        cwd=PROD_IMPL_DIR,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.stdout + result.stderr


@mcp.tool()
def select_applicable_rules(document_json: str) -> str:
    """
    Given a document as a JSON string, returns which ingested rules
    are applicable (by jurisdiction, time window, and matching keys).
    """
    doc_path = "/tmp/mcp_doc.json"
    with open(doc_path, "w") as f:
        f.write(document_json)

    output = run_binary("select", [doc_path])
    return output


@mcp.tool()
def invoke_rule(document_json: str, rule_id: str, rule_rev: int) -> str:
    """
    Applies a specific rule (by id and revision) to a document and
    returns the resulting assertions ("ought" conclusions).
    """
    doc_path = "/tmp/mcp_doc.json"
    with open(doc_path, "w") as f:
        f.write(document_json)

    output = run_binary("invoke", [doc_path, rule_id, str(rule_rev)])

    # Get just lists of assertions from the result
    match = re.search(r"asserts=(\[.*\])", output, re.DOTALL)
    conclusion = match.group(1) if match else output

    return conclusion


@mcp.tool()
def ingest_rule(rule_text: str) -> str:
    """
    Ingests a new rule written in the IOR format (PROPERTIES / IN EFFECT /
    CONDITIONS / ASSERTIONS sections). Returns the rule id and revision.
    """
    rule_path = "/tmp/mcp_ingest_rule.txt"
    with open(rule_path, "w") as f:
        f.write(rule_text)

    output = run_binary("ingest", [rule_path])
    return output


if __name__ == "__main__":
    mcp.run()
