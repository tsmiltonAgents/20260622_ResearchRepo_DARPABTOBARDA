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
- **Next:** commit/push `allprogs.md`, then Phase 2 — grants/contracts for the pandemic-relevant shortlist.
