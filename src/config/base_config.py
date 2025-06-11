from pathlib import Path
from .yml_schema.schema import YmlConfigSchema

import yaml


ROOT = Path(__file__).resolve().parent.parent.parent 
YML_CONFIG_PATH = ROOT / "config.yml"


class YmlLoader(YmlConfigSchema):
    
    @classmethod
    def from_url(cls, url: Path):
        with open(url, "r") as file:
            data = yaml.safe_load(file)

        return cls.model_validate(data)


base_config: YmlConfigSchema = YmlLoader.from_url(YML_CONFIG_PATH)
