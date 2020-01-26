---
layout: post
title: Bridge between Java and NodeJs
description: >
    This post describes a bit problem I hat while implementing the language-server for openVALIDATION: The usage of a JAR-file inside JavaScript. I will discuss my research and my found solutions that might fix the problem.
date:   2020-01-24 10:03:36 +0630
categories: Node.js Java backend
---

<!-- Introduction: description of the problem -->
In my work for implementing a language-server for openVALIDATION I struggled with working with multiple languages.
The plan was to implement an web-based IDE so we can't avoid using JavaScript.
The problem is, that openVALIDATION is written in Java.
Because of this the parser is kinda unreachable.

<!-- REST-API would work -->
To speak with it anyway, we needed to create a REST-Api for it, which is not the problem. With the REST-Api we can provide several paths for parsing and other required functions.

<!-- Cloud: too expensive, working offline -->
But when we use something like a cloud-based REST-Api and every text-change that a user does will lead to very high costs.
Also we wanted the language-server to work independent from the internet for the integration in not web-based IDEs like VSCode.

<!-- Starting of the REST-API is required, possible with java -->
The starting of the REST-API is also not much of a problem, if Java is installed.
But openVALIDATION is a no-code development tool so what an editor would it be, if it requires a programming-language to work with it?
So this is not an option either.

<!-- We want to be language-independent -->
My first thought was, that it shouldn't be such a problem to run a JAR file without Java. I thought about some programs that wrap the JAR to another format to be executed on any platform. After some research I found `launch4j` {% cite launch4j %}.
Launch4j is called a cross-platform tool for wrapping Java applications which sounds like a perfect fit for our needs.

<!-- Launch4j -->
So I downloaded it and tried it out.
The package works perfectly for wrapping the JAR for windows.
It creates and EXE which includes the JAR with an integrated JRE.
But I couldn't find how to wrap a JAR platform independent.
I found out, that the 'cross-platform' says, that the tool itself can be launched on all platforms and NOT to use the JAR on all platforms.
There are some similar tools for linux and mac too but this would lead to a large overhead if the package needs to deliver a wrapped JAR for every platform.
That's why we discarded this idea too.

## npm packages
<!-- found packages to do so -->
Now I searched for npm packages which deliver a bridge between JavaScript and Java.
I thought, I can't be the only one having this problem.
And I wasn't!
There are two packages which try to solve this problem with just downloading the JRE while installing the package. This is the solution!

<!-- problems with the packages -->
But I still got a bit of a problem with the packages.
The first package `node-jre` {% cite node-jre %} uses the official Oracle-JRE which, as far as I know, doesn't fit to the Oracle license.
The second package `njre` {% cite njre %} uses the OpenJDK from the `AdoptOpenJDK API` {% cite openJDK %}.
So with this package can't appear any licensing problems.
But both packages have a huge disadvantage which comes from the overhead which both packages bring to the dependent project.
The JRE is installed on every platform at any time even though there already is a Java installation on the PC.
Also the path of the JRE varies on the different platforms.
The dependent project needs to look for the downloaded JRE and run it.
In the end I couldn't find a project, that totally fits my expectations.

## Own package: `node-java-connector`
<!-- Final solution: download openJDK -->
So I decided to build an own package which should work like this:

1. When installing the package, the JRE should be downloaded.
2. When a Java version exists on the system, the JRE won't be downloaded.
3. The openJDK JRE should be used to be same from licensing problems.
4. The package should provide a API for starting a given JAR file that the dependent package doesn't have to handle the JRE finding by itself.

While implementing it, I oriented myself on the the `njre` package.
I used `find-java-home` {% cite findJavaHome %} to look up, if the platform has Java installed or not.
If not, the JRE gets downloaded in the node-module itself. 
This is also different from the other to packages where the JRE gets downloaded in the root-folder of the dependent project.
Now you don't have to publish the JRE in your own package.

Also I export a function that can be used to run the JAR.
The function itself then handles the finding of the JRE and can take some arguments too.

I already used the package in two projects in the context of openVALIDATION: `openvalidation-npm-cli` {% cite openvalidationNpm %} and `openvalidation-languageserver-backend` {% cite openvalidationBackend %}.

I would be interested in what you think about this.
Did you already struggled with a problem like this? And what was your solution?

__References__
{% bibliography --cited %}
