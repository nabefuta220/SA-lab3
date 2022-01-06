"""
ファイルを実行し、標準出力をファイルで返す
"""

import argparse
import os
import subprocess


def inputer():
    """
    入力時のパーサー
    """
    arg = argparse.ArgumentParser()
    arg.add_argument('command', nargs='*')
    parse = arg.parse_args()
    return parse.command


if __name__ == '__main__':
    command_line = inputer()
    print(command_line)
    out_file = f"output/{os.path.splitext(os.path.basename(command_line[1]))[0]}.txt"
    print(out_file)
    command = ['pipenv', 'run']+command_line
    cp = subprocess.run(command, encoding='utf-8',
                        stdout=subprocess.PIPE, check=True)

    with open(out_file, 'w', encoding='UTF-8') as out_file:
        out_file.write(f"$ {' '.join(command)}\n")
        out_file.write(cp.stdout)
