import pandas as pd
import chardet
def detect_encoding(file_path):
    # ファイルのエンコーディングを検出
    with open(file_path, 'rb') as file:
        detector = chardet.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']

def tsv_to_csv(input_path, output_path):
    print(detect_encoding(input_path))
    # TSVファイルを読み込み
    df = pd.read_csv(input_path, sep='\t',encoding=detect_encoding(input_path))

    # データフレーム内のコンマをアンダーバーに置換
    df.replace(',', '_', regex=True, inplace=True)

    # CSVファイルとして保存
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # 入力と出力のファイルパスを指定
    input_file_path = 'conlang.tsv'
    output_file_path = 'conlang.csv'

    # TSVをCSVに変換して保存
    tsv_to_csv(input_file_path, output_file_path)

    print(f"変換が完了しました。出力ファイル: {output_file_path}")
