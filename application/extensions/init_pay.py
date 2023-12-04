from flask import Flask
from wechatpayv3 import WeChatPay, WeChatPayType

from app.config import PAY_CONFIG

"""

"""


def init_pay():

    wxpay = WeChatPay(
        wechatpay_type=WeChatPayType.MINIPROG,
        mchid=PAY_CONFIG.MCHID,
        private_key=PAY_CONFIG.PRIVATE_KEY,
        cert_serial_no=PAY_CONFIG.CERT_SERIAL_NO,
        apiv3_key=PAY_CONFIG.APIV3_KEY,
        appid=PAY_CONFIG.APPID,
        notify_url=PAY_CONFIG.NOTIFY_URL,
        cert_dir=PAY_CONFIG.CERT_DIR,
        logger=PAY_CONFIG.LOGGER,
        partner_mode=PAY_CONFIG.PARTNER_MODE,
        proxy=PAY_CONFIG.PROXY)
    return wxpay


wxpay = init_pay()
