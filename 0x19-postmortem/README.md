# 0x19. Postmortem
This is a fake postmortem , where in an API infrastructure an outage ocurred. 
The following is the incident report for the Mama Ines API infrastructure outage that occurred on January23, 2021. We recognize that our respected developers and customers have been affected by this service issue, and we apologise to anyone who was impacted.
![](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mercadoslpineda.co%2Fes%2Fcroissant%2F442-croissant-mama-ines-x-330-g-20-unds.html&psig=AOvVaw126MV7QbvVYh1TNs5OjqLm&ust=1612830152385000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLjcg96C2e4CFQAAAAAdAAAAABAD)
## Issue Summary 
Requests to most Mama Ines APIs culminated in 500 error-response messages from 7:31 PM to 9:21 PM PT. The apps that rely on these APIs often return or have decreased feature errors. At its height, 100% of the traffic to this API infrastructure was impacted by the problem. Certain APIs that operate on different infrastructures will continue to be accessed by users.An invalid configuration change that revealed a flaw in a commonly used internal library was the root cause of this outage.
## Timeline
07:31 PM - Outage begins.

07:33 PM - The developer team noticed webpage returning 500 error.

07:35 PM -  A ticket was opened by the developer's team leader. Servers reverted to most recent working change until error is resolved.

08:14 PM - Successful configuration change rollback.

08:45 PM - Server restarts begin.

09:01 PM - Puppet script was created to remove the bug from the servers, and ran `puppet apply` to enact script.

09:21 PM - Servers were updated with new change and 100% of traffic is back online.

## Corrective/Preventative measures
This issue could have been prevented by unit tests or checking code before pressing. Integrate pre-testing prior to moving the development code.
We've done an internal evaluation and examination of the outage in the last two days. The following are steps we are taking to tackle the root causes of the problem and to help reduce recurrence and boost response times:
- Until safer steps are introduced, disable the existing configuration release function. (Accomplished.)
- To be swifter and more stable, adjust the rollback mechanism.
- Fixes and monitors the underlying authentication libraries to better timeout/interrupt errors.
- Enforce staged rollouts with all configuration modifications programmatically.
- Improving the auditing process for all high-risk configuration choices.
- Add a quicker rollback mechanism and boost the process of traffic ramp-up, so that it is possible to correct any potential issues of this kind quickly.
- Build a better system to provide status updates quickly during incidents.

Mama Ines is committed to continually and quickly improving our technology and operational processes to prevent outages. We appreciate your patience and again apologize for the impact to you, your users, and your organization. We thank you for your business and continued support.

