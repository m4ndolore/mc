---
name: opportunity-alerts
description: Set up a weekly email alert for new defense opportunities that match a company's keywords and sources, through Merge Combinator's alert service. Use when someone asks to be notified, watch for new SBIR/STTR topics or solicitations, get a digest, or track a technology area over time.
---

# Opportunity alerts

Sets up a weekly email of new opportunities that match the user's terms. The `create_alert` tool on the `mc-opportunities` MCP server does the work. Merge Combinator sends the emails; this plugin stores nothing.

## How the service works

Tell the user this before you create anything:

- They get a confirmation email first. Nothing is sent until they click the link in it, and the link expires in 48 hours.
- Digests go out on Mondays and list only opportunities they have not been sent before, up to 15 per email.
- A record matches when any keyword appears in its title, description, tags or agency. With no keywords, every new opportunity matches.
- Every digest has a one-click unsubscribe link.
- One confirmation per email address per 24 hours. A second request in that window does nothing.
- Their email address and keywords are stored by Merge Combinator until they unsubscribe. See the plugin's privacy policy.

## Workflow

1. **Get the user's own email address.** Ask for it. Never use an address the user did not give you for this purpose, and never sign up someone else.
2. **Choose keywords.** Up to 10, each a short phrase. Turn the company profile into the terms agencies use: a technology ("edge AI"), a mission ("counter-UAS"), and a component or program if they care about one. Fewer, sharper terms give a better digest. If you just ran `find-opportunities`, reuse the terms that found real matches.
3. **Choose sources** only if the user wants fewer: `sbir`, `darpa`, `diu`, `colosseum`, `ratio`, `sam`. Default is all.
4. **Confirm.** Show the address, keywords and sources and ask "Create this alert?" Call `create_alert` only after a yes.
5. **Report the result** in one line: "Confirmation sent to <email>. Click the link in it within 48 hours to start the Monday digest."

## When it fails

- "Alerts are not configured": the alert service is not switched on yet. Say so, and offer a manual check: run `find-opportunities` with the same terms now.
- "Too many sign-ups right now": ask them to try again in an hour.
- To change keywords: create the alert again after 24 hours. Confirming the new request replaces the old one.
- To stop: the unsubscribe link in any digest.

## Alerts inside Claude Code

If the user wants results in Claude rather than email, a scheduled Claude Code routine can run `find-opportunities` with their terms on a cadence. Offer it as an alternative, not a replacement.
