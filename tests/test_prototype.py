"""Automated test for the Small Business Digital Health Check.

Runs the 5 hand-worked test cases on phone, iPad and laptop screen sizes and
checks the score, band, order of the top actions and that nothing scrolls sideways.

Setup:  pip install playwright && playwright install chromium
Run:    python tests/test_prototype.py                 (tests the live site)
        python tests/test_prototype.py index.html      (tests a local copy)
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

URL = "https://rhtanvir348.github.io/digital-health-check/"
if len(sys.argv) > 1:
    URL = pathlib.Path(sys.argv[1]).resolve().as_uri()

# answers Q1 -> Q20 (Y = Yes, P = Partly, N = No), expected score, band, top actions
CASES = {
    "A Well-prepared shop":     ("YYYYYYYYYYYYYYYYYYYY", "100",  "Good",    []),
    "B Typical cafe":           ("PNNYPYNNPNPNNYNNYYNP", "38.5", "At risk", [7, 12, 2, 3, 8]),
    "C No backups, rest good":  ("NNNYYYYYYYYYYYYYYYYY", "82",   "Good",    [1, 2, 3]),
    "D Starting from zero":     ("NNNNNNNNNNNNNNNNNNNN", "0",    "At risk", [1, 7, 4, 6, 12]),
    "E Secure but weak online": ("YYPYYYYYYYYYYYYYYNNN", "82.5", "Good",    [18, 19, 20, 3]),
}
DEVICES = [("Phone 390x844", {"width": 390, "height": 844}, True),
           ("iPad 820x1180", {"width": 820, "height": 1180}, True),
           ("Laptop 1440x900", {"width": 1440, "height": 900}, False)]

def run():
    failures = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, size, mobile in DEVICES:
            page = browser.new_context(viewport=size, is_mobile=mobile, has_touch=mobile).new_page()
            for case, (answers, score, band, top) in CASES.items():
                page.goto(URL)
                page.click("#start")
                pages = page.locator("fieldset.pg").count()
                for p_i in range(pages):
                    for q in page.locator(f"fieldset.pg[data-p='{p_i}'] .q").all():
                        i = int(q.get_attribute("data-i"))
                        q.locator(f".opt[data-v={answers[i]}]").click()
                    page.click("#go" if p_i == pages - 1 else "#next")
                got_top = [int(t.split("question ")[1].split(" ")[0])
                           for t in page.locator("#acts li .note").all_inner_texts() if "question" in t]
                overflow = page.evaluate("document.documentElement.scrollWidth > innerWidth")
                ok = (page.inner_text("#sc") == score and page.inner_text("#band") == band
                      and got_top == top and not overflow)
                failures += not ok
                print(f"{'PASS' if ok else 'FAIL'}  {name:16} {case:26} "
                      f"{page.inner_text('#sc'):>5} {page.inner_text('#band'):8} {got_top}")
        browser.close()
    print(f"\n{15 - failures}/15 passed")
    return failures

if __name__ == "__main__":
    sys.exit(1 if run() else 0)
