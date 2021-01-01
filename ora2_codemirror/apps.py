from django.apps import AppConfig


class Ora2CodemirrorConfig(AppConfig):
    name = 'ora2_codemirror'

    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'common': { 'relative_path': 'settings.common'},
            },
            'cms.djangoapp': {
                'common': { 'relative_path': 'settings.common'},
            }
        },
    }
