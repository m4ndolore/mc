#!/usr/bin/env bash
# Build upload files for people who install by hand:
#   dist/<plugin>.plugin   Customize > Plugins > Add > Upload plugin
#   dist/<skill>-skill.zip Customize > Skills > + > Upload a skill
set -euo pipefail
cd "$(dirname "$0")"
python3 -m unittest discover -s tests -q
rm -rf dist
mkdir dist
for plugin in plugins/*/; do
  name=$(basename "$plugin")
  (cd "$plugin" && zip -qr "../../dist/${name}.plugin" . -x '*.DS_Store')
  for dir in "$plugin"skills/*/; do
    skill=$(basename "$dir")
    (cd "${plugin}skills" && zip -qr "../../../dist/${skill}-skill.zip" "$skill" -x '*.DS_Store')
  done
done
ls -l dist
