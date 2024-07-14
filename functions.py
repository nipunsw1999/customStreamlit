import time
import streamlit as st

## STATUS ELEMENTS - CALLOUTS

def warn(text:str,seconds:int,done_display_time: int = 2):
    done_message = st.empty()
    done_message.warning(text, icon="⚠️")
    time.sleep(seconds)
    time.sleep(done_display_time)
    done_message.empty()

def err(text:str,seconds:int,done_display_time: int = 2):
    done_message = st.empty()
    done_message.error(text, icon="❌")
    time.sleep(seconds)
    time.sleep(done_display_time)
    done_message.empty()
    
def inf(text:str,seconds:int,done_display_time: int = 2):
    done_message = st.empty()
    done_message.info(text, icon="ℹ️")
    time.sleep(seconds)
    time.sleep(done_display_time)
    done_message.empty()

def completed(text:str,done_display_time:int = 2):
    done_message = st.empty()
    done_message.success(text, icon="✅")
    time.sleep(done_display_time)
    done_message.empty()