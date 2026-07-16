from pathlib import Path

from CODEGUARDIAN.src.discovery.finder import discover_files


class FileCache:

    _cache = {}

    @classmethod
    def get_files(cls, project_path, extensions):

        key = (
            str(Path(project_path).resolve()),
            tuple(sorted(extensions))
        )

        if key not in cls._cache:


     

            cls._cache[key] = discover_files(
                Path(project_path),
                extensions
            )

       

        return cls._cache[key]