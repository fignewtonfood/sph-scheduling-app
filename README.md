# SPH Course Scheduling App — AY 2026-27

Single-page scheduling tool for the OHSU-PSU School of Public Health.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The app — deploy this to GitHub Pages |
| `data.json` | Live database (read on load, written by admin saves) |
| `build.py` | Re-injects SEED_DATA into index.html after editing data.json |

## Deployment (GitHub Pages)

1. Create a public (or private with Pages enabled) GitHub repo
2. Push `index.html` and `data.json` to the `main` branch
3. Enable GitHub Pages (Settings → Pages → Deploy from branch `main` → root `/`)
4. Your app is live at `https://<owner>.github.io/<repo>/`

## Admin Mode

1. Open the app → click **🔐 Admin** in the nav bar
2. Enter your GitHub Owner, Repo Name, Branch, and a Personal Access Token
   - Token needs `repo` scope (or `public_repo` for public repos)
   - The token is stored in **sessionStorage only** and clears when you close the tab
3. Click **Enable Admin Mode**
4. All edits auto-save to `data.json` in your repo ~1.5 seconds after a change

## SharePoint iframe (future)

Once hosted on GitHub Pages, embed via SharePoint's **Embed web part**:
```
<iframe src="https://<owner>.github.io/<repo>/" width="100%" height="800px" frameborder="0"></iframe>
```

Note: `confirm()` dialogs are fully replaced with inline modal confirmations,
so the app is safe to embed in sandboxed iframes.

## Data structure

`data.json` contains three arrays: `courses`, `instructors`, `offerings`.

## FTE rules

- FTE = Effective CR × 0.03
- Applies to: OHSU Primary, Staff, Other, NPS, OHSU Adjunct
- Effective CR = raw CR ÷ 2 for 2-instructor courses (2I flag)
- FTE-Exempt courses excluded from effective CR
