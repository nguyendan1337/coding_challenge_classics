# payouts_flow_challenge.py
"""
STRIPE HACKERRANK OA - PAYOUTS FLOW (MaaS / MMS Team)
======================================================

Stripe processes billions of money movement requests daily. You are implementing core logic for the balance management platform that powers payouts.

Input:
- balances: Dict[str, int]           → current available balance per currency (in cents)
- payout_requests: List[Dict]        → list of payout requests in the exact order they must be processed

Each payout request contains:
    {
        "payout_id": str,
        "amount": int,          # amount in cents
        "currency": str,        # e.g. "USD", "EUR", "GBP"
        "status": "pending"
    }

=== PROGRESSIVE PARTS (You implement ONE function that solves all parts) ===

Part 1: Basic Payout Processing
- Process a single payout.
- No fee yet.
- If available balance >= amount, deduct the amount and set status = "completed".
- Otherwise, set status = "failed" (do not deduct anything).
- Return copies of the updated balances and the processed payouts list.

Part 2: Platform Fee + Status Updates
- Add a 1% platform fee using integer division: fee = amount // 100
- Total to deduct = amount + fee
- Check balance against the total deduction (not just the amount).
- Always update the status to either "completed" or "failed".
- Still mostly simple cases.

Part 3: Multi-Currency + Sequential Processing (Order Matters)
- Process all payouts in the exact order they appear in the list.
- Support multiple currencies in one run.
- Deductions are cumulative: a successful payout reduces the balance for all later payouts in the same currency.
- One payout failing does not affect the processing of subsequent payouts.

Part 4: Edge Cases & Production Requirements
- New currencies not present in the initial balances should be treated as balance = 0.
- If a payout for a new currency fails, still include that currency in the returned balances with value 0.
- Handle zero amount payouts (amount = 0).
- Strictly do NOT mutate any of the input data (balances dict or the payout dictionaries).
- Always return deep copies of the balances and the list of payouts.

Return Value:
    Tuple[Dict[str, int], List[Dict[str, Any]]]
    → (updated_balances_copy, processed_payouts_list_in_order)

This logic is critical — incorrect balance updates or double-processing can cost millions at Stripe scale.
"""

from typing import Dict, List, Tuple, Any

def process_payouts(balances: Dict[str, int], payout_requests: List[Dict[str, Any]]) -> Tuple[Dict[str, int], List[Dict[str, Any]]]:
    # TODO: Implement your solution here (must work for Parts 1 through 4)
    balances_copy = balances.copy()
    processed_payouts = []
    for payout_request in payout_requests:
        amount = payout_request["amount"]
        currency = payout_request["currency"]
        available_balance = 0
        if currency in balances_copy:
            available_balance = balances_copy[currency]
        platform_fee = amount // 100
        transaction_total = amount + platform_fee

        if available_balance >= transaction_total:
            available_balance -= transaction_total
            status = "completed"
        else:
            status = "failed"
        balances_copy[currency] = available_balance
        processed_payout = {
            "payout_id": payout_request["payout_id"],
            "amount": payout_request["amount"],          # amount in cents
            "currency": payout_request["currency"],        # e.g. "USD", "EUR", "GBP"
            "status": status
        }
        processed_payouts.append(processed_payout)

    return (balances_copy, processed_payouts)


# ========================= RUNNABLE TEST CASES =========================
if __name__ == "__main__":
    print("Running Stripe Payouts Flow OA tests...\n")

    # Part 1 + 2
    balances1 = {"USD": 10000}
    req1 = [{"payout_id": "po_1", "amount": 5000, "currency": "USD", "status": "pending"}]
    res1 = process_payouts(balances1, req1)
    print(res1)
    assert res1[0]["USD"] == 4950 and res1[1][0]["status"] == "completed"
    print("✓ Parts 1–2 passed")

    # Part 3
    balances3 = {"USD": 10000, "EUR": 2000}
    req3 = [
        {"payout_id": "po_3", "amount": 3000, "currency": "USD", "status": "pending"},
        {"payout_id": "po_4", "amount": 1500, "currency": "EUR", "status": "pending"},
        {"payout_id": "po_5", "amount": 8000, "currency": "USD", "status": "pending"},
    ]
    res3 = process_payouts(balances3, req3)
    print(res3)
    assert res3[0] == {"USD": 6970, "EUR": 485}
    assert [p["status"] for p in res3[1]] == ["completed", "completed", "failed"]
    print("✓ Part 3 passed")

    # Part 4
    balances4 = {"USD": 5000}
    req4 = [
        {"payout_id": "po_6", "amount": 0, "currency": "GBP", "status": "pending"},
        {"payout_id": "po_7", "amount": 1000, "currency": "GBP", "status": "pending"},
        {"payout_id": "po_8", "amount": 6000, "currency": "USD", "status": "pending"},
    ]
    res4 = process_payouts(balances4, req4)
    print(res4)
    assert res4[0] == {"USD": 5000, "GBP": 0}
    assert [p["status"] for p in res4[1]] == ["completed", "failed", "failed"]
    print("✓ Part 4 passed")

    print("\n🎉 All parts passed!")