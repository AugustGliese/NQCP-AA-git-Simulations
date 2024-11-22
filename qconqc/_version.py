def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import qconqc

    qconqc_path = Path(qconqc.__file__).parent
    return versioningit.get_version(project_dir=qconqc_path.parent)


__version__ = _get_version()
