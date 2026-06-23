# Consolidated CSV database

Structured extraction of the programmes and awards documented across this repo's markdown files, for easy viewing/filtering (open in any spreadsheet tool or `csvlook`/pandas).

Built 2026-06-23 by reading every MD file (`allprogs.md`, `allgrants.md`, `agencies/*.md`, `foundations/*.md`, `themes/air-ppe-uv-glycols.md`) and extracting rows. The MD files remain the authoritative narrative with full caveats and sources; the CSVs are a flattened index.

## Files

### `programs.csv` — 302 programmes/initiatives
Columns: `funder, funder_type, program, acronym_expansion, theme, pandemic_relevance, years, status, source_file`

### `awards.csv` — 606 grants/contracts/awards
Columns: `funder, funder_type, program, recipient, amount, amount_usd_millions, amount_basis, year, theme, purpose, source_file`

`amount_usd_millions` is a **normalized numeric column** for charting (filled for 493/606 = 81% of rows; blank where undisclosed):
- It is the **largest disclosed USD figure stated in the row** (a headline/ceiling value). For rows listing multiple tranches (e.g. "$483M + $472M") it reflects the **largest single one, not the sum**, to avoid double-counting parenthetical breakdowns.
- Non-USD amounts are converted at fixed approximate rates (GBP×1.27, EUR×1.08, DKK×0.145); where a row gives both a local-currency and a USD figure (e.g. "DKK 1.8B (USD 260M)"), the USD figure is used.
- **Do NOT sum this column** as a budget total — it mixes ceilings, obligated amounts, advance-purchase agreements, and cumulative multi-year figures, and COVID DoD/BARDA rows overlap.

## Field notes
- **funder_type** (normalized from funder name): `US HHS`, `US DoD`, `US gov agency`, `US IC` (intelligence), `foundation/philanthropy`, `multilateral/nonprofit`, `corporate`.
- **theme** (controlled vocabulary): `vaccines, therapeutics-antivirals, diagnostics, biosurveillance-detection, MCM-manufacturing, PPE-air-UV, AMR, biosecurity-policy, basic-research, neurotech, synbio, environmental-ag, other`.
- **pandemic_relevance:** `YES / PARTIAL / NO` (programmes).
- **amount:** kept verbatim from the source (e.g. `$483M`, `up to $30M`, `undisclosed`). NOT normalized to a number — many are "up to"/ceiling values, advance-purchase agreements, or undisclosed.
- **amount_basis:** `ceiling`, `obligated`, `advance-purchase`, `undisclosed`, `prize`, etc. — best-effort from context.
- **source_file:** the MD file the row was extracted from (go there for full context, confidence flags, and source URLs).

## Coverage caveats
- **Amounts are not summable.** Ceiling vs obligated vs advance-purchase are mixed; COVID/Operation Warp Speed figures executed via DoD (JPEO-CBRND) overlap with BARDA totals; many figures are press-release "up to" values. Treat the CSV as an index, not an accounting ledger.
- **Representative, not exhaustive** for high-volume funders (NIH, CDC, Gates, USAID) where the underlying MD files already say the grantee lists are representative.
- Some shared-pool awards (e.g. one amount across several recipients) appear as one row per recipient with the shared amount noted.

## Row counts by funder (programmes)
DARPA BTO 68 · BARDA 35 · ARPA-H 19 · NIH/NIAID 15 · CDC 12 · Novo Nordisk 11 · Gates 10 · Wellcome 9 · Skoll/Ending Pandemics 8 · ASPR / USAMRIID-DoD / USDA / DOE-NNSA / CEPI 7 each · DTRA / JPEO-CBRND / DHS / USAID / State / NSF / CZI 6 each · Rockefeller 5 · plus IARPA, In-Q-Tel, Wellcome Leap, Open Philanthropy, Blueprint Biosecurity, Balvi, HHMI, Bloomberg, Trinity Challenge, Schmidt, Resolve to Save Lives, Flu Lab, ELMA, McGovern, Audacious, and the air/PPE government lines (NIOSH, EPA, CDC/EPA).

## Quick recipes
```sh
# all PPE / air / UV / glycol awards
awk -F, 'NR==1 || $8=="PPE-air-UV"' awards.csv | column -s, -t | less -S
# everything BARDA funded
grep '^BARDA,' awards.csv
# count awards per theme
python3 -c "import csv,collections as c; r=list(csv.reader(open('awards.csv')))[1:]; print(c.Counter(x[7] for x in r))"
```
