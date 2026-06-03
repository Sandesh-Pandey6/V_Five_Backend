# Connect PostgreSQL to V Five Backend (pgAdmin)

## What you need

1. **PostgreSQL** running (the server you open in pgAdmin)
2. **Database** named `vfive`
3. A **user + password** that can access that database
4. **`DATABASE_URL`** in `backend/.env` matching pgAdmin
5. **Alembic migration** run once to create tables

---

## Step 1 — pgAdmin: create the database

1. Open **pgAdmin**
2. Connect to your server (e.g. `PostgreSQL 16` on `localhost`)
3. Right-click **Databases** → **Create** → **Database…**
4. **Database name:** `vfive` → **Save**

---

## Step 2 — pgAdmin: note your login details

In pgAdmin, when you connect to the server, you use a **username** and **password**. Common setups:

| Setup | Username | Password |
|--------|----------|----------|
| Default install | `postgres` | The password you chose at install |
| Custom role | e.g. `vfive` | Password you set for that role |

You do **not** need a user named `vfive` unless you created one. Using **`postgres`** is fine.

To create role `vfive` (optional): **Login/Group Roles** → **Create** → **Role** → name `vfive`, set password, then grant privileges on database `vfive`.

---

## Step 3 — Edit `backend/.env`

Open `d:\V Five\backend\.env` and set **one** line (no spaces around `=`):

**If you use the default `postgres` user:**

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/vfive
```

Replace `YOUR_PASSWORD` with your real pgAdmin/PostgreSQL password.

**If you created user `vfive`:**

```env
DATABASE_URL=postgresql+psycopg://vfive:YOUR_PASSWORD@localhost:5432/vfive
```

**URL format:**

```
postgresql+psycopg://USERNAME:PASSWORD@HOST:PORT/DATABASE
```

- **HOST:** usually `localhost`
- **PORT:** usually `5432` (check server properties in pgAdmin if unsure)
- **DATABASE:** `vfive`

---

## Step 4 — Install dependencies (once)

```powershell
cd "d:\V Five\backend"
.\.venv\Scripts\pip install -r requirements.txt
```

---

## Step 5 — Create tables (Alembic)

```powershell
cd "d:\V Five\backend"
.\.venv\Scripts\alembic upgrade head
```

You should see something like `Running upgrade  -> 001`.

In pgAdmin: **vfive** → **Schemas** → **public** → **Tables** → you should see these **6 tables** (same names as the admin sidebar):

| Table | Admin menu |
|--------|------------|
| `home` | Home |
| `courses` | Courses |
| `destinations` | Destinations |
| `study_abroad` | Study Abroad |
| `about_us` | About Us |
| `contact_us` | Contact Us |

---

## Step 6 — Seed default CMS data (optional)

```powershell
.\.venv\Scripts\python scripts\seed_cms.py
```

Or skip — data is auto-seeded on the first API request when the table is empty.

---

## Step 7 — Test connection

```powershell
.\.venv\Scripts\python scripts\test_db.py
```

Expected: `Database connection successful!`

Or start the API:

```powershell
.\.venv\Scripts\uvicorn app.main:app --reload --port 8000
```

Open: http://localhost:8000/api/health  

Look for: `"database": "connected"`

---

## Step 8 — Run the full app

**Terminal 1 — Backend:**

```powershell
cd "d:\V Five\backend"
.\.venv\Scripts\uvicorn app.main:app --reload --port 8000
```

**Terminal 2 — Frontend:**

```powershell
cd "d:\V Five\frontend"
npm run dev
```

Admin saves (Home, Courses, etc.) are stored in **`cms_sections`** in PostgreSQL.

---

## Troubleshooting

| Error | Fix |
|--------|-----|
| `password authentication failed for user "vfive"` | User/password wrong — use `postgres` + your real password in `DATABASE_URL` |
| `database "vfive" does not exist` | Create database `vfive` in pgAdmin (Step 1) |
| `connection refused` | Start PostgreSQL service (Windows Services or pgAdmin server must connect) |
| `relation "home" does not exist` (or other table) | Run `alembic upgrade head` |
| Health shows `database: disconnected` | Fix `DATABASE_URL`, restart uvicorn |

---

## View saved content in pgAdmin

**vfive** → **Schemas** → **public** → **Tables** → e.g. **home** → right-click → **View/Edit Data**

Each table has one (or more) rows; column **`data`** is JSON with that page’s content (text, image URLs, etc.).
