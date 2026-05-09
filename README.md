# Digital Bit

A **learning lab** that combines a Groq-powered note generator, GitHub Actions (and optional external cron), and a **Vite + React + Three.js** front end. New markdown lessons land in `content/modules/<track>/` in a fixed **round-robin track order**; the site reads them at **build time** and presents them as a small curriculum.

---

## Repository layout

```
Digital-Bit/
├── content/modules/          # Generated Markdown notes (one folder per track)
│   ├── dsa-algorithms/
│   ├── frontend-basics/
│   ├── javascript-typescript/
│   ├── backend/
│   ├── system-design/
│   ├── devops/
│   └── dbms/
├── scripts/
│   ├── daily_post.py        # Content-note generator
│   └── autopilot_maintain.py # No-touch task rotator (content/metrics/highlights)
├── web/                     # Frontend (Vite + React + TypeScript + Three.js)
│   ├── src/
│   │   ├── lib/moduleCatalog.ts   # Track labels & order — keep in sync with daily_post.py MODULES
│   │   └── ...
│   ├── package.json
│   └── vite.config.ts
├── .github/workflows/
│   └── daily-content.yml    # CI: checkout → autopilot task → commit → push
├── vercel.json              # Monorepo build: install/build inside web/, SPA rewrites
├── .env.example             # Local Groq key template (never commit real .env)
└── README.md
```

**Important:** The sequence **`MODULES`** in `scripts/daily_post.py` and **`MODULE_CATALOG`** in `web/src/lib/moduleCatalog.ts` describe the same tracks in the **same order**. If you add or reorder tracks, update **both**.

---

## Track order (automation)

Each successful generator run targets **one** module, advancing in order:

1. `dsa-algorithms`  
2. `frontend-basics`  
3. `javascript-typescript`  
4. `backend`  
5. `system-design`  
6. `devops`  
7. `dbms`  

- **On GitHub Actions:** index = `(GITHUB_RUN_NUMBER - 1) % len(MODULES)` so run `#1` hits DSA, `#2` frontend, etc.  
- **Locally:** index = `(number of existing *.md files under content/modules) % len(MODULES)`.

Within a run, the LLM also gets a **random “today’s focus”** line per track so posts don’t all read the same.

---

## Local development

### Generator

```bash
cp .env.example .env   # add GROQ_API_KEY from https://console.groq.com
python3 scripts/daily_post.py
```
### No-touch autopilot (recommended)

```bash
python3 scripts/autopilot_maintain.py
```

`autopilot_maintain.py` rotates genuine maintenance tasks automatically:

- `content-note` → generates a new module markdown note
- `module-metrics` → refreshes `content/automation/module-metrics.json`
- `highlights` → refreshes `content/automation/recent-highlights.md`
- `legacy-upgrade` → updates an existing older module with a senior interview checkpoint
- `ui-polish` → applies safe UI metadata polish in `web/src/lib/moduleCatalog.ts`

Optional env override:

- `AUTOPILOT_MODE=content-note|module-metrics|highlights|legacy-upgrade|ui-polish|combo`
- `AUTOPILOT_ALLOW_NEW_CONTENT=0` disables new-file `content-note` commits in auto rotation


Stderr prints whether Groq succeeded; stdout prints the new file path relative to repo root.

### Website

```bash
cd web
npm install
npm run dev
```

Open the printed localhost URL. Use **`/?m=<track-id>`** to filter (e.g. `/?m=backend`). **`/`** shows all tracks.

### Production build

```bash
cd web && npm run build
```

Output: `web/dist/`.

---

## GitHub Actions

1. **Settings → Actions → General → Workflow permissions:** **Read and write** (so the workflow can push commits).  
2. **Secrets:** `GROQ_API_KEY` (recommended), optional `GIT_USER_NAME`, `GIT_USER_EMAIL`, `LLM_MODEL`.  
3. **`on.schedule`:** GitHub only guarantees a **minimum** of **5 minutes** between scheduled runs; delays are normal. For clock-stable **every 5 minutes**, trigger **`workflow_dispatch`** from an external cron using the REST API and a PAT (see earlier setup notes).

Workflow file: `.github/workflows/daily-content.yml`.

The workflow now runs `scripts/autopilot_maintain.py`, commits only when git has staged changes, and pushes with commit message:

- `autopilot(<mode>): real maintenance update`

---

## Deploy (Vercel)

Root `vercel.json` builds `web/` and sets SPA rewrites for client-side routes.

- **Install:** `npm install --prefix web`  
- **Build:** `npm run build --prefix web`  
- **Output:** `web/dist`

---

## Security

- Never commit **`.env`** or API keys.  
- Rotate any key that appeared in a screenshot or chat.  
- PAT used for `workflow_dispatch` should be **scoped** to this repo and stored only in your scheduler’s secrets.

---

## License

Add a license file when you decide how you want to share the project.
