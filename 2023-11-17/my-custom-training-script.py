import logging
import json
import os
import glob

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger.debug('Hello my custom SageMaker init script!')
    f_output_model = open("/opt/ml/model/my-model.txt", "w")
    f_output_model.write(json.dumps(glob.glob("{}/*/*/*.*".format(os.environ['SM_INPUT_DIR']))))
    f_output_model.close()
    
    f_output_data = open("/opt/ml/output/data/my-data.txt", "w")
    f_output_data.write(json.dumps(dict(os.environ), sort_keys=True, indent=4))
    f_output_data.close()
