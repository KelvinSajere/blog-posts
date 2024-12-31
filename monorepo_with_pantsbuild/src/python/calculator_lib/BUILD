python_sources()
python_distribution(
    name="mydist_with_pants",
    dependencies=[
        # Dependencies on code to be packaged into the distribution.
    ],
    repositories=[
        "https://upload.pypi.org/legacy/",
    ],
    provides=python_artifact(
        name="testing_pants_distribution",
        version="0.0.4",
        long_description="long_description",
        description="An example distribution built with Pants.",
        author="ksajere",
        classifiers=[
            "Programming Language :: Python :: 3.7",
        ],
    ),
)
