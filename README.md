# V Five Education — Backend

FastAPI API for the V Five website: CMS content (PostgreSQL), admin login, contact inquiries, and optional Cloudinary image uploads.

---

## Prerequisites

Install before you start:

| Tool | Version |
|------|---------|
| [Python](https://www.python.org/) | 3.11 or newer |
| [PostgreSQL](https://www.postgresql.org/) | 14+ (pgAdmin optional but helpful) |
| [Git](https://git-scm.com/) | Any recent version |

---

## Step-by-step: from GitHub clone to running API

### Step 1 — Clone the repository

```powershell
git clone <your-github-repo-url>
cd "V Five\backend"
```

macOS / Linux:

```bash
git clone <your-github-repo-url>
cd "V Five/backend"
```

---

### Step 2 — Create a Python virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt.

---

### Step 3 — Install Python packages

```powershell
pip install -r requirements.txt
```

---

### Step 4 — Create your environment file

**Windows:**

```powershell
copy .env.example .env
```

**macOS / Linux:**

```bash
cp .env.example .env
```

Open `.env` in an editor and set at least these values:

| Variable | What to put |
|----------|-------------|
| `DATABASE_URL` | `postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/vfive` |
| `ADMIN_EMAIL` | Email for the first admin login |
| `ADMIN_PASSWORD` | Strong password (not `admin123` in production) |
| `SECRET_KEY` | Long random string for JWT tokens |
| `CORS_ORIGINS` | `http://localhost:3000` (frontend URL) |

`CLOUDINARY_*` is optional — only needed for image uploads in admin.

---

### Step 5 — Create the PostgreSQL database

1. Open **pgAdmin** (or any PostgreSQL client).
2. Connect to your local server.
3. Right-click **Databases** → **Create** → **Database…**
4. Database name: **`vfive`**
5. Click **Save**

If the database already exists, you can skip this step.

More detail: [DATABASE_SETUP.md](./DATABASE_SETUP.md)

---

### Step 6 — Run database migrations (required)

Migrations create and update all tables (CMS pages, admin users, inquiries, footer, etc.).

**Windows:**

```powershell
.\.venv\Scripts\alembic upgrade head
```

**macOS / Linux:**

```bash
.venv/bin/alembic upgrade head
```

**Expected result:** command finishes with no errors. Current head revision is **`007`**.

Verify:

```powershell
.\.venv\Scripts\alembic current
```

Should show: `007 (head)`

#### What the migrations create

| Revision | Purpose |
|----------|---------|
| `001` | Legacy `cms_sections` (migrated away in `002`) |
| `002` | CMS tables: `home`, `courses`, `destinations`, `study_abroad`, `about_us`, `contact_us` |
| `003` | `inquiries` table |
| `004` | `admin_users` table |
| `005` | `role` on admin users (`superadmin` / `user`) |
| `006` | Removes old newsletter table |
| `007` | `footer` CMS table |

#### After every `git pull`

If teammates added new migration files, run again:

```powershell
.\.venv\Scripts\alembic upgrade head
```

#### Windows one-command setup (migrate + seed + test)

From the `backend` folder (creates venv deps if needed):

```powershell
.\migrate.ps1
```

This runs: `pip install` → `alembic upgrade head` → `seed_cms.py` → `seed_admin_users.py` → `test_db.py`

---

### Step 7 — Seed default data (recommended)

**CMS content** (home, courses, destinations, etc.):

```powershell
.\.venv\Scripts\python scripts\seed_cms.py
```

**First admin user** (only if `admin_users` table is empty):

```powershell
.\.venv\Scripts\python scripts\seed_admin_users.py
```

Uses `ADMIN_EMAIL` and `ADMIN_PASSWORD` from `.env`.

> CMS tables also auto-fill on first API request if they are empty, but running the seed scripts is clearer for a fresh install.

---

### Step 8 — Test the database connection

```powershell
.\.venv\Scripts\python scripts\test_db.py
```

You should see:

- `Database connection successful!`
- List of tables including `home`, `footer`, `admin_users`, etc.

---

### Step 9 — Start the API server

```powershell
.\.venv\Scripts\uvicorn app.main:app --reload --port 8000
```

**macOS / Linux:**

```bash
.venv/bin/uvicorn app.main:app --reload --port 8000
```

| URL | Purpose |
|-----|---------|
| http://localhost:8000/api/health | Health + DB status |
| http://localhost:8000/docs | Swagger API docs |

Health check should include `"database": "connected"`.

Leave this terminal running. Start the frontend in a **second terminal** — see [../frontend/README.md](../frontend/README.md).

---

## Common Alembic commands

```powershell
# Apply all pending migrations
.\.venv\Scripts\alembic upgrade head

# Show current DB revision
.\.venv\Scripts\alembic current

# Show migration history
.\.venv\Scripts\alembic history

# Roll back one step (careful — can lose data)
.\.venv\Scripts\alembic downgrade -1
```

---

## Project structure

```
backend/
├── app/
│   ├── main.py              # FastAPI entry
│   ├── routers/             # auth, cms, users, inquiries, uploads
│   ├── db/models.py         # SQLAlchemy models
│   ├── schemas.py           # API models
│   └── defaults.py          # Default CMS JSON
├── alembic/versions/        # Migration files (001–007)
├── scripts/
│   ├── seed_cms.py
│   ├── seed_admin_users.py
│   └── test_db.py
├── requirements.txt
├── .env.example             # Copy to .env (not committed)
├── migrate.ps1              # Windows setup helper
└── DATABASE_SETUP.md
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `password authentication failed` | Fix user/password in `DATABASE_URL` |
| `database "vfive" does not exist` | Create database `vfive` in pgAdmin (Step 5) |
| `connection refused` | Start PostgreSQL service |
| `relation "home" does not exist` | Run `alembic upgrade head` (Step 6) |
| Health shows `database: disconnected` | Check `DATABASE_URL`, restart uvicorn |
| Admin login fails | Run `seed_admin_users.py`; check email/password in `.env` |
| Port 8000 in use | Stop other process or use `--port 8001` and update frontend `.env.local` |

---

## Production checklist

- [ ] Strong `SECRET_KEY` and `ADMIN_PASSWORD`
- [ ] Hosted PostgreSQL with SSL in `DATABASE_URL`
- [ ] `CORS_ORIGINS` set to your real frontend domain
- [ ] Run `alembic upgrade head` on deploy before starting the server
- [ ] Do not commit `.env` (see `.gitignore`)
