import streamlit as st
from easyml.helper import set_png_as_page_bg

# set_png_as_page_bg()

st.title('EasyML.io - Your Intelligent Machine Learning Companion')
github_stars_badge = "[![GitHub stars](https://img.shields.io/github/stars/rimmelasghar/EasyML.io)](https://github.com/rimmelasghar/EasyML.io)"
st.markdown(github_stars_badge, unsafe_allow_html=True)
st.subheader('A place where Machine Learning will be Easy to learn!!')

st.markdown(
    '''Description:

Are you ready to unlock the power of artificial intelligence and machine learning? Look no further than EasyML.io, your trusted companion on the exciting journey into the world of data science and predictive analytics.

Key Features:

🤖 Machine Learning Made Easy: EasyML.io is designed to demystify the complexities of machine learning. Whether you're a seasoned data scientist or a beginner, our intuitive interface makes it easy to build, train, and deploy machine learning models.

📊 Data Visualization: Dive into your data with stunning visualizations. EasyML.io provides powerful charting tools that help you understand your data, identify trends, and make data-driven decisions.

🧠 AutoML: Let EasyML.io's AutoML feature do the heavy lifting. It automatically selects the best algorithms and hyperparameters for your dataset, saving you time and effort.

📈 Predictive Modeling: Create accurate predictive models for tasks like regression, classification, and clustering. EasyML.io supports a wide range of algorithms, ensuring you can tackle any problem.

📚 Educational Resources: Whether you're a novice or an expert, EasyML.io offers a wealth of educational resources. Learn about machine learning concepts, best practices, and stay up-to-date with the latest advancements in AI.

🔒 Security and Privacy: We take your data privacy seriously. EasyML.io ensures the security and confidentiality of your datasets, making it a safe environment for your valuable information.

🚀 Scalable and Deployable: Take your models from experimentation to production with ease. EasyML.io helps you deploy models for real-world applications, whether on the cloud or at the edge.

🌐 Community and Collaboration: Join a thriving community of data enthusiasts. Collaborate on projects, share insights, and gain inspiration from others passionate about AI and ML.

Whether you're building recommendation systems, predicting market trends, or simply exploring the endless possibilities of data, EasyML.io is your indispensable tool. Get started today and embark on a journey of discovery and innovation with machine learning.

Feel free to use and adapt this description for EasyML.io according to your specific app's features and focus.'''
)

st.header("Tools Used")
# Custom CSS styles (inline)
custom_css = """
    <style>
        /* Center align the logos */
        .logo-container {
            text-align: center;
        }

        .logo-container img {
            margin: 0 10px;
            max-height: 60px;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Logos and alignment using HTML
logo_html = """
    <div class="logo-container">
        <img src="https://static.vecteezy.com/system/resources/previews/012/697/295/original/3d-python-programming-language-logo-free-png.png" alt="Python Logo">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" alt="Google Logo">
        <img src="https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="Streamlit Logo">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NumPy_logo.svg/1280px-NumPy_logo.svg.png" alt="Streamlit Logo">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png" alt="Streamlit Logo">
        <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/kaggle_logo_icon_168474.png" alt="Streamlit Logo">
    </div>
"""
st.markdown(logo_html, unsafe_allow_html=True)
