import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

# 密钥存储在仓库管理员手中，如需使用请联系仓库管理员
from api_keys import tencent_ocr_secret_id as secret_id, tencent_ocr_secret_key as secret_key
from tools.ImageTransformer import add_margin
# 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取

def ocr(image_base64):
    try:
        print("[OCR] 提取中...")
        image_base64 = add_margin(image_base64)
        cred = credential.Credential(secret_id, secret_key)
        client = ocr_client.OcrClient(cred, "ap-shanghai")
        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.GeneralFastOCRRequest()
        params = {
            "ImageBase64": image_base64,  # "ImageUrl": None,
            # "Scene": None,
            # "LanguageType": "zh_rare",
            # "IsPdf": False,
            # "PdfPageNumber": None,
            # "IsWords": False
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个GeneralBasicOCRResponse的实例，与请求对象对应
        resp = client.GeneralFastOCR(req)
        # 输出json格式的字符串回包
        obj = json.loads(resp.to_json_string())
        return obj['TextDetections']

    except TencentCloudSDKException as err:
        print(err)
