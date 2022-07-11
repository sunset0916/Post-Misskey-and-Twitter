# Post-Misskey-and-Twitter
コマンドラインからMisskeyとTwitterに同時投稿するやつ

`python PostMisskeyAndTwitter.py [-t,-m] 投稿内容`

`-t`の場合はTwitterのみ、`-m`の場合はMisskeyのみに、指定なしの場合は両方に投稿される

スペースを開けて投稿内容を複数の引数として渡すと改行される

スペースを入れたい場合は""で囲むとよい

各種トークンは自身で用意して必要な部分に入力しておく必要あり

実行する前にPythonの実行環境にTwitterとMisskeyを入れておく必要あり
