"""
Global Beauty Salon Franchise Network - RWA Tokenization Protocol
-------------------------------------------------------------------
Open-Source Web3 Architecture for Crowdfunding Local Salon Openings, 
Automating Chair/Booth Lease Smart Contracts, and Distributing 
Cosmetic Retail Yields to Global Token Holders.

License: MIT
"""

import time
import hashlib
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class SalonFranchiseToken:
    token_id: str
    investor_address: str
    salon_location_code: str
    amount_funded_eur: float
    equity_yield_percentage: float
    timestamp: float = field(default_factory=time.time)

@dataclass
class ChairLeaseContract:
    chair_id: str
    stylist_address: str
    monthly_rent_eur: float
    is_active: bool = True
    last_payment_timestamp: float = field(default_factory=time.time)

class GlobalBeautyTokenEngine:
    """
    Real-World Asset (RWA) Engine for Scaling Beauty Salons Globally.
    Automates booth rentals, tokenizes CapEx investments, and processes
    cosmetic cross-selling distributions.
    """
    def __init__(self, brand_name: str = "AURA-BEAUTY-GLOBAL"):
        self.brand_name = brand_name
        self.investor_registry: Dict[str, SalonFranchiseToken] = {}
        self.chair_leases: Dict[str, ChairLeaseContract] = {}
        self.total_capex_raised_eur: float = 0.0
        self.total_cosmetic_sales_eur: float = 0.0

    def issue_franchise_token(self, investor: str, salon_code: str, funding_eur: float, target_capex: float = 25000.0) -> SalonFranchiseToken:
        """Allows global investors to fund a local salon opening in exchange for yield tokens."""
        token_id = hashlib.sha256(f"{investor}_{salon_code}_{time.time()}".encode()).hexdigest()[:12]
        equity_share = (funding_eur / target_capex) * 100.0

        token = SalonFranchiseToken(
            token_id=token_id,
            investor_address=investor,
            salon_location_code=salon_code,
            amount_funded_eur=funding_eur,
            equity_yield_percentage=equity_share
        )

        self.investor_registry[token_id] = token
        self.total_capex_raised_eur += funding_eur
        print(f"[TOKEN ISSUED] Investor {investor[:8]}... funded €{funding_eur:,.2f} for Salon '{salon_code}' ({equity_share:.2f}% Share)")
        return token

    def register_chair_lease(self, chair_id: str, stylist_address: str, monthly_rent_eur: float) -> ChairLeaseContract:
        """Registers an independent stylist/barber chair lease on smart contract."""
        lease = ChairLeaseContract(
            chair_id=chair_id,
            stylist_address=stylist_address,
            monthly_rent_eur=monthly_rent_eur
        )
        self.chair_leases[chair_id] = lease
        print(f"[CHAIR LEASE REGISTERED] Chair '{chair_id}' leased to {stylist_address[:8]}... for €{monthly_rent_eur:,.2f}/month")
        return lease

    def process_cosmetic_sale_and_yield(self, salon_code: str, sale_amount_eur: float, margin_percent: float = 40.0):
        """Processes retail cosmetic sales and distributes profit margin yields to franchise token holders."""
        profit_margin = sale_amount_eur * (margin_percent / 100.0)
        self.total_cosmetic_sales_eur += sale_amount_eur

        print(f"\n[COSMETIC SALE] Salon '{salon_code}' sold €{sale_amount_eur:,.2f} in cosmetics. Net Margin: €{profit_margin:,.2f}")
        print(f"[YIELD DISTRIBUTION] Distributing profits to RWA Token Holders:")

        for tid, token in self.investor_registry.items():
            if token.salon_location_code == salon_code:
                payout = profit_margin * (token.equity_yield_percentage / 100.0)
                print(f" -> Investor {token.investor_address[:8]}... received €{payout:,.2f} yield dividend.")

    def generate_network_ledger(self):
        """Prints global status summary for brand franchise network."""
        print("\n" + "="*75)
        print(f"      {self.brand_name} - GLOBAL FRANCHISE & RWA LEDGER REPORT")
        print("="*75)
        print(f"Total Franchise CapEx Raised: €{self.total_capex_raised_eur:,.2f}")
        print(f"Total Active Leased Chairs: {len(self.chair_leases)}")
        print(f"Total Cosmetic Retail Revenue: €{self.total_cosmetic_sales_eur:,.2f}")
        print(f"Total Franchise Token Holders: {len(self.investor_registry)}")
        print("="*75 + "\n")


# --- EXECUTION DEMO ---
if __name__ == "__main__":
    engine = GlobalBeautyTokenEngine(brand_name="AURA-BEAUTY-NETWORK")

    print("\n--- 1. FRANCHISE CAPEX CROWDFUNDING (SALON LOCATION: CLUJ-CENTRAL) ---")
    engine.issue_franchise_token("0xInvestorA111...", "SALON-RO-CLUJ-01", funding_eur=10000.0, target_capex=25000.0)
    engine.issue_franchise_token("0xInvestorB222...", "SALON-RO-CLUJ-01", funding_eur=15000.0, target_capex=25000.0)

    print("\n--- 2. CHAIR / BOOTH LEASE REGISTRATION ---")
    engine.register_chair_lease("CHAIR-BARBER-01", "0xStylistMarco...", monthly_rent_eur=500.0)
    engine.register_chair_lease("CHAIR-HAIR-02", "0xStylistElena...", monthly_rent_eur=600.0)

    print("\n--- 3. RETAIL COSMETIC SALES & YIELD DISTRIBUTION ---")
    engine.process_cosmetic_sale_and_yield("SALON-RO-CLUJ-01", sale_amount_eur=2500.0, margin_percent=40.0)

    print("\n--- 4. FRANCHISE NETWORK LEDGER ---")
    engine.generate_network_ledger()
