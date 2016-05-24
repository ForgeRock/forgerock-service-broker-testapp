### Companion test app for the Forgerock Service Broker

This project contains a test app that can be pushed to Cloud Foundry and bound the the Forgerock Service Broker.  The bound test app can then participate in oauth 2 flows.

Specifically, the broker allows the creation of an [OAuth 2.0 Client Credentials Grant Process](https://backstage.forgerock.com/#!/docs/openam/13/admin-guide/chap-oauth2#figure-oauth2-client-cred)  

See installation and use instructions below.


<h3>Getting the Code</h3>

<p>The central project repository lives on the ForgeRock Bitbucket Server at 
<a href="https://stash.forgerock.org/projects/CLOUD/repos/forgerock-service-broker-testapp">https://stash.forgerock.org/projects/CLOUD/repos/forgerock-service-broker-testapp</a>.</p>

<p>Mirrors exist elsewhere (for example GitHub) but all contributions to the project are managed by using pull requests 
to the central repository.</p>

<p>There are two ways to get the code - if you want to run the code unmodified you can simply clone the central repo (or a 
reputable mirror):</p>

<pre><code>git clone https://stash.forgerock.org/cloud/forgerock-service-broker-testapp.git
</code></pre>

<p>If, however, you are considering contributing bug fixes, enhancements, or modifying the code you should fork the project
 and then clone your private fork, as described below:</p>

<ol>
<li>Create an account on <a href="https://backstage.forgerock.com">BackStage</a> - You can use these credentials to create pull requests, report bugs, and
download the enterprise release builds.</li>
<li>Log in to the Bitbucket Server using your BackStage account credentials. </li>
<li>Fork the <code>forgerock-service-broker-testapp</code> project. This will create a fork for you in your own area of Bitbucket Server. Click on your 
profile icon then select 'view profile' to see all your forks. </li>
<li>Clone your fork to your machine.</li>
</ol>

<p>Obtaining the code this way will allow you to create pull requests later. </p>


###How to use the app
   
1. push the app to Cloud Foundry
  
  Clone the testapp, then from the test app project directory:  
 <code>cf push frtestapp</code>

For complete directions on using the test app with the Forgerock Service Broker, go here:  
[https://github.com/ForgeRock/forgerock-service-broker-cloudfoundry](https://github.com/ForgeRock/forgerock-service-broker-cloudfoundry)

#### Licensing

The contents of this file are subject to the terms of the Common Development and Distribution License (the License). You may not use this file except in compliance with the License.
 
You can obtain a copy of the License at:  [https://opensource.org/licenses/CDDL-1.0](https://opensource.org/licenses/CDDL-1.0).  See the License for specific language governing permission and limitations under the License.

 
### Disclaimer
This is an alpha release of unsupported code made available by ForgeRock for community development subject to the license contained in the software. The code is provided on an "as is" basis, without warranty of any kind, to the fullest extent permitted by law. ForgeRock does not warrant or guarantee the individual success developers may have in implementing the code on their development platforms or in production configurations.

ForgeRock does not warrant, guarantee or make any representations regarding the use, results of use, accuracy, timeliness or completeness of any data or information relating to the alpha release of unsupported code. ForgeRock disclaims all warranties, expressed or implied, and in particular, disclaims all warranties of merchantability, and warranties related to the code, or any service or software related thereto.

ForgeRock shall not be liable for any direct, indirect or consequential damages or costs of any type arising out of any action taken by you or others related to the code.

Copyright © 2016 ForgeRock, Inc. All Rights Reserved. 


## All the Links

- [Cloud Foundary Service Broker Spec][service_broker_spec]  
- [Getting Started with OpenAM guide][getting_started_guide]
- [ForgeRock's commercial website][commercial_site]
- [ForgeRock's community website][community_site]
- [ForgeRock's BackStage server][backstage] 
- [OpenAM Project Page][project_page]
- [Community Forums][community_forum]
- [Enterprise Build Downloads][enterprise_builds]
- [Enterprise Documentation][enterprise_docs]
- [Nightly Build Downloads][nightly_builds]
- [Nightly Documentation][nightly_docs]
- [Central Project Repository][central_repo]
- [Issue Tracking][issue_tracking]
- [Contributors][contributors]
- [Coding Standards][coding_standards]
- [Contributions][contribute]
- [How to Buy][how_to_buy]


[commercial_site]: https://www.forgerock.com
[community_site]: https://www.forgerock.org
[backstage]: https://backstage.forgerock.com
[project_page]: https://forgerock.org/openam/
[community_forum]: https://forgerock.org/forum/fr-projects/openam/
[enterprise_builds]: https://backstage.forgerock.com/#!/downloads/OpenAM/OpenAM%20Enterprise#browse
[enterprise_docs]: https://backstage.forgerock.com/#!/docs/openam
[nightly_builds]: https://forgerock.org/downloads/openam-builds/
[nightly_docs]: https://forgerock.org/documentation/openam/
[central_repo]: https://stash.forgerock.org/projects/OPENAM
[issue_tracking]: http://bugster.forgerock.org/
[docs_project]: https://stash.forgerock.org/projects/OPENAM/repos/openam-docs/browse
[contributors]: https://stash.forgerock.org/plugins/servlet/graphs?graph=contributors&projectKey=OPENAM&repoSlug=openam&refId=all-branches&type=c&group=weeks
[coding_standards]: https://wikis.forgerock.org/confluence/display/devcom/Coding+Style+and+Guidelines
[how_to_buy]: https://www.forgerock.com/platform/how-buy/
[contribute]: https://forgerock.org/projects/contribute/
[service_broker_spec]:http://docs.cloudfoundry.org/services/api.html#api-overview  
[getting_started_guide]:https://forgerock.org/openam/doc/bootstrap/getting-started/index.html