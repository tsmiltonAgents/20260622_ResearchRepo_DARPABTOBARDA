# Autonomous grant-database research loop

A self-paced loop that runs for ~5 hours (started **2026-06-23 02:32 BST**, deadline **~07:32 BST**), ideating and executing new grant-database research directions to extend this project.

## How each cycle works
1. Read `BACKLOG.md`; pick the highest-priority `pending` direction.
2. Spawn web-research subagent(s) for that direction (a new funder, country, or thematic cross-cut).
3. Write the resulting markdown file (`international/<x>.md`, `foundations/<x>.md`, or `themes/<x>.md`).
4. Extract its programmes/awards into `data/programs.csv` and `data/awards.csv` (same schema; normalize the new `amount_usd_millions` and `funder_type`).
5. Commit + push.
6. Append a cycle entry to `LOOP_LOG.md`; mark the backlog item `done`. **Ideate:** add any newly-discovered funders/directions to `BACKLOG.md`.
7. If before the deadline, schedule the next cycle (~20–25 min); else stop and write a final summary.

## State files
- `BACKLOG.md` — the prioritized queue (the loop both consumes and adds to it).
- `LOOP_LOG.md` — one entry per completed cycle.

## Design notes
- Runs in the local session (needs the local git repo + `gh`); not a cloud cron job.
- The markdown files stay authoritative (full caveats + sources); the CSVs are the flattened index.
- Amounts kept verbatim + a best-effort numeric column; never naively summed.
