# تغيير الحقوق يعني أنك تعرّفني بأنك شخص فاشل / Changing the credits means you admit you are a failure
# TG @MC_8G 

import requests , os , sys , json
from datetime import datetime

AxS = "ur_axs_tok , حط هنا الاكسس توكن "

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

translations = {
    "en": {
        "select_language": f"{Colors.CYAN}Select Language:{Colors.END}",
        "english": "English",
        "arabic": "Arabic",
        "available_options": f"{Colors.YELLOW}Available Options:{Colors.END}",
        "change_bind": f"{Colors.GREEN}CHANGE BIND EMAIL{Colors.END}",
        "unbind": f"{Colors.BLUE}UNBIND EMAIL{Colors.END}",
        "cancel": f"{Colors.RED}CANCEL BIND REQUEST{Colors.END}",
        "bind_info": f"{Colors.MAGENTA}BIND INFO{Colors.END}",
        "bind_new": f"{Colors.CYAN}BIND NEW EMAIL{Colors.END}",
        "check_links": f"{Colors.YELLOW}CHECK LINKS{Colors.END}",
        "revoke_token": f"{Colors.RED}REVOKE ACCESS TOKEN{Colors.END}",
        "exit": f"{Colors.WHITE}EXIT{Colors.END}",
        "choose_option": f"{Colors.YELLOW}Choose option (1-8):{Colors.END}",
        "access_token": f"{Colors.CYAN}Access Token:{Colors.END}",
        "old_email": f"{Colors.BLUE}Old Email:{Colors.END}",
        "new_email": f"{Colors.GREEN}New Email:{Colors.END}",
        "enter_email": f"{Colors.YELLOW}Enter email:{Colors.END}",
        "enter_otp": f"{Colors.CYAN}Enter OTP from {Colors.BOLD}{{email}}{Colors.END}{Colors.CYAN}:{Colors.END}",
        "enter_otp_simple": f"{Colors.CYAN}Enter OTP:{Colors.END}",
        "enter_security_code": f"{Colors.YELLOW}Enter Security Code:{Colors.END}",
        "checking_bind": f"{Colors.YELLOW}Checking bind info...{Colors.END}",
        "account_info": f"{Colors.GREEN}Account Information:{Colors.END}",
        "current_email": f"{Colors.CYAN}Current Email:{Colors.END}",
        "pending_email": f"{Colors.YELLOW}Pending Email:{Colors.END}",
        "countdown": f"{Colors.MAGENTA}Countdown:{Colors.END}",
        "result": f"{Colors.BLUE}Result:{Colors.END}",
        "success": f"{Colors.GREEN}SUCCESS{Colors.END}",
        "failed": f"{Colors.RED}FAILED{Colors.END}",
        "summary": f"{Colors.CYAN}Summary:{Colors.END}",
        "status": f"{Colors.YELLOW}Status:{Colors.END}",
        "otp_sent": f"{Colors.GREEN}OTP successfully sent to your email!{Colors.END}",
        "otp_failed": f"{Colors.RED}OTP send failed!{Colors.END}",
        "verified": f"{Colors.GREEN}OTP verified! Identity token received.{Colors.END}",
        "verification_failed": f"{Colors.RED}OTP verification failed!{Colors.END}",
        "identity_token": f"{Colors.CYAN}Identity Token:{Colors.END}",
        "verifier_token": f"{Colors.GREEN}Verifier Token:{Colors.END}",
        "rebind_created": f"{Colors.GREEN}Email change request submitted successfully!{Colors.END}",
        "rebind_failed": f"{Colors.RED}Email change failed!{Colors.END}",
        "unbind_created": f"{Colors.GREEN}Unbind request successfully created!{Colors.END}",
        "unbind_failed": f"{Colors.RED}Unbind request failed!{Colors.END}",
        "cancel_success": f"{Colors.GREEN}Successfully Cancel Bind{Colors.END}",
        "cancel_failed": f"{Colors.RED}Bind cancel failed!{Colors.END}",
        "bind_success": f"{Colors.GREEN}Successfully bind new email!{Colors.END}",
        "bind_failed": f"{Colors.RED}Bind new email failed!{Colors.END}",
        "revoke_success": f"{Colors.GREEN}Successfully revoked access token!{Colors.END}",
        "revoke_failed": f"{Colors.RED}Revoke access token failed!{Colors.END}",
        "links_fetched": f"{Colors.GREEN}Links fetched successfully!{Colors.END}",
        "links_failed": f"{Colors.RED}Failed to fetch links!{Colors.END}",
        "invalid_option": f"{Colors.RED}Invalid option! Please try again.{Colors.END}",
        "goodbye": f"{Colors.GREEN}Allah Hafez! 👋{Colors.END}",
        "press_enter": f"{Colors.CYAN}Press Enter to continue...{Colors.END}",
        "sending_otp": f"{Colors.YELLOW}Sending OTP to {Colors.BOLD}{{email}}{Colors.END}{Colors.YELLOW}...{Colors.END}",
        "verifying": f"{Colors.YELLOW}Verifying OTP...{Colors.END}",
        "creating_request": f"{Colors.YELLOW}Creating request...{Colors.END}",
        "step": f"{Colors.CYAN}Step{Colors.END}",
        "of": f"{Colors.WHITE}of{Colors.END}",
        "raw_response": f"{Colors.MAGENTA}Raw Response:{Colors.END}",
        "api_response": f"{Colors.BLUE}API Response{Colors.END}",
        "error": f"{Colors.RED}Error:{Colors.END}",
        "no_token": f"{Colors.RED}No identity token received!{Colors.END}",
        "no_verifier": f"{Colors.RED}No verifier token received!{Colors.END}",
        "parse_error": f"{Colors.RED}Failed to parse response!{Colors.END}",
        "have_security_code": f"{Colors.CYAN}Do you have your current Security Code? (y/n):{Colors.END}",
        "choose_mode": f"{Colors.CYAN}Choose mode (y/n):{Colors.END}",
        "yes": "y",
        "no": "n",
        "platform_info": "Platform Info",
        "secondary_links": "Secondary Links",
        "not_found": "Not Found",
        "main_platform": "Main Platform",
        "email_label": "Email",
        "email_name_label": "Email Name",
        "mobile_label": "Mobile",
        "mobile_to_be_label": "Mobile To Be",
        "request_exec_countdown": "Request Exec Countdown",
        "result_code": "Result Code",
        "timer_info": "Timer Info",
        "confirmed_in": "Confirmed in",
        "confirmed_yes": "Confirmed: Yes",
        "no_pending": "No pending operations",
        "add_email_title": "BIND NEW EMAIL",
        "enter_new_email": "Enter New Email",
        "confirm_bind_otp": "Enter OTP for confirmation",
        "confirm_bind_sec": "Enter Security Code for confirmation",
        "links_title": "CHECK LINKS",
        "revoke_title": "REVOKE ACCESS TOKEN"
    },
    "ar": {
        "select_language": f"{Colors.CYAN}اختر اللغة:{Colors.END}",
        "english": "الإنجليزية",
        "arabic": f"{Colors.YELLOW}العربية{Colors.END}",
        "available_options": f"{Colors.YELLOW}الخيارات المتاحة:{Colors.END}",
        "change_bind": f"{Colors.GREEN}تغيير البريد الإلكتروني المرتبط{Colors.END}",
        "unbind": f"{Colors.BLUE}فك الارتباط{Colors.END}",
        "cancel": f"{Colors.RED}إلغاء طلب الربط{Colors.END}",
        "bind_info": f"{Colors.MAGENTA}معلومات الربط{Colors.END}",
        "bind_new": f"{Colors.CYAN}إضافة بريد إلكتروني جديد{Colors.END}",
        "check_links": f"{Colors.YELLOW}فحص الروابط{Colors.END}",
        "revoke_token": f"{Colors.RED}إبطال رمز الوصول{Colors.END}",
        "exit": f"{Colors.WHITE}خروج{Colors.END}",
        "choose_option": f"{Colors.YELLOW}اختر خيارًا (1-8):{Colors.END}",
        "access_token": f"{Colors.CYAN}رمز الوصول (Access Token):{Colors.END}",
        "old_email": f"{Colors.BLUE}البريد القديم:{Colors.END}",
        "new_email": f"{Colors.GREEN}البريد الجديد:{Colors.END}",
        "enter_email": f"{Colors.YELLOW}أدخل البريد الإلكتروني:{Colors.END}",
        "enter_otp": f"{Colors.CYAN}أدخل OTP المرسل إلى {Colors.BOLD}{{email}}{Colors.END}{Colors.CYAN}:{Colors.END}",
        "enter_otp_simple": f"{Colors.CYAN}أدخل OTP:{Colors.END}",
        "enter_security_code": f"{Colors.YELLOW}أدخل رمز الأمان (Security Code):{Colors.END}",
        "checking_bind": f"{Colors.YELLOW}جاري التحقق من معلومات الربط...{Colors.END}",
        "account_info": f"{Colors.GREEN}معلومات الحساب:{Colors.END}",
        "current_email": f"{Colors.CYAN}البريد الحالي:{Colors.END}",
        "pending_email": f"{Colors.YELLOW}البريد المعلق:{Colors.END}",
        "countdown": f"{Colors.MAGENTA}العد التنازلي:{Colors.END}",
        "result": f"{Colors.BLUE}النتيجة:{Colors.END}",
        "success": f"{Colors.GREEN}نجاح{Colors.END}",
        "failed": f"{Colors.RED}فشل{Colors.END}",
        "summary": f"{Colors.CYAN}ملخص:{Colors.END}",
        "status": f"{Colors.YELLOW}الحالة:{Colors.END}",
        "otp_sent": f"{Colors.GREEN}تم إرسال OTP بنجاح إلى بريدك!{Colors.END}",
        "otp_failed": f"{Colors.RED}فشل إرسال OTP!{Colors.END}",
        "verified": f"{Colors.GREEN}تم التحقق من OTP! تم استلام رمز الهوية.{Colors.END}",
        "verification_failed": f"{Colors.RED}فشل التحقق من OTP!{Colors.END}",
        "identity_token": f"{Colors.CYAN}رمز الهوية (Identity Token):{Colors.END}",
        "verifier_token": f"{Colors.GREEN}رمز التحقق (Verifier Token):{Colors.END}",
        "rebind_created": f"{Colors.GREEN}تم تقديم طلب تغيير البريد بنجاح!{Colors.END}",
        "rebind_failed": f"{Colors.RED}فشل تغيير البريد!{Colors.END}",
        "unbind_created": f"{Colors.GREEN}تم إنشاء طلب فك الارتباط بنجاح!{Colors.END}",
        "unbind_failed": f"{Colors.RED}فشل طلب فك الارتباط!{Colors.END}",
        "cancel_success": f"{Colors.GREEN}تم إلغاء الربط بنجاح{Colors.END}",
        "cancel_failed": f"{Colors.RED}فشل إلغاء الربط!{Colors.END}",
        "bind_success": f"{Colors.GREEN}تم ربط البريد الجديد بنجاح!{Colors.END}",
        "bind_failed": f"{Colors.RED}فشل ربط البريد الجديد!{Colors.END}",
        "revoke_success": f"{Colors.GREEN}تم إبطال رمز الوصول بنجاح!{Colors.END}",
        "revoke_failed": f"{Colors.RED}فشل إبطال رمز الوصول!{Colors.END}",
        "links_fetched": f"{Colors.GREEN}تم جلب الروابط بنجاح!{Colors.END}",
        "links_failed": f"{Colors.RED}فشل جلب الروابط!{Colors.END}",
        "invalid_option": f"{Colors.RED}خيار غير صالح! حاول مرة أخرى.{Colors.END}",
        "goodbye": f"{Colors.GREEN}الله حافظ! 👋{Colors.END}",
        "press_enter": f"{Colors.CYAN}اضغط Enter للمتابعة...{Colors.END}",
        "sending_otp": f"{Colors.YELLOW}جاري إرسال OTP إلى {Colors.BOLD}{{email}}{Colors.END}{Colors.YELLOW}...{Colors.END}",
        "verifying": f"{Colors.YELLOW}جاري التحقق من OTP...{Colors.END}",
        "creating_request": f"{Colors.YELLOW}جاري إنشاء الطلب...{Colors.END}",
        "step": f"{Colors.CYAN}خطوة{Colors.END}",
        "of": f"{Colors.WHITE}من{Colors.END}",
        "raw_response": f"{Colors.MAGENTA}الرد الخام:{Colors.END}",
        "api_response": f"{Colors.BLUE}رد API{Colors.END}",
        "error": f"{Colors.RED}خطأ:{Colors.END}",
        "no_token": f"{Colors.RED}لم يتم استلام رمز الهوية!{Colors.END}",
        "no_verifier": f"{Colors.RED}لم يتم استلام رمز التحقق!{Colors.END}",
        "parse_error": f"{Colors.RED}فشل تحليل الرد!{Colors.END}",
        "have_security_code": f"{Colors.CYAN}هل لديك رمز الأمان الحالي؟ (y/n):{Colors.END}",
        "choose_mode": f"{Colors.CYAN}اختر الوضع (y/n):{Colors.END}",
        "yes": "نعم",
        "no": "لا",
        "platform_info": "معلومات المنصة",
        "secondary_links": "الروابط الثانوية",
        "not_found": "غير موجود",
        "main_platform": "المنصة الرئيسية",
        "email_label": "البريد الإلكتروني",
        "email_name_label": "اسم البريد",
        "mobile_label": "رقم الهاتف",
        "mobile_to_be_label": "رقم الهاتف المنتظر",
        "request_exec_countdown": "الوقت المتبقي للتنفيذ",
        "result_code": "كود النتيجة",
        "timer_info": "معلومات المؤقت",
        "confirmed_in": "مؤكد في",
        "confirmed_yes": "مؤكد: نعم",
        "no_pending": "لا توجد عمليات معلقة",
        "add_email_title": "إضافة بريد إلكتروني جديد",
        "enter_new_email": "أدخل البريد الإلكتروني الجديد",
        "confirm_bind_otp": "أدخل OTP للتأكيد",
        "confirm_bind_sec": "أدخل رمز الأمان للتأكيد",
        "links_title": "فحص الروابط",
        "revoke_title": "إبطال رمز الوصول"
    }
}

current_lang = "en"

def set_language():
    global current_lang
    clear_screen()
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}LANGUAGE SELECTION / اختر اللغة{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
    print(f"{Colors.GREEN}1. English{Colors.END}")
    print(f"{Colors.CYAN}2. العربية (Arabic){Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
    
    choice = input(f"\n{Colors.WHITE}Select language / اختر اللغة {Colors.YELLOW}(1-2){Colors.WHITE}: {Colors.END}").strip()
    
    if choice == "1":
        current_lang = "en"
    elif choice == "2":
        current_lang = "ar"
    else:
        current_lang = "en"
    
    clear_screen()

def t(key, **kwargs):
    text = translations[current_lang].get(key, translations["en"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    banner = f"""
    ███╗   ███╗  █████╗  ███████╗ ██████╗  ██╗   ██╗
  ████╗ ████║ ██╔══██╗ ██╔════╝ ██╔══██╗ ╚██╗ ██╔╝            ██╔████╔██║ ███████║ ███████╗ ██████╔╝  ╚████╔╝
  ██║╚██╔╝██║ ██╔══██║ ╚════██║ ██╔══██╗   ╚██╔╝
  ██║ ╚═╝ ██║ ██║  ██║ ███████║ ██║  ██║    ██║               ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝    ╚═╝

                ██████╗   ██████╗  ████████╗                                ██╔══██╗ ██╔═══██╗ ╚══██╔══╝
                ██████╔╝ ██║   ██║    ██║                                   ██╔══██╗ ██║   ██║    ██║
                ██████╔╝ ╚██████╔╝    ██║
                ╚═════╝   ╚═════╝     ╚═╝
{Colors.MAGENTA}{'='*55}{Colors.END}
{Colors.YELLOW}                     Credits: @MC_8G                    {Colors.END}
{Colors.CYAN}                      xMaSrY                                  {Colors.END}
{Colors.MAGENTA}{'='*55}{Colors.END}
"""
    print(banner)

def show_menu():
    print(f"\n{Colors.BOLD}{t('available_options')}{Colors.END}")
    print(f"{Colors.GREEN}1. {t('change_bind')}{Colors.END}")
    print(f"{Colors.BLUE}2. {t('unbind')}{Colors.END}")
    print(f"{Colors.RED}3. {t('cancel')}{Colors.END}")
    print(f"{Colors.MAGENTA}4. {t('bind_info')}{Colors.END}")
    print(f"{Colors.CYAN}5. {t('bind_new')}{Colors.END}")
    print(f"{Colors.YELLOW}6. {t('check_links')}{Colors.END}")
    print(f"{Colors.RED}7. {t('revoke_token')}{Colors.END}")
    print(f"{Colors.WHITE}8. {t('exit')}{Colors.END}")
    print(f"{Colors.CYAN}{'═'*55}{Colors.END}")

def is_success(rsp):
    if rsp.status_code != 200: 
        return False
    try:
        rj = rsp.json()
        if not rj.get("success"): 
            return False
        data = rj.get("data", {})
        if isinstance(data, dict):
            if data.get("error"): 
                return False
            g_resp = data.get("garena_response", {})
            if isinstance(g_resp, dict) and g_resp.get("error"):
                return False
        err_node = rj.get("error")
        if err_node: 
            return False
        return True
    except:
        return False

def show_res(rsp_json):
    try:
        error_msg = None
        err_node = rsp_json.get('error')
        data_node = rsp_json.get('data', {})

        if isinstance(err_node, dict):
            g_resp = err_node.get('garena_response', {})
            if isinstance(g_resp, dict) and g_resp.get('error'):
                error_msg = g_resp.get('error')
            elif err_node.get('error'):
                error_msg = err_node.get('error')
            elif err_node.get('message'):
                error_msg = err_node.get('message')
            else:
                error_msg = str(err_node)
        elif isinstance(err_node, str):
            error_msg = err_node
            
        if not error_msg and isinstance(data_node, dict):
            if data_node.get('error'):
                error_msg = data_node.get('error')
            elif isinstance(data_node.get('garena_response'), dict) and data_node['garena_response'].get('error'):
                error_msg = data_node['garena_response']['error']
                
        if not error_msg:
            g_resp = rsp_json.get('garena_response', {})
            if isinstance(g_resp, dict) and g_resp.get('error'):
                error_msg = g_resp.get('error')

        if not error_msg and not rsp_json.get('success'):
            error_msg = rsp_json.get('message') or "Unknown Error"

        if error_msg:
            print(f"- {Colors.RED}{t('failed')} ! Error : {error_msg}{Colors.END}")
        else:
            print(f"- {Colors.GREEN}{t('success')}{Colors.END}")
            
        print(f"- {Colors.CYAN}DevELopEr : MaSrY & H4RDIXX{Colors.END}")
        print(f"- {Colors.CYAN}ChanneL   : @MC_8G {Colors.END}\n")
    except:
        print(f"- {Colors.RED}{t('failed')} ! InvaLid ResPonsE{Colors.END}\n")

def convert_seconds(s):
    try:
        s = int(s)
        d, h = divmod(s, 86400)
        h, m = divmod(h, 3600)
        m, s = divmod(m, 60)
        return f"{d} Day {h} Hour {m} Min {s} Sec"
    except:
        return "0 Day 0 Hour 0 Min 0 Sec"

def check_bind_info(access_token=None, show_raw=True):
    if not access_token:
        access_token = AxS
    
    print(f"\n{Colors.GREEN}[✓]{Colors.END} {t('checking_bind')}")
    
    url = "https://bindinfocrownx612.vercel.app/check"
    rsp = requests.get(url, params={'access_token': access_token})
    
    if is_success(rsp):
        data = rsp.json()
        inner_data = data.get("data", {}) if data.get("data") else data
        
        print(f"\n{Colors.CYAN}{'='*55}{Colors.END}")
        print(f"{Colors.GREEN}✓ {t('account_info')}{Colors.END}")
        print(f"{Colors.CYAN}{'='*55}{Colors.END}")
        
        fields = [
            ("status", "Status"),
            ("status_code", "Status Code"),
            ("summary", "Summary"),
            ("countdown_human", "Countdown Human"),
            ("countdown_seconds", "Countdown Seconds"),
            ("current_email", "Current Email"),
            ("pending_email", "Pending Email"),
            ("email_to_be", "Email To Be"),
            ("mobile", "Mobile"),
            ("request_exec_countdown", "Request Exec Countdown"),
            ("result", "Result"),
            ("email", "Email"),
            ("mobile_to_be", "Mobile To Be")
        ]
        for key, label in fields:
            value = inner_data.get(key, '')
            if value:
                print(f"  {Colors.CYAN}{label}:{Colors.END} {Colors.WHITE}{value}{Colors.END}")
        
        email = inner_data.get("email", "")
        email_to_be = inner_data.get("email_to_be", "")
        countdown = inner_data.get("request_exec_countdown", 0)
        
        print("")
        if email == "" and email_to_be != "":
            print(f"  {Colors.YELLOW}Confirmed in : {convert_seconds(countdown)}{Colors.END}")
        elif email != "" and email_to_be == "":
            print(f"  {Colors.GREEN}Confirmed : Yes Good !{Colors.END}")
        elif email == "" and email_to_be == "":
            print(f"  {Colors.RED}No Pending Operations{Colors.END}")
        
        if show_raw:
            print(f"\n  {t('raw_response')}")
            print(f"{Colors.MAGENTA}{'-'*50}{Colors.END}")
            print(f"{Colors.WHITE}{json.dumps(inner_data, indent=2, ensure_ascii=False)}{Colors.END}")
        
        print(f"{Colors.CYAN}{'='*55}{Colors.END}")
        return inner_data
    else:
        try:
            show_res(rsp.json())
        except:
            print(f"  {Colors.RED}✗ {t('error')} HTTP {rsp.status_code}{Colors.END}")
        return None

def change_bind_email():
    print(f"\n{Colors.BOLD}{Colors.GREEN}[ {t('change_bind')} ]{Colors.END}")
    print(f"{Colors.CYAN}{'='*55}{Colors.END}")
    
    access_token = AxS
    
    print(f"\n{Colors.CYAN}Do you have your current Security Code?{Colors.END}")
    print(f"{Colors.GREEN}y {Colors.WHITE}- Yes (Change with Security Code){Colors.END}")
    print(f"{Colors.RED}n {Colors.WHITE}- No (Forgot / Reset Security Code){Colors.END}")
    choice = input(f"\n{t('choose_mode')} ").strip().lower()
    
    if choice == 'y':
        change_bind_with_sec(access_token)
    elif choice == 'n':
        change_bind_no_sec(access_token)
    else:
        print(t('invalid_option'))
    
    input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")

def change_bind_with_sec(access_token):
    email = input(f'{t("enter_new_email")} : ')
    url = "https://chngemailcode48.vercel.app/send_otp"
    rsp = requests.get(url, params={'access_token': access_token, 'email': email})
    
    if is_success(rsp):
        show_res(rsp.json())
        otp = input(f'{t("enter_otp_simple")} : ')
        url_v = "https://chngemailcode48.vercel.app/verify_otp"
        rsp_v = requests.get(url_v, params={'access_token': access_token, 'email': email, 'otp': otp})
        
        if is_success(rsp_v):
            show_res(rsp_v.json())
            auth = rsp_v.json().get("verifier_token") or rsp_v.json().get("data", {}).get("verifier_token")
            sec = input(f'{t("enter_security_code")} : ')
            url_i = "https://chngemailcode48.vercel.app/verify_identity"
            rsp_i = requests.get(url_i, params={'access_token': access_token, 'code': sec})
            
            if is_success(rsp_i):
                show_res(rsp_i.json())
                iden = rsp_i.json().get("identity_token") or rsp_i.json().get("data", {}).get("identity_token")
                url_c = "https://chngemailcode48.vercel.app/create_rebind"
                rsp_c = requests.get(url_c, params={'access_token': access_token, 'email': email, 'identity_token': iden, 'verifier_token': auth})
                
                if is_success(rsp_c):
                    show_res(rsp_c.json())
                    print(f'{Colors.GREEN}Successfully Changed To : {email} !{Colors.END}')
                else:
                    show_res(rsp_c.json())
            else:
                show_res(rsp_i.json())
        else:
            show_res(rsp_v.json())
    else:
        try: show_res(rsp.json())
        except: print(f'{Colors.RED}Failed ! HTTP : {rsp.status_code}{Colors.END}')

def change_bind_no_sec(access_token):
    cur_email = input(f'{t("old_email")} : ')
    url1 = "https://chngeforgotcrownx72.vercel.app/otp"
    rsp1 = requests.get(url1, params={'access_token': access_token, 'current_email': cur_email})
    
    if is_success(rsp1):
        show_res(rsp1.json())
        otp1 = input(f'{t("enter_otp_simple")} : ')
        url2 = "https://chngeforgotcrownx72.vercel.app/verify"
        rsp2 = requests.get(url2, params={'access_token': access_token, 'current_email': cur_email, 'otp': otp1})
        
        if is_success(rsp2):
            show_res(rsp2.json())
            iden = rsp2.json().get("identity_token") or rsp2.json().get("data", {}).get("identity_token")
            new_email = input(f'{t("new_email")} : ')
            url3 = "https://chngeforgotcrownx72.vercel.app/newotp"
            rsp3 = requests.get(url3, params={'access_token': access_token, 'new_email': new_email})
            
            if is_success(rsp3):
                show_res(rsp3.json())
                otp2 = input(f'{t("enter_otp_simple")} : ')
                url4 = "https://chngeforgotcrownx72.vercel.app/newverify"
                rsp4 = requests.get(url4, params={'access_token': access_token, 'new_email': new_email, 'otp': otp2})
                
                if is_success(rsp4):
                    show_res(rsp4.json())
                    auth = rsp4.json().get("verifier_token") or rsp4.json().get("data", {}).get("verifier_token")
                    url5 = "https://chngeforgotcrownx72.vercel.app/change"
                    rsp5 = requests.get(url5, params={'access_token': access_token, 'new_email': new_email, 'identity_token': iden, 'verifier_token': auth})
                    
                    if is_success(rsp5):
                        show_res(rsp5.json())
                        print(f'{Colors.GREEN}Successfully Forgot Security Code & Changed Email !{Colors.END}')
                    else:
                        show_res(rsp5.json())
                else:
                    show_res(rsp4.json())
            else:
                show_res(rsp3.json())
        else:
            show_res(rsp2.json())
    else:
        try: show_res(rsp1.json())
        except: print(f'{Colors.RED}Failed ! HTTP : {rsp1.status_code}{Colors.END}')

def unbind_email():
    print(f"\n{Colors.BOLD}{Colors.BLUE}[ {t('unbind')} ]{Colors.END}")
    print(f"{Colors.CYAN}{'='*55}{Colors.END}")
    
    access_token = AxS
    
    print(f"\n{Colors.CYAN}Do you have your current Security Code?{Colors.END}")
    print(f"{Colors.GREEN}y {Colors.WHITE}- Yes (Unbind with Security Code){Colors.END}")
    print(f"{Colors.RED}n {Colors.WHITE}- No (Forgot Security Code / OTP){Colors.END}")
    choice = input(f"\n{t('choose_mode')} ").strip().lower()
    
    if choice == 'y':
        unbind_with_sec(access_token)
    elif choice == 'n':
        unbind_no_sec(access_token)
    else:
        print(t('invalid_option'))
    
    input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")

def unbind_with_sec(access_token):
    sec = input(f'{t("enter_security_code")} : ')
    url = "https://crownxnewkey10010.vercel.app/securityunbind"
    rsp = requests.get(url, params={'access_token': access_token, 'security_code': sec})
    
    if is_success(rsp):
        show_res(rsp.json())
        print(f'{Colors.GREEN}Unbind Request Created Successfully! 15 Days Timer Started.{Colors.END}')
    else:
        try: show_res(rsp.json())
        except: print(f'{Colors.RED}Failed ! HTTP : {rsp.status_code}{Colors.END}')

def unbind_no_sec(access_token):
    cur_email = input(f'{t("old_email")} : ')
    url1 = "https://chngeforgotcrownx72.vercel.app/otp"
    rsp1 = requests.get(url1, params={'access_token': access_token, 'current_email': cur_email})
    
    if is_success(rsp1):
        show_res(rsp1.json())
        otp = input(f'{t("enter_otp_simple")} : ')
        url2 = "https://chngeforgotcrownx72.vercel.app/verify"
        rsp2 = requests.get(url2, params={'access_token': access_token, 'current_email': cur_email, 'otp': otp})
        
        if is_success(rsp2):
            show_res(rsp2.json())
            iden = rsp2.json().get("identity_token") or rsp2.json().get("data", {}).get("identity_token")
            
            url3 = "https://crownxforgotremove23.vercel.app/forgotunbind"
            rsp3 = requests.get(url3, params={'access_token': access_token, 'identity_token': iden})
            
            if is_success(rsp3):
                show_res(rsp3.json())
                print(f'{Colors.GREEN}Unbind Request Created Successfully! 15 Days Timer Started.{Colors.END}')
            else:
                show_res(rsp3.json())
        else:
            show_res(rsp2.json())
    else:
        try: show_res(rsp1.json())
        except: print(f'{Colors.RED}Failed ! HTTP : {rsp1.status_code}{Colors.END}')

def cancel_bind():
    print(f"\n{Colors.BOLD}{Colors.RED}[ {t('cancel')} ]{Colors.END}")
    print(f"{Colors.CYAN}{'='*55}{Colors.END}")
    
    access_token = AxS
    check_bind_info(access_token, show_raw=False)
    
    url = "https://bindcnclcrownx34.vercel.app/cancelbind"
    rsp = requests.get(url, params={'access_token': access_token})
    if is_success(rsp):
        show_res(rsp.json())
        print(f'{Colors.GREEN}Successfully Cancelled Bind !{Colors.END}')
    else:
        try: show_res(rsp.json())
        except: print(f'{Colors.RED}Failed ! HTTP : {rsp.status_code}{Colors.END}')
    
    input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")

def bind_new_email():
    print(f"\n{Colors.BOLD}{Colors.CYAN}[ {t('add_email_title')} ]{Colors.END}")
    print(f"{Colors.CYAN}{'='*55}{Colors.END}")
    
    access_token = AxS
    email = input(f'{t("enter_new_email")} : ')
    
    url = "https://bindcnclcrownx34.vercel.app/bind"
    rsp = requests.get(url, params={'access_token': access_token, 'email': email})
    if is_success(rsp):
        show_res(rsp.json())
        otp = input(f'{t("confirm_bind_otp")} : ')
        sec = input(f'{t("confirm_bind_sec")} : ')
        url_c = "https://bindcnclcrownx34.vercel.app/confirmbind"
        rsp_c = requests.get(url_c, params={'access_token': access_token, 'email': email, 'otp': otp, 'security_code': sec})
        if is_success(rsp_c):
            show_res(rsp_c.json())
            print(f'{Colors.GREEN}Successfully Adding : {email} To Account !{Colors.END}')
        else:
            show_res(rsp_c.json())
    else:
        try: show_res(rsp.json())
        except: print(f'{Colors.RED}Failed ! HTTP : {rsp.status_code}{Colors.END}')
    
    input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")

def check_links():
    print(f"\n{Colors.BOLD}{Colors.YELLOW}[ {t('links_title')} ]{Colors.END}")
    print(f"{Colors.CYAN}{'='*55}{Colors.END}")
    
    access_token = AxS
    r = requests.get("https://100067.connect.garena.com/bind/app/platform/info/get",
      params={'access_token': access_token},
      headers={'User-Agent':"GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)","Connection":"Keep-Alive","Accept-Encoding":"gzip","If-Modified-Since":"Sun, 18 May 2025 09:37:03 GMT"})
    
    if r.status_code not in [200,201]:
        print(f"{Colors.RED}{t('links_failed')}{Colors.END}")
        input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")
        return
    
    j = r.json()
    platform_names = {3:"Facebook", 8:"Gmail", 10:"iCloud", 5:"VK", 11:"Twitter", 7:"Huawei"}
    bounded = j.get("bounded_accounts", [])
    available = j.get("available_platforms", [])
    
    print(f"\n{Colors.GREEN}> {t('secondary_links')} : <{Colors.END}")
    found = False
    for x in bounded:
        try:
            p = x.get('platform')
            u = x.get('uid')
            uinfo = x.get('user_info', {})
            e = uinfo.get('email', '')
            n = uinfo.get('nickname', '')
            if p in platform_names:
                print(f"\n{Colors.CYAN}=> {platform_names[p]} !{Colors.END}")
                if e: print(f"  {Colors.WHITE}{t('email_label')} : {e}{Colors.END}")
                if n: print(f"  {Colors.WHITE}{t('email_name_label')} : {n}{Colors.END}")
                found = True
        except:
            continue
    if not found:
        print(f"{Colors.RED}{t('not_found')}{Colors.END}")
    
    for k in platform_names:
        if k not in available:
            print(f"\n{Colors.YELLOW}> {t('main_platform')} => {platform_names[k]} ! <{Colors.END}")
            break
    
    input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")

def revoke_token():
    print(f"\n{Colors.BOLD}{Colors.RED}[ {t('revoke_title')} ]{Colors.END}")
    print(f"{Colors.CYAN}{'='*55}{Colors.END}")
    
    access_token = AxS
    url = "https://crownxrevoker73.vercel.app/revoke"
    rsp = requests.get(url, params={'access_token': access_token})
    try:
        rj = rsp.json()
        if rj.get("success"):
            print(f"{Colors.GREEN}{t('revoke_success')}{Colors.END}")
        else:
            err = rj.get("error", {}).get("garena_response", {}).get("error", "Unknown")
            print(f"{Colors.RED}{t('revoke_failed')} ! Error : {err}{Colors.END}")
        print(f"- {Colors.CYAN}DevELopEr : MaSrY & H4RDIXX{Colors.END}")
        print(f"- {Colors.CYAN}ChanneL   : @MC_8G {Colors.END}\n")
    except:
        print(f"{Colors.RED}{t('revoke_failed')} ! HTTP : {rsp.status_code}{Colors.END}\n")
    
    input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")

# ---------- Main ----------
def main():
    set_language()
    
    while True:
        clear_screen()
        show_banner()
        show_menu()
        
        print(f"\n{Colors.BOLD}{t('choose_option')}{Colors.END} ", end="")
        choice = input()
        
        if choice == "1":
            clear_screen()
            show_banner()
            change_bind_email()
        elif choice == "2":
            clear_screen()
            show_banner()
            unbind_email()
        elif choice == "3":
            clear_screen()
            show_banner()
            cancel_bind()
        elif choice == "4":
            clear_screen()
            show_banner()
            check_bind_info(show_raw=True)
            input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")
        elif choice == "5":
            clear_screen()
            show_banner()
            bind_new_email()
        elif choice == "6":
            clear_screen()
            show_banner()
            check_links()
        elif choice == "7":
            clear_screen()
            show_banner()
            revoke_token()
        elif choice == "8":
            print(f"\n{Colors.GREEN}{t('goodbye')}{Colors.END}")
            sys.exit(0)
        else:
            print(f"\n{Colors.RED}{t('invalid_option')}{Colors.END}")
            input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}{t('goodbye')}{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {str(e)}{Colors.END}")
        input(f"\n{Colors.CYAN}{t('press_enter')}{Colors.END}")