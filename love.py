# coding=utf-8
"""
从土味情话中获取每日一句。
 """
import requests

__all__ = ['get_lovelive_info']


def get_lovelive_info():
    """
    :return: str,土味情话。
    """
    print('获取中...')
    try:
        resp = requests.get('https://api.lovelive.tools/api/SweetNothings')
        if resp.status_code == 200:
             print(resp.text)
        else:
             print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


get_one_words = get_lovelive_info

if __name__ == '__main__':
    weather = get_lovelive_info()
    # print(weather)
    pass
