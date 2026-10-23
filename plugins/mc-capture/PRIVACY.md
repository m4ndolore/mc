# Privacy Policy

**MC Capture**
Effective date: October 23, 2026

This policy describes how the MC Capture plugin (the "Plugin") and the Merge Combinator opportunities service it connects to (the "Service") handle information. In this policy, "you" means the person using the Plugin, "Merge Combinator" means the publisher of the Plugin and operator of the Service, and "Your Information" means any document, company detail or other content you share while using the Plugin.

## 1. What the Plugin contains

The Plugin is a set of skills and a connection to the Service at https://api.mergecombinator.com/mcp. The skills are instructions that Claude follows. The Plugin contains no scripts and stores no files.

## 2. Information sent to the Service

When Claude uses the Service on your behalf, the Plugin sends the following to Merge Combinator:

- **Searches:** the search terms, source filters and status filters for each opportunity search, and the topic identifier for each topic lookup.
- **Alerts:** if you ask for an email alert, your email address, the keywords you choose and the source filters you choose.

The Plugin does not send Your Information to the Service in any other case. Documents you share for a bid review or a writing task, and any voice profile you build, stay in your Claude conversation and in files you choose to save.

## 3. Information the Service stores

- **Searches** are not stored with any identifier of you. Merge Combinator's hosting provider, Cloudflare, keeps standard request logs, which include the request path and IP address, for a limited period under its own policies.
- **Alert requests** that you have not confirmed are deleted after 48 hours. The Service also keeps a record that a confirmation email was sent to your address, for 24 hours, to prevent repeated emails.
- **Confirmed alerts** are stored until you unsubscribe. A confirmed alert record contains your email address, your keywords and source filters, the dates you requested and confirmed it, the date of the last digest, and the identifiers of opportunities already sent to you.

## 4. How Merge Combinator uses information

Merge Combinator uses alert information only to send the weekly digest you confirmed and to avoid sending you the same opportunity twice. Merge Combinator does not sell Your Information, does not use your email address for any other mailing, and does not share it except with the email delivery provider in section 5.

## 5. Service providers

- **Cloudflare** hosts the Service and stores alert records.
- **Resend** delivers confirmation and digest emails and receives your email address and the content of each email for that purpose.

## 6. Unsubscribing and deletion

Every digest contains an unsubscribe link. Using it deletes your confirmed alert record. To ask for deletion in any other way, open an issue at https://github.com/m4ndolore/mc/issues without including your email address, and Merge Combinator will reply with a private way to verify the request.

## 7. Anthropic and Claude

The Plugin runs inside Claude, a service operated by Anthropic. Anthropic's handling of your conversations is governed by Anthropic's privacy policy at https://www.anthropic.com/legal/privacy and not by this policy.

## 8. Controlled and sensitive information

Do not share classified information, Controlled Unclassified Information or export-controlled technical data in a Claude conversation unless your organization has approved that use. The Plugin does not send document contents to the Service, but Claude processes everything you share.

## 9. Children

The Plugin is intended for businesses and professionals. It is not intended for anyone under 18.

## 10. Changes to this policy

Merge Combinator will post any change to this policy in this file and update the effective date. The history of this file in the repository shows every prior version.

## 11. Contact

Questions about this policy can be submitted as an issue at https://github.com/m4ndolore/mc/issues.
