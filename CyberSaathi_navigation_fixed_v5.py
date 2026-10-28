import streamlit as st
import re
from urllib.parse import urlparse

st.set_page_config(
    page_title="CyberSaathi | Digital Safety",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- LANGUAGE TEXT --------------------
TEXT = {
    "English": {
        "tagline": "Your Trusted Companion in the Digital World",
        "nav": ["Home", "Scam Awareness", "Link & Message Checkers", "Scenarios", "Quiz", "Lessons", "Safety Centre", "Women's Digital Safety", "Know Your Rights", "Evidence Guide", "Report Cybercrime"],
        "hero1": "Think Safe.", "hero2": "Stay Secure.",
        "intro": "CyberSaathi helps you recognise cyber threats, protect yourself online and find the right help.",
        "link_btn": "Check a Suspicious Link", "msg_btn": "Check a Message",
        "women_title": "Women's Digital Safety", "women_desc": "Know the risks. Stay protected. You are not alone.",
        "explore": "Explore Now", "help": "Need Help Now?", "contacts": "Important contacts and resources",
        "tips": "Quick Safety Tips", "tip1": "Don't share OTPs, passwords or personal details.", "tip2": "Be careful with unknown links and calls.", "tip3": "Verify before you trust.", "tip4": "When in doubt, ask for help.",
        "scam": "Scam Awareness", "scam_desc": "Learn about common scams and how to avoid them.",
        "link": "Link Checker", "link_desc": "Check whether a URL looks suspicious before opening it.",
        "message": "Message Checker", "message_desc": "Look for common pressure tactics and suspicious wording.",
        "scenarios": "Scenarios", "scenarios_desc": "Practise real-life situations and choose the safest option.",
        "quiz": "Quiz", "quiz_desc": "Test your knowledge and learn as you go.",
        "lessons": "Awareness Lessons", "lessons_desc": "Simple lessons for everyday online safety.",
        "smart": "Smart Help", "smart_desc": "Describe your situation and get guidance on next steps.",
        "women": "Women's Digital Safety", "women_card_desc": "Learn, prevent, get help. Your safety matters.",
        "safety": "Safety Centre", "safety_desc": "Quick help, helplines and official resources.",
        "rights": "Know Your Rights", "evidence": "Evidence Guide", "report": "Report Cybercrime",
        "learn": "Learn", "aware": "Be Aware", "safe": "Stay Safe", "get_help": "Get Help",
        "choose": "Choose a section from the navigation above.",
        "check_link": "Check a link", "paste_url": "Paste a web address (URL)", "check": "Check",
        "url_empty": "Please enter a URL.", "url_result_safe": "No obvious warning signs were found. This does not guarantee the website is safe.",
        "url_result_warn": "This URL has warning signs. Do not open it unless you can verify it independently.",
        "message_label": "Paste the message you received", "analyze": "Review message", "message_empty": "Please paste a message.",
        "message_result": "Review these warning signs before responding:",
        "quiz_question": "You receive a message saying your bank account will be blocked unless you click a link. What should you do?",
        "quiz_options": ["Click the link immediately", "Reply with your OTP", "Do not click; contact the bank using its official number", "Forward it to everyone"],
        "submit": "Check answer", "correct": "Correct! Stop and verify using an official contact method.", "incorrect": "Not quite. Do not click the link. Contact the bank through its official app or number.",
        "scam_heading": "Common scams to watch for", "scam_items": ["Bank or KYC warning: criminals pretend your account will be blocked.", "Parcel fee: a fake delivery message asks for a small payment.", "Job offer: a scammer asks you to pay a registration fee.", "Friend in trouble: someone impersonates a friend and urgently asks for money."],
        "lesson_heading": "Everyday safety lessons", "lesson_items": ["Use a unique, strong password for each important account.", "Turn on two-step verification wherever it is available.", "Keep your phone, browser and apps updated.", "Pause before clicking links or opening attachments.", "Never share an OTP, PIN or password with anyone."],
        "rights_heading": "Know your rights", "rights_items": ["You can report suspected cybercrime through official reporting channels.", "Keep messages, transaction references and other relevant evidence.", "Contact your bank quickly if money has been taken or a payment seems fraudulent.", "Do not pay someone who promises to recover money in exchange for an upfront fee."],
        "evidence_heading": "Preserve evidence safely", "evidence_items": ["Take screenshots that show the sender, date, time and message.", "Keep transaction IDs, phone numbers, URLs and email details.", "Do not edit the original screenshots or messages.", "Store a backup somewhere secure and avoid publicly posting personal details."],
        "report_heading": "Report cybercrime", "report_text": "If you are in India, use the official National Cyber Crime Reporting Portal or call 1930 for urgent financial cyber fraud. If you are in immediate danger, contact local emergency services.",
        "smart_heading": "Tell us what happened", "smart_label": "Describe the situation (do not include passwords or OTPs)", "smart_button": "Show next steps",
        "smart_steps": ["Stop replying and do not send money or codes.", "Save screenshots and relevant details.", "Contact your bank or service provider through official contact details if an account or payment is involved.", "Report the incident through an official channel and ask a trusted person for help."],
        "scenario_heading": "Choose the safest response", "scenario_q": "A delivery message asks you to pay a small fee using a link. What is safest?", "scenario_options": ["Pay quickly so the parcel is not returned", "Open the link and enter card details", "Check the delivery company using its official app or website", "Send your OTP to the sender"], "scenario_check": "Check choice",
        "scenario_good": "Good choice. Verify using the official app or website.", "scenario_bad": "Avoid the link. Check directly with the delivery company using its official app or website.",
        "footer": "CyberSaathi — For Everyone | Simple • Accessible • Safe",
    },
    "Malayalam": {
        "tagline": "ഡിജിറ്റൽ ലോകത്തിലെ നിങ്ങളുടെ വിശ്വസ്ത കൂട്ടുകാരൻ",
        "nav": ["ഹോം", "തട്ടിപ്പ് ബോധവൽക്കരണം", "ലിങ്ക് / സന്ദേശ പരിശോധന", "സാഹചര്യങ്ങൾ", "ക്വിസ്", "പാഠങ്ങൾ", "സുരക്ഷാ കേന്ദ്രം", "സ്ത്രീകളുടെ ഡിജിറ്റൽ സുരക്ഷ", "നിങ്ങളുടെ അവകാശങ്ങൾ", "തെളിവ് മാർഗ്ഗനിർദ്ദേശം", "സൈബർ കുറ്റകൃത്യം റിപ്പോർട്ട്"],
        "hero1": "സുരക്ഷിതമായി ചിന്തിക്കൂ.", "hero2": "സുരക്ഷിതരായിരിക്കൂ.",
        "intro": "സൈബർ ഭീഷണികൾ തിരിച്ചറിയാനും ഓൺലൈനിൽ സുരക്ഷിതരാകാനും CyberSaathi സഹായിക്കുന്നു.",
        "link_btn": "സംശയാസ്പദമായ ലിങ്ക് പരിശോധിക്കുക", "msg_btn": "സന്ദേശം പരിശോധിക്കുക",
        "women_title": "സ്ത്രീകളുടെ ഡിജിറ്റൽ സുരക്ഷ", "women_desc": "അപകടങ്ങൾ തിരിച്ചറിയൂ. സുരക്ഷിതരായിരിക്കൂ. നിങ്ങൾ ഒറ്റയ്ക്കല്ല.",
        "explore": "കൂടുതൽ അറിയുക", "help": "ഉടൻ സഹായം വേണോ?", "contacts": "പ്രധാന നമ്പറുകളും വിവരങ്ങളും",
        "tips": "വേഗത്തിലുള്ള സുരക്ഷാ നിർദ്ദേശങ്ങൾ", "tip1": "OTP, പാസ്‌വേഡ്, വ്യക്തിഗത വിവരങ്ങൾ പങ്കിടരുത്.", "tip2": "അറിയാത്ത ലിങ്കുകളും കോളുകളും സൂക്ഷിക്കുക.", "tip3": "വിശ്വസിക്കുന്നതിന് മുമ്പ് പരിശോധിക്കുക.", "tip4": "സംശയമുണ്ടെങ്കിൽ സഹായം തേടുക.",
        "scam": "തട്ടിപ്പ് ബോധവൽക്കരണം", "scam_desc": "സാധാരണ തട്ടിപ്പുകളും അവ ഒഴിവാക്കുന്ന വഴികളും അറിയുക.",
        "link": "ലിങ്ക് പരിശോധന", "link_desc": "തുറക്കുന്നതിന് മുമ്പ് URL സംശയാസ്പദമാണോ എന്ന് പരിശോധിക്കുക.",
        "message": "സന്ദേശ പരിശോധന", "message_desc": "സന്ദേശത്തിലെ സംശയകരമായ വാക്കുകളും സമ്മർദ്ദ തന്ത്രങ്ങളും കണ്ടെത്തുക.",
        "scenarios": "സാഹചര്യങ്ങൾ", "scenarios_desc": "യഥാർത്ഥ ജീവിത സാഹചര്യങ്ങളിൽ സുരക്ഷിതമായ തീരുമാനം തിരഞ്ഞെടുക്കുക.",
        "quiz": "ക്വിസ്", "quiz_desc": "നിങ്ങളുടെ അറിവ് പരിശോധിച്ച് പഠിക്കുക.",
        "lessons": "ബോധവൽക്കരണ പാഠങ്ങൾ", "lessons_desc": "ദൈനംദിന ഓൺലൈൻ സുരക്ഷയ്ക്കുള്ള ലളിതമായ പാഠങ്ങൾ.",
        "smart": "സ്മാർട്ട് സഹായം", "smart_desc": "നിങ്ങളുടെ സാഹചര്യം വിവരിച്ച് അടുത്ത നടപടികൾ അറിയുക.",
        "women": "സ്ത്രീകളുടെ ഡിജിറ്റൽ സുരക്ഷ", "women_card_desc": "പഠിക്കുക, പ്രതിരോധിക്കുക, സഹായം തേടുക.",
        "safety": "സുരക്ഷാ കേന്ദ്രം", "safety_desc": "സഹായം, ഹെൽപ്‌ലൈനുകൾ, ഔദ്യോഗിക വിവരങ്ങൾ.",
        "rights": "നിങ്ങളുടെ അവകാശങ്ങൾ", "evidence": "തെളിവ് മാർഗ്ഗനിർദ്ദേശം", "report": "സൈബർ കുറ്റകൃത്യം റിപ്പോർട്ട്",
        "learn": "പഠിക്കുക", "aware": "ജാഗ്രത പാലിക്കുക", "safe": "സുരക്ഷിതരാകുക", "get_help": "സഹായം തേടുക",
        "choose": "മുകളിലെ മെനുവിൽ നിന്ന് ഒരു വിഭാഗം തിരഞ്ഞെടുക്കുക.",
        "check_link": "ലിങ്ക് പരിശോധിക്കുക", "paste_url": "വെബ് വിലാസം (URL) നൽകുക", "check": "പരിശോധിക്കുക",
        "url_empty": "ദയവായി URL നൽകുക.", "url_result_safe": "വ്യക്തമായ മുന്നറിയിപ്പ് കണ്ടെത്തിയില്ല. അതുകൊണ്ട് വെബ്സൈറ്റ് സുരക്ഷിതമാണെന്ന് ഉറപ്പില്ല.",
        "url_result_warn": "ഈ URL-ൽ മുന്നറിയിപ്പ് സൂചനകളുണ്ട്. സ്വതന്ത്രമായി പരിശോധിക്കാതെ തുറക്കരുത്.",
        "message_label": "ലഭിച്ച സന്ദേശം ഇവിടെ ചേർക്കുക", "analyze": "സന്ദേശം പരിശോധിക്കുക", "message_empty": "ദയവായി സന്ദേശം ചേർക്കുക.",
        "message_result": "മറുപടി നൽകുന്നതിന് മുമ്പ് ഈ മുന്നറിയിപ്പുകൾ പരിശോധിക്കുക:",
        "quiz_question": "ലിങ്ക് അമർത്തിയില്ലെങ്കിൽ ബാങ്ക് അക്കൗണ്ട് തടയും എന്ന് സന്ദേശം ലഭിച്ചാൽ എന്ത് ചെയ്യണം?",
        "quiz_options": ["ഉടൻ ലിങ്ക് തുറക്കുക", "OTP മറുപടിയായി അയയ്ക്കുക", "ലിങ്ക് തുറക്കാതെ ഔദ്യോഗിക നമ്പറിൽ ബാങ്കിനെ ബന്ധപ്പെടുക", "എല്ലാവർക്കും അയയ്ക്കുക"],
        "submit": "ഉത്തരം പരിശോധിക്കുക", "correct": "ശരി! ഔദ്യോഗിക മാർഗം ഉപയോഗിച്ച് സ്ഥിരീകരിക്കുക.", "incorrect": "വീണ്ടും ശ്രമിക്കുക. ലിങ്ക് തുറക്കാതെ ബാങ്കിന്റെ ഔദ്യോഗിക ആപ്പ് അല്ലെങ്കിൽ നമ്പർ ഉപയോഗിക്കുക.",
        "scam_heading": "ശ്രദ്ധിക്കേണ്ട സാധാരണ തട്ടിപ്പുകൾ", "scam_items": ["ബാങ്ക് / KYC മുന്നറിയിപ്പ്: അക്കൗണ്ട് തടയും എന്ന് പറഞ്ഞ് ഭയപ്പെടുത്തുന്നു.", "പാഴ്സൽ ഫീസ്: ചെറിയ തുക അടയ്ക്കാൻ വ്യാജ സന്ദേശം.", "ജോലി വാഗ്ദാനം: രജിസ്ട്രേഷൻ ഫീസ് ആവശ്യപ്പെടുന്നു.", "സുഹൃത്തിന്റെ പേരിൽ പണം ചോദിക്കൽ: അടിയന്തരമായി പണം അയക്കാൻ ആവശ്യപ്പെടുന്നു."],
        "lesson_heading": "ദൈനംദിന സുരക്ഷാ പാഠങ്ങൾ", "lesson_items": ["ഓരോ അക്കൗണ്ടിനും വ്യത്യസ്തവും ശക്തവുമായ പാസ്‌വേഡ് ഉപയോഗിക്കുക.", "സാധ്യമെങ്കിൽ രണ്ട് ഘട്ട സ്ഥിരീകരണം ഓണാക്കുക.", "ഫോണും ആപ്പുകളും പുതുക്കി വയ്ക്കുക.", "ലിങ്കുകൾ തുറക്കുന്നതിന് മുമ്പ് നിർത്തി ചിന്തിക്കുക.", "OTP, PIN, പാസ്‌വേഡ് എന്നിവ ആരുമായും പങ്കിടരുത്."],
        "rights_heading": "നിങ്ങളുടെ അവകാശങ്ങൾ അറിയുക", "rights_items": ["സൈബർ കുറ്റകൃത്യം ഔദ്യോഗിക മാർഗങ്ങളിലൂടെ റിപ്പോർട്ട് ചെയ്യാം.", "സന്ദേശങ്ങൾ, ഇടപാട് വിവരങ്ങൾ, മറ്റ് തെളിവുകൾ സൂക്ഷിക്കുക.", "പണം നഷ്ടപ്പെട്ടാൽ ഉടൻ ബാങ്കിനെ ബന്ധപ്പെടുക.", "മുൻകൂർ ഫീസ് വാങ്ങി പണം തിരികെ നൽകാമെന്ന് പറയുന്നവരെ വിശ്വസിക്കരുത്."],
        "evidence_heading": "തെളിവുകൾ സുരക്ഷിതമായി സൂക്ഷിക്കുക", "evidence_items": ["അയച്ചയാൾ, തീയതി, സമയം എന്നിവ കാണുന്ന സ്ക്രീൻഷോട്ടുകൾ എടുക്കുക.", "ഇടപാട് നമ്പർ, ഫോൺ നമ്പർ, URL, ഇമെയിൽ വിവരങ്ങൾ സൂക്ഷിക്കുക.", "യഥാർത്ഥ സന്ദേശങ്ങളോ സ്ക്രീൻഷോട്ടുകളോ മാറ്റരുത്.", "സുരക്ഷിതമായ ബാക്കപ്പ് സൂക്ഷിക്കുക; സ്വകാര്യ വിവരങ്ങൾ പൊതുവിൽ ഇടരുത്."],
        "report_heading": "സൈബർ കുറ്റകൃത്യം റിപ്പോർട്ട് ചെയ്യുക", "report_text": "ഇന്ത്യയിൽ ഔദ്യോഗിക National Cyber Crime Reporting Portal ഉപയോഗിക്കുക. അടിയന്തര സാമ്പത്തിക സൈബർ തട്ടിപ്പിന് 1930-ൽ വിളിക്കുക. ഉടൻ അപകടമുണ്ടെങ്കിൽ പ്രാദേശിക അടിയന്തര സേവനങ്ങളെ ബന്ധപ്പെടുക.",
        "smart_heading": "എന്താണ് സംഭവിച്ചതെന്ന് പറയൂ", "smart_label": "സാഹചര്യം വിവരിക്കുക (പാസ്‌വേഡ് അല്ലെങ്കിൽ OTP ചേർക്കരുത്)", "smart_button": "അടുത്ത നടപടികൾ കാണിക്കുക",
        "smart_steps": ["മറുപടി നിർത്തുക; പണമോ കോഡുകളോ അയക്കരുത്.", "സ്ക്രീൻഷോട്ടുകളും വിവരങ്ങളും സൂക്ഷിക്കുക.", "അക്കൗണ്ടോ പണമിടപാടോ ബന്ധപ്പെട്ടാൽ ഔദ്യോഗിക നമ്പറിൽ ബന്ധപ്പെടുക.", "ഔദ്യോഗികമായി റിപ്പോർട്ട് ചെയ്യുകയും വിശ്വസ്തരിൽ നിന്ന് സഹായം തേടുകയും ചെയ്യുക."],
        "scenario_heading": "സുരക്ഷിതമായ പ്രതികരണം തിരഞ്ഞെടുക്കുക", "scenario_q": "പാഴ്സൽ ലഭിക്കാൻ ചെറിയ ഫീസ് അടയ്ക്കാൻ ലിങ്ക് വന്നാൽ എന്താണ് സുരക്ഷിതം?", "scenario_options": ["ഉടൻ പണം അടയ്ക്കുക", "ലിങ്ക് തുറന്ന് കാർഡ് വിവരങ്ങൾ നൽകുക", "കമ്പനിയുടെ ഔദ്യോഗിക ആപ്പ് അല്ലെങ്കിൽ വെബ്സൈറ്റ് പരിശോധിക്കുക", "OTP അയയ്ക്കുക"], "scenario_check": "ഉത്തരം പരിശോധിക്കുക",
        "scenario_good": "ശരിയായ തിരഞ്ഞെടുപ്പ്. ഔദ്യോഗിക ആപ്പ് അല്ലെങ്കിൽ വെബ്സൈറ്റ് പരിശോധിക്കുക.", "scenario_bad": "ലിങ്ക് ഒഴിവാക്കുക. ഔദ്യോഗിക ആപ്പ് അല്ലെങ്കിൽ വെബ്സൈറ്റ് വഴി പരിശോധിക്കുക.",
        "footer": "CyberSaathi — എല്ലാവർക്കുമായി | ലളിതം • ലഭ്യമാകുന്നത് എളുപ്പം • സുരക്ഷിതം",
    },
    "Hindi": {
        "tagline": "डिजिटल दुनिया में आपका भरोसेमंद साथी",
        "nav": ["होम", "घोटालों से जागरूकता", "लिंक और संदेश जाँच", "परिस्थितियाँ", "क्विज़", "पाठ", "सुरक्षा केंद्र", "महिलाओं की डिजिटल सुरक्षा", "अपने अधिकार जानें", "सबूत मार्गदर्शिका", "साइबर अपराध रिपोर्ट करें"],
        "hero1": "सुरक्षित सोचें।", "hero2": "सुरक्षित रहें।", "intro": "CyberSaathi आपको साइबर खतरों को पहचानने, ऑनलाइन सुरक्षित रहने और सही मदद पाने में मदद करता है।",
        "link_btn": "संदिग्ध लिंक जाँचें", "msg_btn": "संदेश जाँचें", "women_title": "महिलाओं की डिजिटल सुरक्षा", "women_desc": "जोखिम जानें। सुरक्षित रहें। आप अकेले नहीं हैं।",
        "explore": "और जानें", "help": "अभी मदद चाहिए?", "contacts": "महत्वपूर्ण संपर्क और संसाधन", "tips": "त्वरित सुरक्षा सुझाव",
        "tip1": "OTP, पासवर्ड या निजी जानकारी साझा न करें।", "tip2": "अनजान लिंक और कॉल से सावधान रहें।", "tip3": "भरोसा करने से पहले जाँचें।", "tip4": "संदेह हो तो मदद माँगें।",
        "scam": "घोटालों से जागरूकता", "scam_desc": "आम घोटालों और उनसे बचने के तरीके जानें।", "link": "लिंक जाँचक", "link_desc": "खोलने से पहले URL में संदेह के संकेत जाँचें।",
        "message": "संदेश जाँचक", "message_desc": "संदेश में दबाव डालने वाली भाषा और संदेहजनक शब्द पहचानें।", "scenarios": "परिस्थितियाँ", "scenarios_desc": "वास्तविक परिस्थितियों में सुरक्षित विकल्प चुनें।",
        "quiz": "क्विज़", "quiz_desc": "अपनी जानकारी जाँचें और सीखें।", "lessons": "जागरूकता पाठ", "lessons_desc": "रोज़मर्रा की ऑनलाइन सुरक्षा के सरल पाठ।",
        "smart": "स्मार्ट मदद", "smart_desc": "अपनी स्थिति बताएँ और अगले कदम जानें।", "women": "महिलाओं की डिजिटल सुरक्षा", "women_card_desc": "सीखें, बचाव करें और मदद पाएँ।",
        "safety": "सुरक्षा केंद्र", "safety_desc": "त्वरित मदद, हेल्पलाइन और आधिकारिक संसाधन।", "rights": "अपने अधिकार जानें", "evidence": "सबूत मार्गदर्शिका", "report": "साइबर अपराध रिपोर्ट करें",
        "learn": "सीखें", "aware": "सतर्क रहें", "safe": "सुरक्षित रहें", "get_help": "मदद पाएँ", "choose": "ऊपर के मेनू से एक भाग चुनें।",
        "check_link": "लिंक जाँचें", "paste_url": "वेब पता (URL) डालें", "check": "जाँचें", "url_empty": "कृपया URL डालें।", "url_result_safe": "कोई स्पष्ट चेतावनी नहीं मिली। इससे वेबसाइट सुरक्षित होने की गारंटी नहीं मिलती।", "url_result_warn": "इस URL में चेतावनी के संकेत हैं। स्वतंत्र रूप से जाँचे बिना न खोलें।",
        "message_label": "मिला हुआ संदेश यहाँ डालें", "analyze": "संदेश की समीक्षा करें", "message_empty": "कृपया संदेश डालें।", "message_result": "जवाब देने से पहले इन चेतावनी संकेतों को देखें:",
        "quiz_question": "बैंक खाता बंद होने की धमकी देकर लिंक पर क्लिक करने को कहा जाए तो क्या करें?", "quiz_options": ["तुरंत लिंक खोलें", "OTP भेजें", "लिंक न खोलें; बैंक के आधिकारिक नंबर पर संपर्क करें", "सबको आगे भेजें"],
        "submit": "उत्तर जाँचें", "correct": "सही! आधिकारिक तरीके से पुष्टि करें।", "incorrect": "फिर कोशिश करें। लिंक न खोलें; बैंक के आधिकारिक ऐप या नंबर से संपर्क करें।",
        "scam_heading": "आम घोटाले जिनसे सावधान रहें", "scam_items": ["बैंक/KYC चेतावनी: खाते बंद होने का डर दिखाते हैं।", "पार्सल शुल्क: नकली संदेश छोटी रकम माँगता है।", "नौकरी का प्रस्ताव: पंजीकरण शुल्क माँगा जाता है।", "दोस्त के नाम पर पैसे माँगना: जल्दी पैसे भेजने का दबाव।"],
        "lesson_heading": "रोज़मर्रा की सुरक्षा के पाठ", "lesson_items": ["हर महत्वपूर्ण खाते के लिए अलग मजबूत पासवर्ड रखें।", "जहाँ संभव हो दो-चरण सत्यापन चालू करें।", "फोन और ऐप अपडेट रखें।", "लिंक खोलने से पहले रुककर सोचें।", "OTP, PIN या पासवर्ड किसी से साझा न करें।"],
        "rights_heading": "अपने अधिकार जानें", "rights_items": ["संदिग्ध साइबर अपराध को आधिकारिक माध्यम से रिपोर्ट कर सकते हैं।", "संदेश, लेन-देन संदर्भ और अन्य सबूत सुरक्षित रखें।", "पैसे खोने पर तुरंत बैंक से संपर्क करें।", "पहले शुल्क लेकर पैसे वापस दिलाने का वादा करने वालों से सावधान रहें।"],
        "evidence_heading": "सबूत सुरक्षित रखें", "evidence_items": ["भेजने वाले, तारीख, समय सहित स्क्रीनशॉट लें।", "लेन-देन ID, फोन नंबर, URL और ईमेल विवरण रखें।", "मूल संदेश या स्क्रीनशॉट न बदलें।", "सुरक्षित बैकअप रखें और निजी जानकारी सार्वजनिक न करें।"],
        "report_heading": "साइबर अपराध रिपोर्ट करें", "report_text": "भारत में आधिकारिक National Cyber Crime Reporting Portal का उपयोग करें। तत्काल वित्तीय साइबर धोखाधड़ी के लिए 1930 पर कॉल करें। तत्काल खतरे में स्थानीय आपातकालीन सेवाओं से संपर्क करें।",
        "smart_heading": "बताएँ क्या हुआ", "smart_label": "स्थिति बताएँ (पासवर्ड या OTP न लिखें)", "smart_button": "अगले कदम दिखाएँ",
        "smart_steps": ["जवाब देना बंद करें और पैसे या कोड न भेजें।", "स्क्रीनशॉट और जरूरी विवरण सुरक्षित रखें।", "खाते या भुगतान से जुड़ा मामला हो तो आधिकारिक संपर्क से बैंक/सेवा प्रदाता से बात करें।", "आधिकारिक माध्यम से रिपोर्ट करें और भरोसेमंद व्यक्ति से मदद लें।"],
        "scenario_heading": "सबसे सुरक्षित जवाब चुनें", "scenario_q": "डिलीवरी का संदेश छोटी फीस के लिए लिंक भेजता है। सबसे सुरक्षित क्या है?", "scenario_options": ["तुरंत भुगतान करें", "लिंक खोलकर कार्ड विवरण भरें", "कंपनी की आधिकारिक ऐप या वेबसाइट जाँचें", "OTP भेजें"], "scenario_check": "उत्तर जाँचें",
        "scenario_good": "सही चुनाव। आधिकारिक ऐप या वेबसाइट से जाँचें।", "scenario_bad": "लिंक से बचें। कंपनी की आधिकारिक ऐप या वेबसाइट से जाँचें।", "footer": "CyberSaathi — सभी के लिए | सरल • सुलभ • सुरक्षित",
    },
    "Tamil": {
        "tagline": "டிஜிட்டல் உலகில் உங்கள் நம்பகமான துணை",
        "nav": ["முகப்பு", "மோசடி விழிப்புணர்வு", "இணைப்பு மற்றும் செய்தி சரிபார்ப்பு", "சூழல்கள்", "வினாடி வினா", "பாடங்கள்", "பாதுகாப்பு மையம்", "பெண்களின் டிஜிட்டல் பாதுகாப்பு", "உங்கள் உரிமைகள்", "ஆதார வழிகாட்டி", "சைபர் குற்றத்தைப் புகாரளி"],
        "hero1": "பாதுகாப்பாக சிந்தியுங்கள்.", "hero2": "பாதுகாப்பாக இருங்கள்.", "intro": "சைபர் ஆபத்துகளை அறிந்து, இணையத்தில் பாதுகாப்பாக இருக்க CyberSaathi உதவுகிறது.",
        "link_btn": "சந்தேக இணைப்பைச் சரிபார்க்கவும்", "msg_btn": "செய்தியைச் சரிபார்க்கவும்", "women_title": "பெண்களின் டிஜிட்டல் பாதுகாப்பு", "women_desc": "ஆபத்துகளை அறியுங்கள். பாதுகாப்பாக இருங்கள். நீங்கள் தனியாக இல்லை.",
        "explore": "மேலும் அறிக", "help": "உடனடி உதவி வேண்டுமா?", "contacts": "முக்கிய தொடர்புகள் மற்றும் ஆதாரங்கள்", "tips": "விரைவு பாதுகாப்பு குறிப்புகள்",
        "tip1": "OTP, கடவுச்சொல் அல்லது தனிப்பட்ட தகவலைப் பகிர வேண்டாம்.", "tip2": "அறியாத இணைப்புகள் மற்றும் அழைப்புகளில் கவனமாக இருங்கள்.", "tip3": "நம்புவதற்கு முன் சரிபார்க்கவும்.", "tip4": "சந்தேகம் இருந்தால் உதவி கேளுங்கள்.",
        "scam": "மோசடி விழிப்புணர்வு", "scam_desc": "பொதுவான மோசடிகள் மற்றும் அவற்றைத் தவிர்ப்பது எப்படி என்பதை அறிக.", "link": "இணைப்பு சரிபார்ப்பு", "link_desc": "திறப்பதற்கு முன் URL-ஐச் சரிபார்க்கவும்.",
        "message": "செய்தி சரிபார்ப்பு", "message_desc": "சந்தேகமான சொற்கள் மற்றும் அழுத்தம் கொடுக்கும் முறைகளைக் கவனியுங்கள்.", "scenarios": "சூழல்கள்", "scenarios_desc": "நிஜ வாழ்க்கை சூழல்களில் பாதுகாப்பான தேர்வைப் பயிற்சி செய்யுங்கள்.",
        "quiz": "வினாடி வினா", "quiz_desc": "உங்கள் அறிவைச் சோதித்து கற்றுக்கொள்ளுங்கள்.", "lessons": "விழிப்புணர்வு பாடங்கள்", "lessons_desc": "தினசரி இணைய பாதுகாப்புக்கான எளிய பாடங்கள்.",
        "smart": "சிறப்பு உதவி", "smart_desc": "உங்கள் நிலையை விவரித்து அடுத்த படிகளை அறியுங்கள்.", "women": "பெண்களின் டிஜிட்டல் பாதுகாப்பு", "women_card_desc": "கற்றுக்கொள்ளுங்கள், தடுக்குங்கள், உதவி பெறுங்கள்.",
        "safety": "பாதுகாப்பு மையம்", "safety_desc": "உதவி, உதவி எண்கள் மற்றும் அதிகாரப்பூர்வ தகவல்கள்.", "rights": "உங்கள் உரிமைகள்", "evidence": "ஆதார வழிகாட்டி", "report": "சைபர் குற்றத்தைப் புகாரளி",
        "learn": "கற்றுக்கொள்", "aware": "விழிப்புடன் இரு", "safe": "பாதுகாப்பாக இரு", "get_help": "உதவி பெறு", "choose": "மேலே உள்ள மெனுவிலிருந்து ஒரு பகுதியைத் தேர்ந்தெடுக்கவும்.",
        "check_link": "இணைப்பைச் சரிபார்க்கவும்", "paste_url": "இணைய முகவரியை (URL) உள்ளிடவும்", "check": "சரிபார்", "url_empty": "URL உள்ளிடவும்.", "url_result_safe": "தெளிவான எச்சரிக்கை இல்லை. இதனால் தளம் பாதுகாப்பானது என்று உறுதி செய்ய முடியாது.", "url_result_warn": "இந்த URL-ல் எச்சரிக்கை அறிகுறிகள் உள்ளன. தனியாகச் சரிபார்க்காமல் திறக்க வேண்டாம்.",
        "message_label": "பெற்ற செய்தியை இங்கே ஒட்டவும்", "analyze": "செய்தியை மதிப்பாய்வு செய்", "message_empty": "செய்தியை உள்ளிடவும்.", "message_result": "பதிலளிக்கும் முன் இந்த எச்சரிக்கைகளைப் பாருங்கள்:",
        "quiz_question": "வங்கிக் கணக்கு முடக்கப்படும் என்று கூறி இணைப்பைக் கிளிக் செய்யச் சொன்னால் என்ன செய்ய வேண்டும்?", "quiz_options": ["உடனே இணைப்பைத் திறக்கவும்", "OTP அனுப்பவும்", "இணைப்பைத் திறக்காமல் வங்கியின் அதிகாரப்பூர்வ எண்ணைத் தொடர்புகொள்ளவும்", "அனைவருக்கும் அனுப்பவும்"],
        "submit": "பதிலைச் சரிபார்", "correct": "சரி! அதிகாரப்பூர்வ வழியில் உறுதிப்படுத்துங்கள்.", "incorrect": "மீண்டும் முயற்சிக்கவும். இணைப்பைத் திறக்காமல் வங்கியின் அதிகாரப்பூர்வ செயலி அல்லது எண்ணைப் பயன்படுத்துங்கள்.",
        "scam_heading": "கவனிக்க வேண்டிய பொதுவான மோசடிகள்", "scam_items": ["வங்கி/KYC எச்சரிக்கை: கணக்கு முடக்கப்படும் என்று பயமுறுத்துதல்.", "பார்சல் கட்டணம்: சிறிய தொகை கேட்கும் போலியான செய்தி.", "வேலை வாய்ப்பு: பதிவு கட்டணம் கேட்பது.", "நண்பர் பெயரில் பணம் கேட்பது: அவசரமாக பணம் அனுப்பச் சொல்வது."],
        "lesson_heading": "தினசரி பாதுகாப்புப் பாடங்கள்", "lesson_items": ["ஒவ்வொரு முக்கிய கணக்கிற்கும் வலுவான தனித்த கடவுச்சொல் பயன்படுத்துங்கள்.", "இரண்டு-படி சரிபார்ப்பை இயக்குங்கள்.", "தொலைபேசி மற்றும் செயலிகளைப் புதுப்பிக்கவும்.", "இணைப்பைத் திறப்பதற்கு முன் சிந்தியுங்கள்.", "OTP, PIN அல்லது கடவுச்சொல்லைப் பகிர வேண்டாம்."],
        "rights_heading": "உங்கள் உரிமைகளை அறியுங்கள்", "rights_items": ["சந்தேகமான சைபர் குற்றத்தை அதிகாரப்பூர்வமாகப் புகாரளிக்கலாம்.", "செய்திகள் மற்றும் பரிவர்த்தனை விவரங்களைச் சேமிக்கவும்.", "பணம் இழந்தால் உடனே வங்கியைத் தொடர்புகொள்ளுங்கள்.", "முன்பணம் வாங்கி பணத்தை மீட்டுத் தருவதாகக் கூறுபவர்களை நம்ப வேண்டாம்."],
        "evidence_heading": "ஆதாரங்களைப் பாதுகாப்பாக வைத்திருங்கள்", "evidence_items": ["அனுப்பியவர், தேதி, நேரம் தெரியும் வகையில் திரைப்பிடிப்புகள் எடுக்கவும்.", "பரிவர்த்தனை ID, தொலைபேசி எண், URL, மின்னஞ்சல் விவரங்களைச் சேமிக்கவும்.", "அசல் செய்திகளை மாற்ற வேண்டாம்.", "பாதுகாப்பான காப்புப்பிரதி வைத்திருங்கள்; தனிப்பட்ட தகவலைப் பொதுவில் இட வேண்டாம்."],
        "report_heading": "சைபர் குற்றத்தைப் புகாரளிக்கவும்", "report_text": "இந்தியாவில் அதிகாரப்பூர்வ National Cyber Crime Reporting Portal-ஐப் பயன்படுத்தவும். அவசர நிதி மோசடிக்கு 1930-ஐ அழைக்கவும். உடனடி ஆபத்து இருந்தால் உள்ளூர் அவசர சேவைகளைத் தொடர்புகொள்ளவும்.",
        "smart_heading": "என்ன நடந்தது என்று கூறுங்கள்", "smart_label": "நிலையை விவரிக்கவும் (கடவுச்சொல் அல்லது OTP சேர்க்க வேண்டாம்)", "smart_button": "அடுத்த படிகளைக் காட்டு",
        "smart_steps": ["பதிலளிப்பதை நிறுத்தி பணம் அல்லது குறியீடுகளை அனுப்ப வேண்டாம்.", "திரைப்பிடிப்புகள் மற்றும் விவரங்களைச் சேமிக்கவும்.", "கணக்கு அல்லது பணம் தொடர்பானால் அதிகாரப்பூர்வ தொடர்பு வழியாக வங்கியை அணுகவும்.", "அதிகாரப்பூர்வமாகப் புகாரளித்து நம்பகமானவரிடம் உதவி கேளுங்கள்."],
        "scenario_heading": "பாதுகாப்பான பதிலைத் தேர்ந்தெடுக்கவும்", "scenario_q": "டெலிவரி செய்தி சிறிய கட்டணத்திற்காக இணைப்பை அனுப்புகிறது. பாதுகாப்பானது எது?", "scenario_options": ["உடனே பணம் செலுத்தவும்", "இணைப்பைத் திறந்து அட்டை விவரங்களை உள்ளிடவும்", "நிறுவனத்தின் அதிகாரப்பூர்வ செயலி அல்லது இணையதளத்தைச் சரிபார்க்கவும்", "OTP அனுப்பவும்"], "scenario_check": "பதிலைச் சரிபார்",
        "scenario_good": "சரியான தேர்வு. அதிகாரப்பூர்வ செயலி அல்லது இணையதளத்தில் சரிபார்க்கவும்.", "scenario_bad": "இணைப்பைத் தவிர்க்கவும். அதிகாரப்பூர்வ செயலி அல்லது இணையதளத்தில் சரிபார்க்கவும்.", "footer": "CyberSaathi — அனைவருக்கும் | எளிமை • அணுகக்கூடியது • பாதுகாப்பு",
    },
    "Kannada": {
        "tagline": "ಡಿಜಿಟಲ್ ಜಗತ್ತಿನಲ್ಲಿ ನಿಮ್ಮ ವಿಶ್ವಾಸಾರ್ಹ ಸಂಗಾತಿ",
        "nav": ["ಮುಖಪುಟ", "ಮೋಸಗಳ ಬಗ್ಗೆ ಅರಿವು", "ಲಿಂಕ್ ಮತ್ತು ಸಂದೇಶ ಪರಿಶೀಲನೆ", "ಪರಿಸ್ಥಿತಿಗಳು", "ಕ್ವಿಜ್", "ಪಾಠಗಳು", "ಸುರಕ್ಷತಾ ಕೇಂದ್ರ", "ಮಹಿಳೆಯರ ಡಿಜಿಟಲ್ ಸುರಕ್ಷತೆ", "ನಿಮ್ಮ ಹಕ್ಕುಗಳು", "ಸಾಕ್ಷ್ಯ ಮಾರ್ಗದರ್ಶಿ", "ಸೈಬರ್ ಅಪರಾಧ ವರದಿ"],
        "hero1": "ಸುರಕ್ಷಿತವಾಗಿ ಯೋಚಿಸಿ.", "hero2": "ಸುರಕ್ಷಿತವಾಗಿರಿ.", "intro": "ಸೈಬರ್ ಅಪಾಯಗಳನ್ನು ಗುರುತಿಸಲು ಮತ್ತು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿರಲು CyberSaathi ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "link_btn": "ಸಂದೇಹಾಸ್ಪದ ಲಿಂಕ್ ಪರಿಶೀಲಿಸಿ", "msg_btn": "ಸಂದೇಶ ಪರಿಶೀಲಿಸಿ", "women_title": "ಮಹಿಳೆಯರ ಡಿಜಿಟಲ್ ಸುರಕ್ಷತೆ", "women_desc": "ಅಪಾಯಗಳನ್ನು ತಿಳಿಯಿರಿ. ಸುರಕ್ಷಿತವಾಗಿರಿ. ನೀವು ಒಬ್ಬರಲ್ಲ.",
        "explore": "ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ", "help": "ಈಗ ಸಹಾಯ ಬೇಕೇ?", "contacts": "ಮುಖ್ಯ ಸಂಪರ್ಕಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳು", "tips": "ತ್ವರಿತ ಸುರಕ್ಷತಾ ಸಲಹೆಗಳು",
        "tip1": "OTP, ಪಾಸ್‌ವರ್ಡ್ ಅಥವಾ ವೈಯಕ್ತಿಕ ಮಾಹಿತಿಯನ್ನು ಹಂಚಬೇಡಿ.", "tip2": "ಅಪರಿಚಿತ ಲಿಂಕ್ ಮತ್ತು ಕರೆಗಳ ಬಗ್ಗೆ ಎಚ್ಚರಿಕೆ ಇರಲಿ.", "tip3": "ನಂಬುವ ಮೊದಲು ಪರಿಶೀಲಿಸಿ.", "tip4": "ಸಂದೇಹವಿದ್ದರೆ ಸಹಾಯ ಕೇಳಿ.",
        "scam": "ಮೋಸಗಳ ಬಗ್ಗೆ ಅರಿವು", "scam_desc": "ಸಾಮಾನ್ಯ ಮೋಸಗಳು ಮತ್ತು ಅವುಗಳಿಂದ ತಪ್ಪಿಸಿಕೊಳ್ಳುವ ವಿಧಾನಗಳನ್ನು ತಿಳಿಯಿರಿ.", "link": "ಲಿಂಕ್ ಪರಿಶೀಲಕ", "link_desc": "ತೆರೆಯುವ ಮೊದಲು URL ಅನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "message": "ಸಂದೇಶ ಪರಿಶೀಲಕ", "message_desc": "ಸಂದೇಶದಲ್ಲಿನ ಅನುಮಾನಾಸ್ಪದ ಪದಗಳು ಮತ್ತು ಒತ್ತಡದ ತಂತ್ರಗಳನ್ನು ಗಮನಿಸಿ.", "scenarios": "ಪರಿಸ್ಥಿತಿಗಳು", "scenarios_desc": "ನೈಜ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಸುರಕ್ಷಿತ ಆಯ್ಕೆಯನ್ನು ಅಭ್ಯಾಸ ಮಾಡಿ.",
        "quiz": "ಕ್ವಿಜ್", "quiz_desc": "ನಿಮ್ಮ ಜ್ಞಾನವನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಕಲಿಯಿರಿ.", "lessons": "ಜಾಗೃತಿ ಪಾಠಗಳು", "lessons_desc": "ದೈನಂದಿನ ಆನ್‌ಲೈನ್ ಸುರಕ್ಷತೆಯ ಸರಳ ಪಾಠಗಳು.",
        "smart": "ಸ್ಮಾರ್ಟ್ ಸಹಾಯ", "smart_desc": "ನಿಮ್ಮ ಪರಿಸ್ಥಿತಿಯನ್ನು ವಿವರಿಸಿ ಮುಂದಿನ ಹಂತಗಳನ್ನು ತಿಳಿಯಿರಿ.", "women": "ಮಹಿಳೆಯರ ಡಿಜಿಟಲ್ ಸುರಕ್ಷತೆ", "women_card_desc": "ಕಲಿಯಿರಿ, ತಡೆಯಿರಿ, ಸಹಾಯ ಪಡೆಯಿರಿ.",
        "safety": "ಸುರಕ್ಷತಾ ಕೇಂದ್ರ", "safety_desc": "ತ್ವರಿತ ಸಹಾಯ, ಸಹಾಯವಾಣಿ ಮತ್ತು ಅಧಿಕೃತ ಸಂಪನ್ಮೂಲಗಳು.", "rights": "ನಿಮ್ಮ ಹಕ್ಕುಗಳು", "evidence": "ಸಾಕ್ಷ್ಯ ಮಾರ್ಗದರ್ಶಿ", "report": "ಸೈಬರ್ ಅಪರಾಧ ವರದಿ",
        "learn": "ಕಲಿಯಿರಿ", "aware": "ಎಚ್ಚರಿಕೆಯಿಂದಿರಿ", "safe": "ಸುರಕ್ಷಿತವಾಗಿರಿ", "get_help": "ಸಹಾಯ ಪಡೆಯಿರಿ", "choose": "ಮೇಲಿನ ಮೆನುವಿನಿಂದ ಒಂದು ವಿಭಾಗ ಆಯ್ಕೆಮಾಡಿ.",
        "check_link": "ಲಿಂಕ್ ಪರಿಶೀಲಿಸಿ", "paste_url": "ವೆಬ್ ವಿಳಾಸ (URL) ನಮೂದಿಸಿ", "check": "ಪರಿಶೀಲಿಸಿ", "url_empty": "ದಯವಿಟ್ಟು URL ನಮೂದಿಸಿ.", "url_result_safe": "ಸ್ಪಷ್ಟ ಎಚ್ಚರಿಕೆ ಕಂಡುಬಂದಿಲ್ಲ. ಇದರಿಂದ ವೆಬ್‌ಸೈಟ್ ಸುರಕ್ಷಿತವೆಂದು ಖಚಿತವಾಗುವುದಿಲ್ಲ.", "url_result_warn": "ಈ URL ನಲ್ಲಿ ಎಚ್ಚರಿಕೆಯ ಸೂಚನೆಗಳಿವೆ. ಸ್ವತಂತ್ರವಾಗಿ ಪರಿಶೀಲಿಸದೆ ತೆರೆಯಬೇಡಿ.",
        "message_label": "ಸ್ವೀಕರಿಸಿದ ಸಂದೇಶವನ್ನು ಇಲ್ಲಿ ಅಂಟಿಸಿ", "analyze": "ಸಂದೇಶ ಪರಿಶೀಲಿಸಿ", "message_empty": "ದಯವಿಟ್ಟು ಸಂದೇಶವನ್ನು ಅಂಟಿಸಿ.", "message_result": "ಉತ್ತರಿಸುವ ಮೊದಲು ಈ ಎಚ್ಚರಿಕೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ:",
        "quiz_question": "ಬ್ಯಾಂಕ್ ಖಾತೆ ನಿರ್ಬಂಧಿಸಲಾಗುತ್ತದೆ ಎಂದು ಲಿಂಕ್ ಕ್ಲಿಕ್ ಮಾಡಲು ಸಂದೇಶ ಬಂದರೆ ಏನು ಮಾಡಬೇಕು?", "quiz_options": ["ತಕ್ಷಣ ಲಿಂಕ್ ತೆರೆಯಿರಿ", "OTP ಕಳುಹಿಸಿ", "ಲಿಂಕ್ ತೆರೆಯದೆ ಬ್ಯಾಂಕಿನ ಅಧಿಕೃತ ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ", "ಎಲ್ಲರಿಗೂ ಕಳುಹಿಸಿ"],
        "submit": "ಉತ್ತರ ಪರಿಶೀಲಿಸಿ", "correct": "ಸರಿಯಾಗಿದೆ! ಅಧಿಕೃತ ಮಾರ್ಗದ ಮೂಲಕ ದೃಢೀಕರಿಸಿ.", "incorrect": "ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ. ಲಿಂಕ್ ತೆರೆಯದೆ ಬ್ಯಾಂಕಿನ ಅಧಿಕೃತ ಆಪ್ ಅಥವಾ ಸಂಖ್ಯೆಯನ್ನು ಬಳಸಿ.",
        "scam_heading": "ಗಮನಿಸಬೇಕಾದ ಸಾಮಾನ್ಯ ಮೋಸಗಳು", "scam_items": ["ಬ್ಯಾಂಕ್/KYC ಎಚ್ಚರಿಕೆ: ಖಾತೆ ನಿರ್ಬಂಧಿಸಲಾಗುತ್ತದೆ ಎಂದು ಹೆದರಿಸುವುದು.", "ಪಾರ್ಸೆಲ್ ಶುಲ್ಕ: ಸಣ್ಣ ಮೊತ್ತ ಕೇಳುವ ನಕಲಿ ಸಂದೇಶ.", "ಉದ್ಯೋಗ ಆಫರ್: ನೋಂದಣಿ ಶುಲ್ಕ ಕೇಳುವುದು.", "ಸ್ನೇಹಿತನ ಹೆಸರಿನಲ್ಲಿ ಹಣ ಕೇಳುವುದು: ತುರ್ತಾಗಿ ಹಣ ಕಳುಹಿಸಲು ಒತ್ತಾಯಿಸುವುದು."],
        "lesson_heading": "ದೈನಂದಿನ ಸುರಕ್ಷತಾ ಪಾಠಗಳು", "lesson_items": ["ಪ್ರತಿ ಪ್ರಮುಖ ಖಾತೆಗೆ ಬಲವಾದ ವಿಭಿನ್ನ ಪಾಸ್‌ವರ್ಡ್ ಬಳಸಿ.", "ಸಾಧ್ಯವಾದಲ್ಲಿ ಎರಡು ಹಂತದ ಪರಿಶೀಲನೆ ಆನ್ ಮಾಡಿ.", "ಫೋನ್ ಮತ್ತು ಆಪ್‌ಗಳನ್ನು ನವೀಕರಿಸಿ.", "ಲಿಂಕ್ ತೆರೆಯುವ ಮೊದಲು ಯೋಚಿಸಿ.", "OTP, PIN ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್ ಹಂಚಬೇಡಿ."],
        "rights_heading": "ನಿಮ್ಮ ಹಕ್ಕುಗಳನ್ನು ತಿಳಿಯಿರಿ", "rights_items": ["ಸಂದೇಹಾಸ್ಪದ ಸೈಬರ್ ಅಪರಾಧವನ್ನು ಅಧಿಕೃತವಾಗಿ ವರದಿ ಮಾಡಬಹುದು.", "ಸಂದೇಶಗಳು ಮತ್ತು ವ್ಯವಹಾರದ ವಿವರಗಳನ್ನು ಉಳಿಸಿ.", "ಹಣ ಕಳೆದುಕೊಂಡರೆ ತಕ್ಷಣ ಬ್ಯಾಂಕ್ ಸಂಪರ್ಕಿಸಿ.", "ಮುಂಗಡ ಶುಲ್ಕ ಪಡೆದು ಹಣ ಮರಳಿ ಕೊಡುತ್ತೇವೆ ಎನ್ನುವವರನ್ನು ನಂಬಬೇಡಿ."],
        "evidence_heading": "ಸಾಕ್ಷ್ಯವನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಉಳಿಸಿ", "evidence_items": ["ಕಳುಹಿಸಿದವರು, ದಿನಾಂಕ ಮತ್ತು ಸಮಯ ಕಾಣುವ ಸ್ಕ್ರೀನ್‌ಶಾಟ್ ತೆಗೆದುಕೊಳ್ಳಿ.", "ವ್ಯವಹಾರ ID, ಫೋನ್ ಸಂಖ್ಯೆ, URL ಮತ್ತು ಇಮೇಲ್ ವಿವರ ಉಳಿಸಿ.", "ಮೂಲ ಸಂದೇಶ ಅಥವಾ ಸ್ಕ್ರೀನ್‌ಶಾಟ್ ಬದಲಿಸಬೇಡಿ.", "ಸುರಕ್ಷಿತ ಬ್ಯಾಕಪ್ ಇಡಿ; ಖಾಸಗಿ ಮಾಹಿತಿಯನ್ನು ಸಾರ್ವಜನಿಕವಾಗಿ ಹಂಚಬೇಡಿ."],
        "report_heading": "ಸೈಬರ್ ಅಪರಾಧ ವರದಿ ಮಾಡಿ", "report_text": "ಭಾರತದಲ್ಲಿ ಅಧಿಕೃತ National Cyber Crime Reporting Portal ಬಳಸಿ. ತುರ್ತು ಹಣಕಾಸು ಸೈಬರ್ ವಂಚನೆಗೆ 1930 ಕರೆ ಮಾಡಿ. ತಕ್ಷಣದ ಅಪಾಯವಿದ್ದರೆ ಸ್ಥಳೀಯ ತುರ್ತು ಸೇವೆಗಳನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "smart_heading": "ಏನಾಯಿತು ಎಂದು ತಿಳಿಸಿ", "smart_label": "ಪರಿಸ್ಥಿತಿಯನ್ನು ವಿವರಿಸಿ (ಪಾಸ್‌ವರ್ಡ್ ಅಥವಾ OTP ಸೇರಿಸಬೇಡಿ)", "smart_button": "ಮುಂದಿನ ಹಂತಗಳನ್ನು ತೋರಿಸಿ",
        "smart_steps": ["ಉತ್ತರಿಸುವುದನ್ನು ನಿಲ್ಲಿಸಿ; ಹಣ ಅಥವಾ ಕೋಡ್ ಕಳುಹಿಸಬೇಡಿ.", "ಸ್ಕ್ರೀನ್‌ಶಾಟ್ ಮತ್ತು ವಿವರಗಳನ್ನು ಉಳಿಸಿ.", "ಖಾತೆ ಅಥವಾ ಪಾವತಿಗೆ ಸಂಬಂಧಿಸಿದ್ದರೆ ಅಧಿಕೃತ ಸಂಪರ್ಕದ ಮೂಲಕ ಬ್ಯಾಂಕ್ ಅನ್ನು ಸಂಪರ್ಕಿಸಿ.", "ಅಧಿಕೃತವಾಗಿ ವರದಿ ಮಾಡಿ ಮತ್ತು ವಿಶ್ವಾಸಾರ್ಹ ವ್ಯಕ್ತಿಯಿಂದ ಸಹಾಯ ಪಡೆಯಿರಿ."],
        "scenario_heading": "ಸುರಕ್ಷಿತ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ", "scenario_q": "ಡೆಲಿವರಿ ಸಂದೇಶ ಸಣ್ಣ ಶುಲ್ಕಕ್ಕಾಗಿ ಲಿಂಕ್ ಕಳುಹಿಸಿದರೆ ಸುರಕ್ಷಿತ ಕ್ರಮ ಯಾವುದು?", "scenario_options": ["ತಕ್ಷಣ ಪಾವತಿಸಿ", "ಲಿಂಕ್ ತೆರೆದು ಕಾರ್ಡ್ ವಿವರ ನಮೂದಿಸಿ", "ಕಂಪನಿಯ ಅಧಿಕೃತ ಆಪ್ ಅಥವಾ ವೆಬ್‌ಸೈಟ್ ಪರಿಶೀಲಿಸಿ", "OTP ಕಳುಹಿಸಿ"], "scenario_check": "ಉತ್ತರ ಪರಿಶೀಲಿಸಿ",
        "scenario_good": "ಸರಿಯಾದ ಆಯ್ಕೆ. ಅಧಿಕೃತ ಆಪ್ ಅಥವಾ ವೆಬ್‌ಸೈಟ್ ಮೂಲಕ ಪರಿಶೀಲಿಸಿ.", "scenario_bad": "ಲಿಂಕ್ ತಪ್ಪಿಸಿ. ಅಧಿಕೃತ ಆಪ್ ಅಥವಾ ವೆಬ್‌ಸೈಟ್ ಮೂಲಕ ಪರಿಶೀಲಿಸಿ.", "footer": "CyberSaathi — ಎಲ್ಲರಿಗಾಗಿ | ಸರಳ • ಸುಲಭವಾಗಿ ಲಭ್ಯ • ಸುರಕ್ಷಿತ",
    },
}

# -------------------- EXTRA TRANSLATIONS --------------------
EXTRA = {
"English": {
 "quiz_title":"Cyber Safety Quiz — 15 Questions", "quiz_intro":"Choose an answer for each question, then check your score.", "quiz_submit":"Check my score", "quiz_reset":"Reset quiz", "score":"Your score", "quiz_feedback":"Read the explanations and try again to improve.",
 "smart_title":"Tell CyberSaathi what is happening", "smart_hint":"Use simple words. Do not enter passwords, OTPs, bank details or private photos.", "smart_analyse":"Show my next steps", "smart_result":"Possible warning signs", "not_diagnosis":"This tool cannot confirm that you are under attack. It gives general safety guidance based on words you enter.",
 "women_intro":"If you feel scared, confused or threatened online, take one step at a time. You do not have to handle it alone.", "women_emergency":"If you are in immediate physical danger, move to a safer place if possible and call 112 or someone you trust.", "women_steps_title":"What to do, step by step", "women_steps":["1. Pause. Do not reply to threats, click links, send money or share an OTP.","2. Get to safety. If someone is threatening you, tell a trusted person and avoid meeting them alone.","3. Save evidence. Keep screenshots, profile links, phone numbers, dates, messages and payment IDs. Do not edit the originals.","4. Secure your accounts. Change passwords from a safe device, sign out other sessions and turn on two-step verification.","5. Block and report the account on the app after saving evidence. Tighten privacy settings and remove unknown followers.","6. If intimate images are used to threaten you, do not pay or send more images. Save evidence and report the account and incident.","7. If money was taken in India, contact your bank/payment app immediately and call 1930 as soon as possible.","8. Report online at the official National Cyber Crime Reporting Portal. Ask a trusted person to stay with you while you report."],
 "women_topics":["Online stalking or repeated unwanted messages","Fake profile, impersonation or account takeover","Threats, blackmail or intimate-image abuse","Dating, relationship or sextortion scam","UPI, shopping, job or financial fraud","Private account, location and device safety"],
 "women_note":"You are not to blame for someone else's abuse. If it feels unsafe, seek help from a trusted person or official service.",
 "official":"Open official cybercrime portal", "helplines":"Tap a number to call from a phone that supports calling", "back_home":"Home", "section":"Open section", "home_hint":"Use the buttons below to open each working section.",
 "analysis_words":["money","transfer","payment","upi","bank","otp","password","login","blocked","urgent","threat","blackmail","private photo","photo","video","stalking","fake profile","impersonat","hack","account","job fee","parcel","prize","police","police case","remote access","screen share","loan","investment"],
 "analysis_advice":["Do not send money, OTPs or passwords.","Do not click links or install apps sent by an unknown person.","Contact your bank or app through its official app or number if money or an account is involved.","Save screenshots and details before blocking or deleting anything.","Change compromised passwords from a trusted device and enable two-step verification.","Tell a trusted person and report through the official service if needed."]
},
"Malayalam": {
 "quiz_title":"സൈബർ സുരക്ഷാ ക്വിസ് — 15 ചോദ്യങ്ങൾ", "quiz_intro":"ഓരോ ചോദ്യത്തിനും ഉത്തരം തിരഞ്ഞെടുത്ത് അവസാനം സ്കോർ പരിശോധിക്കുക.", "quiz_submit":"എന്റെ സ്കോർ പരിശോധിക്കുക", "quiz_reset":"ക്വിസ് വീണ്ടും തുടങ്ങുക", "score":"നിങ്ങളുടെ സ്കോർ", "quiz_feedback":"വിശദീകരണങ്ങൾ വായിച്ച് വീണ്ടും ശ്രമിക്കാം.",
 "smart_title":"എന്താണ് സംഭവിക്കുന്നതെന്ന് പറയൂ", "smart_hint":"ലളിതമായി എഴുതുക. പാസ്‌വേഡ്, OTP, ബാങ്ക് വിവരങ്ങൾ അല്ലെങ്കിൽ സ്വകാര്യ ചിത്രങ്ങൾ ചേർക്കരുത്.", "smart_analyse":"അടുത്ത നടപടികൾ കാണിക്കുക", "smart_result":"ശ്രദ്ധിക്കേണ്ട സൂചനകൾ", "not_diagnosis":"നിങ്ങൾ ആക്രമണത്തിനിരയായെന്ന് ഈ ഉപകരണം ഉറപ്പിക്കാൻ കഴിയില്ല. നിങ്ങൾ എഴുതിയ വാക്കുകളെ അടിസ്ഥാനമാക്കി പൊതുവായ സുരക്ഷാ നിർദ്ദേശങ്ങൾ നൽകുന്നു.",
 "women_intro":"ഓൺലൈനിൽ പേടിയോ ആശയക്കുഴപ്പമോ ഭീഷണിയോ തോന്നിയാൽ ഓരോ ഘട്ടമായി മുന്നോട്ട് പോകുക. നിങ്ങൾ ഒറ്റയ്ക്കല്ല.", "women_emergency":"ഉടൻ ശാരീരിക അപകടമുണ്ടെങ്കിൽ കഴിയുമെങ്കിൽ സുരക്ഷിത സ്ഥലത്തേക്ക് മാറി 112-ലോ വിശ്വസിക്കുന്ന ഒരാളെയോ വിളിക്കുക.", "women_steps_title":"ഘട്ടം ഘട്ടമായി ചെയ്യേണ്ടത്", "women_steps":["1. നിർത്തി ചിന്തിക്കുക. ഭീഷണിക്ക് മറുപടി നൽകരുത്; ലിങ്ക് തുറക്കരുത്; പണമോ OTP-യോ പങ്കിടരുത്.","2. സുരക്ഷ ഉറപ്പാക്കുക. ആരെങ്കിലും ഭീഷണിപ്പെടുത്തിയാൽ വിശ്വസിക്കുന്ന ഒരാളോട് പറയുക; ഒറ്റയ്ക്ക് കാണാൻ പോകരുത്.","3. തെളിവുകൾ സൂക്ഷിക്കുക. സ്ക്രീൻഷോട്ടുകൾ, പ്രൊഫൈൽ ലിങ്കുകൾ, നമ്പറുകൾ, തീയതി, സന്ദേശങ്ങൾ, പേയ്‌മെന്റ് ID എന്നിവ സൂക്ഷിക്കുക.","4. അക്കൗണ്ടുകൾ സുരക്ഷിതമാക്കുക. സുരക്ഷിത ഉപകരണത്തിൽ നിന്ന് പാസ്‌വേഡ് മാറ്റി മറ്റ് സെഷനുകളിൽ നിന്ന് ലോഗ് ഔട്ട് ചെയ്ത് രണ്ട് ഘട്ട പരിശോധന ഓൺ ചെയ്യുക.","5. തെളിവുകൾ സൂക്ഷിച്ച ശേഷം ആപ്പിൽ അക്കൗണ്ട് ബ്ലോക്ക് ചെയ്ത് റിപ്പോർട്ട് ചെയ്യുക. സ്വകാര്യതാ ക്രമീകരണങ്ങൾ പരിശോധിക്കുക.","6. സ്വകാര്യ ചിത്രങ്ങൾ ഉപയോഗിച്ച് ഭീഷണിപ്പെടുത്തിയാൽ പണം നൽകരുത്, കൂടുതൽ ചിത്രങ്ങൾ അയക്കരുത്. തെളിവ് സൂക്ഷിച്ച് റിപ്പോർട്ട് ചെയ്യുക.","7. ഇന്ത്യയിൽ പണം നഷ്ടപ്പെട്ടാൽ ഉടൻ ബാങ്കിനെയോ പേയ്‌മെന്റ് ആപ്പിനെയോ ബന്ധപ്പെടുകയും 1930-ൽ വിളിക്കുകയും ചെയ്യുക.","8. ഔദ്യോഗിക National Cyber Crime Reporting Portal വഴി റിപ്പോർട്ട് ചെയ്യുക. വിശ്വസിക്കുന്ന ഒരാളുടെ സഹായം തേടുക."],
 "women_topics":["ഓൺലൈൻ പിന്തുടരൽ അല്ലെങ്കിൽ ആവർത്തിച്ചുള്ള അനാവശ്യ സന്ദേശങ്ങൾ","വ്യാജ പ്രൊഫൈൽ അല്ലെങ്കിൽ അക്കൗണ്ട് കൈയേറ്റം","ഭീഷണി, ബ്ലാക്ക്മെയിൽ അല്ലെങ്കിൽ സ്വകാര്യ ചിത്രങ്ങളുടെ ദുരുപയോഗം","ബന്ധം/ഡേറ്റിംഗ് തട്ടിപ്പ്","UPI, ഷോപ്പിംഗ്, ജോലി അല്ലെങ്കിൽ സാമ്പത്തിക തട്ടിപ്പ്","സ്വകാര്യത, ലൊക്കേഷൻ, ഉപകരണ സുരക്ഷ"], "women_note":"മറ്റൊരാളുടെ ദുരുപയോഗത്തിന് നിങ്ങൾ കുറ്റക്കാരിയല്ല. വിശ്വസിക്കുന്ന ഒരാളുടെയോ ഔദ്യോഗിക സേവനത്തിന്റെയോ സഹായം തേടുക.",
 "official":"ഔദ്യോഗിക സൈബർ കുറ്റകൃത്യ പോർട്ടൽ തുറക്കുക", "helplines":"വിളിക്കാൻ കഴിയുന്ന ഫോണിൽ നമ്പറിൽ അമർത്തുക", "back_home":"ഹോം", "section":"വിഭാഗം തുറക്കുക", "home_hint":"പ്രവർത്തിക്കുന്ന വിഭാഗങ്ങൾ തുറക്കാൻ താഴെയുള്ള ബട്ടണുകൾ ഉപയോഗിക്കുക.",
 "analysis_words":["പണം","ട്രാൻസ്ഫർ","പേയ്മെന്റ്","യുപിഐ","ബാങ്ക്","ഒടിപി","പാസ്‌വേഡ്","ലോഗിൻ","ബ്ലോക്ക്","അടിയന്തരം","ഭീഷണി","ബ്ലാക്ക്മെയിൽ","സ്വകാര്യ ചിത്രം","ചിത്രം","വീഡിയോ","പിന്തുടരൽ","വ്യാജ പ്രൊഫൈൽ","ഹാക്ക്","അക്കൗണ്ട്","ജോലി ഫീസ്","പാർസൽ","സമ്മാനം","പോലീസ്","റിമോട്ട് ആക്സസ്","സ്ക്രീൻ ഷെയർ","ലോൺ","നിക്ഷേപം"],
 "analysis_advice":["പണം, OTP, പാസ്‌വേഡ് എന്നിവ അയക്കരുത്.","അപരിചിതർ അയക്കുന്ന ലിങ്ക് തുറക്കുകയോ ആപ്പ് ഇൻസ്റ്റാൾ ചെയ്യുകയോ അരുത്.","പണമോ അക്കൗണ്ടോ ബന്ധപ്പെട്ടാൽ ഔദ്യോഗിക ആപ്പ്/നമ്പർ വഴി ബാങ്കിനെ ബന്ധപ്പെടുക.","ബ്ലോക്ക് ചെയ്യുന്നതിന് മുമ്പ് സ്ക്രീൻഷോട്ടുകളും വിവരങ്ങളും സൂക്ഷിക്കുക.","സുരക്ഷിത ഉപകരണത്തിൽ നിന്ന് പാസ്‌വേഡ് മാറ്റി രണ്ട് ഘട്ട പരിശോധന ഓൺ ചെയ്യുക.","വിശ്വസിക്കുന്ന ഒരാളോട് പറയുകയും ആവശ്യമെങ്കിൽ ഔദ്യോഗികമായി റിപ്പോർട്ട് ചെയ്യുകയും ചെയ്യുക."]
},
"Hindi": {
 "quiz_title":"साइबर सुरक्षा क्विज़ — 15 सवाल", "quiz_intro":"हर सवाल का जवाब चुनें और अंत में अपना स्कोर देखें।", "quiz_submit":"मेरा स्कोर देखें", "quiz_reset":"क्विज़ फिर से शुरू करें", "score":"आपका स्कोर", "quiz_feedback":"समझाइश पढ़ें और बेहतर करने के लिए फिर कोशिश करें।",
 "smart_title":"बताएँ कि आपके साथ क्या हो रहा है", "smart_hint":"आसान शब्दों में लिखें। पासवर्ड, OTP, बैंक जानकारी या निजी तस्वीरें न लिखें।", "smart_analyse":"अगले कदम दिखाएँ", "smart_result":"संभावित चेतावनी संकेत", "not_diagnosis":"यह टूल पक्का नहीं बता सकता कि आप पर साइबर हमला हुआ है। यह लिखे गए शब्दों के आधार पर सामान्य सुरक्षा सलाह देता है।",
 "women_intro":"ऑनलाइन डर, उलझन या धमकी महसूस हो तो एक-एक कदम उठाएँ। आपको अकेले इससे निपटने की ज़रूरत नहीं है।", "women_emergency":"अगर तुरंत शारीरिक खतरा है, तो संभव हो तो सुरक्षित जगह जाएँ और 112 या किसी भरोसेमंद व्यक्ति को कॉल करें।", "women_steps_title":"कदम-दर-कदम क्या करें", "women_steps":["1. रुकें। धमकी का जवाब न दें, लिंक न खोलें और पैसे या OTP साझा न करें।","2. सुरक्षित रहें। धमकी मिलने पर भरोसेमंद व्यक्ति को बताएँ और अकेले मिलने न जाएँ।","3. सबूत बचाएँ: स्क्रीनशॉट, प्रोफ़ाइल लिंक, नंबर, तारीख, संदेश और भुगतान ID सुरक्षित रखें।","4. सुरक्षित डिवाइस से पासवर्ड बदलें, अन्य सेशन लॉगआउट करें और दो-चरण सत्यापन चालू करें।","5. सबूत बचाने के बाद ऐप पर अकाउंट ब्लॉक और रिपोर्ट करें। प्राइवेसी सेटिंग्स जाँचें।","6. निजी तस्वीरों से ब्लैकमेल हो तो पैसे न दें और और तस्वीरें न भेजें। सबूत बचाकर रिपोर्ट करें।","7. भारत में पैसे चले गए हों तो तुरंत बैंक/पेमेंट ऐप से संपर्क करें और 1930 पर कॉल करें।","8. आधिकारिक National Cyber Crime Reporting Portal पर रिपोर्ट करें और भरोसेमंद व्यक्ति की मदद लें।"],
 "women_topics":["ऑनलाइन पीछा करना या बार-बार परेशान करने वाले संदेश","फर्जी प्रोफ़ाइल या अकाउंट पर कब्ज़ा","धमकी, ब्लैकमेल या निजी तस्वीरों का दुरुपयोग","डेटिंग या रिश्ते से जुड़ा धोखा","UPI, खरीदारी, नौकरी या वित्तीय धोखाधड़ी","प्राइवेसी, लोकेशन और डिवाइस सुरक्षा"], "women_note":"दूसरे व्यक्ति के दुर्व्यवहार के लिए आप दोषी नहीं हैं। भरोसेमंद व्यक्ति या आधिकारिक सेवा से मदद लें।",
 "official":"आधिकारिक साइबर अपराध पोर्टल खोलें", "helplines":"कॉल करने वाले फोन पर नंबर दबाएँ", "back_home":"होम", "section":"सेक्शन खोलें", "home_hint":"काम करने वाले सेक्शन खोलने के लिए नीचे दिए बटन दबाएँ।",
 "analysis_words":["पैसा","ट्रांसफर","पेमेंट","यूपीआई","बैंक","ओटीपी","पासवर्ड","लॉगिन","ब्लॉक","तुरंत","धमकी","ब्लैकमेल","निजी फोटो","फोटो","वीडियो","पीछा","फर्जी प्रोफाइल","हैक","अकाउंट","नौकरी शुल्क","पार्सल","इनाम","पुलिस","रिमोट एक्सेस","स्क्रीन शेयर","लोन","निवेश"],
 "analysis_advice":["पैसे, OTP या पासवर्ड न भेजें।","अनजान व्यक्ति के लिंक न खोलें और ऐप इंस्टॉल न करें।","पैसे या अकाउंट का मामला हो तो बैंक से आधिकारिक ऐप/नंबर पर संपर्क करें।","ब्लॉक या डिलीट करने से पहले स्क्रीनशॉट और जानकारी बचाएँ।","सुरक्षित डिवाइस से पासवर्ड बदलें और दो-चरण सत्यापन चालू करें।","भरोसेमंद व्यक्ति को बताएँ और ज़रूरत हो तो आधिकारिक रिपोर्ट करें।"]
},
"Tamil": {
 "quiz_title":"சைபர் பாதுகாப்பு வினாடி வினா — 15 கேள்விகள்", "quiz_intro":"ஒவ்வொரு கேள்விக்கும் பதிலைத் தேர்ந்தெடுத்து இறுதியில் மதிப்பெண்ணைப் பாருங்கள்.", "quiz_submit":"என் மதிப்பெண்ணைப் பார்க்க", "quiz_reset":"மீண்டும் தொடங்கு", "score":"உங்கள் மதிப்பெண்", "quiz_feedback":"விளக்கங்களைப் படித்து மீண்டும் முயற்சிக்கவும்.",
 "smart_title":"உங்களுக்கு என்ன நடக்கிறது என்று சொல்லுங்கள்", "smart_hint":"எளிய வார்த்தைகளில் எழுதுங்கள். கடவுச்சொல், OTP, வங்கி விவரம் அல்லது தனிப்பட்ட படங்களைச் சேர்க்க வேண்டாம்.", "smart_analyse":"அடுத்த படிகளைக் காட்டு", "smart_result":"கவனிக்க வேண்டிய அறிகுறிகள்", "not_diagnosis":"நீங்கள் தாக்குதலுக்கு உள்ளாகியுள்ளீர்கள் என்று இந்த கருவி உறுதிப்படுத்த முடியாது. இது பொதுவான பாதுகாப்பு ஆலோசனைகளை வழங்குகிறது.",
 "women_intro":"இணையத்தில் பயம், குழப்பம் அல்லது மிரட்டல் ஏற்பட்டால் ஒவ்வொரு படியாகச் செயல்படுங்கள். நீங்கள் தனியாக இல்லை.", "women_emergency":"உடனடி உடல் ஆபத்து இருந்தால் பாதுகாப்பான இடத்திற்குச் சென்று 112 அல்லது நம்பகமான ஒருவரை அழைக்கவும்.", "women_steps_title":"படிப்படியாக என்ன செய்ய வேண்டும்", "women_steps":["1. நிறுத்துங்கள். மிரட்டலுக்கு பதிலளிக்காதீர்கள்; இணைப்பைத் திறக்காதீர்கள்; பணம் அல்லது OTP பகிராதீர்கள்.","2. பாதுகாப்பாக இருங்கள். மிரட்டல் இருந்தால் நம்பகமான ஒருவரிடம் சொல்லுங்கள்; தனியாகச் சந்திக்க வேண்டாம்.","3. ஆதாரங்களைச் சேமிக்கவும்: திரைப்பிடிப்புகள், சுயவிவர இணைப்புகள், எண்கள், தேதிகள், செய்திகள், பரிவர்த்தனை ID.","4. பாதுகாப்பான சாதனத்தில் கடவுச்சொல்லை மாற்றி மற்ற அமர்வுகளிலிருந்து வெளியேறி இரு-படி சரிபார்ப்பை இயக்கவும்.","5. ஆதாரங்களைச் சேமித்த பின் செயலியில் கணக்கைத் தடுத்து புகாரளிக்கவும். தனியுரிமை அமைப்புகளைச் சரிபார்க்கவும்.","6. தனிப்பட்ட படங்களால் மிரட்டினால் பணம் கொடுக்கவோ மேலும் படங்களை அனுப்பவோ வேண்டாம். ஆதாரங்களைச் சேமித்து புகாரளிக்கவும்.","7. இந்தியாவில் பணம் இழந்தால் உடனே வங்கி/பணம் செலுத்தும் செயலியைத் தொடர்புகொண்டு 1930 அழைக்கவும்.","8. அதிகாரப்பூர்வ National Cyber Crime Reporting Portal-ல் புகாரளித்து நம்பகமானவரின் உதவியைப் பெறவும்."],
 "women_topics":["இணையத்தில் பின்தொடர்தல் அல்லது தொந்தரவு செய்திகள்","போலி சுயவிவரம் அல்லது கணக்கு கைப்பற்றல்","மிரட்டல், பிளாக்மெயில் அல்லது தனிப்பட்ட படங்களின் தவறான பயன்பாடு","டேட்டிங் அல்லது உறவு மோசடி","UPI, ஷாப்பிங், வேலை அல்லது பண மோசடி","தனியுரிமை, இருப்பிடம் மற்றும் சாதன பாதுகாப்பு"], "women_note":"மற்றொருவரின் துன்புறுத்தலுக்கு நீங்கள் காரணமல்ல. நம்பகமானவர் அல்லது அதிகாரப்பூர்வ சேவையிடம் உதவி கேளுங்கள்.",
 "official":"அதிகாரப்பூர்வ சைபர் குற்ற இணையதளத்தைத் திறக்கவும்", "helplines":"அழைக்கக்கூடிய தொலைபேசியில் எண்ணைத் தொடவும்", "back_home":"முகப்பு", "section":"பகுதியைத் திறக்கவும்", "home_hint":"செயல்படும் பகுதிகளைத் திறக்க கீழே உள்ள பொத்தான்களைப் பயன்படுத்தவும்.",
 "analysis_words":["பணம்","பரிமாற்றம்","கட்டணம்","upi","வங்கி","otp","கடவுச்சொல்","உள்நுழைவு","தடுக்கப்படும்","அவசரம்","மிரட்டல்","பிளாக்மெயில்","தனிப்பட்ட படம்","படம்","வீடியோ","பின்தொடர்தல்","போலி சுயவிவரம்","ஹேக்","கணக்கு","வேலை கட்டணம்","பார்சல்","பரிசு","காவல்","ரிமோட் அணுகல்","திரை பகிர்வு","கடன்","முதலீடு"],
 "analysis_advice":["பணம், OTP அல்லது கடவுச்சொல்லை அனுப்பாதீர்கள்.","அறியாதவர்கள் அனுப்பும் இணைப்புகளைத் திறக்கவோ செயலிகளை நிறுவவோ வேண்டாம்.","பணம் அல்லது கணக்கு தொடர்பானால் அதிகாரப்பூர்வ செயலி/எண் மூலம் வங்கியைத் தொடர்புகொள்ளுங்கள்.","தடுப்பதற்கு அல்லது நீக்குவதற்கு முன் திரைப்பிடிப்புகளையும் விவரங்களையும் சேமிக்கவும்.","பாதுகாப்பான சாதனத்தில் கடவுச்சொல்லை மாற்றி இரு-படி சரிபார்ப்பை இயக்கவும்.","நம்பகமானவரிடம் சொல்லி தேவையானால் அதிகாரப்பூர்வமாக புகாரளிக்கவும்."]
},
"Kannada": {
 "quiz_title":"ಸೈಬರ್ ಸುರಕ್ಷತಾ ರಸಪ್ರಶ್ನೆ — 15 ಪ್ರಶ್ನೆಗಳು", "quiz_intro":"ಪ್ರತಿ ಪ್ರಶ್ನೆಗೆ ಉತ್ತರ ಆಯ್ಕೆಮಾಡಿ, ಕೊನೆಯಲ್ಲಿ ನಿಮ್ಮ ಅಂಕಗಳನ್ನು ನೋಡಿ.", "quiz_submit":"ನನ್ನ ಅಂಕಗಳನ್ನು ಪರಿಶೀಲಿಸಿ", "quiz_reset":"ಮತ್ತೆ ಪ್ರಾರಂಭಿಸಿ", "score":"ನಿಮ್ಮ ಅಂಕಗಳು", "quiz_feedback":"ವಿವರಣೆಗಳನ್ನು ಓದಿ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
 "smart_title":"ನಿಮಗೆ ಏನಾಗುತ್ತಿದೆ ಎಂದು ತಿಳಿಸಿ", "smart_hint":"ಸರಳ ಪದಗಳಲ್ಲಿ ಬರೆಯಿರಿ. ಪಾಸ್‌ವರ್ಡ್, OTP, ಬ್ಯಾಂಕ್ ವಿವರ ಅಥವಾ ಖಾಸಗಿ ಚಿತ್ರಗಳನ್ನು ಸೇರಿಸಬೇಡಿ.", "smart_analyse":"ಮುಂದಿನ ಕ್ರಮಗಳನ್ನು ತೋರಿಸಿ", "smart_result":"ಗಮನಿಸಬೇಕಾದ ಎಚ್ಚರಿಕೆಗಳು", "not_diagnosis":"ನೀವು ದಾಳಿಗೆ ಒಳಗಾಗಿದ್ದೀರಿ ಎಂದು ಈ ಸಾಧನ ಖಚಿತಪಡಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ. ಇದು ಸಾಮಾನ್ಯ ಸುರಕ್ಷತಾ ಸಲಹೆ ನೀಡುತ್ತದೆ.",
 "women_intro":"ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಭಯ, ಗೊಂದಲ ಅಥವಾ ಬೆದರಿಕೆ ಎದುರಾದರೆ ಒಂದೊಂದು ಹಂತವಾಗಿ ಮುಂದುವರಿಯಿರಿ. ನೀವು ಒಬ್ಬರಲ್ಲ.", "women_emergency":"ತಕ್ಷಣದ ದೈಹಿಕ ಅಪಾಯವಿದ್ದರೆ ಸುರಕ್ಷಿತ ಸ್ಥಳಕ್ಕೆ ತೆರಳಿ 112 ಅಥವಾ ನಂಬಿಕೆಯ ವ್ಯಕ್ತಿಗೆ ಕರೆ ಮಾಡಿ.", "women_steps_title":"ಹಂತ ಹಂತವಾಗಿ ಏನು ಮಾಡಬೇಕು", "women_steps":["1. ನಿಲ್ಲಿಸಿ. ಬೆದರಿಕೆಗೆ ಉತ್ತರಿಸಬೇಡಿ; ಲಿಂಕ್ ತೆರೆಯಬೇಡಿ; ಹಣ ಅಥವಾ OTP ಹಂಚಬೇಡಿ.","2. ಸುರಕ್ಷಿತವಾಗಿರಿ. ಬೆದರಿಕೆ ಇದ್ದರೆ ನಂಬಿಕೆಯ ವ್ಯಕ್ತಿಗೆ ತಿಳಿಸಿ; ಒಬ್ಬರೇ ಭೇಟಿಯಾಗಬೇಡಿ.","3. ಸಾಕ್ಷ್ಯ ಉಳಿಸಿ: ಸ್ಕ್ರೀನ್‌ಶಾಟ್, ಪ್ರೊಫೈಲ್ ಲಿಂಕ್, ಫೋನ್ ಸಂಖ್ಯೆ, ದಿನಾಂಕ, ಸಂದೇಶ ಮತ್ತು ಪಾವತಿ ID.","4. ಸುರಕ್ಷಿತ ಸಾಧನದಿಂದ ಪಾಸ್‌ವರ್ಡ್ ಬದಲಿಸಿ, ಇತರ ಸೆಷನ್‌ಗಳಿಂದ ಲಾಗ್ ಔಟ್ ಮಾಡಿ, ಎರಡು ಹಂತದ ಪರಿಶೀಲನೆ ಆನ್ ಮಾಡಿ.","5. ಸಾಕ್ಷ್ಯ ಉಳಿಸಿದ ನಂತರ ಆ್ಯಪ್‌ನಲ್ಲಿ ಖಾತೆಯನ್ನು ಬ್ಲಾಕ್ ಮಾಡಿ ವರದಿ ಮಾಡಿ. ಗೌಪ್ಯತಾ ಸೆಟ್ಟಿಂಗ್ ಪರಿಶೀಲಿಸಿ.","6. ಖಾಸಗಿ ಚಿತ್ರಗಳಿಂದ ಬೆದರಿಸಿದರೆ ಹಣ ಕೊಡಬೇಡಿ ಅಥವಾ ಇನ್ನಷ್ಟು ಚಿತ್ರ ಕಳುಹಿಸಬೇಡಿ. ಸಾಕ್ಷ್ಯ ಉಳಿಸಿ ವರದಿ ಮಾಡಿ.","7. ಭಾರತದಲ್ಲಿ ಹಣ ಕಳೆದುಕೊಂಡರೆ ತಕ್ಷಣ ಬ್ಯಾಂಕ್/ಪಾವತಿ ಆ್ಯಪ್ ಸಂಪರ್ಕಿಸಿ ಮತ್ತು 1930 ಕರೆ ಮಾಡಿ.","8. ಅಧಿಕೃತ National Cyber Crime Reporting Portal ನಲ್ಲಿ ವರದಿ ಮಾಡಿ; ನಂಬಿಕೆಯ ವ್ಯಕ್ತಿಯ ಸಹಾಯ ಪಡೆಯಿರಿ."],
 "women_topics":["ಆನ್‌ಲೈನ್ ಹಿಂಬಾಲಿಕೆ ಅಥವಾ ಕಿರುಕುಳ ಸಂದೇಶಗಳು","ನಕಲಿ ಪ್ರೊಫೈಲ್ ಅಥವಾ ಖಾತೆ ಕಬಳಿಕೆ","ಬೆದರಿಕೆ, ಬ್ಲ್ಯಾಕ್‌ಮೇಲ್ ಅಥವಾ ಖಾಸಗಿ ಚಿತ್ರಗಳ ದುರುಪಯೋಗ","ಡೇಟಿಂಗ್ ಅಥವಾ ಸಂಬಂಧದ ವಂಚನೆ","UPI, ಶಾಪಿಂಗ್, ಉದ್ಯೋಗ ಅಥವಾ ಹಣಕಾಸು ವಂಚನೆ","ಗೌಪ್ಯತೆ, ಸ್ಥಳ ಮತ್ತು ಸಾಧನ ಸುರಕ್ಷತೆ"], "women_note":"ಇತರರ ದುರುಪಯೋಗಕ್ಕೆ ನೀವು ಕಾರಣರಲ್ಲ. ನಂಬಿಕೆಯ ವ್ಯಕ್ತಿ ಅಥವಾ ಅಧಿಕೃತ ಸೇವೆಯಿಂದ ಸಹಾಯ ಪಡೆಯಿರಿ.",
 "official":"ಅಧಿಕೃತ ಸೈಬರ್ ಅಪರಾಧ ಪೋರ್ಟಲ್ ತೆರೆಯಿರಿ", "helplines":"ಕರೆ ಮಾಡಲು ಸಾಧ್ಯವಾದ ಫೋನ್‌ನಲ್ಲಿ ಸಂಖ್ಯೆಯನ್ನು ಒತ್ತಿ", "back_home":"ಮುಖಪುಟ", "section":"ವಿಭಾಗ ತೆರೆಯಿರಿ", "home_hint":"ಕೆಳಗಿನ ಬಟನ್‌ಗಳನ್ನು ಬಳಸಿ ವಿಭಾಗಗಳನ್ನು ತೆರೆಯಿರಿ.",
 "analysis_words":["ಹಣ","ವರ್ಗಾವಣೆ","ಪಾವತಿ","upi","ಬ್ಯಾಂಕ್","otp","ಪಾಸ್‌ವರ್ಡ್","ಲಾಗಿನ್","ಬ್ಲಾಕ್","ತುರ್ತು","ಬೆದರಿಕೆ","ಬ್ಲ್ಯಾಕ್‌ಮೇಲ್","ಖಾಸಗಿ ಚಿತ್ರ","ಚಿತ್ರ","ವೀಡಿಯೊ","ಹಿಂಬಾಲಿಕೆ","ನಕಲಿ ಪ್ರೊಫೈಲ್","ಹ್ಯಾಕ್","ಖಾತೆ","ಉದ್ಯೋಗ ಶುಲ್ಕ","ಪಾರ್ಸೆಲ್","ಬಹುಮಾನ","ಪೊಲೀಸ್","ರಿಮೋಟ್ ಪ್ರವೇಶ","ಸ್ಕ್ರೀನ್ ಹಂಚಿಕೆ","ಸಾಲ","ಹೂಡಿಕೆ"],
 "analysis_advice":["ಹಣ, OTP ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್ ಕಳುಹಿಸಬೇಡಿ.","ಅಪರಿಚಿತರು ಕಳುಹಿಸಿದ ಲಿಂಕ್ ತೆರೆಯಬೇಡಿ ಅಥವಾ ಆ್ಯಪ್ ಸ್ಥಾಪಿಸಬೇಡಿ.","ಹಣ ಅಥವಾ ಖಾತೆಗೆ ಸಂಬಂಧಿಸಿದರೆ ಅಧಿಕೃತ ಆ್ಯಪ್/ಸಂಖ್ಯೆಯಿಂದ ಬ್ಯಾಂಕ್ ಸಂಪರ್ಕಿಸಿ.","ಬ್ಲಾಕ್ ಅಥವಾ ಅಳಿಸುವ ಮೊದಲು ಸ್ಕ್ರೀನ್‌ಶಾಟ್ ಮತ್ತು ವಿವರ ಉಳಿಸಿ.","ಸುರಕ್ಷಿತ ಸಾಧನದಿಂದ ಪಾಸ್‌ವರ್ಡ್ ಬದಲಿಸಿ ಮತ್ತು ಎರಡು ಹಂತದ ಪರಿಶೀಲನೆ ಆನ್ ಮಾಡಿ.","ನಂಬಿಕೆಯ ವ್ಯಕ್ತಿಗೆ ತಿಳಿಸಿ; ಅಗತ್ಯವಿದ್ದರೆ ಅಧಿಕೃತವಾಗಿ ವರದಿ ಮಾಡಿ."]
}
}

# Quiz questions are stored in English for consistent scoring; the interface and safety guidance are translated.
QUIZ = [
("A caller says your bank account will be blocked. What should you do?",["Share your OTP","Click their link","Call the bank using its official number","Give your PIN"],2,"Banks do not need you to tell them your OTP or PIN."),
("Someone asks for your OTP to receive a prize. What is safest?",["Send it quickly","Never share it","Post it online","Ask them to send another link"],1,"An OTP is meant only for you."),
("A job offer asks for a registration fee before an interview. What should you do?",["Pay immediately","Check the company independently","Send ID and bank details","Borrow money to pay"],1,"Upfront fees can be a warning sign of a fake job offer."),
("A friend messages from a new number asking for urgent money. What should you do?",["Transfer immediately","Verify by calling your friend on a known number","Share your bank login","Send your card photo"],1,"Scammers may impersonate people you know."),
("You receive a parcel-fee link you were not expecting. What should you do?",["Pay the fee","Enter card details","Check the delivery company's official app","Send an OTP"],2,"Check delivery updates through an official channel."),
("What is a strong password practice?",["Use 123456","Use the same password everywhere","Use a long, unique password","Share it with a friend"],2,"Unique passwords limit damage if one account is compromised."),
("What does two-step verification do?",["Adds another sign-in check","Makes every link safe","Stops all spam","Replaces every password"],0,"It adds a layer of protection to your account."),
("A stranger asks you to install a remote-access app to fix a bank issue. What should you do?",["Install it","Give them screen access","Decline and contact the bank officially","Share your PIN"],2,"Remote access can let a scammer control or view your device."),
("You clicked a suspicious link and entered your password. What should you do first?",["Ignore it","Change the password from a trusted device and secure the account","Send the password to support","Click the link again"],1,"Change compromised credentials promptly and enable extra security."),
("Someone threatens to share your private photos unless you pay. What is safest?",["Pay and send more photos","Keep it secret forever","Save evidence, don't pay, and seek trusted/official help","Meet them alone"],2,"Do not pay or send more content; preserve evidence and report."),
("You see a social-media account pretending to be you. What should you do?",["Send it your password","Save evidence and report the fake profile","Share more personal details","Ignore all account security"],1,"Report impersonation through the platform and warn trusted contacts if needed."),
("A message says 'act now or you will be arrested' and includes a payment link. What is this?",["A reason to pay immediately","A possible pressure tactic or scam","Proof the sender is police","A safe government link"],1,"Scams often use fear and urgency to stop you thinking clearly."),
("You lost money to an online payment scam in India. What should you do?",["Wait a month","Contact your bank/payment provider and call 1930 quickly","Delete all messages","Pay a recovery agent upfront"],1,"Fast reporting may help the response. Never pay upfront recovery-fee promises."),
("Which detail should you avoid posting publicly?",["A general safety tip","Your OTP, password or full bank details","A public news link","A non-private hobby"],1,"Keep authentication codes and sensitive financial details private."),
("What should you do before trusting a surprising message from a known person?",["Verify using another known contact method","Forward it to everyone","Send money first","Share an OTP"],0,"Verify requests through a separate, trusted channel."),
]

st.set_page_config(page_title="CyberSaathi | Digital Safety", page_icon="🛡️", layout="wide", initial_sidebar_state="collapsed")
lang = st.session_state.get("language", "English")
if lang not in TEXT: lang = "English"
T = TEXT[lang]
X = EXTRA[lang]

# Translate quiz questions and options for each language.
QUIZ_TRANSLATIONS = {
"English": [],
"Malayalam": [
("ബാങ്ക് അക്കൗണ്ട് തടയും എന്ന് വിളിച്ചയാൾ പറയുന്നു. എന്ത് ചെയ്യണം?",["OTP പങ്കിടുക","ലിങ്ക് തുറക്കുക","ഔദ്യോഗിക നമ്പറിൽ ബാങ്കിനെ വിളിക്കുക","PIN നൽകുക"],"OTP അല്ലെങ്കിൽ PIN ആരോടും പറയരുത്."),
("സമ്മാനം ലഭിക്കാൻ OTP ചോദിക്കുന്നു. സുരക്ഷിതമായത് ഏത്?",["ഉടൻ അയയ്ക്കുക","ഒരിക്കലും പങ്കിടരുത്","ഓൺലൈനിൽ പോസ്റ്റ് ചെയ്യുക","മറ്റൊരു ലിങ്ക് ചോദിക്കുക"],"OTP നിങ്ങൾക്കായി മാത്രം ഉള്ളതാണ്."),
("അഭിമുഖത്തിന് മുമ്പ് ജോലി വാഗ്ദാനം രജിസ്ട്രേഷൻ ഫീസ് ചോദിക്കുന്നു. എന്ത് ചെയ്യണം?",["ഉടൻ പണം നൽകുക","കമ്പനിയെ സ്വതന്ത്രമായി പരിശോധിക്കുക","ID, ബാങ്ക് വിവരങ്ങൾ അയയ്ക്കുക","കടം വാങ്ങുക"],"മുൻകൂർ ഫീസ് വ്യാജ ജോലി വാഗ്ദാനത്തിന്റെ സൂചനയായേക്കാം."),
("പുതിയ നമ്പറിൽ നിന്ന് സുഹൃത്ത് അടിയന്തരമായി പണം ചോദിക്കുന്നു. എന്ത് ചെയ്യണം?",["ഉടൻ അയയ്ക്കുക","അറിയാവുന്ന നമ്പറിൽ വിളിച്ച് സ്ഥിരീകരിക്കുക","ബാങ്ക് ലോഗിൻ പങ്കിടുക","കാർഡ് ചിത്രം അയയ്ക്കുക"],"തട്ടിപ്പുകാർ പരിചയക്കാരായി നടിക്കാം."),
("പ്രതീക്ഷിക്കാത്ത പാർസൽ ഫീസ് ലിങ്ക് ലഭിച്ചു. എന്ത് ചെയ്യണം?",["ഫീസ് അടയ്ക്കുക","കാർഡ് വിവരങ്ങൾ നൽകുക","ഔദ്യോഗിക ഡെലിവറി ആപ്പ് പരിശോധിക്കുക","OTP അയയ്ക്കുക"],"ഔദ്യോഗിക മാർഗം വഴി ഡെലിവറി വിവരം പരിശോധിക്കുക."),
("ശക്തമായ പാസ്‌വേഡ് ശീലം ഏതാണ്?",["123456 ഉപയോഗിക്കുക","എല്ലായിടത്തും ഒരേ പാസ്‌വേഡ്","നീളമുള്ള വ്യത്യസ്ത പാസ്‌വേഡ്","സുഹൃത്തിനോട് പങ്കിടുക"],"വ്യത്യസ്ത പാസ്‌വേഡുകൾ ഒരു അക്കൗണ്ട് ചോർന്നാലുള്ള അപകടം കുറയ്ക്കും."),
("രണ്ട് ഘട്ട പരിശോധന എന്ത് ചെയ്യുന്നു?",["കൂടുതൽ ലോഗിൻ പരിശോധന ചേർക്കുന്നു","എല്ലാ ലിങ്കുകളും സുരക്ഷിതമാക്കുന്നു","സ്പാം പൂർണ്ണമായി തടയും","പാസ്‌വേഡ് വേണ്ടാതാക്കും"],"ഇത് അക്കൗണ്ടിന് അധിക സുരക്ഷ നൽകുന്നു."),
("ബാങ്ക് പ്രശ്നം പരിഹരിക്കാൻ അപരിചിതൻ റിമോട്ട് ആപ്പ് ഇൻസ്റ്റാൾ ചെയ്യാൻ പറയുന്നു. എന്ത് ചെയ്യണം?",["ഇൻസ്റ്റാൾ ചെയ്യുക","സ്ക്രീൻ ആക്സസ് നൽകുക","നിരസിച്ച് ബാങ്കിനെ ഔദ്യോഗികമായി ബന്ധപ്പെടുക","PIN പങ്കിടുക"],"റിമോട്ട് ആക്സസ് വഴി മറ്റൊരാൾക്ക് നിങ്ങളുടെ ഉപകരണം കാണാനോ നിയന്ത്രിക്കാനോ കഴിയും."),
("സംശയാസ്പദ ലിങ്കിൽ പാസ്‌വേഡ് നൽകി. ആദ്യം എന്ത് ചെയ്യണം?",["അവഗണിക്കുക","സുരക്ഷിത ഉപകരണത്തിൽ നിന്ന് പാസ്‌വേഡ് മാറ്റുക","സപ്പോർട്ടിന് പാസ്‌വേഡ് അയയ്ക്കുക","ലിങ്ക് വീണ്ടും തുറക്കുക"],"ചോർന്ന പാസ്‌വേഡ് ഉടൻ മാറ്റി അധിക സുരക്ഷ ഓൺ ചെയ്യുക."),
("സ്വകാര്യ ചിത്രങ്ങൾ പങ്കിടുമെന്ന് പറഞ്ഞ് പണം ആവശ്യപ്പെടുന്നു. സുരക്ഷിതമായത്?",["പണം നൽകി കൂടുതൽ ചിത്രങ്ങൾ അയയ്ക്കുക","ഒരിക്കലും പറയരുത്","തെളിവ് സൂക്ഷിച്ച് സഹായം തേടുക; പണം നൽകരുത്","ഒറ്റയ്ക്ക് കാണുക"],"പണം നൽകരുത്; തെളിവുകൾ സൂക്ഷിച്ച് റിപ്പോർട്ട് ചെയ്യുക."),
("നിങ്ങളായി നടിക്കുന്ന സോഷ്യൽ മീഡിയ അക്കൗണ്ട് കണ്ടു. എന്ത് ചെയ്യണം?",["പാസ്‌വേഡ് അയയ്ക്കുക","തെളിവ് സൂക്ഷിച്ച് വ്യാജ അക്കൗണ്ട് റിപ്പോർട്ട് ചെയ്യുക","കൂടുതൽ വിവരങ്ങൾ നൽകുക","സുരക്ഷ അവഗണിക്കുക"],"പ്ലാറ്റ്ഫോമിൽ വ്യാജ അക്കൗണ്ട് റിപ്പോർട്ട് ചെയ്യുക."),
("'ഇപ്പോൾ പണം നൽകുക, അല്ലെങ്കിൽ അറസ്റ്റ് ചെയ്യും' എന്ന സന്ദേശം ലഭിച്ചു. ഇത് എന്തായിരിക്കാം?",["ഉടൻ പണം നൽകാനുള്ള കാരണം","ഭയപ്പെടുത്തുന്ന തട്ടിപ്പ് സൂചന","അയച്ചയാൾ പോലീസ് ആണെന്ന തെളിവ്","സുരക്ഷിത സർക്കാർ ലിങ്ക്"],"തട്ടിപ്പുകാർ ചിന്തിക്കാൻ സമയം നൽകാതിരിക്കാൻ ഭയം ഉപയോഗിക്കും."),
("ഇന്ത്യയിൽ ഓൺലൈൻ പേയ്‌മെന്റ് തട്ടിപ്പിൽ പണം നഷ്ടപ്പെട്ടു. എന്ത് ചെയ്യണം?",["ഒരു മാസം കാത്തിരിക്കുക","ബാങ്കിനെ ഉടൻ ബന്ധപ്പെടുകയും 1930 വിളിക്കുകയും ചെയ്യുക","എല്ലാ സന്ദേശങ്ങളും ഇല്ലാതാക്കുക","മുൻകൂർ ഫീസ് നൽകുക"],"വേഗത്തിൽ റിപ്പോർട്ട് ചെയ്യുക; പണം തിരികെ തരാമെന്ന് പറയുന്നവർക്ക് മുൻകൂർ പണം നൽകരുത്."),
("പൊതുവായി പോസ്റ്റ് ചെയ്യരുതാത്തത് ഏത്?",["സാധാരണ സുരക്ഷാ നിർദ്ദേശം","OTP, പാസ്‌വേഡ്, ബാങ്ക് വിവരങ്ങൾ","പൊതു വാർത്താ ലിങ്ക്","സ്വകാര്യതയില്ലാത്ത ഹോബി"],"രഹസ്യ കോഡുകളും സാമ്പത്തിക വിവരങ്ങളും സ്വകാര്യമായി സൂക്ഷിക്കുക."),
("പരിചയമുള്ള ഒരാളിൽ നിന്ന് വിചിത്രമായ സന്ദേശം ലഭിച്ചാൽ എന്ത് ചെയ്യണം?",["മറ്റൊരു അറിയാവുന്ന മാർഗത്തിൽ സ്ഥിരീകരിക്കുക","എല്ലാവർക്കും അയയ്ക്കുക","ആദ്യം പണം അയയ്ക്കുക","OTP പങ്കിടുക"],"വിശ്വസനീയമായ വേറൊരു മാർഗം ഉപയോഗിച്ച് സ്ഥിരീകരിക്കുക.")],
"Hindi": [
("कोई कहता है कि आपका बैंक खाता बंद हो जाएगा। क्या करें?",["OTP बताएँ","लिंक खोलें","बैंक के आधिकारिक नंबर पर कॉल करें","PIN दें"],"बैंक को अपना OTP या PIN न बताएँ."),
("इनाम पाने के लिए कोई OTP माँगता है। सुरक्षित कदम क्या है?",["तुरंत भेजें","कभी साझा न करें","ऑनलाइन पोस्ट करें","दूसरा लिंक माँगें"],"OTP केवल आपके लिए होता है."),
("नौकरी के लिए इंटरव्यू से पहले रजिस्ट्रेशन फीस माँगी जाती है। क्या करें?",["तुरंत भुगतान करें","कंपनी की स्वतंत्र जाँच करें","ID और बैंक जानकारी भेजें","उधार लें"],"पहले पैसे माँगना नकली नौकरी का संकेत हो सकता है."),
("नए नंबर से दोस्त तुरंत पैसे माँगता है। क्या करें?",["तुरंत भेजें","पहचाने हुए नंबर पर कॉल करके पुष्टि करें","बैंक लॉगिन दें","कार्ड की फोटो भेजें"],"धोखेबाज़ आपके जानने वालों का रूप ले सकते हैं."),
("अनजान पार्सल-फीस लिंक आया। क्या करें?",["फीस भरें","कार्ड जानकारी दें","डिलीवरी कंपनी के आधिकारिक ऐप में जाँचें","OTP भेजें"],"आधिकारिक माध्यम से डिलीवरी की जानकारी जाँचें."),
("मज़बूत पासवर्ड की अच्छी आदत क्या है?",["123456 रखें","हर जगह वही पासवर्ड","लंबा और अलग पासवर्ड रखें","दोस्त को बताएँ"],"अलग पासवर्ड से एक अकाउंट की समस्या दूसरे तक कम फैलती है."),
("दो-चरण सत्यापन क्या करता है?",["लॉगिन में एक अतिरिक्त जाँच जोड़ता है","हर लिंक सुरक्षित बनाता है","सारा स्पैम रोकता है","पासवर्ड की ज़रूरत हटाता है"],"यह अकाउंट को सुरक्षा की एक अतिरिक्त परत देता है."),
("कोई बैंक समस्या ठीक करने के लिए रिमोट ऐप इंस्टॉल करने को कहता है। क्या करें?",["इंस्टॉल करें","स्क्रीन एक्सेस दें","मना करें और बैंक से आधिकारिक रूप से संपर्क करें","PIN बताएँ"],"रिमोट एक्सेस से कोई आपका डिवाइस देख या नियंत्रित कर सकता है."),
("संदिग्ध लिंक पर पासवर्ड डाल दिया। पहले क्या करें?",["अनदेखा करें","सुरक्षित डिवाइस से पासवर्ड बदलें","सपोर्ट को पासवर्ड भेजें","लिंक फिर खोलें"],"पासवर्ड तुरंत बदलें और अतिरिक्त सुरक्षा चालू करें."),
("निजी तस्वीरें साझा करने की धमकी देकर पैसे माँगे जाते हैं। क्या करें?",["पैसे दें और और तस्वीरें भेजें","किसी को न बताएँ","सबूत बचाएँ, मदद लें और पैसे न दें","अकेले मिलने जाएँ"],"पैसे न दें; सबूत सुरक्षित रखकर रिपोर्ट करें."),
("कोई सोशल मीडिया पर आपकी नकली प्रोफ़ाइल बनाता है। क्या करें?",["पासवर्ड भेजें","सबूत बचाकर नकली प्रोफ़ाइल रिपोर्ट करें","और जानकारी दें","सुरक्षा छोड़ दें"],"प्लेटफ़ॉर्म पर नकली प्रोफ़ाइल रिपोर्ट करें."),
("'अभी भुगतान करें वरना गिरफ्तार होंगे' संदेश क्या हो सकता है?",["तुरंत भुगतान का कारण","डराकर ठगने की कोशिश","पुलिस होने का प्रमाण","सरकारी सुरक्षित लिंक"],"ठग जल्दबाज़ी और डर का इस्तेमाल करते हैं."),
("भारत में ऑनलाइन पेमेंट धोखाधड़ी से पैसे गए। क्या करें?",["एक महीने प्रतीक्षा करें","बैंक/पेमेंट ऐप से तुरंत संपर्क करें और 1930 कॉल करें","संदेश मिटाएँ","रिकवरी एजेंट को पहले पैसे दें"],"जल्दी रिपोर्ट करें; पैसे वापस दिलाने के नाम पर अग्रिम फीस न दें."),
("कौन-सी जानकारी सार्वजनिक रूप से साझा नहीं करनी चाहिए?",["सामान्य सुरक्षा सलाह","OTP, पासवर्ड या बैंक विवरण","सार्वजनिक समाचार लिंक","गैर-निजी शौक"],"OTP और वित्तीय जानकारी निजी रखें."),
("जान-पहचान वाले से अजीब संदेश आए तो क्या करें?",["दूसरे भरोसेमंद तरीके से पुष्टि करें","सबको भेजें","पहले पैसे भेजें","OTP बताएँ"],"अलग और भरोसेमंद माध्यम से पुष्टि करें.")]
 ,
"Tamil": [
("வங்கி கணக்கு முடக்கப்படும் என்று ஒருவர் சொன்னால் என்ன செய்ய வேண்டும்?",["OTP பகிரவும்","இணைப்பைத் திறக்கவும்","வங்கியின் அதிகாரப்பூர்வ எண்ணை அழைக்கவும்","PIN கொடுக்கவும்"],"OTP அல்லது PIN யாரிடமும் சொல்ல வேண்டாம்."),
("பரிசு பெற OTP கேட்கிறார்கள். பாதுகாப்பானது எது?",["உடனே அனுப்பவும்","பகிர வேண்டாம்","ஆன்லைனில் இடவும்","மற்றொரு இணைப்பைக் கேட்கவும்"],"OTP உங்களுக்காக மட்டுமே."),
("வேலைக்கான நேர்காணலுக்கு முன் பதிவு கட்டணம் கேட்கிறார்கள். என்ன செய்ய வேண்டும்?",["உடனே செலுத்தவும்","நிறுவனத்தை தனியாகச் சரிபார்க்கவும்","வங்கி விவரம் அனுப்பவும்","கடன் வாங்கவும்"],"முன்கூட்டியே கட்டணம் கேட்பது போலி வேலைக்கான அறிகுறியாக இருக்கலாம்."),
("புதிய எண்ணில் நண்பர் அவசரமாகப் பணம் கேட்கிறார். என்ன செய்ய வேண்டும்?",["உடனே அனுப்பவும்","அறிந்த எண்ணில் அழைத்து உறுதிப்படுத்தவும்","வங்கி உள்நுழைவைப் பகிரவும்","அட்டை படத்தை அனுப்பவும்"],"மோசடிக்காரர்கள் நண்பரைப் போல நடிக்கலாம்."),
("எதிர்பாராத பார்சல் கட்டண இணைப்பு வந்தால்?",["கட்டணம் செலுத்தவும்","அட்டை விவரம் தரவும்","அதிகாரப்பூர்வ செயலியில் சரிபார்க்கவும்","OTP அனுப்பவும்"],"அதிகாரப்பூர்வ வழியில் சரிபார்க்கவும்."),
("வலுவான கடவுச்சொல் பழக்கம் எது?",["123456","எங்கும் ஒரே கடவுச்சொல்","நீளமான தனித்த கடவுச்சொல்","நண்பரிடம் பகிரவும்"],"ஒவ்வொரு கணக்குக்கும் தனித்த கடவுச்சொல் பயன்படுத்தவும்."),
("இரு-படி சரிபார்ப்பு என்ன செய்கிறது?",["கூடுதல் உள்நுழைவு சரிபார்ப்பு சேர்க்கிறது","எல்லா இணைப்புகளையும் பாதுகாக்கிறது","ஸ்பாமை முழுவதும் நிறுத்துகிறது","கடவுச்சொல் தேவையில்லை"],"இது கூடுதல் பாதுகாப்பை வழங்குகிறது."),
("வங்கி உதவிக்கு ரிமோட் செயலியை நிறுவச் சொன்னால்?",["நிறுவவும்","திரை அணுகல் கொடுக்கவும்","மறுத்து வங்கியை அதிகாரப்பூர்வமாக தொடர்புகொள்ளவும்","PIN பகிரவும்"],"ரிமோட் அணுகல் உங்கள் சாதனத்தை மற்றவர் கட்டுப்படுத்த அனுமதிக்கலாம்."),
("சந்தேக இணைப்பில் கடவுச்சொல் உள்ளிட்டுவிட்டால்?",["புறக்கணிக்கவும்","பாதுகாப்பான சாதனத்தில் கடவுச்சொல்லை மாற்றவும்","ஆதரவுக்கு கடவுச்சொல் அனுப்பவும்","இணைப்பை மீண்டும் திறக்கவும்"],"கடவுச்சொல்லை உடனே மாற்றி கூடுதல் பாதுகாப்பை இயக்கவும்."),
("தனிப்பட்ட படங்களை வெளியிடுவதாக மிரட்டி பணம் கேட்டால்?",["பணம் கொடுத்து மேலும் படங்கள் அனுப்பவும்","யாரிடமும் சொல்ல வேண்டாம்","ஆதாரங்களைச் சேமித்து உதவி பெறவும்; பணம் கொடுக்க வேண்டாம்","தனியாகச் சந்திக்கவும்"],"பணம் கொடுக்காமல் ஆதாரங்களைச் சேமித்து புகாரளிக்கவும்."),
("உங்களைப் போல போலி சமூக ஊடக கணக்கு இருந்தால்?",["கடவுச்சொல் அனுப்பவும்","ஆதாரத்தைச் சேமித்து புகாரளிக்கவும்","மேலும் தகவல் தரவும்","பாதுகாப்பை புறக்கணிக்கவும்"],"தளத்தில் போலி கணக்கைப் புகாரளிக்கவும்."),
("'இப்போது பணம் செலுத்தாவிட்டால் கைது' என்ற செய்தி என்னவாக இருக்கலாம்?",["உடனே செலுத்த வேண்டும்","பயமுறுத்தும் மோசடி","அனுப்பியவர் காவலர் என்பதற்கான சான்று","பாதுகாப்பான அரசு இணைப்பு"],"மோசடிக்காரர்கள் பயத்தையும் அவசரத்தையும் பயன்படுத்துவார்கள்."),
("இந்தியாவில் இணையப் பண மோசடியில் பணம் இழந்தால்?",["ஒரு மாதம் காத்திருக்கவும்","வங்கியை உடனே தொடர்புகொண்டு 1930 அழைக்கவும்","செய்திகளை அழிக்கவும்","முன்கூட்டியே மீட்பு கட்டணம் செலுத்தவும்"],"விரைவில் புகாரளிக்கவும்; மீட்புக் கட்டணம் முன்கூட்டியே செலுத்த வேண்டாம்."),
("பொதுவில் பகிரக்கூடாதது எது?",["பொதுவான பாதுகாப்பு குறிப்பு","OTP, கடவுச்சொல் அல்லது வங்கி விவரம்","பொது செய்தி இணைப்பு","தனிப்பட்டதல்லாத பொழுதுபோக்கு"],"OTP மற்றும் நிதி விவரங்களை ரகசியமாக வைத்திருங்கள்."),
("அறிந்த ஒருவரிடமிருந்து விசித்திரமான செய்தி வந்தால்?",["வேறு நம்பகமான வழியில் உறுதிப்படுத்தவும்","அனைவருக்கும் அனுப்பவும்","முதலில் பணம் அனுப்பவும்","OTP பகிரவும்"],"வேறு நம்பகமான வழியில் உறுதிப்படுத்தவும்.")],
"Kannada": [
("ಬ್ಯಾಂಕ್ ಖಾತೆ ನಿರ್ಬಂಧಿಸಲಾಗುತ್ತದೆ ಎಂದು ಯಾರಾದರೂ ಹೇಳಿದರೆ ಏನು ಮಾಡಬೇಕು?",["OTP ಹಂಚಿ","ಲಿಂಕ್ ತೆರೆಯಿರಿ","ಬ್ಯಾಂಕಿನ ಅಧಿಕೃತ ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ","PIN ನೀಡಿ"],"OTP ಅಥವಾ PIN ಅನ್ನು ಯಾರಿಗೂ ಹೇಳಬೇಡಿ."),
("ಬಹುಮಾನ ಪಡೆಯಲು OTP ಕೇಳುತ್ತಾರೆ. ಸುರಕ್ಷಿತ ಕ್ರಮ ಯಾವುದು?",["ತಕ್ಷಣ ಕಳುಹಿಸಿ","ಹಂಚಬೇಡಿ","ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಹಾಕಿ","ಮತ್ತೊಂದು ಲಿಂಕ್ ಕೇಳಿ"],"OTP ನಿಮಗಾಗಿ ಮಾತ್ರ."),
("ಉದ್ಯೋಗ ಸಂದರ್ಶನಕ್ಕೂ ಮೊದಲು ನೋಂದಣಿ ಶುಲ್ಕ ಕೇಳಿದರೆ?",["ತಕ್ಷಣ ಪಾವತಿಸಿ","ಕಂಪನಿಯನ್ನು ಸ್ವತಂತ್ರವಾಗಿ ಪರಿಶೀಲಿಸಿ","ಬ್ಯಾಂಕ್ ವಿವರ ಕಳುಹಿಸಿ","ಸಾಲ ಮಾಡಿ"],"ಮುಂಗಡ ಶುಲ್ಕ ನಕಲಿ ಉದ್ಯೋಗದ ಸೂಚನೆಯಾಗಿರಬಹುದು."),
("ಹೊಸ ಸಂಖ್ಯೆಯಿಂದ ಸ್ನೇಹಿತ ತುರ್ತಾಗಿ ಹಣ ಕೇಳಿದರೆ?",["ತಕ್ಷಣ ಕಳುಹಿಸಿ","ತಿಳಿದಿರುವ ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ ದೃಢೀಕರಿಸಿ","ಬ್ಯಾಂಕ್ ಲಾಗಿನ್ ಹಂಚಿ","ಕಾರ್ಡ್ ಚಿತ್ರ ಕಳುಹಿಸಿ"],"ವಂಚಕರು ಪರಿಚಿತರಂತೆ ನಟಿಸಬಹುದು."),
("ನಿರೀಕ್ಷಿಸದ ಪಾರ್ಸೆಲ್ ಶುಲ್ಕದ ಲಿಂಕ್ ಬಂದರೆ?",["ಶುಲ್ಕ ಪಾವತಿಸಿ","ಕಾರ್ಡ್ ವಿವರ ನೀಡಿ","ಅಧಿಕೃತ ಡೆಲಿವರಿ ಆ್ಯಪ್ ಪರಿಶೀಲಿಸಿ","OTP ಕಳುಹಿಸಿ"],"ಅಧಿಕೃತ ಮಾರ್ಗದಿಂದ ಪರಿಶೀಲಿಸಿ."),
("ಬಲವಾದ ಪಾಸ್‌ವರ್ಡ್ ಅಭ್ಯಾಸ ಯಾವುದು?",["123456 ಬಳಸಿ","ಎಲ್ಲೆಡೆ ಒಂದೇ ಪಾಸ್‌ವರ್ಡ್","ಉದ್ದವಾದ ವಿಭಿನ್ನ ಪಾಸ್‌ವರ್ಡ್","ಸ್ನೇಹಿತನಿಗೆ ಹೇಳಿ"],"ಪ್ರತಿ ಖಾತೆಗೆ ವಿಭಿನ್ನ ಪಾಸ್‌ವರ್ಡ್ ಬಳಸಿ."),
("ಎರಡು ಹಂತದ ಪರಿಶೀಲನೆ ಏನು ಮಾಡುತ್ತದೆ?",["ಹೆಚ್ಚುವರಿ ಲಾಗಿನ್ ಪರಿಶೀಲನೆ ಸೇರಿಸುತ್ತದೆ","ಎಲ್ಲಾ ಲಿಂಕ್‌ಗಳನ್ನು ಸುರಕ್ಷಿತಗೊಳಿಸುತ್ತದೆ","ಎಲ್ಲ ಸ್ಪ್ಯಾಮ್ ತಡೆಯುತ್ತದೆ","ಪಾಸ್‌ವರ್ಡ್ ಬೇಡವಾಗುತ್ತದೆ"],"ಇದು ಹೆಚ್ಚುವರಿ ರಕ್ಷಣೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ."),
("ಬ್ಯಾಂಕ್ ಸಮಸ್ಯೆಗೆ ರಿಮೋಟ್ ಆ್ಯಪ್ ಸ್ಥಾಪಿಸಲು ಅಪರಿಚಿತರು ಹೇಳಿದರೆ?",["ಸ್ಥಾಪಿಸಿ","ಸ್ಕ್ರೀನ್ ಪ್ರವೇಶ ನೀಡಿ","ನಿರಾಕರಿಸಿ ಬ್ಯಾಂಕ್ ಅನ್ನು ಅಧಿಕೃತವಾಗಿ ಸಂಪರ್ಕಿಸಿ","PIN ಹಂಚಿ"],"ರಿಮೋಟ್ ಪ್ರವೇಶದಿಂದ ನಿಮ್ಮ ಸಾಧನವನ್ನು ನಿಯಂತ್ರಿಸಬಹುದು."),
("ಸಂದೇಹಾಸ್ಪದ ಲಿಂಕ್‌ನಲ್ಲಿ ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿದರೆ?",["ನಿರ್ಲಕ್ಷಿಸಿ","ಸುರಕ್ಷಿತ ಸಾಧನದಿಂದ ಪಾಸ್‌ವರ್ಡ್ ಬದಲಿಸಿ","ಸಹಾಯಕ್ಕೆ ಪಾಸ್‌ವರ್ಡ್ ಕಳುಹಿಸಿ","ಲಿಂಕ್ ಮತ್ತೆ ತೆರೆಯಿರಿ"],"ತಕ್ಷಣ ಪಾಸ್‌ವರ್ಡ್ ಬದಲಿಸಿ ಹೆಚ್ಚುವರಿ ಸುರಕ್ಷತೆ ಆನ್ ಮಾಡಿ."),
("ಖಾಸಗಿ ಚಿತ್ರಗಳನ್ನು ಹಂಚುವುದಾಗಿ ಬೆದರಿಸಿ ಹಣ ಕೇಳಿದರೆ?",["ಹಣ ಕೊಟ್ಟು ಇನ್ನಷ್ಟು ಚಿತ್ರ ಕಳುಹಿಸಿ","ಯಾರಿಗೂ ಹೇಳಬೇಡಿ","ಸಾಕ್ಷ್ಯ ಉಳಿಸಿ ಸಹಾಯ ಪಡೆಯಿರಿ; ಹಣ ಕೊಡಬೇಡಿ","ಒಬ್ಬರೇ ಭೇಟಿ ಮಾಡಿ"],"ಹಣ ಕೊಡಬೇಡಿ; ಸಾಕ್ಷ್ಯ ಉಳಿಸಿ ವರದಿ ಮಾಡಿ."),
("ನಿಮ್ಮಂತೆ ನಕಲಿ ಸಾಮಾಜಿಕ ಮಾಧ್ಯಮ ಖಾತೆ ಕಂಡರೆ?",["ಪಾಸ್‌ವರ್ಡ್ ಕಳುಹಿಸಿ","ಸಾಕ್ಷ್ಯ ಉಳಿಸಿ ನಕಲಿ ಖಾತೆ ವರದಿ ಮಾಡಿ","ಹೆಚ್ಚಿನ ಮಾಹಿತಿ ನೀಡಿ","ಸುರಕ್ಷತೆ ನಿರ್ಲಕ್ಷಿಸಿ"],"ವೇದಿಕೆಯಲ್ಲಿ ನಕಲಿ ಖಾತೆಯನ್ನು ವರದಿ ಮಾಡಿ."),
("'ಈಗ ಪಾವತಿಸದಿದ್ದರೆ ಬಂಧನ' ಎಂಬ ಸಂದೇಶ ಏನಾಗಿರಬಹುದು?",["ತಕ್ಷಣ ಪಾವತಿಸಲು ಕಾರಣ","ಭಯ ಹುಟ್ಟಿಸುವ ವಂಚನೆ","ಕಳುಹಿಸಿದವರು ಪೊಲೀಸರೆಂಬ ಸಾಕ್ಷಿ","ಸುರಕ್ಷಿತ ಸರ್ಕಾರಿ ಲಿಂಕ್"],"ವಂಚಕರು ಭಯ ಮತ್ತು ತುರ್ತು ಪರಿಸ್ಥಿತಿಯನ್ನು ಬಳಸುತ್ತಾರೆ."),
("ಭಾರತದಲ್ಲಿ ಆನ್‌ಲೈನ್ ಹಣ ವಂಚನೆಯಿಂದ ಹಣ ಕಳೆದುಕೊಂಡರೆ?",["ಒಂದು ತಿಂಗಳು ಕಾಯಿರಿ","ಬ್ಯಾಂಕ್ ಸಂಪರ್ಕಿಸಿ 1930ಗೆ ಬೇಗ ಕರೆ ಮಾಡಿ","ಸಂದೇಶ ಅಳಿಸಿ","ಮುಂಗಡ ಶುಲ್ಕ ಕೊಡಿ"],"ಬೇಗ ವರದಿ ಮಾಡಿ; ಹಣ ಮರಳಿಸಲು ಮುಂಗಡ ಶುಲ್ಕ ಕೊಡಬೇಡಿ."),
("ಸಾರ್ವಜನಿಕವಾಗಿ ಹಂಚಬಾರದ ಮಾಹಿತಿ ಯಾವುದು?",["ಸಾಮಾನ್ಯ ಸುರಕ್ಷತಾ ಸಲಹೆ","OTP, ಪಾಸ್‌ವರ್ಡ್ ಅಥವಾ ಬ್ಯಾಂಕ್ ವಿವರ","ಸಾರ್ವಜನಿಕ ಸುದ್ದಿ ಲಿಂಕ್","ಖಾಸಗಿಯಲ್ಲದ ಹವ್ಯಾಸ"],"OTP ಮತ್ತು ಹಣಕಾಸಿನ ವಿವರಗಳನ್ನು ಖಾಸಗಿಯಾಗಿ ಇಡಿ."),
("ಪರಿಚಿತರಿಂದ ವಿಚಿತ್ರ ಸಂದೇಶ ಬಂದರೆ?",["ಬೇರೆ ತಿಳಿದ ಮಾರ್ಗದಲ್ಲಿ ದೃಢೀಕರಿಸಿ","ಎಲ್ಲರಿಗೂ ಕಳುಹಿಸಿ","ಮೊದಲು ಹಣ ಕಳುಹಿಸಿ","OTP ಹಂಚಿ"],"ಬೇರೆ ವಿಶ್ವಾಸಾರ್ಹ ಮಾರ್ಗದಿಂದ ದೃಢೀಕರಿಸಿ.")]
}

st.markdown("""
<style>
:root{color-scheme:light}.stApp{background:linear-gradient(180deg,#eff8ff 0%,#fff 58%,#eef9ff 100%);color:#102f67}
.block-container{max-width:1500px;padding-top:.6rem;padding-bottom:1.4rem}
h1,h2,h3,p,li,label,div{font-family:Arial,'Noto Sans Malayalam','Noto Sans Devanagari',sans-serif}
h1,h2,h3,p,li,label{color:#12366f}.topbar{background:linear-gradient(100deg,#092d68,#1260a8);border-radius:0 0 24px 24px;padding:20px 24px;color:#fff;margin-bottom:15px;box-shadow:0 8px 22px #163b7120}
.brand{font-size:clamp(30px,3.5vw,44px);font-weight:900;color:#fff;line-height:1.15}.brand span{color:#14d2f4}.tagline{color:#fff!important;font-size:16px;margin-top:5px;font-weight:600}
.hero{background:linear-gradient(110deg,#fff,#dff3ff);border:2px solid #b9e3ff;border-radius:24px;padding:25px;min-height:250px}.hero h1{font-size:clamp(38px,4.3vw,58px);font-weight:900;line-height:1.02;margin:0;color:#092d68}.hero h1 span{color:#006be8}.hero p{font-size:19px;font-weight:600;line-height:1.5;color:#12366f!important}
.panel,.feature{border-radius:20px;padding:18px;border:1px solid #cfe4ff;margin-bottom:12px;color:#12366f!important}.panel h3,.feature h3{font-size:21px;font-weight:850;margin:0 0 8px}.panel p,.feature p{color:#12366f!important;font-size:15px;font-weight:600;line-height:1.45}.feature{min-height:145px}.pink{background:linear-gradient(120deg,#fff0f4,#ffdce7)}.blue{background:linear-gradient(120deg,#eaf6ff,#d4ecff)}.green{background:linear-gradient(120deg,#e9fff1,#cff8df)}.purple{background:linear-gradient(120deg,#f5eaff,#e5d4ff)}.yellow{background:linear-gradient(120deg,#fff8df,#ffedb0)}.teal{background:linear-gradient(120deg,#e1fbff,#c9f6f8)}.women{background:linear-gradient(120deg,#fff0ff,#edd8ff);border:2px solid #e4c1ff}.helpbox{background:linear-gradient(120deg,#e9f6ff,#dff2ff)}.tipsbox{background:linear-gradient(120deg,#e7fff2,#d0f9e7)}
.stButton>button{border-radius:12px;border:2px solid #b7d8ff;background:#075bd9;color:white;font-weight:800;min-height:2.8rem;font-size:16px}.stButton>button:hover{background:#003f9e;color:#fff;border-color:#003f9e} .stTextInput input,.stTextArea textarea{color:#102f67!important;background:#fff!important;border:2px solid #a9d1f5!important;font-size:17px!important}.stSelectbox label,.stRadio label,.stTextArea label,.stTextInput label{font-weight:800!important;color:#12366f!important}
div[data-testid="stAlert"]{font-weight:600}a{font-weight:800}footer{visibility:hidden}
</style>
""",unsafe_allow_html=True)

# Header and language selector
h1,h2=st.columns([5,1])
with h1: st.markdown(f'<div class="topbar"><div class="brand">🛡️ Cyber<span>Saathi</span></div><div class="tagline">{T["tagline"]}</div></div>',unsafe_allow_html=True)
with h2:
    selected_lang=st.selectbox("Language / ഭാഷ / भाषा / தமிழ் / ಕನ್ನಡ",list(TEXT.keys()),index=list(TEXT.keys()).index(lang),key="language")
    lang=selected_lang; T=TEXT[lang]; X=EXTRA[lang]

english_nav = TEXT["English"]["nav"]
if "nav_choice_en" not in st.session_state or st.session_state["nav_choice_en"] not in english_nav:
    st.session_state["nav_choice_en"] = "Home"

nav_items = T["nav"]
nav_key = f"navigation_{lang}"
expected_nav_label = nav_items[english_nav.index(st.session_state["nav_choice_en"])]

# Keep the dropdown selection in sync with the page shown. The callback updates
# the English page name whenever the user selects a different translated label.
if st.session_state.get(nav_key) != expected_nav_label:
    st.session_state[nav_key] = expected_nav_label

def on_navigation_change():
    chosen_label = st.session_state.get(nav_key, nav_items[0])
    if chosen_label in nav_items:
        st.session_state["nav_choice_en"] = english_nav[nav_items.index(chosen_label)]

st.selectbox(
    "Choose a page",
    options=nav_items,
    key=nav_key,
    label_visibility="collapsed",  # removes the visible “Choose a page” label
    on_change=on_navigation_change,
)
page = st.session_state["nav_choice_en"]

def go(target):
    # Update only the internal page here. The dropdown's widget state is
    # synchronized at the start of the next run, before the widget is created.
    # Changing nav_key here would cause StreamlitWidgetAlreadyInstantiatedError.
    if target in english_nav:
        st.session_state["nav_choice_en"] = target
        st.rerun()

def back_to_dashboard():
    # Only update the internal destination in callbacks. The dropdown key is
    # synchronized at the top of the next script run before its widget exists.
    st.session_state["nav_choice_en"] = "Home"

# Always show a clear way back to the dashboard on every inner page.
if page != "Home":
    back_col, current_col = st.columns([1, 4])
    with back_col:
        st.button(
            "⬅  Back to Dashboard",
            key=f"back_dashboard_{lang}",
            use_container_width=True,
            on_click=back_to_dashboard,
        )
    with current_col:
        st.caption("To return, click Back to Dashboard or select Home from the page menu above.")

if page=="Home":
    left,right=st.columns([2.2,1])
    with left:
        st.markdown(f'<div class="hero"><h1>{T["hero1"]}<br><span>{T["hero2"]}</span></h1><p>{T["intro"]}</p></div>',unsafe_allow_html=True)
        b1,b2=st.columns(2)
        with b1:
            if st.button("🔎  "+T["link_btn"],use_container_width=True): go("Link & Message Checkers")
        with b2:
            if st.button("✉️  "+T["msg_btn"],use_container_width=True): go("Link & Message Checkers")
    with right:
        st.markdown(f'<div class="panel women" style="min-height:190px"><div style="font-size:48px;text-align:center">🛡️🌸</div><h3>CyberSaathi {T["women_title"]}</h3><p>{T["women_desc"]}</p></div>',unsafe_allow_html=True)
        if st.button("🌸  "+T["explore"],key="women_explore_home",use_container_width=True): go("Women's Digital Safety")
    cards=[("scam","🛡️",T["scam"],T["scam_desc"],"pink","Scam Awareness"),("link","🔗",T["link"],T["link_desc"],"blue","Link & Message Checkers"),("message","✉️",T["message"],T["message_desc"],"green","Link & Message Checkers"),("scenarios","🧠",T["scenarios"],T["scenarios_desc"],"purple","Scenarios"),("quiz","📋",T["quiz"],T["quiz_desc"],"yellow","Quiz"),("lessons","📖",T["lessons"],T["lessons_desc"],"teal","Lessons"),("smart","🆘",T["smart"],T["smart_desc"],"purple","Safety Centre"),("safety","🛡️",T["safety"],T["safety_desc"],"blue","Safety Centre")]
    for row in range(3):
        cols=st.columns(3)
        for col_idx in range(3):```python
    for row in range((len(cards) + 2) // 3):
        cols = st.columns(3)
        for col_idx in range(3):
            card_idx = row * 3 + col_idx
            if card_idx >= len(cards):
                continue
            key, icon, title, desc, color, target = cards[card_idx]
            with cols[col_idx]:
                st.markdown(f'<div class="feature {color}"><div style="font-size:34px">{icon}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
                if st.button(T["explore"] + " →", key=f"home_{key}_{lang}", use_container_width=True):
                    go(target)
    key,icon,title,desc,color,target=cards[row*3+col_idx]
            with cols[col_idx]:
                st.markdown(f'<div class="feature {color}"><div style="font-size:34px">{icon}</div><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
                if st.button(T["explore"]+" →",key=f"home_{key}_{lang}",use_container_width=True): go(target)
    st.markdown(f'<div class="panel helpbox"><h2>📞 {T["help"]}</h2><p>{T["contacts"]}</p><p>{X["helplines"]}</p></div>',unsafe_allow_html=True)
    contacts=[("112","Emergency Assistance","tel:112"),("1930","Financial Cyber Fraud","tel:1930"),("14416","Mental Health (Tele-MANAS)","tel:14416"),("181","Women Helpline (availability varies by state)","tel:181"),("cybercrime.gov.in","Report Cybercrime (National Portal)","https://cybercrime.gov.in")]
    cols=st.columns(2)
    for i,(number,desc,url) in enumerate(contacts):
        with cols[i%2]: st.markdown(f'<div class="panel" style="background:#fff;padding:13px 16px"><h3 style="margin:0"><a href="{url}" target="_blank" style="color:#064fbb;text-decoration:none">📞 {number} ↗</a></h3><p>{desc}</p></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="panel tipsbox"><h3>🛡️ {T["tips"]}</h3><p>✅ {T["tip1"]}<br>✅ {T["tip2"]}<br>✅ {T["tip3"]}<br>✅ {T["tip4"]}</p></div>',unsafe_allow_html=True)

elif page=="Quiz":
    st.title("📋 "+X["quiz_title"]); st.write(X["quiz_intro"])
    bank=QUIZ if lang=="English" else [(QUIZ[i][0],QUIZ[i][1],QUIZ[i][2],QUIZ[i][3]) for i in range(15)]
    trans=QUIZ_TRANSLATIONS.get(lang,[])
    if lang!="English" and len(trans)==15:
        bank=[(trans[i][0],trans[i][1],QUIZ[i][2],trans[i][2]) for i in range(15)]
    with st.form(f"quiz_form_{lang}"):
        answers=[]
        for i,(q,opts,correct,explain) in enumerate(bank): answers.append(st.radio(f"{i+1}. {q}",opts,key=f"q_{lang}_{i}"))
        submitted=st.form_submit_button(X["quiz_submit"],use_container_width=True)
    if submitted:
        score=0
        for i,ans in enumerate(answers):
            q,opts,correct,explain=bank[i]
            if opts.index(ans)==correct: score+=1; st.success(f"{i+1}. ✓ {explain}")
            else: st.warning(f"{i+1}. {explain}")
        st.subheader(f'{X["score"]}: {score}/15')
        st.progress(score/15)
        st.info(X["quiz_feedback"])

elif page=="Safety Centre":
    st.title("🆘 "+X["smart_title"]); st.write(X["smart_hint"])
    situation=st.text_area(T["smart_label"],height=150,key=f"smart_text_{lang}")
    if st.button(X["smart_analyse"],use_container_width=True):
        if not situation.strip(): st.warning(T["message_empty"])
        else:
            lower=situation.lower(); words=X["analysis_words"]
            matches=[w for w in words if w.lower() in lower]
            st.subheader(X["smart_result"])
            if matches: st.warning(" • ".join(matches[:8]))
            else: st.info("No obvious keyword was detected. This does not mean the situation is safe.")
            for advice in X["analysis_advice"]: st.markdown("✅ "+advice)
            st.info(X["not_diagnosis"])
    st.divider(); st.subheader(T["help"])
    st.markdown(f'<p><a href="tel:112">📞 112 — Emergency assistance</a></p><p><a href="tel:1930">📞 1930 — Financial cyber fraud (India)</a></p><p><a href="tel:181">📞 181 — Women helpline (availability varies by state)</a></p><p><a href="https://cybercrime.gov.in" target="_blank">🌐 {X["official"]}</a></p>',unsafe_allow_html=True)

elif page=="Women's Digital Safety":
    st.title("🌸 "+T["women_title"]); st.success(X["women_intro"]); st.error(X["women_emergency"])
    st.subheader(X["women_steps_title"])
    for step in X["women_steps"]: st.markdown(f'<div class="panel women"><p style="font-size:17px;font-weight:700">{step}</p></div>',unsafe_allow_html=True)
    st.subheader({"English":"Choose what you need help with","Malayalam":"നിങ്ങൾക്ക് എന്ത് സഹായമാണ് വേണ്ടത്?","Hindi":"आपको किस चीज़ में मदद चाहिए?","Tamil":"எந்த உதவி தேவை?","Kannada":"ನಿಮಗೆ ಯಾವ ಸಹಾಯ ಬೇಕು?"}[lang])
    st.caption({"English":"Click a topic to see what to do next.","Malayalam":"അടുത്തതായി എന്ത് ചെയ്യണമെന്ന് അറിയാൻ ഒരു വിഷയം തിരഞ്ഞെടുക്കുക.","Hindi":"अगला कदम जानने के लिए किसी विषय पर क्लिक करें।","Tamil":"அடுத்து என்ன செய்ய வேண்டும் என்பதை அறிய ஒரு தலைப்பைத் தேர்ந்தெடுக்கவும்.","Kannada":"ಮುಂದಿನ ಕ್ರಮ ತಿಳಿಯ ವಿಷಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ."}[lang])
    # Use a radio selector instead of separate buttons. Streamlit reliably
    # updates the selected topic on every rerun, including language changes.
    selected_topic = st.radio(
        "Choose a topic",
        options=list(range(len(X["women_topics"]))),
        format_func=lambda idx: "🆘  " + X["women_topics"][idx],
        key=f"women_topic_choice_{lang}",
        label_visibility="collapsed",
    )
    st.markdown(f'<div class="panel women"><h3>📌 {X["women_topics"][selected_topic]}</h3></div>', unsafe_allow_html=True)
    guidance = {
        0: [0, 1, 2, 4, 7], 1: [2, 3, 4, 7], 2: [1, 2, 4, 5, 7],
        3: [0, 2, 3, 7], 4: [0, 2, 6, 7], 5: [3, 4, 2]
    }.get(selected_topic, [0, 2, 7])
    st.subheader("Next steps")
    for number, step_index in enumerate(guidance, start=1):
        st.markdown(f'<div class="panel blue"><p style="font-size:17px;font-weight:700">{number}. {X["women_steps"][step_index]}</p></div>', unsafe_allow_html=True)
    st.info(X["women_note"])
    st.warning(X["women_note"])
    st.markdown(f'<div class="panel helpbox"><h3>📞 {T["help"]}</h3><p><a href="tel:112">112 — Emergency assistance</a></p><p><a href="tel:181">181 — Women helpline (availability varies by state)</a></p><p><a href="tel:1930">1930 — Financial cyber fraud in India</a></p><p><a href="https://cybercrime.gov.in" target="_blank">{X["official"]}</a></p></div>',unsafe_allow_html=True)

elif page=="Scam Awareness":
    st.title("🛡️ "+T["scam"]); st.subheader(T["scam_heading"])
    for item in T["scam_items"]: st.info(item)

elif page=="Link & Message Checkers":
    st.title("🔎 "+T["link"]+" / "+T["message"]); st.subheader(T["check_link"])
    url=st.text_input(T["paste_url"],placeholder="https://example.com",key="url_input")
    if st.button(T["check"],key="url_check"):
        if not url.strip(): st.warning(T["url_empty"])
        else:
            value=url.strip(); parsed=urlparse(value if re.match(r"^https?://",value,re.I) else "https://"+value); host=parsed.netloc.lower()
            suspicious=(not host or " " in value or any(x in host for x in ["verify-account","free-gift","urgent-login","bit.ly","tinyurl.com"]) or re.search(r"\d{5,}",host) is not None or host.count("-")>=3 or parsed.scheme!="https")
            if suspicious:
                st.warning(T["url_result_warn"])
            else:
                st.success(T["url_result_safe"])
    st.divider(); message=st.text_area(T["message_label"],height=130,key="message_input")
    if st.button(T["analyze"],key="message_check"):
        if not message.strip(): st.warning(T["message_empty"])
        else:
            lower=message.lower(); flags=[]
            patterns=[(r"\b(otp|one.time.password|pin|password)\b","Requests an OTP, PIN or password"),(r"\b(urgent|immediately|right now|today only|account blocked|suspended)\b","Uses urgency or threats"),(r"\b(prize|winner|lottery|free gift|claim now)\b","Promises a prize or gift"),(r"\b(pay|payment|fee|transfer|send money)\b","Asks for money or payment"),(r"https?://|www\.","Contains a link")]
            for pat,reason in patterns:
                if re.search(pat,lower): flags.append(reason)
            st.subheader(T["message_result"])
            for flag in flags: st.warning("⚠️ "+flag)
            if not flags: st.info(T["url_result_safe"])
            st.caption("Basic awareness check only; it cannot guarantee whether a message is safe.")

elif page == "Scenarios":
    st.title("🧠 Real-Life Cyber Safety Scenarios")
    st.write("Read each situation, choose what you would do, and press **Check answer**. Open any card below to practise. These examples are for awareness and learning.")

    SCENARIO_BANK = [
        {
            "title": "1. Fake parcel delivery fee",
            "story": "You receive a text saying your parcel will be returned unless you pay a small fee through a link. You are not expecting a delivery.",
            "options": ["Pay the fee quickly", "Open the link and enter card details", "Check the delivery company using its official app or website", "Send the sender your OTP"],
            "correct": 2,
            "why": "Scammers use small fees and urgent messages to steal card details. Check delivery updates through the company's official app or website."
        },
        {
            "title": "2. Bank account warning",
            "story": "A message says your bank account will be blocked in 10 minutes unless you click a link and verify your details.",
            "options": ["Click the link immediately", "Reply with your OTP", "Ignore the link and contact the bank using its official app or number", "Forward the message to your contacts"],
            "correct": 2,
            "why": "A threat and a short deadline are common pressure tactics. Contact the bank using a number or app you find independently."
        },
        {
            "title": "3. Job offer with a fee",
            "story": "Someone offers you a job without an interview but asks you to pay a registration or training fee first.",
            "options": ["Pay because the job sounds good", "Check the company and job opening independently before sharing details or money", "Send your bank password", "Share the offer publicly with your ID documents"],
            "correct": 1,
            "why": "A request for money before a job is confirmed is a warning sign. Verify the company through its official website and contact details."
        },
        {
            "title": "4. Friend asks for urgent money",
            "story": "A message from a friend’s account says they are in trouble and need money immediately. The writing feels unusual.",
            "options": ["Transfer money straight away", "Ask for their OTP", "Verify by calling your friend on a number you already know", "Send your card details to help them"],
            "correct": 2,
            "why": "An account may be hacked or impersonated. Confirm the request through a separate, trusted contact method before sending money."
        },
        {
            "title": "5. Caller asks for an OTP",
            "story": "A caller claims to be from customer support and says they need your OTP to stop a suspicious transaction.",
            "options": ["Read the OTP to the caller", "Share only the first half", "Do not share it; end the call and contact the service through its official channel", "Send a screenshot of the message"],
            "correct": 2,
            "why": "Never share OTPs, PINs or passwords with anyone. Contact the bank or service provider directly if you are worried."
        },
        {
            "title": "6. QR code to receive money",
            "story": "A buyer says you must scan a QR code and enter your UPI PIN to receive money for an item you are selling.",
            "options": ["Scan it and enter your UPI PIN", "Do what the buyer says because they sound trustworthy", "Do not enter your UPI PIN to receive money; verify the payment in your payment app", "Share your screen with the buyer"],
            "correct": 2,
            "why": "A UPI PIN is used to authorise payments, not to receive money. Never follow payment instructions from a stranger without checking."
        },
        {
            "title": "7. Prize or lottery message",
            "story": "You get a message saying you won a prize, but you must pay a processing fee and provide personal details to claim it.",
            "options": ["Pay the processing fee", "Send your ID and bank details", "Treat it as suspicious and verify the claim independently; do not pay", "Share the link with friends"],
            "correct": 2,
            "why": "Unexpected prizes that require advance payment are a common scam pattern. Do not share financial details or pay to claim an unverified prize."
        },
        {
            "title": "8. Fake social-media profile",
            "story": "You find a profile using your name and photos and sending messages to your friends as if it were you.",
            "options": ["Send the profile your password", "Save screenshots, report the impersonating profile, and warn trusted contacts", "Give the profile more personal information", "Click any recovery link it sends"],
            "correct": 1,
            "why": "Keep evidence, report the fake account using the platform's reporting tools, and let friends know through a trusted channel."
        },
        {
            "title": "9. Suspicious public Wi-Fi login",
            "story": "At a café, a Wi-Fi page asks for your banking password or an OTP before you can connect.",
            "options": ["Enter your banking password", "Use the same password you use everywhere", "Do not provide banking credentials; use mobile data for sensitive activity", "Ask a stranger to log in for you"],
            "correct": 2,
            "why": "A Wi-Fi login should not need your banking password. Avoid banking or sensitive account access on untrusted networks."
        },
        {
            "title": "10. Threat to share private photos",
            "story": "Someone threatens to share your private photos unless you send money or more pictures.",
            "options": ["Pay them and send more pictures", "Meet them alone to settle it", "Do not send more content or money; save evidence and seek trusted and official help", "Delete all evidence and stay silent"],
            "correct": 2,
            "why": "You are not to blame. Preserve messages and account details, block/report the person when safe, and ask a trusted person or official service for help. If you are in immediate danger, contact emergency services."
        },
    ]

    for i, scenario in enumerate(SCENARIO_BANK):
        with st.expander(scenario["title"], expanded=(i == 0)):
            st.markdown("**Situation**")
            st.write(scenario["story"])
            answer = st.radio(
                "What would you do?",
                scenario["options"],
                key=f"scenario_choice_{i}_{lang}",
                index=None,
            )
            if st.button("Check answer", key=f"scenario_check_{i}_{lang}", use_container_width=True):
                if answer is None:
                    st.warning("Choose an answer first.")
                else:
                    st.session_state[f"scenario_feedback_{i}_{lang}"] = (scenario["options"].index(answer) == scenario["correct"])
            feedback_key = f"scenario_feedback_{i}_{lang}"
            if feedback_key in st.session_state:
                if st.session_state[feedback_key]:
                    st.success("✅ Good choice! " + scenario["why"])
                else:
                    st.warning("💡 Not the safest choice. " + scenario["why"])

    st.info("Safety reminder: never share OTPs, PINs or passwords. If money is lost to cyber fraud in India, contact your bank quickly and call 1930 as soon as possible.")

elif page=="Lessons":
    st.title("📖 "+T["lesson_heading"])
    for item in T["lesson_items"]: st.markdown("✅ "+item)

elif page=="Know Your Rights":
    st.title("⚖️ "+T["rights_heading"])
    for item in T["rights_items"]: st.markdown("✅ "+item)

elif page=="Evidence Guide":
    st.title("🗂️ "+T["evidence_heading"])
    for item in T["evidence_items"]: st.markdown("✅ "+item)

elif page=="Report Cybercrime":
    st.title("📣 "+T["report_heading"]); st.write(T["report_text"])
    st.markdown('<div class="panel helpbox"><h3>Official reporting</h3><p><a href="https://cybercrime.gov.in" target="_blank">https://cybercrime.gov.in ↗</a></p><p><a href="tel:1930">📞 1930 — Financial cyber fraud in India</a></p><p><a href="tel:112">📞 112 — Emergency assistance</a></p></div>',unsafe_allow_html=True)

st.markdown("---")
st.markdown(f'<div style="text-align:center;padding:12px;color:#12366f;font-weight:800">{T["footer"]}</div>',unsafe_allow_html=True)
