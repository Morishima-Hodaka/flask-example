"""
flask-sms
发送短信
"""
from flask_sms import SMS

sms = SMS()


def init_sms(app):
    sms.init_app(app)
    # 设置短信时间限制
    app.config['SMS_RATE_LIMIT'] = 1
    # 设置每天最大发送次数
    app.config['SMS_DAILY_LIMIT'] = 1000
    app.config['SMS_ALIYUN_ACCESS_KEY_ID'] = "LTAI5tCjRtrr1UW1iRsk35Q1"
    app.config['SMS_ALIYUN_ACCESS_KEY_SECRET'] = "rS57GCavJykbsrfEiX090yIVFUWCx6"
    app.config['SMS_ALIYUN_SMS_SIGN_NAME'] = "台州派电网络科技有限公司"  # （签名名称）
    app.config['SMS_ALIYUN_SMS_TEMPLATE_CODE'] = "SMS_279357125"  # （模板）@杜双 杜总  麻烦配置一下短信参数
    app.config["SMS_REDIS_HOST"]="127.0.0.1"
    app.config["SMS_REDIS_PORT"]=6379

# app.config["SSMS_ALIYUN_SMS_SIGN_NAME"] = "广东硅基数字产业"
# app.config["SMS_ALIYUN_SMS_TEMPLATE_CODE"] = "SMS_287730560"
# app.config["SMS_ALIYUN_ACCESS_KEY_ID"] = "LTAI5t5ab2xw5mqu7ggb6WHx"
# app.config["SMS_ALIYUN_ACCESS_KEY_SECRET"] = "MBihnx35M3I0C2pmb67i38uw3TMZ5"

# os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'] = 'LTAI5tCjRtrr1UW1iRsk35Q1'
# os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'] = 'rS57GCavJykbsrfEiX090yIVFUWCx6'
# d = {
#     "sign_name": "安徽杰森电子科技有限公司",
#     "template_code": "SMS_276255133",
#     "phone_numbers": "15119569881",
#     "template_param": '{"code":"1234"}',
# }
# # queries['PhoneNumbers'] = '18025223075'
# # queries['SignName'] = '安徽杰森电子科技有限公司'
# # queries['TemplateCode'] = 'SMS_276255133'
# # queries['TemplateParam'] = '{"code":"1234"}'
