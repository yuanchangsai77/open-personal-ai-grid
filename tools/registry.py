from tools.ledger import add_expense

TOOLS = {
    "ledger.add_expense": add_expense
}


def call_tool(name, params):

    if name not in TOOLS:
        return "tool not found"

    return TOOLS[name](**params)