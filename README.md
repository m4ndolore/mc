# mc

Claude plugins from [Merge Combinator](https://mergecombinator.com), a venture studio for national security.

```
/plugin marketplace add m4ndolore/mc
```

## Plugins

| Plugin | What it does | Status |
|---|---|---|
| [MC Capture](plugins/mc-capture/README.md) (`mc-capture`) | Find defense funding opportunities, get weekly alerts, and steel-man and red-team a bid | 0.1.1 |

Install one with `/plugin install <plugin>@mc`.

## Repository layout

```
.claude-plugin/
  marketplace.json       lists every plugin in this repo
plugins/
  <plugin>/
    .claude-plugin/
      plugin.json        manifest (name, version, icon, URLs)
      icon.svg
    .mcp.json            MCP servers the plugin connects
    skills/<skill>/
      SKILL.md           instructions Claude follows
      references/        detail the skill loads when it needs it
    README.md
    PRIVACY.md
    TERMS.md
tests/                   structure checks for every plugin
```

## Adding a plugin

1. Create `plugins/<name>/` with the layout above. Use the `mc-` prefix: plugin names are shared across the Claude plugin directory.
2. Add it to `.claude-plugin/marketplace.json` and to the table above.
3. Give it its own `PRIVACY.md` that says exactly what it sends and stores, and a `TERMS.md`. Set `privacyPolicyUrl`, `termsOfServiceUrl` and `documentationUrl` in `plugin.json`.
4. Run the checks below.

## Development

```
python3 -m unittest discover tests     # manifest and skill structure
claude plugin validate .               # marketplace and plugin manifests
./build.sh                             # checks, then dist/ upload files
```

The opportunities service and MCP server live in Merge Combinator's site repository (`cloudflare/opportunities-api`).
