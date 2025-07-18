python_sources(name="lib")
file(name="type-flag", source="py.typed")

python_distribution(
    name="dist",
    dependencies=[":lib", ":type-flag"],
    wheel=True,
    sdist=True,
    provides=python_artifact(
        name="nacc-common",
        version="1.2.3",
        description="NACC Data Platform utilities",
        author="NACC",
        author_email="nacchelp@uw.edu",
        url="https://github.com/naccdata/data-platform-demos",
    ),
)
