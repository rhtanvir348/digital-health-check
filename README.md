# Small Business Digital Health Check

ITIH101 Innovation Hub 1 · Group 03 · Project 6

**Live site:** https://rhtanvir348.github.io/digital-health-check/

A free web tool for small business owners. Answer 20 Yes / Partly / No questions about IT security and online presence, get a score out of 100 and the five most important things to fix, each linked to official advice (cyber.gov.au, business.gov.au, Business Queensland).

- Plain HTML, CSS and JavaScript in one file (`index.html`), no frameworks, hosted free on GitHub Pages
- Scoring runs in the browser; nothing is saved or sent anywhere
- No names, passwords or financial details are asked
- Separate layouts for phone, tablet and laptop
- Print / save as PDF and Copy results so owners can keep their report

## Scoring
- Yes = full points, Partly = half, No = 0 (total 100)
- 80+ Good · 50–79.5 Needs work · below 50 At risk
- Top 5 = most points lost; tie → higher-points question first, then lower question number

## Testing
- `tests/test-cases.md` – the 5 hand-worked test cases and results for each version
- `tests/test_prototype.py` – automated check of all 5 cases on phone, iPad and laptop sizes

## Versions
- v1.1 (11 Nov) – scoring, band, top 5; questions reworded after owner interviews
- v1.3 (Week 3) – print/save as PDF, copy results, date, phone layout; advice links moved to the new ACSC Small business cyber security handbook
- v1.4 (Week 3) – new responsive design: 6 colour-coded area pages, progress bar and step tracker, score-ring results; scoring unchanged

## Team
Masrafi Zaman Risan (Team Leader) · Md Rakibul Hasan Tanvir (Technical Lead) · Tahjib Islam Bhuiyan (Research Lead) · Md Shyreen Kabir Shopta (Testing Lead) · Ahosan Afri (Documentation Lead)

*This tool is a guide only and is not professional advice.*
