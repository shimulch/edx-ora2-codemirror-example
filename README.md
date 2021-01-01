Example app to demonstrate pluggable ORA2 submission editor.

#### Things that makes it available in ORA2

- Added in settings via - ``ora2_codemirror/settings/common.py``
- Codemirror related files are in - ``static/vendor/``
- Codemirror editor controller - ``static/js/openassessment-editor-codemirror.js``.

The controller js is not fully implemented for Codemirror. It is just to demonstrate how the controller and vendor js can be loaded from an external django app.

The controller js is using some es6 syntax like ``class`` etc. Ideally we should prefer using es5 here.
