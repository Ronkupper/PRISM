# Getting started with PRISM

Step-by-step install and first engagement, by platform. The framework is identical everywhere — only **install** and **invocation** differ.

**Pick your surface:**

- **[Claude Cowork](#claude-cowork)** — the Claude desktop app; richest for multi-session work. Install the Skill.
- **[Claude Chat](#claude-chat)** — web or the desktop Chat tab. Install the Skill, *or* just attach one file.
- **[Claude Code](#claude-code)** — terminal CLI, for developers. Install the Skill.
- **[Single file](#single-file-any-vendor)** — ChatGPT, Gemini, Perplexity, or anywhere you'd rather use one artifact.

**Prerequisite (all Claude surfaces):** a paid plan — Pro, Max, Team, or Enterprise. The free tier does not include plugins, Cowork, or Code.

After install, the engagement flow is the same on every surface — see **[Run the engagement](#run-the-engagement)**.

---

## Claude Cowork

Cowork runs in the **Claude desktop app**, not a browser.

### 1. Open Cowork

1. Install or update the Claude desktop app and sign in.
2. Switch to **Cowork** in the mode picker at the top of the window.
3. First time only: in a new Cowork session, type `/setup-cowork` and press Enter to run the guided setup.

### 2. Create a project

A project is a workspace that keeps its files, instructions, and memory across sessions — a good fit for PRISM's multi-session model.

1. At the bottom of the prompt box, click **Work in a project** → hover **Projects** → **Create new project**.
2. Choose **Start from scratch**.
3. Name it (e.g. `PRISM audits`), pick a folder on your computer, leave instructions blank for now, confirm **Memory** is on, and click **Create**.

### 3. Install the PRISM Skill

1. Open the **Cowork** tab, then open **Customize** in the left sidebar → **Plugins** tab.
2. In **Personal plugins**, click **+** → **Add marketplace** → **Add from a repository**.
3. Enter `Ronkupper/PRISM` (or `https://github.com/Ronkupper/PRISM`) and sync.
4. PRISM appears in the list — click **Install**.

### 4. Start an engagement

In a Cowork session, ask in plain language:

```
Run a PRISM audit on <your subject>.
```

(On Claude / Claude Code you can also use the `/prism-start <subject>` command. It's untested in Cowork, so use the plain-language form there if the command doesn't appear in the `/` menu.)

Then follow **[Run the engagement](#run-the-engagement)**.

---

## Claude Chat

Two ways: the **Skill** (recommended; same as Cowork) or a **single file** (fastest, zero install).

### Option A — install the Skill

Skills from plugins work in chat too.

1. Open **Customize** in the left sidebar → **Plugins** tab.
2. In **Personal plugins**, click **+** → **Add marketplace** → **Add from a repository**.
3. Enter `Ronkupper/PRISM`, sync, then click **Install**.

### Option B — attach the single file

1. Download `PRISM.md` (stable) or `PRISM_v2_12_1.md` (version-pinned) from the repo.
   Raw URL: `https://raw.githubusercontent.com/Ronkupper/PRISM/main/PRISM.md`
2. *Recommended:* create a **Project** (sidebar → **Projects** → **Create Project** → name it), then add `PRISM.md` to project knowledge so every chat in it has the framework loaded. Or attach `PRISM.md` directly to a single chat.

### Start an engagement

```
Run a PRISM audit on <your subject>.
```

On the Skill you can also use `/prism-start <subject>`. Then follow **[Run the engagement](#run-the-engagement)**.

---

## Claude Code

For the terminal. Requires a paid plan (free tier excluded).

### 1. Install Claude Code

Native installer (recommended — no Node.js):

- macOS / Linux / WSL: `curl -fsSL claude.ai/install.sh | bash`
- Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

Or with npm (Node.js 18+): `npm install -g @anthropic-ai/claude-code`

Then start and log in:

```
claude
/login
```

Official setup reference: <https://code.claude.com/docs/en/setup>

### 2. Install the PRISM Skill

In a Claude Code session:

```
/plugin marketplace add Ronkupper/PRISM
/plugin install prism@prism
```

### 3. Start an engagement

```
/prism-start <your subject>
```

Or ask in plain language: `Run a PRISM audit on <your subject>.` Then follow **[Run the engagement](#run-the-engagement)**.

---

## Single file (any vendor)

On ChatGPT, Gemini, Perplexity, or anywhere you'd rather use one artifact: attach `PRISM.md` to a fresh chat and ask `Run a PRISM audit on <subject>.` The single file carries the whole framework, including the Lens Library (Appendix G).

Note: orchestration is built and tested on **Claude** — running it on another vendor is likely workable but untested.

---

## Run the engagement

Once PRISM is active, the flow is the same on every surface:

1. **State the subject.** Tell it what you want to audit or research.
2. **Setup probes (P1–P7).** Answer the seven scope-definition probes. They grade your draft strategy against the **Lens Library** (the audit-scope catalog) so silent gaps surface *before* any prompt ships.
3. **Iterate to readiness.** Refine scope until you clear three-layer readiness.
4. **Dispatch.** Send the atomic prompts it produces to whichever model suits each one. They're self-contained, so the executing model needs no knowledge of PRISM.
5. **Continue across sessions.** Each session updates the Master and a *What's next* note. Reopen later — even in a fresh chat — and ask `What's next?` (or run `/prism-whats-next` on the Skill) to resume exactly where you left off.

Worked example: §15 of `PRISM.md`.

---

## Notes

- **`/prism-start` scope.** Confirmed on Claude and Claude Code; untested in Cowork. The natural-language form (`Run a PRISM audit on…`) works everywhere and is the portable path on non-Claude vendors.
- **Installing via the app vs. the CLI.** In Cowork and Chat you install through the **Customize → Plugins** UI — typing `/plugin …` in the chat box won't work there (that syntax is Claude Code only).
- **Updating the Skill.** Cowork / Chat: Customize → Plugins → refresh the marketplace. Code: `/plugin marketplace update`, then `/plugin install prism@prism`.
