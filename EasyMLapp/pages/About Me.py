import streamlit as st


st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)

custom_css = """
    <style>
        h1{
            text-align: center;
        }
        .card-container {
            background-color: #f4f4f4;
            border-radius: 5px;
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 400px;
            margin: auto;
        }

        .profile-image {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 0 auto 20px;
            display: block;
        }

        .name {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }

        .skills {
            font-size: 16px;
            color: #666;
            margin-bottom: 20px;
        }

        .social-links {
            display: flex;
            justify-content: center;
        }

        .social-links a {
            text-decoration: none;
            color: #007bff;
            margin: 0 10px;
            font-size: 24px;
        }

    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Profile card content
profile_card = """
    <h1>About Me 🚀</h1>
    <div class="card-container">
        <img class="profile-image" src="https://avatars.githubusercontent.com/u/82160813?v=4" alt="User Image" />
        <div class="name">Rimmel Asghar</div>
        <div class="skills">Software Engineer with love For Machine Learning<br>Know more about me by visiting the Following links</div>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/janedoe/" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/janedoe" target="_blank"><i class="fab fa-github"></i></a>
            <a href="https://twitter.com/janedoe" target="_blank"><i class="fab fa-kaggle"></i></a>
            <a href="https://twitter.com/janedoe" target="_blank"><i class="fab fa-behance"></i></a>
            <a href="https://twitter.com/janedoe" target="_blank"><i class="fab fa-medium"></i></a>
        </div>
        
    </div>
"""

st.markdown(profile_card, unsafe_allow_html=True)
