import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import CTransformers



# llm = ChatOpenAI()
llm = CTransformers(
    model = 'llama-2-7b-chat.ggmlv3.q2_K.bin',
    model_type='llama'
)


st.title('인공지능 백과사전')

content = st.text_input('주제를 제시해주세요.')

if st.button('정보 작성 요청하기'):
    with st.spinner('정보 작성 중...'):
        result = llm.predict(content + "search for this word")
        st.write(result)
