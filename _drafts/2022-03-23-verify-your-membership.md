---

date: 2022-03-23 00:00:00-0700
categories: blog
author: Andrew van der Stock
author_image: /assets/images/people/staff_andrew.jpg
layout: blogpost
title: OWASP Membership Data Cleanup - please verify your membership
excerpt_separator: <!--more-->

---

As a result of historically poor data quality, communications are being sent to folks who have lifetime memberships, or have memberships that don't expire for some time. This can be construed as an extremely poor customer experience, for which I unconditionally apologize. Data quality is a shared responsbility between OWASP and our members: OWASP needs to maintain an accurate single source of truth, and our members need to maintain their own data. In the past, issues crept in that allowed for multiple records, and many members never updated incorrect data. As we move to a new AMS, we have to clean up our data, but additionally, right now, we want these incorrect emails and deactivations to stop, and for that, we need your help.

Our call to action is every member should login to the [OWASP Membership portal](https://members.owasp.org) with your owasp.org email address, review, and as necessary update their membership data and contact preferences. Please update your membership record. If you can't login, please [log a support ticket](https://owasporg.atlassian.net/servicedesk/customer/portal/9). 

<!--more-->

Right now, poor data quality is creating about 3-5 support tickets per day, and likely some members are just giving up. This is creating a lot of confusion and dissatisfaction and we want to fix it and make it right.

## Call to Action - Please Verify and Update your data

If we don't resolve the data quality issues now, the new AMS will suffer from the same problem as our current system does - garbage in, garbage out. We need your help to test and correct your data.

Please login to the [OWASP Membership portal](https://members.owasp.org) with your owasp.org email address, review, and as necessary update their membership data and contact preferences. Please update your membership record. If you can't login, please [log a support ticket](https://owasporg.atlassian.net/servicedesk/customer/portal/9). If you do not currently have an owasp.org email address and are a member, you can provision one at [Manage Membership](https://owasp.org/manage-membership/)

You can also send an email to membership@owasp.com if you have questions that do not require an immediate answer or resolution. In general, logging tickets is the fastest way to get help.

## What is going wrong?

OWASP automation to clear up expired OWASP membership and associated owasp.org email accounts has been going for a couple of months now. Due to the amount of emails it sends and resulting deactivation of membership and email, between 3-5 members log support tickets, which usually have either multiple records or incorrect data or both. We will continue to investigate fuzzy data searches to identify more records at risk and fix them, but there will still be poor quality records.

This issue revolves around two main items: members having multiple records, such as registering with an old email address and then renewing through an owasp.org email address, or one or more membership records have missing or incorrect data, particularly relating to mismatched names or email addresses.

The automation process iterates over all owasp.org email addresses every night and compares them to OWASP memberships. For members with multiple records, one of the records is likely expired or was never a member. We need to merge these records to ensure continuous membership. For example, the code cannot tell if two records for "Andrew van der Stock" with two different email addresses are the same person. Even staff might have a hard time with that for particularly common names.

## What we are doing about it

We will process support tickets and get things fixed for you. Once a support ticket has been logged, our Chapter and Membership Manager will review the issue, and likely manually merge all your records into a single record or work with you to manually correct whatever is causing the issue. We will check our payments platform to confirm or correct membership dates. After this is done, the membership issue should go away, but we'd like for you to review and update your membership data just in case.

We have been working behind the scenes to improve your membership data, looking for likely duplicate records. All the easily matchable records have been merged for a month or more. We are now looking into doing fuzzy name and email searches to identify likely similar accounts, but if the names are sufficiently different or email addresses wildly different, there will still be records that we don't yet know about.

We are implementing and communicating with our community to participate in this data quality improvement drive, and promoting it every week on our social media, membership mail outs, and more until we need to freeze membership applications and data changes so we import and migrate to the new AMS.

## Making things right

Data quality is a shared responsibility: members need to verify and keep their details up to date. OWASP needs an AMS that maintains a single source of truth and keeps accurate records, which we will be finally getting in the next few months.

I understand and apologize for the distress and disruption caused by this issue. We hope that once the new AMS is in place, we will have sufficient data quality that this will not be an issue after June this year. Until then, as a thank you for you taking the time to update your data with us, we will be making it right, by:

- Every resolved membership deactivation support ticket since automation started will have an additional week added to the end of your current membership to cover any membership days lost due to resolving the issue.
- For Lifetime members, I will contact them individually, and obtain contact information to send them a gold Lifetime membership pin.
- If you want to stand in the Global Board election, and there was a more than a seven day "lapse" of membership created by data quality issues, please let us know in the support ticket or create a new one if you've already been assisted. You can do that right up until you submit your nomination as a candidate.
