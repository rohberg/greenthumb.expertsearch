
=======================
greenthumb.expertsearch
=======================

This is an example Plone Add-On for Svelte integration. It is part of the Talk **Interactive Components in Plone Classic with Svelte**. Find the HOWTO script at https://interactive-components-in-classic-plone.readthedocs.io/en/latest/ .

Features
--------

Expert search: Find experts (Membrane users with additional fields (see behavior in this add-on) by searchstring and region.


Installation
------------

Install greenthumb.expertsearch by adding it to your buildout::

    [buildout]

    ...

    eggs =
        greenthumb.expertsearch


and then running ``bin/buildout``


Compile Svelte code::

    cd rohberg.expertsearch/svelte_src/my-svelte-app
    npm install
    npm run dev


Paste `<div class="expertsearch-plus" />` in one of your pages to see the expert search.
