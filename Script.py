class script(object):
    #start_text
    START_TXT = """
𝐇𝐞𝐲 {},
😎 <b>{}</b>, 𝐘𝐨𝐮𝐫 𝐌𝐨𝐯𝐢𝐞 𝐁𝐮𝐝𝐝𝐲!
🌟 𝐓𝐞𝐥𝐥 𝐦𝐞 𝐲𝐨𝐮𝐫 𝐦𝐨𝐯𝐢𝐞 𝐰𝐢𝐬𝐡,
😋 𝐋𝐞𝐭'𝐬 𝐦𝐚𝐤𝐞 𝐦𝐨𝐯𝐢𝐞 𝐦𝐚𝐠𝐢𝐜!
🔮 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 <a href=https://t.me/iPRIMEHUB>𝐏𝐫𝐢𝐦𝐞𝐇𝐮𝐛™</a>.
"""
    #status_text
    STATUS_TXT = """Total Files: <code>{}</code>
Total Users: <code>{}</code>
"""

    REQ_TEXT  = """#NewRequest
Bot - {}
Name - {} (<code>{}</code>)
Request - <b>{}</b>
"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    #request_message
    REQM = """**To request for a movie please pass movie details along with** /request **command.**\n**Example**: <code>/request Avengers 2019</code>"""

    #request reply
    REQ_REPLY = """📍 **Your Request for** {} **has been submitted to the admins.**\n\n🚀 **Your Request Will Be Uploaded soon.**\n\n📌 **Please Note that Admins might be busy. So, this may take more time.**"""

    #remove ads
    REMADS_TEXT = """
<b>Free</b>\nAds & no direct links\n\n<b>Premium</b>\nDirect files & no creepy ads, faster response time, no waiting time, premium access of our other services\n\n<b>Plan Cost - ₹20/month & ₹100/6Month </b>\nPrices may increase in the future.\n<b>UPI</b> -\n    <code>iPrimeHub@axl</code>
"""
    #confirm text
    CNFRM_TEXT = """
**To Confirm Payment Process Please Send Your Transaction Screenshot Or Transaction ID To** <a href=https://t.me/lemx4>ｒｙｍｅ</a>\n\n**Admin delays may occur, request refund if plan activation fails.**
"""
    # Terms & Conditions
    TERMS = """
**Use of our service implies agreement to the following terms:**

1. The bot is provided "as is," and we reserve the right to modify or discontinue it without prior notice.
2. While we strive for accurate movie information, availability cannot be guaranteed.
3. We retain the right to update these terms without prior notification.
4. Advertisements are independent of us; any actions resulting from them are your sole responsibility.
5. The bot may collect your user ID for updates and record payment history for premium users.
6. We reserves the right to terminate services for users who violate these terms or engage in any form of abuse or misconduct.
7. We disclaim responsibility for any copyright infringement, and users are solely responsible for the utilization of our services.

**Your utilization of the bot signifies acknowledgment and acceptance of these terms.**
"""



    # removing blacklisted words
    BLACKLIST = ['www', 'tamilblaster', 'filmyzilla', 'streamershub', 'xyz', 'cine', 'link',
                'cloudsmoviesstore', 'moviez2you', 'bkp', 'cinema', 'filmy', 'bot', 'flix',
                '4u', 'hub', 'movies', 'otthd', 'telegram', 'hoichoihok',
                '@', 'filmy', 'films', 'cinema', 'join', 'club', 'apd',
                'backup', 'primeroom', 'theprofffesorr', 'premium', 'vip', '4wap', 'toonworld4all', 'mlwbd'
                'Telegram@alpacinodump', 'bollywood', "AllNewEnglishMovie", "7MovieRulz", "1TamilMV",
                'Bazar', '_Corner20', 'CornersOfficial❣️', 'support', 'iMediaShare', '[', ']', '&', '✅',
                'Uᴘʟᴏᴀᴅᴇᴅ', 'Bʏ', ':', 'PFM', 'alpacinodump']
