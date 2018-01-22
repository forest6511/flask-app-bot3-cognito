## 概要
いつも通りの勉強アプリ。Cognito機能がどのようなものか試してみる。  
Python軽量フレームワークとboto3を使って、AWSのCognito機能を使って、ユーザー登録・仮パスワードのメールアドレスを送信する。

---
### 環境
Mac OS  
python:3.5.0 

### pip インストールモジュール
Flask - Microframework for Python.  
boto3 - AWS operation module(S3/Cognito etc.)

```    
pip install -r requirements.txt
```

*boto3をpip(global)で既にインストールしてる場合はupgradeで最新化すること。最新化していない場合はcognito APIが使えない場合がある*


### Flask Webアプリケーション起動
```  
$ python main.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 240-769-624
```  

### Cognito create user response
```  
response= {'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 
'HTTPHeaders': {'date': 'Mon, 22 Jan 2018 16:28:31 GMT', 
'content-length': '351', 
'content-type': 'application/x-amz-json-1.1', 'connection': 'keep-alive', 
'x-amzn-requestid': 'mask(random id)'}, 
'RequestId': 'mask(random id)'}, 
'User': {'Username': 'mask(email-address)', 'UserStatus': 'FORCE_CHANGE_PASSWORD', 
'UserLastModifiedDate': datetime.datetime(2018, 1, 23, 1, 28, 30, 558000, tzinfo=tzlocal()), 
'UserCreateDate': datetime.datetime(2018, 1, 23, 1, 28, 30, 558000, tzinfo=tzlocal()), 
'Attributes': [{'Name': 'sub', 'Value': 'XXXXXXXXXXXXXXXXXX'}, 
{'Name': 'email_verified', 'Value': 'true'}, 
{'Name': 'email', 'Value': 'hogehoge@hoge.hoe'}], 
'Enabled': True}}
```  