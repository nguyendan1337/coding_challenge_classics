# balance_ledger_reconciliation_challenge.py
"""
STRIPE HACKERRANK OA - BALANCE LEDGER RECONCILIATION (MaaS / MMS Team)
=====================================================================

You are implementing the core **Balance Ledger Reconciliation** engine used by Stripe’s Money Movement and Storage platform.

This system reconciles the **expected ledger balance** (what our internal records say) against **actual money-movement events** (charges, refunds, payouts, fees, etc.).

Input:
- opening_balance: Dict[str, int]   → currency → amount in cents (starting balance)
- events: List[Dict]                → list of money movement events in arrival order

Each event has:
{
    "event_id": str,          # unique, used for idempotency
    "type": str,              # "charge", "refund", "payout", "fee", "adjustment"
    "amount": int,            # cents (positive for all)
    "currency": str,
    "related_id": str or None # e.g. payout_id or charge_id for refunds
}

=== PROGRESSIVE PARTS (implement ONE function that solves all parts) ===

Part 1: Basic Reconciliation
- Start with opening_balance
- For each event: add/subtract amount from ledger balance
  • charge → +amount (money in)
  • refund → -amount (money out)
  • payout → -amount (money out)
  • fee → -amount
  • adjustment → +amount or -amount depending on sign (but amount is always positive here)

Part 2: Event Types & Sign Logic
- Full sign rules:
    - "charge"      → +amount
    - "refund"      → -amount
    - "payout"      → -amount
    - "fee"         → -amount
    - "adjustment"  → +amount (always credit)
- Ignore unknown event types silently

Part 3: Idempotency + Sequential Processing
- Skip any event whose "event_id" has already been seen
- Process events in the exact order they arrive
- Support multiple currencies

Part 4: Discrepancy Detection & Report (Production Requirement)
- After processing all events, compute final_ledger_balance
- Return a reconciliation report:
    Tuple[Dict[str, int], Dict[str, Any]]
    (final_ledger, report)
- report = {
    "status": "balanced" | "discrepancy",
    "discrepancies": List[Dict]   # only if status == "discrepancy"
    "processed_events": int
  }
- discrepancy example: {"currency": "USD", "expected": 10000, "actual": 9500, "difference": 500}

Strict rules:
- Do NOT mutate any input data
- Return deep copies
- Must be 100% correct — incorrect reconciliation at Stripe scale costs millions

Return Value:
    Tuple[Dict[str, int], Dict[str, Any]]
"""

from typing import Dict, List, Tuple, Any
from copy import deepcopy

def reconcile_ledger(opening_balance: Dict[str, int], events: List[Dict[str, Any]]) -> Tuple[Dict[str, int], Dict[str, Any]]:
    # TODO: Implement full logic for Parts 1–4 here
    pass


# ========================= RUNNABLE TEST CASES =========================
if __name__ == "__main__":
    print("Running Stripe Balance Ledger Reconciliation OA tests...\n")

    # Test data
    opening = {"USD": 10000, "EUR": 5000}

    events1 = [
        {"event_id": "evt1", "type": "charge", "amount": 3000, "currency": "USD"},
        {"event_id": "evt2", "type": "payout", "amount": 2000, "currency": "USD"},
        {"event_id": "evt3", "type": "fee",    "amount": 50,   "currency": "USD"},
    ]

    result1 = reconcile_ledger(opening, events1)
    final_bal, report = result1
    assert final_bal["USD"] == 10000 + 3000 - 2000 - 50 == 7950
    assert report["status"] == "balanced"
    print("✓ Parts 1–3 passed")

    # Part 4 - Discrepancy
    events2 = events1 + [
        {"event_id": "evt4", "type": "refund", "amount": 1000, "currency": "USD"},
        {"event_id": "evt1", "type": "charge", "amount": 500, "currency": "USD"},  # duplicate → ignored
    ]
    result2 = reconcile_ledger(opening, events2)
    final_bal2, report2 = result2
    assert report2["status"] == "balanced"
    assert report2["processed_events"] == 4
    print("✓ Part 4 passed (idempotency + discrepancy report)")

    print("\n🎉 All 4 parts passed! This is exactly the style used for MaaS balance reconciliation OAs.")