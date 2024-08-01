---

date: 2024-08-01 00:00:00-0700
categories: blog
author: Andrew van der Stock
author_image: /assets/images/people/staff_andrew.jpg
layout: blogpost
title: OWASP Email Problems (and solutions)
excerpt_separator: <!--more-->

---

Recently, Google, Microsoft, and Yahoo and other major email providers have been implementing stricter email authentication controls. This is a good thing, as it helps to reduce the amount of spam and phishing emails that we all receive. However, it can also cause problems for legitimate email senders, such as OWASP. In the last month or so, we have experienced great difficulty in sending emails to Microsoft email addresses (Office 365, Exchange Online, Outlook, Hotmail, Live, etc). This has been a major problem for us, as many of our members and volunteers use Microsoft email addresses. We have been working hard to resolve this issue. In this post, we document a solution that every Microsoft user needs to do to reliably receive our email.

We have created staff accounts on owaspfoundation.org. Our staff will only let you know how to un-quarantine our emails, with a link to this blog post, and to ask that you reply to the original email once restored to your Inbox.

<!--more-->

OWASP has had the various controls (SPF, DKIM, DMARC) in place for several years. They were not as tight as they were required to be under the new February 2024 email guidelines promulgated by all major email providers. We have now tightened those controls to be in line with the requirements.

However, Microsoft users need to whitelist our email domains, and click "This is not junk" on our emails. This will help to improve our reputation with Microsoft, and ensure that our emails are delivered to your inbox. This is unfortunately a manual process, and one you may not realize that you need to do.

## Outlook users

1. Review your junk mail folder
2. If you find an email from an owasp.org or owasp.com email address in your junk mail folder, click on the email, and then click "This is not junk" in the toolbar. You can also just drag the message back to your Inbox. This will move the email to your inbox, and will help to improve our reputation with Microsoft
3. You can also add the email address to your safe senders list, which will help to ensure that future emails are always delivered to your inbox.

## Microsoft 365 - Exchange Online Protection (EOP) or Microsoft Defender for Office 365

If your organization uses Microsoft Office 365 or Microsoft Exchange Online, there is potentially a separate step you need to do to release the message from quarantine, and then for your administrator to add our email domains to the allow list.

- [How to release emails from quarantine as a user](https://learn.microsoft.com/en-us/defender-office-365/quarantine-end-user#take-action-on-quarantined-email)

Once requested, please ask your admins to release the email, and add owasp.org and owasp.com to allow sender list so that they don't need to do this for every email.

- [Manage quarantined messages and files as an admin](https://learn.microsoft.com/en-us/defender-office-365/quarantine-admin-manage-messages-files?source=recommendations)
- [How to handle Legitimate emails getting blocked (False Positive), using Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/how-to-handle-false-positives-in-microsoft-defender-for-office-365)
