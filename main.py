from requests import get, post
import concurrent.futures

sessionid = ''
aweme_id = ''

def set_private(aweme_id):
    try:
        url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/aweme/modify/visibility/?aweme_id={aweme_id}&type=3&aid=1233'
        headers = {
            'user-agent': 'com.zhiliaoapp.musically/2023604040 (Linux; U; Android 7.1.2; en; ASUS_Z01QD; Build/N2G48H;tt-ok/3.12.13.4-tiktok)',
            'cookie': f'sessionid={sessionid}'
        }
        r = get(url, headers=headers).text
    except:
        pass

def delete_video(aweme_id):
    try:
        url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/aweme/delete/?aweme_id={aweme_id}&delete_type=1&aid=1233'
        headers = {
            'user-agent': 'com.zhiliaoapp.musically/2023604040 (Linux; U; Android 7.1.2; en; ASUS_Z01QD; Build/N2G48H;tt-ok/3.12.13.4-tiktok)',
            'cookie': f'sessionid={sessionid}'
        }
        r = get(url, headers=headers).text
    except:
        pass

def restore_video(aweme_id):
    try:
        url = 'https://api16-normal-c-useast1a.tiktokv.com/tiktok/activity_center/trash_bin/recover/v1/?aid=1233'
        headers = {
            'user-agent': 'com.zhiliaoapp.musically/2023604040 (Linux; U; Android 7.1.2; en; ASUS_Z01QD; Build/N2G48H;tt-ok/3.12.13.4-tiktok)',
            'cookie': f'sessionid={sessionid}'
        }
        payload = {
            'aweme_ids': f'["{aweme_id}"]'
        }
        r = post(url, headers=headers, data=payload).text
        if 'recover_success_items' in r:
            print('Success')
    except:
        pass

def main():
    set_private(aweme_id)

    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        while True:
            futures = []
            futures.append(executor.submit(delete_video, aweme_id))
            futures.append(executor.submit(restore_video, aweme_id))

main()
