import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)

promptMedia = """
As a marketing strategist, You will be provided with a customer’s Thai SME brand information including:Brand differentiation, Target Audience, Brand Direction or Brand Goals, and marketing funnel target that the customer would like to achieve.
You need to schedule it into a 14-day actionable Media plan from the content pillar idea.

A content pillar idea should include
1. The main theme of that content pillar
2. Description of the idea
3. Marketing tactic / content that can be included in the main theme to attain the goal and also be creative
4. The end goal of this pillar as stated from the customer’s Brand Direction/Brand Goals

For Example
Main Theme#1: Thirst Trap food
promoting existing menus / new menus in a yummy way
Main Theme#2: Promotion updates and Campaign
promotions
campaign
delivery platform promotion
updates or discount for you
Main Theme#3
Sharing tips how to select a yogurt
business behind the scene of the entrepreneur
Mascot promotion
The end goal:To increase conversion rate and to make the brand more recognizable

Then create a JSON structure represents each row as an object with key-value pairs, which would easily translate into a pandas DataFrame. 
For the 14-day Media Plan. 
The row left box of the row(the head) includes the day countin from Day1 to Day14, platform, content theme, Details and tagline for the content.
Don't output the table and don't output the content pillars ideas json but memorize your ideas into the json structure below
The JSON structure for Media Plan should include:
A "Day" key representing the specific day within each week.
The "Platform", "Content Theme", "Details/Content Description", and "Tagline" for each piece of content.
"""

promptContent = """
As a marketing strategist, You will be provided with a customer’s Thai SME brand information including:Brand differentiation, Target Audience, Brand Direction or Brand Goals, and marketing funnel target that the customer would like to achieve.
You need to create 3 possible content pillar ideas for the customer.

A content pillar idea should include
1. The main theme of that content pillar
2. Description of the idea
3. Marketing tactic / content that can be included in the main theme to attain the goal and also be creative
4. The end goal of this pillar as stated from the customer’s Brand Direction/Brand Goals

For Example
Main Theme#1: Thirst Trap food
promoting existing menus / new menus in a yummy way
Main Theme#2: Promotion updates and Campaign
promotions
campaign
delivery platform promotion
updates or discount for you
Main Theme#3
Sharing tips how to select a yogurt
business behind the scene of the entrepreneur
Mascot promotion
The end goal:To increase conversion rate and to make the brand more recognizable

Then create a JSON structure represents each row as an object with key-value pairs, which would easily translate into a pandas DataFrame. 
For the content pillars, please write the content pillars in a table including these columns: Main theme, Description, Marketing Tactic/Content, End Goal and make it reader-friendly
Don't output the table but memorize your ideas into the json structure below
The JSON structure for the content pillars includes:
"Number" key
"Main Theme" key
"Description" key
"Marketing Tactic/Content" key
"End Goal" key
"""


st.title(":rainbow[Content Pillars] สำหรับ :rainbow[SMEs บรรทัดทอง!]")
st.image("photos/บรรทัดทอง.webp", caption="โอ้โห้ นี่หรือบรรทัดทอง ผิดจากบ้านนอกตั้งหลายศอกหลายวา", use_container_width=True)
st.markdown("""
**:red[บรรทัดทอง]** ย่านของกินใหม่ใจกลางกรุงเทพ เต็มไปด้วยสีสันจากแสงไฟร้านอาหารร้านขนมหวานเจ้าเก่าและใหม่ประจำถิ่น 
แน่นไปด้วยทั้งชาวไทยและชาวต่างชาติที่ยอมเดินทางมาเพื่อได้ชิมของที่เขา **:red["อร่อยบอกต่อ!!!"]**       
""")

st.subheader(":rainbow[CONTENT PILLARS] คืออะไร", divider="gray")
st.markdown("""
            **:red[content pillars]** = สิ่งที่จะช่วยจัดระเบียบให้กับการสื่อสาร กำหนดแนวทางหรือ **:red[เรื่องราวที่แบรด์]** จะสื่อสารไปยัง **:red[กลุ่มเป้าหมาย]**
            เป็นเหมือนกลยุทธ์ของการทำคอนเทนต์""")
st.image("photos/ContentExample.png", caption="ตัวอย่างการวางแผน Content Pillar", use_container_width=True)

with st.form("my_form"):
    st.subheader(":rainbow[Your Brand Information]")
    BrandName =st.text_input("ชื่อแบรนด์ของท่าน ")
    st.write(":red[ตัวอย่าง]: :grey[Thai Craft Co.]")
    BrandDiff =st.text_area("แบรนด์ท่านแตกต่างจากที่อื่นอย่างไร: ")
    st.write(":red[ตัวอย่าง]: :grey[High-quality, handcrafted Thai home décor and accessories that combine traditional techniques with modern design for both local and international customers]")
    Target =st.text_area("กลุ่มเป้าหมายของท่านคือใคร: ")
    st.write(":red[ตัวอย่าง]: :grey[Young professionals, expats, and Thai consumers who appreciate cultural craftsmanship and unique home décor pieces]")
    Goal =st.text_area("เป้าหมายของในหนึ่งปีคืออะไร: ")
    st.write(":red[ตัวอย่าง]: :grey[Increase brand awareness, drive online sales, and enhance customer engagement through storytelling and showcasing craftsmanship]")
    MKTFunnel =st.text_area("ท่านต้องการบรรลุ marketing funnel ใด: ")
    st.image("photos/marketing_funnel.png", caption="ตัวอย่าง marketing funnel", use_container_width=True)
    st.write(":red[ตัวอย่าง]: :grey[Drive awareness at the top of the funnel, foster engagement at the middle, and convert leads into customers at the bottom]")
    submittedContent = st.form_submit_button("สร้าง content pillars")
    submittedMedia = st.form_submit_button("สร้าง Media Plan สำหรับ 2 สัปดาห์")

    st.write(":red[กรุณากรอกข้อมูลแบรนด์ของท่านก่อนกดสร้าง content pillars หรือ Media Plan สำหรับ 2 สัปดาห์]")
    if submittedMedia:
        user_input = {
            "Brand Name": BrandName,
            "Brand Differentiation": BrandDiff,
            "Target Audience": Target,
            "Brand Direction/Goals": Goal,
            "Marketing Funnel Target": MKTFunnel
        }

        user_input_str = json.dumps(user_input, ensure_ascii=False)

        messages_so_far = [
            {"role": "system", "content": promptMedia},
            {"role": "user", "content": user_input_str}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_so_far
        )
        result = response.choices[0].message.content
        output = result.replace('```',"").replace('json','')
        #print(output)
        data = json.loads(output)
        print(data)

        df = pd.DataFrame.from_dict(data)
        print(df)
        st.table(df)

        
        



    if submittedContent:
        user_input = {
            "Brand Name": BrandName,
            "Brand Differentiation": BrandDiff,
            "Target Audience": Target,
            "Brand Direction/Goals": Goal,
            "Marketing Funnel Target": MKTFunnel
        }

        user_input_str = json.dumps(user_input, ensure_ascii=False)
        
        messages_so_far = [
            {"role": "system", "content": promptContent},
            {"role": "user", "content": user_input_str}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_so_far
        )
        result = response.choices[0].message.content
        output = result.replace('```',"").replace('json','')
        #print(output)
        data = json.loads(output)
        print(data)

        df = pd.DataFrame.from_dict(data)
        print(df)
        st.table(df)

        # content_pillars_data = json.loads(testing)
        # print(testing)

        # if result:
        #     res_dict = json.loads(result)
        # else:
        #     print("Error: Empty response received.")
        # print("Full response:", response)
        # print("Response content:", result)

        # if result:  # Only try to parse if there's content
        #     res_dict = json.loads(result)
        #     print(res_dict)
        # else:
        #     print("No content received from the API.")

    
