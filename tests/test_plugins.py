"""Structure checks for every plugin listed in the marketplace."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def frontmatter(path):
    match = FRONTMATTER.match(path.read_text())
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def plugin_dirs():
    return [(p["name"], (ROOT / p["source"]).resolve()) for p in MARKETPLACE["plugins"]]


class MarketplaceTest(unittest.TestCase):
    def test_marketplace_name(self):
        self.assertEqual(MARKETPLACE["name"], "mc")

    def test_plugin_names_are_prefixed(self):
        for name, _ in plugin_dirs():
            self.assertTrue(name.startswith("mc-"), name)


class PluginTest(unittest.TestCase):
    def test_manifest_matches_marketplace(self):
        for name, path in plugin_dirs():
            manifest = json.loads((path / ".claude-plugin" / "plugin.json").read_text())
            self.assertEqual(manifest["name"], name)
            self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
            for key in ("privacyPolicyUrl", "supportUrl", "homepage", "repository"):
                self.assertTrue(manifest[key].startswith("https://"), key)
            self.assertTrue((path / manifest["icon"]).is_file(), manifest["icon"])

    def test_privacy_policy_exists(self):
        for _, path in plugin_dirs():
            self.assertTrue((path / "PRIVACY.md").is_file())

    def test_mcp_servers_use_https(self):
        for _, path in plugin_dirs():
            mcp = path / ".mcp.json"
            if not mcp.exists():
                continue
            for name, server in json.loads(mcp.read_text())["mcpServers"].items():
                self.assertTrue(server["url"].startswith("https://"), name)

    def test_skills(self):
        for _, path in plugin_dirs():
            skills = sorted((path / "skills").iterdir())
            self.assertTrue(skills)
            for skill in skills:
                fields = frontmatter(skill / "SKILL.md")
                self.assertEqual(fields.get("name"), skill.name)
                description = fields.get("description", "")
                self.assertTrue(20 < len(description) <= 1024, skill.name)

    def test_relative_links_resolve(self):
        for _, path in plugin_dirs():
            for md in path.rglob("*.md"):
                for target in re.findall(r"\]\(([^)#:]+)(?:#[^)]*)?\)", md.read_text()):
                    self.assertTrue((md.parent / target).exists(), f"{md}: {target}")


if __name__ == "__main__":
    unittest.main()
