from setuptools import setup

setup(
    entry_points={
        "lms.djangoapp": [
            "ora2_codemirror = ora2_codemirror.apps:Ora2CodemirrorConfig",
        ],
        "cms.djangoapp": [
            "ora2_codemirror = ora2_codemirror.apps:Ora2CodemirrorConfig",
        ],
    }
)
