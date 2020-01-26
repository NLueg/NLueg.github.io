---
layout: post
title: Bridge between Java and NodeJs
description: >
 This post describes a problem I had while implementing the language-server for openVALIDATION: The usage of a JAR-file inside JavaScript. I will discuss my research and my found solutions that might fix the problem.
date: 2020-01-26 10:03:36 +0630
categories: Node.js Java backend
---

<!-- Introduction: Description of the problem -->
I recently worked on implementing a language-server for the DSL openVALIDATION.
The plan was, to deliver an IDE to simplify the usage of the language.
Because we wanted to implement a web-based IDE we couldn't avoid using JavaScript or TypeScript for the editor.
We also preferred TypeScript for the implementation of the language-server to be more reusable.
The problem we then had is, that openVALIDATION is written in Java and we don't want to duplicate the parsing logic to TypeScript.
So we needed to find a way to connect the Java implementation with the TypeScript language-server.

I will first explain the different ways I tried and will then come to my final solution: writing an own package.

## Different Approaches

First, we created a REST-API, that the language-server can speak with the parser.
Implementing it in Java wasn't the problem.
With the implemented REST-API, we can provide several paths for parsing and other required functions.

<!-- Cloud: too expensive, working offline -->
Then we thought about how to publish the API.
The usage of something like a cloud-based REST-API would lead to very high costs because every text-change of a user would call this Apis.
Also, we wanted the language-server to work independently from the internet for the integration in not web-based IDEs like VSCode.

<!-- Starting of the REST-API is required, possible with java -->
Because of this, we wanted to deliver the REST-API when the language-server gets installed and run it in a separate process.
This is also not much of a problem if Java is installed.
But openVALIDATION is a no-code development tool so what an editor would it be if it requires a programming-language to work with it?
So this is not an option either.

<!-- We want to be language-independent -->
My first thought was, that it shouldn't be such a problem to run a JAR file without Java.
I thought about some programs that wrap the JAR to another format to be executed on any platform.
After some research I found `launch4j` {% cite launch4j %}.
Launch4j is called a cross-platform tool for wrapping Java applications which sounds like a perfect fit for my needs.

<!-- Launch4j -->
So I downloaded it and tried it out.
The package works perfectly for wrapping the JAR for windows.
It creates an EXE-File which includes the JAR with an integrated JRE.
But I couldn't find out, how to wrap a JAR platform-independent.
I discovered, that the 'cross-platform' says, that the tool itself can be launched on all platforms and NOT to use the JAR on all platforms.
There are some similar tools for Linux and Mac but this would lead to a large overhead if the package needs to deliver a wrapped JAR for every platform.
That's why I discarded this idea too.

<!-- found packages to do so -->
Next, I searched for npm packages that deliver a bridge between JavaScript and Java.
I thought I can't be the only one having this problem.
And I wasn't!
Two packages try to solve this problem by downloading the platform-specific JRE while installing the package. 
This is the solution!

<!-- problems with the packages -->
But I still got a bit of a problem with the packages.
The first package `node-jre` {% cite node-jre %} uses the official Oracle-JRE which, as far as I know, doesn't fit to the Oracle license.
The second package `njre` {% cite njre %} uses the OpenJDK from the `AdoptOpenJDK API` {% cite openJDK %}.
With this package, I am secured from any licensing problems.
But both packages have a huge disadvantage which comes from the overhead which both packages bring to the dependent project.
The JRE is installed on every platform at any time even though there already is a Java installation on the PC.
Also, the path of the JRE varies on the different platforms because of the folder-structure of OpenJDK.
The dependent project needs to look for the downloaded JRE and run it.
In the end, I couldn't find a project, that fits my expectations.

## Solution: `node-java-connector`
<!-- Final solution: download OpenJDK -->
So I decided to build an own package which should work like this:

1. When installing the package, the JRE gets downloaded.
2. When a Java version exists on the system, the JRE won't be downloaded.
3. The OpenJDK JRE should be used to be saved from licensing problems.
4. The package should provide an API for starting a given JAR file that the dependent package doesn't have to the JRE by itself.

While implementing it, I oriented myself on the the `njre` package.
Also, I used `find-java-home` {% cite findJavaHome %} to look up, if the platform has Java installed or not.
If not, the JRE gets downloaded in the node-module itself.
This is also different from the other to packages where the JRE gets downloaded in the root folder of the dependent project.
Now you don't publish the JRE in your package.

Also a function gets exported, that can be used to run the JAR.
The function itself then handles the finding of the JRE and can take some arguments too.

I already used the package in two projects in the context of openVALIDATION: `openvalidation-npm-cli` {% cite openvalidationNpm %} and `openvalidation-languageserver-backend` {% cite openvalidationBackend %}.
The first project wraps the opennvalidation-cli, which is written in Java, as an npm-package.
The second project deals with the problem I explained at the beginning: start the backend for the language-server with JavaScript.

You can find the package on npm and install it in your project like this:

```sh
npm install node-java-connector
```

You then need to define a new file that should be named like `install.js` which calls the `install` method inside the package.
This can be written like this:

```js
const njb = require("node-java-connector");

njb
 .install(8, { type: "jre" })
 .then(dir => {})
 .catch(err => {
 console.log(err);
 });
```

In your `package.json` you then need to define inside the `script` tag, that the file should be run while installing your project like this:

```json
{
 ...
 "scripts": {
 "install": "node install.js",
 }
 ...
}
```

This handles the installing of the required JRE.
Now everything is set up and you can run the JAR by calling `executeJar`.

I would be interested in what you think about this.
Did you already struggle with a similar problem? And what was your solution?

__References__
{% bibliography --cited %}
