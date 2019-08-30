---
layout: post
title:  My Current Work
description: In my very first post I want explain the topic of my bachelor-thesis.
date:   2019-08-08 21:03:36 +0630
categories: bachelor-thesis IDE texteditor openVALIDATION
---

In my very first post I want to write over the topic of my bachelor-thesis.
This is just a small overview but I will explain each topic in a separate post.

In general I want to implement an Texteditor for the domain-specific language (DSL) openVALIDATION.
 <!-- {% cite openVALGitbook %}. -->
This is a DSL which can represent validation-rules and is very close to natural-language.
After the definition of a rule, code can be generated in different programming-languages.
Currently code can be generated in the languages C#, Java, JavaScript and NodeJs.

The editor should be web based and Open-Source for a strong extensibility and many possibilities for integrate it.
Therefore we use the Language-Server Protocol which tries to be an API between multiple language-extensions and texteditors.
<!-- Therefore we use the Language-Server Protocol {% cite lsp %} which tries to be an API between multiple language-extensions and texteditors. -->
It's currently implemented for about 99 languages and 23 texteditors.
<!-- It's currently implemented for about 99 languages {% cite lspServers %} and 23 texteditors {% cite lspTools %}. -->

The main part of my thesis is the implementation of language-features for openVALIDATION.
After my work I will publish this also on my GitHub profile, that the extension can be integrated in several editors.

This post aims so give a short overview about what I currently work on.
I will update this post in a few days with more details about the general topic.
Also I will create for the following topics an own post:

1. What is the language-server protocol
2. Which web based Open-Source editor is the most used and excepted one?
3. How does Syntax-Highlighting work for a natural language?
4. Who can context sensitive code completion work for a natural langauge? 

<!-- __References__
{% bibliography --cited %} -->
