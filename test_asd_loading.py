#!/usr/bin/env python3
"""
Test script to demonstrate loading allosteric ligands from ASD database
"""

import sys
from pathlib import Path

# Add the hackathon directory to the path
sys.path.insert(0, str(Path(__file__).parent / "hackathon"))

from predict_hackathon import load_reference_allosteric_ligands

def main():
    print("=" * 80)
    print("Testing ASD Allosteric Ligand Loading")
    print("=" * 80)
    print()
    
    # Test with a small limit to avoid long API calls
    print("Loading allosteric ligands (max 10 from ASD for testing)...")
    print()
    
    ligands = load_reference_allosteric_ligands(max_asd_ligands=10)
    
    print()
    print("=" * 80)
    print(f"Summary: Loaded {len(ligands)} total allosteric ligands")
    print()
    
    if len(ligands) > 0:
        print(f"First 5 SMILES:")
        for i, smiles in enumerate(ligands[:5], 1):
            print(f"  {i}. {smiles}")
    
    print()
    print("Note: A cache file has been created at:")
    print("  /home/ubuntu/will/boltz-hackathon-template/asd_smiles_cache.json")
    print()
    print("Future calls will use this cache to avoid API calls.")
    print("=" * 80)

if __name__ == "__main__":
    main()

