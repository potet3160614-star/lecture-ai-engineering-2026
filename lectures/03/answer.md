# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：各用語に対して通常のLLMではLoRAとQRoLAの違いを比較するが、エージェントはそれぞれの用語に反応して用語集から説明を挙げただけであった。
- `--trace` で見えたツール呼び出し（ツール名と引数）：以下のような出力を得た。
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.0008513'), details={'text_prompt_tokens': 1196}, input_text_tokens=1196, input_tokens=1196, output_tokens=197, requests=2, tool_calls=2)
- 1つの質問での LLM 呼び出し回数（`requests`）：2回
- 追加したツールと、docstring に書いた説明：
make_quiz(lecture: int) -> str:
    """指定した回の用語集から確認問題を1問作り、問題と答えを返す。

    「第2回の確認問題を出して」のように、講義内容の確認問題を求められたときに使う。
    """

## 宿題

- 取り組んだレベル：実装
- やったこと：学習の記録をLearning_log/フォルダに保存するツールsave_learning_logを作成した。
- 結果：save_learning_log(content) を追加し、学習記録を learning_log/learning_log.md に日時付きで追記するようにしました。エージェントでは requires_approval=True で登録し、CLIに保存内容を表示して確認します。y / yes / はい で承認した場合のみ保存し、それ以外は保存しません。
- 気づき・疑問：実装することには成功し、実際に学習内容の保存に成功した。今回の記録では指示文に完全に忠実な記録ではなかったので内容によっては保存した学習内容の書き方に揺れがあるのではないかと思った。今後の学習でこの学習記録ツールの記録構造についても学習させることができるのか気になった。
