"""
Stripe-Style Ledger System (HARD MODE)

You are building a simplified financial ledger system similar to Stripe.

This system must correctly handle:
- Idempotent transactions
- Failed debit handling
- Audit logging
- Reconciliation with external systems

------------------------------------------------
Transaction Format:
------------------------------------------------
txn = {
    "id": str,
    "account_id": str,
    "amount": int,
    "type": "credit" | "debit"
}

------------------------------------------------
Part 1: Apply Transaction
------------------------------------------------
Implement:
    apply_transaction(txn)

Rules:
- Transactions must be idempotent (same txn_id processed once)
- Credit always succeeds
- Debit succeeds only if sufficient balance exists
- Failed debits must NOT modify balance
- Every transaction must be recorded in an audit log with status

Status values:
- "SUCCESS"
- "FAILED"
- "IGNORED" (duplicate txn)

------------------------------------------------
Part 2: Balance Query
------------------------------------------------
get_balance(account_id) -> int

- Missing accounts return 0

------------------------------------------------
Part 3: Reconciliation
------------------------------------------------
reconcile(account_id, external_balance) -> dict

Return:
{
    "internal": int,
    "external": int,
    "difference": external - internal
}

------------------------------------------------
Part 4: Audit Log
------------------------------------------------
get_audit_log() -> list
Returns all processed transaction records
"""

class Ledger:
    def __init__(self):
        # TODO:
        # - store balances per account
        # - store processed transaction IDs for idempotency
        self.accounts = {}
        self.transaction_history = set()
        self.txn_status = {}
        self.audit_log = []


    def apply_transaction(self, txn):
        """
        txn = {
            "id": str,
            "account_id": str,
            "amount": int,
            "type": "credit" or "debit"
        }
        """
        # TODO:
        # 1. Check if txn["id"] already processed → if yes, ignore
        # 2. Get current balance (default 0)
        # 3. If debit:
        #       - ensure balance >= amount
        #       - if not, reject
        # 4. Apply update
        # 5. Save transaction id
        txn_id = txn["id"]
        account_id = txn["account_id"]
        status = None

        if txn_id in self.transaction_history:
            status = "IGNORED"
            self.txn_status[txn_id] = status
            return

        if account_id not in self.accounts:
            self.accounts[account_id] = 0

        current_balance = self.accounts[account_id]

        if txn["type"] == "credit":
            current_balance += txn["amount"]
            status = "SUCCESS"
        elif txn["type"] == "debit":
            if txn["amount"] <= current_balance:
                current_balance -= txn["amount"]
                status = "SUCCESS"
            else:
                status = "FAILED"

        self.accounts[account_id] = current_balance
        self.txn_status[txn_id] = status
        if status == "SUCCESS":
            self.transaction_history.add(txn_id)
        self.audit_log.append({
            "id": txn_id,
            "account_id": account_id,
            "type": txn["type"],
            "amount": txn["amount"],
            "status": status
        })

    def get_balance(self, account_id):
        # TODO:
        # return balance (default 0)
        return self.accounts.get(account_id, 0)


    def reconcile(self, account_id, external_balance):
        # TODO:
        # return external_balance - internal_balance
        return {
            "internal": self.accounts.get(account_id, 0),
            "external": external_balance,
            "difference": external_balance - self.accounts[account_id]
        }

    def get_audit_log(self):
        return self.audit_log


# ---------- TEST CASES ----------
ledger = Ledger()

# ----------------------------
# Basic credit
# ----------------------------
ledger.apply_transaction({
    "id": "t1",
    "account_id": "A",
    "amount": 100,
    "type": "credit"
})

assert ledger.get_balance("A") == 100

# ----------------------------
# Valid debit
# ----------------------------
ledger.apply_transaction({
    "id": "t2",
    "account_id": "A",
    "amount": 30,
    "type": "debit"
})

assert ledger.get_balance("A") == 70

# ----------------------------
# Duplicate transaction (ignored)
# ----------------------------
ledger.apply_transaction({
    "id": "t2",
    "account_id": "A",
    "amount": 30,
    "type": "debit"
})

assert ledger.get_balance("A") == 70

# ----------------------------
# Failed debit (insufficient funds)
# ----------------------------
ledger.apply_transaction({
    "id": "t3",
    "account_id": "A",
    "amount": 100,
    "type": "debit"
})

assert ledger.get_balance("A") == 70

# status tracking
audit = ledger.get_audit_log()
statuses = {t["id"]: t["status"] for t in audit}

assert statuses["t1"] == "SUCCESS"
assert statuses["t2"] == "SUCCESS"
assert statuses["t3"] == "FAILED"

# ----------------------------
# Reconciliation
# ----------------------------
result = ledger.reconcile("A", 80)

assert result["internal"] == 70
assert result["external"] == 80
assert result["difference"] == 10

print("Stripe-level ledger tests passed!")