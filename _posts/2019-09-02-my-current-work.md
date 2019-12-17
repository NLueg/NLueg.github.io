---
layout: post
title:  Short overview of the topic of my bachelor-thesis
description: >
    In my very first post, I want to explain the topic of my bachelor thesis.
    My thesis is about the implementation of a text-editor for the DSL openVALIDATION.
    In this post, I want to give a short overview and talk about future topics.
date:   2019-09-02 10:03:36 +0630
categories: bachelor-thesis IDE text-editor openVALIDATION
---

In my very first post, I want to write about the topic of my bachelor thesis.
This is just a small overview but I will explain each topic in a separate post.

In general, I want to implement a text editor for the domain-specific language (DSL) openVALIDATION {% cite openVALGitbook %}.
This is a DSL that can represent validation-rules and is very close to natural-language.
After the definition of a rule, code can be generated in different programming languages.
Currently, code can be generated in the languages C#, Java, JavaScript and Node.js.
The language is quite new and will be published on GitHub soon {% cite openVALGithub %}

The editor for the language should be web-based and Open-Source for strong extensibility and many possibilities to integrate it.
Therefore we use the Language Server Protocol {% cite lsp %} which tries to be an API between multiple language-extensions and text editors.
It's currently implemented for about 99 languages {% cite lspServers %} and 23 text editors {% cite lspTools %}.

The main part of my thesis is the implementation of language-features for openVALIDATION.
After my work, I will publish this also on my [GitHub](https://github.com/NLueg) profile, that the extension can be integrated into several editors.

The main features of this extension will be linting, autocompletion and syntax-highlighting.
Linting is the analysis of code while writing it.
Autocompletion means the providing of symbols. We want to provide context-sensitive autocompletion, where you only show symbols, that are valid in a given context.
Last but not least, syntax-highlighting is the consistent highlighting of words that are in the same group.
Groups are e.g. keywords or methods.

Autocompletion and syntax-highlighting are a bit of a problem because the language is very close to natural language.
For the autocompletion function, the abstract-syntax-tree (AST) needs to be used and modified to simplify the usage.

In the future post I want to answer the following questions:

1. What is the Language Server Protocol?
2. Which web-based Open-Source editor is the most used and accepted one?
3. How does syntax-highlighting work for a natural language?
4. How can context-sensitive code completion work for a natural language? 

__References__
{% bibliography --cited %}