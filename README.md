# nacc-common

> **⚠️ This repository has been archived.** Development and releases have moved to the [flywheel-gear-extensions](https://github.com/naccdata/flywheel-gear-extensions) monorepo.

## Where to find things

- **Source code**: [flywheel-gear-extensions/nacc-common](https://github.com/naccdata/flywheel-gear-extensions/tree/main/nacc-common)
- **Releases**: [flywheel-gear-extensions releases](https://github.com/naccdata/flywheel-gear-extensions/releases?q=nacc-common)
- **Changelog**: [docs/nacc_common/CHANGELOG.md](https://github.com/naccdata/flywheel-gear-extensions/blob/main/docs/nacc_common/CHANGELOG.md)
- **Issues**: [flywheel-gear-extensions issues](https://github.com/naccdata/flywheel-gear-extensions/issues)

## Installation

Install the latest release directly:

```
pip install https://github.com/naccdata/flywheel-gear-extensions/releases/download/nacc-common%2Fv3.1.0/nacc_common-3.1.0-py3-none-any.whl
```

Or in `requirements.txt`:

```text
nacc_common @ https://github.com/naccdata/flywheel-gear-extensions/releases/download/nacc-common%2Fv3.1.0/nacc_common-3.1.0-py3-none-any.whl
```

The URL format is consistent across versions — replace the version number to use a different release.

## Migration from this repo

If you were referencing releases from this repository, update your dependency URLs from:

```text
# Old (this repo)
nacc_common @ https://github.com/naccdata/nacc-common/releases/download/v3.0.0/nacc_common-3.0.0-py3-none-any.whl

# New (flywheel-gear-extensions)
nacc_common @ https://github.com/naccdata/flywheel-gear-extensions/releases/download/nacc-common%2Fv3.1.0/nacc_common-3.1.0-py3-none-any.whl
```

Note the tag format changed from `v3.0.0` to `nacc-common/v3.1.0` (URL-encoded as `nacc-common%2Fv3.1.0`).
