import streamlit as st
import pywhatkit as pwk

# Title of the app
st.title("WhatsApp Message Sender")

# Instructions for users
st.write("""
This app allows you to send WhatsApp messages directly from your browser at a scheduled time.  
Make sure your phone is connected to WhatsApp Web!
""")

# Input fields
phone = st.text_input("Enter Phone Number (include country code, e.g., +1234567890):")
message = st.text_area("Enter Your Message:")
hour = st.number_input("Enter Hour (24-hour format, e.g., 14 for 2 PM):", min_value=0, max_value=23, step=1)
minute = st.number_input("Enter Minute (e.g., 30):", min_value=0, max_value=59, step=1)

# Button to trigger message sending
if st.button("Send Message"):
    if phone and message:
        try:
            # Schedule the message at the specified time
            pwk.sendwhatmsg(phone, message, int(hour), int(minute))
            st.success(f"Message to {phone} has been scheduled for {hour:02d}:{minute:02d}!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all the required fields (phone, message, hour, and minute).")


