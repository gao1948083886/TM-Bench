# For correcting encoding errors of Mongolian characters

import json
from tqdm import tqdm 
import os.path as osp
from mongolian_correct.oyun_correct import oyun_correct

Base_path = 'Upload_data'

class Correct:
    def __init__(self, base_path):
        self.Base_path = base_path

    def AGNews(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['dialogue'] = oyun_correct(item['dialogue'])
                item['summary'] = oyun_correct(item['summary'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def ARC(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['dialogue'] = oyun_correct(item['dialogue'])
                item['summary'] = oyun_correct(item['summary'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def CMMT(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['dialogue'] = oyun_correct(item['dialogue'])
                item['summary'] = oyun_correct(item['summary'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def HellaSwag(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['query'] = oyun_correct(item['query'])
                for choice in item['choices']:
                    choice['summary'] = oyun_correct(choice['summary'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def MMLU(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['question'] = oyun_correct(item['question'])
                item['hypothesis'] = oyun_correct(item['hypothesis'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def MNLI(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['premise'] = oyun_correct(item['premise'])
                item['hypothesis'] = oyun_correct(item['hypothesis'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def MRPC(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['text1'] = oyun_correct(item['text1'])
                item['text2'] = oyun_correct(item['text2'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def QNLI(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['text1'] = oyun_correct(item['text1'])
                item['text2'] = oyun_correct(item['text2'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)

    def RTE(self, path):
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            for item in data:
                item['text1'] = oyun_correct(item['text1'])
                item['text2'] = oyun_correct(item['text2'])
        with open(path, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)


def main():
    Corrector = Correct(base_path=Base_path)

    all_attributes = dir(Corrector)
    functions = [
        attr for attr in all_attributes
        if callable(getattr(Corrector, attr)) and not attr.startswith("__")
    ]

    for fun in tqdm(functions, desc="Correcting datasets"):
        dataset_path = f"{fun}"  
        method = getattr(Corrector, fun)
        method(osp.join('TM-', dataset_path))

if __name__ == "__main__":
    main()

