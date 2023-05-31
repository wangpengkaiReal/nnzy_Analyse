from constants import TaskType
from foo import Analyes
from foo import Keyword_Explorer
from foo import DZDP_Analyes


run_config = {
    "task_type": 3,

}


def run(config):
    if config['task_type'] == TaskType.Analyes:
        Analyes.Data_Analyse('input_data/yjygx_input_data')
    elif config['task_type'] == TaskType.Keyword_Explorer:
        Keyword_Explorer.explorer()
    elif config['task_type'] == TaskType.DZDP_Analyes:
        DZDP_Analyes.DZDP_Analyes('input_data/dzdp_input_data')

if __name__ == '__main__':
    run(run_config)

