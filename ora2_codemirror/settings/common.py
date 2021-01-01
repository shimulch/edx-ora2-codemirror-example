
def plugin_settings(settings):
    available_editors = getattr(settings, 'ORA_AVAILABLE_EDITORS', {})
    available_editors['codemirror'] = {
        'display_name': 'Codemirror',
        'js': [
            '/static/vendor/CodeMirror-5.59.1/codemirror.min.js',
            '/static/js/openassessment-editor-codemirror.js'
        ],
        'css': [
            '/static/vendor/CodeMirror-5.59.1/codemirror.min.css',
        ]
    }
    setattr(settings, 'ORA_AVAILABLE_EDITORS', available_editors)
