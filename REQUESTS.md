# Requests Log

> Chronological record of what the user asked for, so the project history is auditable. Detailed method/findings live in `RESEARCH_LOG.md`.

## 2026-06-22

1. **Start a research project** in the folder; always write all research and thinking to a markdown file; make a GitHub repo named exactly after the parent folder; commit and push regularly.
   - → Scaffolding + repo `20260622_researchrepo` created.

2. **Phase 1:** Research all DARPA BTO and BARDA programmes that have been run → `allprogs.md`; commit and push.
   - → Done. ~68 DARPA BTO programmes + full BARDA structure, pandemic-relevance flagged.

3. **Phase 2:** Identify which programmes are pandemic-relevant; find all grants/contracts those programmes gave out → `allgrants.md`; push.
   - → Done. DARPA + BARDA award inventories with ceiling-vs-obligated and confidence flags.

4. **Make the repo public** and **rename** it to `20260622_ResearchRepo_DARPABTOBARDA`.
   - → Done. Repo is public; local remote updated.

5. **Expand the research (long agentic loop):** think of other USG agencies that do similar work → find their programmes → then their grantees. **In parallel,** do the same for foundations (CEPI, Wellcome, Gates, etc.). Add more folder structure to enable this. Keep these requests logged.
   - → In progress. New `agencies/` and `foundations/` directories; one markdown file per entity (programmes + grantees). See `RESEARCH_LOG.md` for waves and `agencies/README.md` / `foundations/README.md` for the registries. Wave 1 + most of Wave 2 done; USDA, Open Philanthropy, CZI being redone (failed on rate limits).

6. **Extend coverage** to airborne-mitigation technologies — **respiratory PPE, air purifiers/filtration, germicidal UV (UVGI/far-UVC), and glycol-vapor air disinfection** — across the agencies/funders. And **build a CSV database** consolidating the programmes and grants from all the MD files for easy viewing.
   - → In progress. New `themes/air-ppe-uv-glycols.md` and `data/programs.csv` + `data/awards.csv`.
