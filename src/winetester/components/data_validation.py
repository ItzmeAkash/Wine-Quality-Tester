import pandas as pd
from winetester.entity.config_entity import DataValidationConfig
import os
from winetester import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation_status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation_status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e
    
    # def validate_datatype(self) -> bool:
        
    #     try:
    #         validate_data = None
    #         data = pd.read_csv(self.config.unzip_data_dir)
    #         datatype = data.dtypes
            
    #         all_datatype = self.config.all_schema.values()
            
    #         for data in datatype:
    #             if data not in all_datatype:
    #                 validate_data = False
    #                 with open(self.config.STATUS_FILE,'w') as f:
    #                     f.write(f"validate_datatype: {validate_data}")
    #             else:
    #                 validate_data = True
    #                 with open(self.config.STATUS_FILE,'w') as f:
    #                     f.write(f"validate_datatype: {validate_data}")
                        
    #         return validate_data
    #     except Exception as e:
    #         raise e