# chargebacks_challenge.py
"""
STRIPE HACKERRANK OA - CHARGEBACKS / DISPUTE PROCESSING (MaaS / MMS Team)
========================================================================

You are building the **Chargeback & Dispute Engine** that processes real-time chargeback events and updates merchant balances and payment statuses.

This is one of the most common OA topics for financial backend roles at Stripe.

Input:
- payments: Dict[str, Dict]          → payment_id → payment object (initial state)
- chargeback_events: List[Dict]      → list of incoming chargeback events in arrival order

Each payment starts as:
{"payment_id": str, "amount": int, "currency": str, "status": "succeeded", "balance_impact": int}

Each chargeback event:
{
    "event_id": str,           # for idempotency
    "type": "chargeback",      # always this for now
    "payment_id": str,
    "amount": int,             # disputed amount in cents
    "currency": str,
    "fee": int                 # chargeback fee charged by Stripe (e.g. 1500 cents)
}

=== PROGRESSIVE PARTS ===

Part 1: Basic Chargeback Processing
- For each chargeback, mark the related payment status = "charged_back"
- Deduct the disputed amount + fee from the merchant’s ledger balance (simulated via payment.balance_impact)

Part 2: Idempotency
- Ignore duplicate events (same event_id)

Part 3: Multi-currency + Full State Update
- Support multiple currencies
- Update the payment object with new status and final balance impact

Part 4: Production Rules & Report
- If chargeback amount > original payment amount → still allow (full reversal + fee)
- Return final_payments state + a summary report
- Report contains: number of chargebacks processed, total fees charged, total disputed amount

Return Value:
    Tuple[Dict[str, Dict], Dict[str, Any]]
    (updated_payments_copy, summary_report)
"""

from typing import Dict, List, Tuple, Any
from copy import deepcopy

def process_chargebacks(payments: Dict[str, Dict], chargeback_events: List[Dict[str, Any]]) -> Tuple[Dict[str, Dict], Dict[str, Any]]:
    # TODO: Implement full logic for Parts 1–4 here
    pass


# ========================= RUNNABLE TEST CASES =========================
if __name__ == "__main__":
    print("Running Stripe Chargebacks OA tests...\n")

    payments = {
        "pi_1": {"payment_id": "pi_1", "amount": 10000, "currency": "USD", "status": "succeeded", "balance_impact": 10000},
        "pi_2": {"payment_id": "pi_2", "amount": 2500,  "currency": "EUR", "status": "succeeded", "balance_impact": 2500},
    }

    events = [
        {"event_id": "cb1", "type": "chargeback", "payment_id": "pi_1", "amount": 10000, "currency": "USD", "fee": 1500},
        {"event_id": "cb2", "type": "chargeback", "payment_id": "pi_2", "amount": 1000,  "currency": "EUR", "fee": 1500},
        {"event_id": "cb1", "type": "chargeback", "payment_id": "pi_1", "amount": 5000,  "currency": "USD", "fee": 1500},  # duplicate
    ]

    result = process_chargebacks(payments, events)
    updated_payments, report = result

    assert updated_payments["pi_1"]["status"] == "charged_back"
    assert updated_payments["pi_1"]["balance_impact"] == 10000 - 10000 - 1500 == -1500
    assert report["total_chargebacks"] == 2
    assert report["total_fees"] == 3000
    print("✓ Parts 1–4 passed (idempotency + multi-currency + report)")

    print("\n🎉 All 4 parts passed! This matches recent chargeback/dispute OAs for MaaS teams.")