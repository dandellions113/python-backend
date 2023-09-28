import loader
import request
import db_upload
from tqdm import tqdm
langs=[{'hi':[{"finance":"वित्त"},{"railway":"रेल"},{"health":"स्वास्थ्य"},{"education":"शिक्षा"},{"defence":"रक्षा"}]},
       {'te':[{"finance":"ఆర్థిక"},{"railway":"రైల్వే"},{"health":"ఆరోగ్య"},{"education":"విద్యా"},{"defence":"రక్షణ"}]},
       {'pa':[{"finance":"ਵਿੱਤ"},{"railway":"ਰੇਲਵੇ "},{"health":"ਸਿਹਤ"},{"education":"ਸਿੱਖਿਆ"},{"defence":"ਰੱਖਿਆ"}]},
       {'en':[{"finance":"finance"},{"railway":"railway"},{"health":"health"},{"education":"education"},{"defence":"defence"}]},
       {'ta':[{"finance":"நிதி"},{"railway":"ரயில்வே"},{"health":"சுகாதார "},{"education":"கல்வி"},{"defence":"பாதுகாப்பு"}]}]
# keywords=['Minister of Finance of India','Minister of Railways of India','Ministry of Health and Family Welfare, Government of India','Ministry of Education of India','Ministry of Defence']
for x in langs:
    for lang,ls in x.items():
        for dct in ls:
            for f_key,r_key in tqdm(dct.items()):
                raw_data=request.main(lang,r_key,f_key)
                # print(raw_data)
                processed_data=loader.main(raw_data,f_key)
                db_upload.main(processed_data,f_key)
                # print(x)
                # print(lang,r_key)
    
    
    
    
    
    
    
    
    
    
    
    
    # for keyword in keywords:
    #     temp=request.main(lang=lang,keyword=keyword)
    #     print(str(temp)[:100])
    #     print()
        
    #     pro_temp=loader.main(temp,keyword)
    #     print(str(pro_temp)[:100])
        