"""
https://www.ys7.com/
萤石，是安全智能生活主流品牌，利用智能硬件、互联网云服务、人工智能（AI）和机器人等技术，
努力为用户打造一个智能化的工作、生活和学习环境，为用户营造以智能技术为基础的居住环境。
萤石提供住宅、办公室、商铺、学校、酒店等居住场所智能化的产品和服务。
萤石云
"""
import requests


class init_fluorite_cloud:
    pass

    url = None
    headers = {}

    # 获取accessToken
    def get_access_token(self):
        url = "https://open.ys7.com/api/lapp/token/get"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {"appKey": "442e826d6f9346b780aca970af45c3e4", "appSecret": "4ede3c7c52851402818ba325930fd406"}

        r = requests.post(url, params, headers=headers)
        print(r)
        print(r.url)

        print(r.json())

    # 获取播放地址
    def get_play_url(self):
        """
        accessToken	String	授权过程获取的access_token	Y
        deviceSerial	String	设备序列号例如427734222，均采用英文符号，限制最多50个字符	Y
        channelNo	Integer	通道号，非必选，默认为1	N
        protocol	Integer	流播放协议，1-ezopen、2-hls、3-rtmp、4-flv，默认为1	N
        code	String	ezopen协议地址的设备的视频加密密码	N
        expireTime	Integer	过期时长，单位秒；针对hls/rtmp/flv设置有效期，相对时间；30秒-720天	N
        type	String	地址的类型，1-预览，2-本地录像回放，3-云存储录像回放，非必选，默认为1；回放仅支持rtmp、ezopen、flv协议	N
        quality	Integer	视频清晰度，1-高清（主码流）、2-流畅（子码流）	N
        startTime	String	本地录像/云存储录像回放开始时间,云存储开始结束时间必须在同一天，示例：2019-12-01 00:00:00	N
        stopTime	String	本地录像/云存储录像回放结束时间,云存储开始结束时间必须在同一天，示例：2019-12-01 23:59:59	N
        supportH265	Integer	请判断播放端是否要求播放视频为H265编码格式,1表示需要，0表示不要求	N
        playbackSpeed	String	回放倍速。倍速为 -1（ 支持的最大倍速）、0.5、1、2、4、8、16；
        仅支持protocol为4-flv
        且
        type为2-本地录像回放（ 部分设备可能不支持16倍速） 或者 3-云存储录像回放	N
        gbchannel	String	国标设备的通道编号，视频通道编号ID
        """
        url = "https://open.ys7.com/api/lapp/v2/live/address/get"
        accessToken = "at.03f64hm21ezf7gm38360xikw3ewkzaq2-73tl5u75f1-16gk0aq-cuuzertka"
        deviceSerial = "BB5597556"
        code = "GSSMSS"
        # 流播放协议，1-ezopen、2-hls、3-rtmp、4-flv，默认为1
        protocol = 3
        # 过期时长，单位秒；针对hls/rtmp/flv设置有效期，相对时间；30秒-720天
        expireTime = 60 * 60 * 24 *720
        data = {"accessToken": accessToken, "deviceSerial": deviceSerial, "code": code, "protocol": protocol,"expireTime": expireTime}
        r = requests.post(url=url, data=data)
        print(r.json())


a = init_fluorite_cloud()
a.get_access_token()
a.get_play_url()
