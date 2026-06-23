# Interesting Findings

Patterns that emerge from reading across the whole corpus (DARPA BTO + BARDA, 14 US agencies, 10 foundations, and the airborne-mitigation theme) and from the consolidated `data/` CSVs (302 programmes, 606 awards, 44 funders, 515 distinct recipients).

> **Read these with the standing caveat:** dollar figures are *not summable* — ceilings, obligated amounts, advance-purchase agreements, and cumulative multi-year totals are mixed; COVID figures executed via DoD (JPEO-CBRND) overlap with BARDA; grantee lists are representative, not exhaustive. The numbers below are directional, not audited.

---

## 1. The money is at procurement, not discovery — by ~150×
The 28 awards of **≥ $1 billion** in the database carry a combined headline value of **~$101 billion**. Every one is a COVID-era vaccine/therapeutic **advance-purchase or stockpile** deal (Pfizer Paxlovid 2×$5.29B, Sanofi/GSK $2.1B, Moderna ~$2.5B, Regeneron $2.94B, Emergent ACAM2000 ~$2B ceiling) or a cumulative multilateral commitment (Global Fund ~$33B, Gavi ~$7.7B).

By contrast, **all of DARPA BTO's biosecurity research awards combined total ~$702 million** — i.e. the entire upstream "invent the countermeasure" portfolio is ~0.7% of what was spent *buying* countermeasures once the pandemic hit. The discovery base is cheap; the panic-buying is not.

## 2. A small set of organizations sits at the center of the entire ecosystem
A handful of recipients are funded by **five different funders each**, spanning the discovery→development→procurement→intelligence chain:
- **Moderna** — DARPA BTO (ADEPT mRNA, 2013) → NIH/NIAID (VRC co-invented mRNA-1273) → BARDA (OWS) → JPEO-CBRND (DoD contracting) → CEPI. The COVID vaccine rode a decade of government de-risking before 2020.
- **Ginkgo Bioworks** — DARPA, DTRA, IARPA (FELIX engineered-DNA detection), BARDA (BioMaP), ARPA-H (WHEAT). It is the connective tissue of US biosecurity engineering biology.
- **Columbia University** — appears across DTRA, NSF, *and* the far-UVC funders (Shostack, Balvi, Ushio) — the same institution bridges classic biodefense and the new air-disinfection field.

Recurring **contractor "arsenal" firms** show up across DARPA/BARDA/DTRA/DHS/USDA: **Battelle, Emergent BioSolutions, Texas A&M/TEES, RTI International, MRIGlobal, Mapp, Draper**. The US "pandemic-industrial base" is narrow and reused.

## 3. COVID's speed was bought a decade earlier
The fast 2020 products were pre-positioned platforms, not new ideas:
- **DARPA ADEPT (2013)** funded Moderna's mRNA antibody platform (~$25M) and (via **P3**, 2017) AbCellera, Vanderbilt, and Duke antibody pipelines — which produced the **first COVID antibody drug (bamlanivimab)** and **Evusheld**.
- **NIAID's VRC** supplied the prefusion-spike design behind the mRNA vaccine.
- **BARDA's CIADM** manufacturing centers (2012, post-H1N1) became OWS production lines.

The lesson recurs in the data: every "100-day" or "60-day" capability (P3, NOW, NIH AViDD, CEPI's 100 Days Mission) is an attempt to institutionalize that pre-positioning.

## 4. A steep transparency gradient — defense and intelligence disclose least
Share of a funder's awards where the **amount is undisclosed**:

| High disclosure | | Low disclosure | |
|---|---|---|---|
| Gates Foundation | 0% | In-Q-Tel | 75% |
| Novo Nordisk | 0% | Wellcome Trust | 50% |
| DTRA | 0% | USAMRIID/DoD | 44% |
| NSF | 0% | USAID | 38% |
| CDC | 3% | DARPA BTO | 35% |
| BARDA | 4% | JPEO-CBRND | 30% |

US **HHS procurement** (BARDA, CDC, ASPR) and the **big foundations** (which publish grant databases) are the most transparent; **defense research, intelligence investment, and even Wellcome** are the most opaque. (Caveat: "undisclosed" here = not public, which partly reflects classification and philanthropic discretion, not necessarily secrecy.)

## 5. Airborne transmission — the defining feature of COVID — is funded mostly by *non-traditional* philanthropy
Of the 48 itemized PPE / air-filtration / germicidal-UV / glycol awards, **29 come from foundations/philanthropy vs 16 from US HHS**. And the philanthropic share is dominated by **newcomers**, not the pandemic giants:
- **Open Philanthropy** (11 awards — far-UVC, next-gen PPE), **Blueprint Biosecurity** (8 — far-UVC/PPE/glycol), **Balvi / Vitalik Buterin crypto-philanthropy** (7 — $9.4M U Maryland germicidal UV, $15M UCSD).
- **Gates, Wellcome, and CEPI are essentially absent** from air-disinfection. Gates funds vaccines/diagnostics; the foundational 2018 far-UVC paper was funded by the **Shostack Foundation + NIH**, not Gates. Rockefeller funds air *monitoring*, not disinfection.

A defining transmission route got niche, idiosyncratic funding rather than mainstream investment.

## 6. Government air/PPE money was reactive and is shrinking; one forward-looking program remains
US government PPE spending was a **2020 surge**: DPA Title III ~$3.2B across 182 firms (3M $126M+$76M, Honeywell, Moldex), the **Battelle $415M mask-decontamination contract** (of which only ~$150M was ever invoiced before it was shut down). The only sustained, forward-looking federal program for indoor air is **ARPA-H BREATHE** (up to $156M, 2024). Worker-respirator R&D (NIOSH/NPPTL) and elastomeric/PAPR work is modest by comparison.

## 7. Glycol air disinfection: an 80-year-old idea revived in 2026 by a single grantmaker
Triethylene/propylene-glycol vapor air disinfection was demonstrated by **Robertson and Puck in the 1940s** and then almost entirely abandoned. Its modern revival rests on **two** threads: **EPA's emergency authorization of Grignard Pure** (a TEG product) in 2021, and **Blueprint Biosecurity's GlycolISER program** (~$4.5M across 7 grantees, March 2026). A potentially useful countermeasure sat essentially unfunded for ~80 years — a vivid example of how the field neglects non-pharmaceutical controls.

## 8. "Ceiling vs obligated" routinely inflates the headlines by 2–10×
The data is full of cases where the announced number far exceeds money actually spent:
- **Chemonics GHSC-PSM**: $9.5B ceiling / $6.72B obligated.
- **SIGA TPOXX**: ~$52M base / up to $629M ceiling.
- **Battelle mask decon**: $415M ceiling / ~$150M invoiced.
- **Moderna's RRPV H5N1 flu awards** ($176M + $590M): obligated, then **cancelled by HHS in 2025**.

Any tally built from press-release "up to" figures will substantially overstate real spend — which is exactly why the CSV keeps `amount` verbatim and flags `amount_basis`.

## 9. Foundations and government occupy complementary niches
The corpus shows a clean division of labor:
- **CEPI and Gates** fund vaccine R&D for *neglected epidemic pathogens that government largely ignores* — Lassa, Nipah, MERS, Rift Valley fever, Chikungunya, "Disease X."
- **BARDA/ASPR** funds the *acute stockpile and procurement* (smallpox, anthrax, COVID, pandemic flu).
- **NIH/NSF** fund *basic/upstream* science; **DARPA/DTRA** fund *high-risk platforms*; **CDC/USAID** fund *surveillance systems*.

Few funders span niches — CEPI co-funds with BARDA (e.g. NOW, Project NextGen) and the Gates+Wellcome+Novo Nordisk trio co-funds AMR (Gr-ADI), but the ecosystem is mostly specialized rather than redundant.

## 10. 2025 was a year of structural retrenchment — "cycles of panic and neglect" made concrete
Across multiple independent files, the same year recurs as a contraction point:
- **USAID dissolved** into the State Department (July 1, 2025); PREDICT/STOP Spillover terminated.
- **Moderna's H5N1 pandemic-flu mRNA awards cancelled** by HHS (mid-2025).
- **DHS's CWMD office** proposed for dissolution (FY2026 budget); **BD21** biodetection discontinued (Sept 2024).
- **CDC** facing ~50% proposed cuts; **PEPFAR/Gavi** funding frozen/withheld.
- Rockefeller had already wound down its **Pandemic Prevention Institute** (~2022), its head Rick Bright citing philanthropy's "**cycles of panic and neglect**."

The pattern Bright named is visible across the dataset: a 2020–2022 surge of programmes and dollars, followed by a 2023–2025 drawdown — even as the underlying biological risk did not change.

---

### How to explore further
Open `data/awards.csv` and `data/programs.csv` in a spreadsheet and filter by `theme`, `funder`, `funder_type`, or `pandemic_relevance`. The `amount_usd_millions` column is a best-effort headline value (largest disclosed USD figure per row; blank where undisclosed) for charting — see `data/README.md` for the parsing rules and why the column must not be naively summed. Each row's `source_file` points back to the markdown file with full context, confidence flags, and source URLs.
