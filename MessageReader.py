import win32com.client

outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
msg = outlook.OpenSharedItem('C:\\Users\\Anirudh\\AppData\\Local\\Temp\\Share your team with others.msg')

print(f'From: {msg.SenderName}')
print(f'SenderEmail: {msg.SenderEmailAddress}')
print(f'SentDate: {msg.SentOn}')
print(f'To: {msg.To}')
print(f'CC: {msg.CC}')
print(f'BCC: {msg.BCC}')
print(f'Subject: {msg.Subject}')
print(f'Body: {msg.Body}')

count_attachments = msg.Attachments.Count
print(count_attachments)
if count_attachments > 0:
    for item in range(count_attachments):
        print('Attachments: ', msg.Attachments.Item(item + 1).Filename)
