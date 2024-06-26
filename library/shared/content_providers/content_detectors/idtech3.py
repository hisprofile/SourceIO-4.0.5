from pathlib import Path


from ..zip_content_provider import ZIPContentProvider
from .....library.utils.path_utilities import backwalk_file_resolver
from ..content_provider_base import ContentProviderBase
from ..gma_provider import GMAContentProvider
from ..non_source_sub_manager import NonSourceContentProvider
from ..source1_content_provider import GameinfoContentProvider
from .source1_common import Source1Common


class IDTech3Detector(Source1Common):
    @classmethod
    def scan(cls, path: Path) -> dict[str, ContentProviderBase]:
        base_dir = backwalk_file_resolver(path, 'base')
        if base_dir is None:
            return {}
        game_name = base_dir.parent.stem
        content_providers = {game_name: NonSourceContentProvider(base_dir)}
        for pk3_file in base_dir.glob('*.pk3'):
            content_providers[pk3_file.name] = ZIPContentProvider(pk3_file)

        return content_providers

    @classmethod
    def register_common(cls, root_path: Path, content_providers: dict[str, ContentProviderBase]):
        super().register_common(root_path, content_providers)
