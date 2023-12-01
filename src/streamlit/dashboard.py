import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import os
import sys

rpath = os.path.abspath('../..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_top_users_with_highest_replies(data):
    row_with_highest_replies = df.loc[df['reply_count'].idxmax()]
    user_with_highest_replies = row_with_highest_replies['sender_name']
    num_replies = row_with_highest_replies['reply_count']

    # Streamlit app
    st.title('Top User with the Highest Replies Plot')

    # Create a DataFrame for the bar chart
    chart_data = pd.DataFrame({
        'User': [user_with_highest_replies],
        'Number of Replies': [num_replies]
    })

    # Bar chart in Streamlit
    st.bar_chart(chart_data.set_index('User'))

def draw_df(data):
    st.title('usernames with highest replies')
    users = data.sort_values(by='reply_count', ascending=False).head(10)
    users_replies = users[['sender_name', 'reply_count']]
    st.table(users_replies.reset_index(drop=True))

def draw_message_with_replies(data):
    df = data.sort_values(by='reply_count', ascending=False).head(10)
    channels_replies = df[['channel', 'reply_count']]
    st.table(channels_replies.reset_index(drop=True))

def draw_reply_per_user_per_channel(data):
    grouped_df = data.groupby(['channel', 'sender_name'])['reply_count'].sum().unstack()
    grouped_df.plot(kind='bar', figsize=(15, 7.5), stacked=True)
    
    plt.figure(figsize=(15, 7.5))
    grouped_df.plot(kind='bar', stacked=True)

    plt.title('Reply Counts per User per Channel')
    plt.xlabel('Channel')
    plt.ylabel('Total Reply Count')
    plt.legend(title='Sender Name', bbox_to_anchor=(1, 1))
    #st.pyplot(plt)

if __name__ == '__main__':
    sl =SlackDataLoader('../../data/Anonymized_B6SlackExport_25Nov23/anonymized')
    df = sl.create_dataframe()
    col1, col2 = st.columns(2)
    with col1:
        plot_top_users_with_highest_replies(df)
    with col2:
        draw_df(df)
    
    col1, col2 = st.columns(2)
    with col1:
        draw_message_with_replies(df)
    with col2:
        draw_reply_per_user_per_channel(df)