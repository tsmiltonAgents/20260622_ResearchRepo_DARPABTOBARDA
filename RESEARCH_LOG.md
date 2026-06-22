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

---

## 2026-06-22 — Repo admin

- **User request:** make the repo public and rename it to `20260622_ResearchRepo_DARPABTOBARDA`.
- → Done via `gh repo edit --visibility public` and `gh repo rename`. Local remote updated automatically. (Local folder name unchanged.)

---

## 2026-06-22 — Phase 3 kickoff: USG agencies + foundations (parallel)

**User request (verbatim intent):** run a long agentic loop — think of other USG agencies that do similar work to DARPA BTO/BARDA, find their programmes, then their grantees; *in parallel* do the same for foundations (CEPI, Wellcome, Gates, etc.); add more folder structure to enable this; keep these requests logged. (Also recorded in `REQUESTS.md` #5.)

**Structure added:**
- `agencies/` — one MD per USG agency (programmes + grantees); registry in `agencies/README.md`.
- `foundations/` — one MD per funder (programmes + grantees); registry in `foundations/README.md`.
- `REQUESTS.md` — chronological log of user requests.

**Scope decision (logged for transparency):** "find their grantees" is bounded to pandemic/biosecurity/infectious-disease/MCM work and to *notable/major* awardees — not exhaustive grant-database dumps (NIH/Gates each make thousands of awards). Files state where a full list is impractical and give the largest/most representative awards with sources.

**Plan — research waves (agencies and foundations run concurrently):**
- *Wave 1 (agencies):* NIH/NIAID, CDC, ASPR, DTRA, JPEO-CBRND, DoD medical (USAMRIID/MRDC/CDMRP). *(foundations parallel:)* CEPI, Gates, Wellcome.
- *Wave 2 (agencies):* DHS, USAID, USDA, State Dept, DOE/NNSA, NSF, IARPA/In-Q-Tel, ARPA-H. *(foundations parallel:)* Wellcome Leap, Open Philanthropy, Rockefeller, CZI, Novo Nordisk, Skoll, other funders.
- Each entity researched by a dedicated web-enabled subagent; results written to its file; committed/pushed per wave.

### Wave 1 complete (2026-06-22)
Ran 9 parallel web-enabled subagents. Files written:
- Agencies: `niaid.md`, `cdc.md`, `aspr.md`, `dtra.md`, `jpeo-cbrnd.md`, `dod-medical.md`
- Foundations: `cepi.md`, `gates.md`, `wellcome.md`

**Highlights / cross-checks the agents caught:**
- **NIH/NIAID** is the upstream-research counterpart to BARDA/DARPA: AViDD Centers (~$577M, 9 centers, 2022), CREID, CEIRR, CIVICs, ReVAMPP, VRC (co-developed Moderna mRNA-1273), ~$1B biocontainment lab network. "Prototype pathogen" approach spans ~10 viral families (not "25+").
- **CDC** funds via cooperative agreements (ELC since 1995, ~65 jurisdictions, the main COVID-supplement conduit; PHEP; CFA $200M ARPA; Insight Net up to $262.5M/>$148M awarded). SNS moved CDC→ASPR in 2018.
- **ASPR (non-BARDA):** PHEMCE, SNS (~$980M FY24), Project BioShield SRF ($825M FY24), HPP (~$240M/yr, 62 recipients), RDHRS, DPA Title III. Phlow $354M flagged as a BARDA award (no double-count).
- **DTRA:** JSTO/CBDP S&T (~$1.4–1.7B CBDP), CTR/BTRP (formerly CBEP; ~$139–235M recent), DOMANE drug-repurposing, BSVE biosurveillance. Overseas partner labs (Lugar/Tbilisi, Almaty, Ukraine) — surveillance, not bioweapons (2022 disinformation debunked).
- **JPEO-CBRND:** DoD acquisition counterpart to BARDA; MCDC OTA (~$10B ceiling, >$7.8B awarded). During COVID it was the **contracting vehicle** for ~$10.8B of HHS/BARDA OWS money — overlaps with BARDA, not additive. Clean MCDC awards: Regeneron $450.2M, AstraZeneca AZD7442 ~$486M, Cepheid ~$3.7M.
- **DoD medical:** USAMRIID (only DoD BSL-4; ZMapp, TPOXX), WRAIR (RTS,S malaria, RV144 HIV, SpFN COVID), NMRC/NAMRU (PfSPZ, enteric vaccines), CDMRP (~$20B cumulative; TBDRP), GEIS (~$60M/yr to 6 overseas labs). HJF is the dominant funding intermediary.
- **CEPI:** vaccine-developer awards well-documented — Lassa/MERS/Nipah/RVF/Chikungunya portfolios + COVID (Novavax up to ~$384–399M, its largest; Moderna's first investment only ~$0.9M). 100 Days Mission / $3.5B plan.
- **Gates:** >$30.6B to vaccines since 2000; Gavi ~$7.7B cumulative (largest grantee); CEPI co-founder; CTA (with Wellcome/Mastercard); WHO ~$5.5B cumulative. Caught: no direct Gates→MPP grant; "$15M Pandemic Fund" likely Rockefeller's; Afrigen reportedly not Gates-funded.
- **Wellcome:** three-challenge strategy (Infectious Disease/Mental Health/Climate); CEPI co-founder ($100M + $300M joint pledge); CTA ($50M); CARB-X/GARDP (AMR); Sanger Institute (wholly owned); overseas units (KEMRI-Wellcome £91M, MORU, MLW, OUCRU); ISARIC.

**Recurring caveat across all:** federal/foundation databases resisted automated fetching; most figures are press-release "ceiling"/"up to" values, flagged per file. Awardee lists are representative, not exhaustive (esp. NIH, CDC, Gates).
**Next:** Wave 2 — DHS, USAID, USDA, State, DOE/NNSA, NSF, intel (IARPA/In-Q-Tel), ARPA-H + foundations (Wellcome Leap, Open Phil, Rockefeller, CZI, Novo Nordisk, Skoll, other funders).
