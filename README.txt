KOTE Multi Asset Windows Local v1.3

1. Close previous KOTE black command window.
2. Extract this ZIP to a new folder.
3. Double-click START_KOTE.bat (Python 3 required).
4. Visit http://localhost:8505 and click Sync NAVs & recalculate.
5. Scroll below the original dashboard to view the historical NAV chart, 10/20/30-year scenario simulator, monthly SWP schedule and annual legacy milestones.
6. Change assumptions and click Recalculate projection. Export monthly projection CSV if desired.

Important: For offline use, copy nav_cache folder from your previous installation into this new folder BEFORE opening, or sync online first. Keep your nav_cache folder for future upgrades.

Historical chart uses actual downloaded fund NAV histories and virtual transactions. Forecast is purely hypothetical, with annual assumed rates of 5%, 9%, 12%, or custom, compounded monthly. Forecast excludes taxes, loads, inflation, and fund-specific return variation. It is not investment advice or a guarantee. Nippon Small Cap lump-sum purchase is hypothetical subject to investment restrictions.

V1.4: The first SWP is calculated automatically from the virtual purchase date: the first 10th of a month at least one calendar year after purchase. The field is read-only. Each fund redemption also checks its actual first NAV purchase date for one-year eligibility.

V1.5 historical example: set Virtual purchase date to 2023-01-01 and valuation date to 2026-10-08; first scheduled SWP is 2024-01-10, and past withdrawals are calculated from NAV history. Click Sync NAVs & recalculate. For a 2023-01-15 purchase, first SWP is 2024-02-10, ensuring a full year has elapsed.

V1.6: Annual extra withdrawal and month removed from simulator. Annual SWP rise (%) now lives in simulator and applies to historical and future SWPs; click Sync NAVs & recalculate after changing it. The rate increases monthly SWP on each SWP anniversary.

V1.7: Annual SWP rise (%) moved into the main control row directly beside Monthly SWP (₹). Same single input controls historical and projected SWPs.
