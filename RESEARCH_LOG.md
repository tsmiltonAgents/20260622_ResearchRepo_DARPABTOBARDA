# Research Log

> Running log of all research, notes, and reasoning. Newest entries at the bottom.

---

## 2026-06-22 — Project initialized

- Created research project scaffolding in `20260622_researchrepo`.
- Initialized git repository and GitHub remote (`20260622_researchrepo`).
- Established log structure: this file is the single source of truth for all research and thinking.
- **Next:** awaiting research topic from user. Once received, scope the question, plan sub-topics, and begin source gathering.

---

## 2026-06-22 — Topic received: DARPA BTO & BARDA programmes

**Task (Phase 1):** Catalogue every DARPA Biological Technologies Office (BTO) and BARDA programme → `allprogs.md`.
**Task (Phase 2):** Identify pandemic-relevant programmes → find all grants/contracts they awarded → `allgrants.md`.

### Method
- Ran two parallel research agents (general-purpose, web-enabled): one for DARPA BTO, one for BARDA.
- Each returned a source-backed catalogue with a pandemic/infectious-disease flag (YES/PARTIAL/NO).
- Compiled both into `allprogs.md` with summary tables + per-programme detail, grouped by theme.

### Key findings
- **DARPA BTO:** ~68 distinct programmes/challenges catalogued (canonical Wikipedia list of ~44 + ~24 newer 2020–2026 starts/legacy efforts). BTO established April 2014. Clear pandemic cluster (YES): ADEPT, P3, PREEMPT, Prophecy, INTERCEPT, THoR, PREPARE, DIGET, NOW, HEALR, AIM, Prometheus, AMPHORA, Friend or Foe, ReVector, Bio-Attribution Challenge.
- **BARDA:** Established 2006 under PAHPA, part of HHS/ASPR. Core divisions (CBRN; Influenza & Emerging Infectious Diseases), DRIVe (ENACT, Solving Sepsis, ReDIRECT, BARDA Accelerator Network), BARDA Ventures, Project BioShield, manufacturing infra (CIADM, FFMN, BioMaP), and COVID programmes (OWS, Antiviral Program for Pandemics, Project NextGen, RRPV).
- **Corrections caught by agents:** "BEACON" is NOT a real BARDA program (prompt conflation). Several DARPA programs commonly mislabelled BTO actually belong to DSO/I2O/TTO (SD2, Make-It, OFFSET, 7-Day Biodefense). "Biological Robustness" = BRICS; no nematode program exists.

### Caveats
- DARPA pages are archival; PM names/dates are best-effort from BAAs/press. Estimated year ranges flagged with `~`.
- Committed/pushed `allprogs.md`.

---

## 2026-06-22 — Phase 2: grants & contracts (allgrants.md)

### Method
- Took the pandemic-relevant shortlist from `allprogs.md` (DARPA BTO "YES" + key "PARTIAL"; BARDA pandemic portfolios).
- Ran **5 parallel research agents** (web-enabled): (1) DARPA therapeutics/prevention cluster; (2) DARPA diagnostics/detection cluster; (3) BARDA COVID-19 / Operation Warp Speed; (4) BARDA influenza + EID + manufacturing infrastructure; (5) BARDA Antiviral Program for Pandemics + Project NextGen + DRIVe + Ventures + RRPV + BioMaP.
- Each agent captured recipient / amount (ceiling vs obligated) / date / purpose / source, with explicit confidence flags and instructions not to invent awards.
- Compiled all into `allgrants.md`: Part 1 DARPA (1A therapeutics, 1B diagnostics), Part 2 BARDA (2A COVID, 2B flu, 2C EID, 2D manufacturing, 2E APP, 2F NextGen, 2G DRIVe, 2H Ventures, 2I RRPV, 2J BioMaP).

### Notable findings / data-quality catches
- **DARPA programs are mostly structured as a few prime awards.** P3 = 4 primes (AbCellera $30M, Vanderbilt $28M, Duke $12.8M, MedImmune undisclosed). NOW = 2 primes (Moderna $56M, GE $41M). DIGET = single prime to MRIGlobal ($36.7M ceiling) with 5 subs — NOT "6 awards."
- **Many DARPA amounts are genuinely undisclosed** (all HEALR teams, all AIM teams, ReVector Stanford). Reported transparently rather than guessed.
- **BARDA's biggest dollars are COVID** (OWS: Sanofi/GSK $2.1B, Pfizer Paxlovid $5.29Bx2, Moderna ~$955M dev + ~$1.5B purchase, etc.) and EID procurement (SIGA TPOXX up to $629M, Emergent ACAM2000 up to ~$2B ceiling).
- **Key corrections caught:** AViDD Centers (~$577M) are NIH/NIAID, not BARDA; Invivyd has no NextGen award; Sherlock not a confirmed DIGET awardee; Gilead remdesivir + Abbott/Ellume/OraSure mfg were not BARDA; Medicago/FluGen flu were DARPA/DoD; Bio-Attribution is a prize ($180K pool), not contracts.
- **Recent reversals noted:** Moderna's RRPV pandemic-flu awards ($176M + $590M) were obligated then **cancelled by HHS mid-2025**; the Moderna H5 follow-on (~$590M) likewise terminated.

### Caveats
- Ceiling vs obligated distinction preserved per row. Federal databases (USAspending/FPDS) resisted automated extraction; most figures come from press releases (often "up to"). PIIDs and GAO report numbers are cited for audit-grade follow-up.
- **Phase 2 complete.** Both deliverables (`allprogs.md`, `allgrants.md`) pushed.
