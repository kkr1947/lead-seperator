import pandas as pd  
import numpy as np

df = pd.read_csv("./new.csv")

# Extract contact us page from homepage
def contact_page(st):
    li = st.split(',')

        
    ls = [match for match in li if "contact" in match]
    if len(ls):
        ls = ls[0]
        return ls
    else:
        return ("")
# df['hlink']+
df['contact'] = df[df['heading'].apply(contact_page).str.contains('contact')]['hlink']+df[df['heading'].apply(contact_page).str.contains('contact')]['heading'].apply(contact_page).apply(lambda x:x[1:])

# Extracting facebook leads from a tags
def face_extract(st):
    li = st.split(',')

        
    ls = [match for match in li if "facebook" in match]
    if len(ls):
        ls = ls[0]
        return ls
    else:
        return ("")

df['facebook'] = df[df['heading'].apply(face_extract).str.contains('facebook')]['heading'].apply(face_extract)


# Extracting instagram leads from a tags
def insta_extract(st):
    li = st.split(',')

        
    ls = [match for match in li if "instagram" in match]
    if len(ls):
        ls = ls[0]
        return ls
    else:
        return ("")

df['instagram'] = df[df['heading'].apply(insta_extract).str.contains('instagram')]['heading'].apply(insta_extract)


# Extracting youtube leads from a tags
def youtube_extract(st):
    li = st.split(',')

        
    ls = [match for match in li if "youtube" in 
          match]
    if len(ls):
        ls = ls[0]
        return ls
    else:
        return ("")
df['youtube'] = df[df['heading'].apply(youtube_extract).str.contains('youtube')]['heading'].apply(youtube_extract)

# Extracting emails leads from a tags
def email_extract(st):
    li = st.split(',')

        
    ls = [match for match in li if "@" in match]
    if len(ls):
        ls = ls[0]
        return ls
    else:
        return ("")
# df['hlink']+
df['email'] = df[df['heading'].apply(email_extract).str.contains('@')]['heading'].apply(email_extract).apply(lambda x: x[7:].replace('mailto:',""))

df.to_csv('final_data.csv', index=False) #writing data
