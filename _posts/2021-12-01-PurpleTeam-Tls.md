---
date:   2021-12-01 09:00:00 -0700
categories: blog
author: Kim Carter
author_image: /www-project-purpleteam/assets/images/posts/PT_SSLDeploy_210c.png
layout: blogpost
title: PurpleTeam TLS Tester Implementation
excerpt_separator: <!--more-->

---

The _PurpleTeam_ TLS _Tester_ is now implemented. All core components were released as version `1.0.0-alpha.3`. To hear about the highlights and significant changes that were made as part of the release, see the following



<iframe width="894" height="500" src="https://www.youtube.com/embed/ACuaP-ZToKw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<!--more-->

<br>

The details of the above video can be found [here](https://purpleteam-labs.com/project/video-pt-full-system-run-2021/).

# Contents

* [Documentation](#documentation)
* [Work items created](#work-items-created)
* [Synchronisation](#synchronisation)
  * [Time-outs](#time-outs)
    * [CLI](#cli)
      * [For the `test` command](#for-the-test-command)
      * [For `tester[ Progress | PctComplete | BugCount ]` updates](#for-tester-progress--pctcomplete--bugcount--updates)
    * [Orchestrator](#orchestrator)
    * [App Tester](#app-tester)
    * [Tls Tester](#tls-tester)
  * [Message flows](#message-flows)
* [TLS Tester Implementation](#tls-tester-implementation)

All of the release notes can be accessed from the [Github issue](https://github.com/purpleteam-labs/purpleteam/issues/60).

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Massive set of releases just gone live around the new <a href="https://twitter.com/hashtag/SSL?src=hash&amp;ref_src=twsrc%5Etfw">#SSL</a> <a href="https://twitter.com/hashtag/TLS?src=hash&amp;ref_src=twsrc%5Etfw">#TLS</a> <a href="https://twitter.com/hashtag/Tester?src=hash&amp;ref_src=twsrc%5Etfw">#Tester</a> <a href="https://t.co/f0bPNRBjUh">https://t.co/f0bPNRBjUh</a></p>&mdash; PurpleTeam (@purpleteamlabs) <a href="https://twitter.com/purpleteamlabs/status/1433018222412910595?ref_src=twsrc%5Etfw">September 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

# Documentation

* The [Definitions](https://purpleteam-labs.com/doc/definitions/) were updated
* The [Log and Outcomes files](https://purpleteam-labs.com/doc/log-and-outcomes-files/) page was created, providing details of the _Outcomes_ archive, what's in it and how to read specific files. You can also [see the contents](https://www.youtube.com/watch?v=nJNAbGLCGNY&t=346s) of the _Outcomes_ archive for [this _Job_ file](https://github.com/purpleteam-labs/purpleteam/blob/main/testResources/jobs/job_1.0.0-alpha.3_local)
* The main architecture diagrams for [`cloud`](https://purpleteam-labs.com/doc/cloud/) and [`local`](https://purpleteam-labs.com/doc/local/set-up/) have been updated
* The _Job_ file schema has been [documented](https://purpleteam-labs.com/doc/job-file/)
* A [FAQ](https://purpleteam-labs.com/doc/faq/) page was created
* [Setting up](https://purpleteam-labs.com/doc/local/set-up/#tls-scanner) the Tls Tester, although this is trivial
* [Debugging the Tls Tester](https://purpleteam-labs.com/doc/local/workflow/#other-testers)

# Work items created

As a result of the Tls Tester Implementation

* [Re-work orchestrator.js](https://github.com/purpleteam-labs/purpleteam/issues/87)
* [Create Tester reset for "Tester failure:" occurrances](https://github.com/purpleteam-labs/purpleteam/issues/88)
* [Improve orchestrator Tester model error handling](https://github.com/purpleteam-labs/purpleteam/issues/89)
* [Re-work App and Tls Tester models](https://github.com/purpleteam-labs/purpleteam/issues/90)
* [Re-work Dockerfiles](https://github.com/purpleteam-labs/purpleteam/issues/91)
* [Extract common code into package](https://github.com/purpleteam-labs/purpleteam/issues/92)
* [Blog post on the TLS Scanner](https://github.com/purpleteam-labs/purpleteam/issues/93)

# Synchronisation

There ended up being quite a bit of work done around synchronisation of the components, and there is still work to be done. There were architectural decisions made several years ago that needed some modification, and as you can see from the [Work items created](#work-items-created) there is ongoing work that needs to be done.

For example I discovered near the end of the implementation another edge-case around state of a given _Tester_ being incorrect if a different _Tester_ is in a `Tester failure:` state.
You can read about the issue [here](https://github.com/purpleteam-labs/purpleteam/issues/88). We will be addressing this one soon.

Then there is this [lack of retry issue](https://github.com/purpleteam-labs/purpleteam/issues/89) in the _orchestrator_ _Tester_ models which was found near the end of the TLS implementation work also, which probably won't occur very often at all (we have never witnessed it), but it still needs to be fixed.

> Before we get started discussing the synchronisation of components, you will need some understanding of the various relevant time-outs in the code base.

## Time-outs

Many of the time-out issues with AWS just don't exist when running `local`ly. AWS Api Gateway does not support streaming, so we need to use long polling (`lp`) between the CLI and the _orchestrator_ in the `cloud` environment.

### CLI

#### For the `test` command

The initial request to the _orchestrator_ for the `test` command has a set of timeouts, but it must stop trying before the back-end fails due to:

* Stage Two containers not being up and responsive within the currently `120000` (`s2containers.serviceDiscoveryServiceInstances.timeoutToBeAvailable`) + `30000` (`s2containers.responsive.timeout`) duration
* The Stage Two container service discovery services not being up and responsive within the same duration as above

<div id="cli_continues_to_retry"></div>

If the CLI continues to retry after a back-end timeout, then it may continue to do so indefinitely if unsupervised, as is likely if being used in [`noUi` mode](https://github.com/purpleteam-labs/purpleteam#ui).

The [time-out series](https://github.com/purpleteam-labs/purpleteam/blob/0a054e46d02bfbd561f8b2797e86a9d16df484d3/src/presenter/apiDecoratingAdapter.js#L215) for the `test` command currently looks like the following for the `cloud` environment. The CLI doesn't timeout at all for `local`:

Tries:

1. 23000,
2. 15000,
3. 15000,
4. 10010,
5. 10010,
6. 10010,
7. 10010,
8. 10010,
9. 10010,
10. 10010,
11. 10010,
12. 10010,
13. 0 // Cancel

This adds up to 143090 + some request and response latency, a little short of 150000 + some comms latency in the AWS machine.

#### For `tester`[ `Progress` | `PctComplete` | `BugCount` ] updates

Five long-poll request attempts with no data returned from the _orchestrator_ and the CLI gives up.

```javascript
// ...,
testerFeedbackComms: {
  longPoll: {
    nullProgressMaxRetries: {
      doc: 'The number of times (sequentially receiving an event with a data object containing a property with a null value) to poll the backend when the orchestrator is not receiving feedback from the testers.',
      format: 'int',
      default: 5
    }
  }
},
// ...
```

### Orchestrator

The following is used in the `testerWatcher` and needs to be well under the AWS API Gateway timeout which is 30 seconds:

```javascript
// ...,
testerFeedbackComms: {
  // ...,
  longPoll: {
    timeout: {
      doc: 'A double that expresses seconds to wait for blocking Redis commands. We need to timeout well before the AWS Api Gateway timeout.',
      format: Number,
      default: 20.0
    }
  }
}
```

### App Tester

```javascript
// ...,
s2Containers: {
  serviceDiscoveryServiceInstances: {
    timeoutToBeAvailable: {
      doc: 'The duration in milliseconds before giving up on waiting for the s2 Service Discovery Service Instances to be available.',
      format: 'duration',
      default: 120000
    },
    retryIntervalToBeAvailable: {
      doc: 'The retry interval in milliseconds for the s2 Service Discovery Service Instances to be available.',
      format: 'duration',
      default: 5000
    }
  },
  responsive: {
    timeout: {
      doc: 'The duration in milliseconds before giving up on waiting for the s2 containers to be responsive.',
      format: 'duration',
      default: 30000
    },
    retryInterval: {
      doc: 'The retry interval in milliseconds for the s2 containers to be responsive.',
      format: 'duration',
      default: 2000
    }
  }
},
// ...
```

The `emissary.apiFeedbackSpeed` is used to send the CLI the following message types: `testerProgress`, `testerPctComplete` and `testerBugCount`, thus keeping the `lp` alive. This duration needs to be less than the _orchestrator's_ `20` second `testerFeedbackComms.longPoll.timeout`.

```javascript
emissary: {
  // ...,
  apiFeedbackSpeed: {
    doc: 'The speed to poll the Zap API for feedback of test progress',
    format: 'duration',
    default: 5000
  },
  // ...
```

### TLS Tester

If we don't receive any update from the TLS _Emissary_ within this duration (`messageChannelHeartBeatInterval`) then the TLS _Tester_ sends the CLI a `testerProgress` message with the `textData`: `Tester is awaiting Emissary feedback...`. This duration needs to be less than the _orchestrator's_ `20` second `testerFeedbackComms.longPoll.timeout` to make sure the CLI continues to poll the _orchestrator_ for `tester[Progress|PctComplete|BugCount]` updates.


```javascript
// ...,
messageChannelHeartBeatInterval: {
  doc: 'This is used to send heart beat messages every n milliseconds. Primarily to keep the orchestrator\'s testerWatcher longPoll timeout from being reached.',
  format: 'duration',
  default: 15000
},
// ...
```

## Message flows

There are two flow types in play between the _orchestrator_ and the CLI, namely Server Sent Events (`sse`) and Long Polling (`lp`).

> Before reading this section dive over to the _orchestrator_ <a href="https://github.com/purpleteam-labs/purpleteam-orchestrator/blob/main/README.md#configuration" target="_blank">README</a> for a quick run-down on how _PurpleTeam_ is using `sse` and `lp`.&nbsp;

Before The TLS implementation, the `testerFeedbackComms.medium` was defined in the configuration for both the _orchestrator_ and the CLI. Both configurations had to match. If they didn't the _orchestrator_ would respond with an error message. Now this is defined in the _orchestrator_ only and the _orchestrator_ tells the CLI which medium it should use before stating either `sse` or `lp`.

<br>

When the CLI runs the `test` command, there are three significant sequential events, I'll brush over or omit less significant events to make explaining the flow easier to understand. If you'd rather just read the code it's [here](https://github.com/purpleteam-labs/purpleteam-orchestrator/blob/15804fe13a294d7b37b5f2758833f562298f5685/src/api/orchestration/models/orchestrate.js#L177):

1. **CLI makes a `POST` request** to the _orchestrator's_ `/test` route with the _Job_, and continues to do so according to it's [retry schedule](#cli_continues_to_retry).  
  The _orchestrator's_ `testTeamAttack` routine is where a lot of the decision making occurs  
   * If a _Test Run_ is already in progress (`initTesterResponsesForCli` is defined) and the _orchestrator_ already has the responses from the requests to the _Testers_ `/init-tester` route (`initTesterResponsesForCli` has a length), whether the _Testers_ were successfully initialised or not, then the _Tester_ responses along with whether to use `sse` or `lp` to subscribe to _Tester_ feedback are returned to the CLI
   * If a _Test Run_ is already in progress (`initTesterResponsesForCli` is defined), the _orchestrator_ causes a client-side time-out because a response from the request to the _Testers_ `/init-tester` route has not yet been received, and the _orchestrator_ wants the CLI to try again once it times out
   * If execution gets past the above then a _Test Run_ is not currently in progress, so the _orchestrator_:
     1. Sets a in-progress flag
     2. Asks it's _Tester_ models to initialise their _Testers_ and wait for the responses
     3. Once all of the responses are received, the _orchestrator_ populates a `failedTesterInitialisations` array with any `Tester failure:`... messages
     4. The _orchestrator_ creates a `startTesters` boolean and assigns it true if every active _Tester_ has it's state set to `Tester initialised.`... (not `Awaiting Job.`, `Initialising Tester.`, or `[App|Tls] tests are running.`), otherwise false is assigned
     5. If there were any `failedTesterInitialisations` or `startTesters` is false:
        1. `initTesterResponsesForCli` is populated with the responses from trying to initialise the _Testers_ (both successful and/or unsuccessful)
        2. A response is returned to the CLI with `initTesterResponsesForCli` and whether the _orchestrator_ expects the CLI to use `sse` or `lp`
     6. Otherwise:
        1. The _orchestrator_ invokes each _Testers_ `/start-tester` route
        2. If we are running in `cloud` the _orchestrator_ warms up the _Test Session_ message (Redis) channels and lists, this waits for all _Testers_ of the represented _Test Sessions_ to provide their first message set. These message sets are assigned to an array called `warmUpTestSessionMessageSets` which looks like the following before being populated with messages:  
```javascript
        [
          {
                channelName: 'app-lowPrivUser',
                testerMessageSet: []
          }, {
                channelName: 'app-adminUser',
                testerMessageSet: []
          }, {
                channelName: 'tls-NA',
                testerMessageSet: []
          }
        ]
```  
           
           If _Testers_ are started and the _orchestrator_ did not subscribe to the _Test Session_ message channels, it would never know when the _Test Sessions_ are finished in order to clean-up, so this subscription must occur
        3. `initTesterResponsesForCli` is populated with the responses from trying to initialise the _Testers_ (only successful)
        4. A response is returned to the CLI with `initTesterResponsesForCli` and whether the _orchestrator_ expects the CLI to use `sse` or `lp`
2. **CLI makes a `GET` request** to either of the following (currently this happens whether all _Testers_ were initialised successfully or not, there is no point in this happening if there were any `Tester failure:` messages returned from any _Testers_, we will change this soon):
   * If using `sse`? &nbsp; `/tester-feedback/{testerName}/{sessionId}`:  
     In this case messages from the _Test Sessions_ continue to flow through the Redis channels and the _orchestrator_ continues to push them to the CLI
   * If using `lp`? &nbsp; `/poll-tester-feedback/{testerName}/{sessionId}`:  
     In this case the CLI starts the long-poll process, the _orchestrator_ checks to see if `warmUpTestSessionMessageSets` contains an element for the given channel name (BTW: channel names are constructed like: `${testerName}-${sessionId`) (this will only happen in the `cloud` environment), if so it is `splice`d out and returned, if not the `pollTesterMessages` of the `testerWatcher` is invoked. `pollTesterMessages` is responsible for providing a callback to each Redis channel which when invoked takes the given message from a _Testers_ _Test Session_ and pushes it on to the tail of a Redis list with the same name as the Redis channel that the message was received from. Each time the CLI requests a message set for a given _Test Session_, if no messages are yet available it waits (on Redis `blpop` (blocking head pop)), if messages are available, they are popped (Redis `lpop` (non blocking head pop)) from the head of the Redis list
3. **CLI makes a `GET` request** to the `/outcomes` route
   * This happens once the CLI receives a message starting with `All Test Sessions of all Testers are finished`. By the time this has happens, the _orchestrator_ has already cleaned up the _Testers_ and created the _Outcomes_ archive based on the results and reports generated by the _Testers_

# TLS Tester Implementation

Unlike the App _Tester_ ([app-scanner](https://github.com/purpleteam-labs/purpleteam-app-scanner)) which supervises an external _Emissary_ (Zaproxy), the TLS _Tester_ ([tls-scanner](https://github.com/purpleteam-labs/purpleteam-tls-scanner)) supervises an embedded _Emissary_ (testssl.sh). This means that the TLS _Emissary_ runs within the same container as the TLS _Tester_.

The [_Job_](https://purpleteam-labs.com/doc/job-file/) file which the [_Build User_](https://purpleteam-labs.com/doc/definitions/) provides to the [CLI](https://github.com/purpleteam-labs/purpleteam) contains everything required to get the TLS _Emissary_ running and targeting your website or web API.

The implementation of the TLS _Tester_ was actually the easy part of this release. An additional stage one container image was required for `local` and also in the Terraform configuration for `cloud` in the form of AWS ECS Task Definition modification. The AWS ECR deployment script needed adding to.

The new TLS _Tester_ isn't that different from the App _Tester_ other than it is a lot simpler because we don't have to bring up stage two containers, and all the potential synchronisation issues around external _Emissaries_.

The execution flow goes from the `/init-tester` and `/start-tester` [routes](https://github.com/purpleteam-labs/purpleteam-tls-scanner/blob/main/src/api/tls/routes/post.js) to the [model](https://github.com/purpleteam-labs/purpleteam-tls-scanner/blob/main/src/api/tls/models/tls.js).

`/init-tester` basically sets the _Tester_ up with the _Build User_ supplied _Job_ and sets the `status`.

`/start-tester` [starts (`spawn`s)](https://github.com/purpleteam-labs/purpleteam-tls-scanner/blob/7b2d453c63f6a280132b45d2db9a546bf6fc0d19/src/api/tls/models/tls.js#L74) the [Cucumber CLI](https://github.com/purpleteam-labs/purpleteam-tls-scanner/blob/main/src/scripts/runCuc.js#L71),
which initialises the [Cucumber world](https://github.com/purpleteam-labs/purpleteam-tls-scanner/blob/main/src/steps/world.js) which is where most of the domain specific parts are glued together, and the actual Cucumber Steps (tests) are run.

The following are added to the Cucumber `world`:

* The `messagePublisher` (pushes messages onto Redis `${testerName}-${sessionId` channels)
* `sut` (System Under Test) domain object
* `testssl` domain object

The [testssl.sh process is `spawn`ed](https://github.com/purpleteam-labs/purpleteam-tls-scanner/blob/7b2d453c63f6a280132b45d2db9a546bf6fc0d19/src/steps/tls_scan_steps.js#L78).

When ever the TLS _Emissary_ writes to `stdout` the _Tester_ deals with it [here](https://github.com/purpleteam-labs/purpleteam-tls-scanner/blob/7b2d453c63f6a280132b45d2db9a546bf6fc0d19/src/steps/tls_scan_steps.js#L80).

