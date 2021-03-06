*Looking for a shareable component template? Go here --> [sveltejs/component-template](https://github.com/sveltejs/component-template)*

---

# Your svelte app "expertsearch-plus", integrated in Plone CMS

This is a project template for [Svelte](https://svelte.dev) apps. It is based on https://github.com/sveltejs/template.

## Get started

Install the dependencies...

```bash
cd svelte_apps/expertsearch_plus
npm install
```

...then start [Rollup](https://rollupjs.org):

```bash
npm run dev
```

Navigate to [localhost:5000](http://localhost:5000). You should see your app running. Edit a component file in `src`, save it, and reload the page to see your changes.

By default, the server will only respond to requests from localhost. To allow connections from other computers, edit the `sirv` commands in package.json to include the option `--host 0.0.0.0`.

If you're using [Visual Studio Code](https://code.visualstudio.com/) we recommend installing the official extension [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode). If you are using other editors you may need to install a plugin in order to get syntax highlighting and intellisense.

If you are testing the app inside Plone, you probably have to relead manually for now.

## Building and running in production mode

To create an optimised version of the app:

```bash
npm run build
```

This will build the bundles and copy all needed files into the Plone package apps directory.

You can run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to platforms like [Heroku](https://heroku.com).


## Using TypeScript

This template comes with a script to set up a TypeScript development environment, you can run it immediately after cloning the template with:

```bash
node scripts/setupTypeScript.js
```

Or remove the script via:

```bash
rm scripts/setupTypeScript.js
```

## Integrating the app into Plone

To use the app in Plone, you can add an HTML element with the id "expertsearch-plus", for example with the TinyMCE editor in SourceCode mode:

    <div id="expertsearch-plus"></div>
