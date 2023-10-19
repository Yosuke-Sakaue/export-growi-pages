## Summary
入力されたGrowiパス配下のmdファイルを抽出し、パスの構成を再帰的にoutputディレクトリに出力するスクリプト

## Usage
1. create .env file
1. pip install python-dotenv
1. python main.py <Growiのページパス（例：/〇〇/××）>

## Requarements Env
```
GROWI_BASE_URL
GROWI_API_TOKEN
FILE_NAME_ID_OPTION=False
```
FILE_NAME_ID_OPTIONがTrueの場合、ファイル名がページIDで作成され、output配下へフラットに出力される
※デフォルトはFalse

https://tips.weseek.co.jp/5e4d5253340a4f0049473d2b
