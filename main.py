# Flask Webアプリケーション
import traceback

# Pythonの場合はboto3でcognitoやs3などにアクセス
# Javaの場合はSDKあり：https://qiita.com/moritalous/items/2bebddefbdbcc1a57ed1
import boto3
from flask import Flask, render_template, request

# Flask App起動(port:5000)
app = Flask(__name__)


def cognito_register_user(email):
    """
    Ref: https://boto3.readthedocs.io/en/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_create_user
    :param email:
    :return:
    """

    print("sign up user: ", email)

    try:
        # 認証開始（IAMでcognitoを使用できるユーザーを作成・払い出しを行い、アクセスキー・シークセット設定）
        aws_client = boto3.client('cognito-idp',
                                  region_name = "ap-northeast-1",
                                  aws_access_key_id = "xxxxxxxxxxxxxxx",
                                  aws_secret_access_key = "xxxxxxxxxxxxxxx",)

        # ユーザー作成
        response = aws_client.admin_create_user(
            # cognito設定時のユーザープールID
            UserPoolId="xxxxxxxxxxxxxxx",
            Username=email,
            UserAttributes=[
                {"Name": "email","Value": email},
                # Email送信でバリデーション(Email送信で仮パスワード)
                { "Name": "email_verified", "Value": "true" }
            ],
            DesiredDeliveryMediums=['EMAIL']
        )

        print("response=", response)

        # 認証完了
        return response
    except:
        # エラーメッセージをprint表示
        traceback.print_exc()
    return None


@app.route('/')
def root():
    """
    メール登録のみ行います
    メール入力フォームのHTMLを返却するのみ
    """
    return render_template('register_email.html', title='register mail')


@app.route('/register/email', methods=['POST'])
def sign_up():
    """
    メール登録処理
    メール登録後フォームのHTMLを返却
    """
    if request.method == 'POST':
        email = request.form['email']
        print("email=", email)
        cognito_register_user(email)
    return render_template('register_email_complete.html', title='flask test', email=email)


# Flask App Main.
if __name__ == "__main__":
    app.run(debug=True)
