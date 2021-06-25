import streamlit as st
import sqlite3
import base64
import pandas as pd
import numpy as np
from streamlit import caching
from tensorflow.keras.models import model_from_json
import base64
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt
from scipy.ndimage.filters import uniform_filter1d, gaussian_filter
conn = sqlite3.connect('data3.db')
c= conn.cursor()

def create_table():
    
    c.execute('CREATE TABLE IF NOT EXISTS user(username TEXT UNIQUE,password TEXT NOT NULL)')
    


def login_user(username,password):
    c.execute('SELECT * FROM user WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data
def insert(name,password):
    conn=sqlite3.connect('data3.db')
    cur = conn.cursor()
    if cur.execute('SELECT * FROM user WHERE username = ?', (name,)):
        if cur.fetchone():
          st.warning('Error User already exist')
        else:
           cur.execute('INSERT INTO user VALUES(?,?)', (name, password))
           st.success('Register Entry sucess')


    conn.commit()
    conn.close()
def view_all_users():
    c.execute('SELECT * FROM user')
    data = c.fetchall()
    return data
def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()
    return block1, block2

def clean_blocks(blocks):
    for block in blocks:
        block.empty()

def login1(blocks):
    blocks[0].markdown("""
        <style>
                input {
                -webkit-text-security: disc;
            }
        </style>
        """, unsafe_allow_html=True)

    return blocks[0].text_input('username')

def login2(blocks):
    blocks[1].markdown("""
        <style>
                input {
                -webkit-text-security: disc;
            }
        </style>
        """, unsafe_allow_html=True)
    
    return blocks[1].text_input('password',type='password')


def main():
    st.set_page_config(page_title="Exoplanet Hunters",
                initial_sidebar_state="collapsed",
                page_icon="🔮")
    
    menu = ["Home","Visualize","Transit method","Login","SignUp","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    #if choice == "users":
    #    c = view_all_users()
     #   st.write(c)   
    if choice=="Transit method":
        main_bg = "012.jpg"
        main_bg_ext = "jpg"

        st.markdown(
            f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;

        }}

        </style>
        """,
            unsafe_allow_html=True
        )
        html_temp = """ 
            <div> 
            <h1 style ="color:black;
                        text-align:center;
                        font-weight:bold;
                        font-size:40px;
                        font-style:normal;
                        font-family:Courier New;">Transit Photometry</h1> 
                         </div>
            """
            
        st.markdown(html_temp, unsafe_allow_html=True)
        image = "transit.gif"
        st.image(image)
        st.markdown("**There are a lot of planets outside our solar system.These planets are known as exoplanets or extrasolar planets. It is difficult to detect them because they are very near to their host stars compared to the observation distance. They only reflect a little light compared to their stars. When a planet crosses in front of it’s star there is a slight decrease in the light intensity curve of the star. Periodic decrease in the flux curve of the star shows the presence of planets as planets are bodies that revolve in an orbit around the stars.This method of detecting the exoplanets, by continually observing dips in it’s brightness is called transit photometry.**")
        st.text(" ")
        st.markdown("**Feed the light curve data from transit method into this application to predict the possibility of exoplanets together with artificial intelligence**")   
    
    if choice == "Home":
        main_bg = "11.gif"
        main_bg_ext = "gif"

        st.markdown(
            f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
        }}
        </style>
        """,
            unsafe_allow_html=True)
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")     
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        html_temp = """ 
            <div> 
            <h1 style ="color:#FF00FF;
                        text-align:center;
                        font-weight:bold;
                        font-size:85px;
                        font-style:normal;
                        font-family:Courier New;">STELLA-GAZERS</h1>   </div>
            """
            
        st.markdown(html_temp, unsafe_allow_html=True)
        
        html_temp = """ 
            <div> 
                <h3 style ="border:5px #A9A9A9;
                        border-radius:100px;
                        border-style: outset;
                        color:white;
                        text-align:center;
                        font-weight:bold;
                        font-size:40px;
                        font-style:normal;
                        font-family:"Courier New";">Welcome ..Let's hunt for some exoplanets together with AI</h3> 
            
            </div>
            """
            
        st.markdown(html_temp, unsafe_allow_html=True)
        
    elif choice == "Login":
        main_bg = "012.jpg"
        main_bg_ext = "jpg"

        st.markdown(
            f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;

        }}

        </style>
        """,
            unsafe_allow_html=True
        )

        st.header("Login section")
    
        blk1 = generate_login_block()
        blk2 = generate_login_block()
        
        
        username = login1(blk1)         
        password = login2(blk2)
        c1, c2, c3 = st.beta_columns([1,1,1])
        login_check_box = c2.checkbox("Login")
        if login_check_box:
            
            result = login_user(username,password)
            if result:
                st.success("Successfully logged in as {}".format(username))
                
                list_of_pages = ['Predict using LSTM','Predict using CNN']
                page= st.radio("TASKS",list_of_pages)
                if page=='Predict using LSTM':
                    html_temp = """ 
                        <div> 
                        <h1 style ="color:black;
                                    text-align:center;
                                    font-weight:bold;
                                    font-size:50px;
                                    font-style:normal;
                                    font-family:"Lucida Console", "Courier New", monospace;">Prediction using LSTM</h1>  
                        </div> 
                        """
                    st.markdown(html_temp, unsafe_allow_html=True)
                
                    data = st.file_uploader(
                        label="Enter the data to be tested", type=['csv'])


                    if data is not None:
                        test = pd.read_csv(data)
                        x_test = test.drop('LABEL', axis=1)
                        rows = st.slider("Select the input row", 1, 570, 1)
                        rows1 = rows+1
                        st.write(rows)
                        plot = pd.DataFrame(x_test[rows:rows1].values).T
                        st.text("Click here to view the flux curve")
                        c1, c2, c3 = st.beta_columns([1,1,1])
                        with c2:
                            view_flux = st.button('View the flux curve')
                                               
                        if view_flux:
                            st.title('Light curve for star {}'.format(rows))
                            st.write(x_test[rows:rows1].T)
                            st.line_chart(plot)
                        st.write("Click below to predict")
                        c1, c2, c3 = st.beta_columns([1,1,1])
                        with c2:
                            lstm_button = st.button('Predict using lstm')     
                            
                        if lstm_button:

                            json_file = open('LSTM_model (2).json', 'r')
                            loaded_model_json = json_file.read()
                            json_file.close()
                            loaded_model = model_from_json(loaded_model_json)
                            loaded_model.load_weights("LSTM_model (2).h5")
                            loaded_model.summary()
                            y_pred = loaded_model.predict((x_test.values.reshape(
                                x_test.shape[0], x_test.shape[1], -1))[rows:rows1])

                            html_temp = """ 
                                <div style ="background-color:black;padding:13px"> 
                                <h2 style ="color:white;text-align:center;">The prediction probability is </h2> 
                                </div> 
                                """
                            st.markdown(html_temp, unsafe_allow_html=True)
                            st.write(y_pred)
                            
                            if y_pred < 0.5:
                                
                                html_temp = """ 
                                <div style ="background-color:pink;padding:10px"> 
                                <h3 style ="color:black;text-align:center;">Nope ! </h3> 
                                </div> 
                                """
                                st.markdown(html_temp, unsafe_allow_html=True)
                            else:
                                
                                html_temp = """ 
                                <div style ="background-color:pink;padding:10px"> 
                                <h3 style ="color:black;text-align:center;">Wohoo ! We found an exoplanet for the star !</h3> 
                                </div> 
                                """
                                st.markdown(html_temp, unsafe_allow_html=True)
                    with st.beta_expander("Model Details LSTM"):
                        c1, c2, c3 = st.beta_columns([1,1,1])
                        with c2:
                            img= "lstm_plot_main.png"
                            st.image(img)

                if page =='Predict using CNN':
                    html_temp = """ 
                        <div> 
                        <h1 style ="color:black;
                                    text-align:center;
                                    font-weight:bold;
                                    font-size:50px;
                                    font-style:normal;
                                    font-family:"Lucida Console", "Courier New", monospace;">Prediction using CNN</h1>  
                        </div> 
                        """
                    st.markdown(html_temp, unsafe_allow_html=True)
                
                    data1 = st.file_uploader(
                        label="Enter the data to be tested", type=['csv'])

                    if data1 is not None:
                        test = pd.read_csv(data1)
                        rows = st.slider("Select the input row", 1, 570, 1)
                        rows1 = rows+1
                        st.write(rows)
                        
                        x_test = test.drop('LABEL', axis=1)
                        x_test = np.array(x_test)

                        def detrender_normalizer(light_flux):
                            flux1 = light_flux
                            flux2 = gaussian_filter(flux1, sigma=10)
                            flux3 = flux1 - flux2
                            flux3normalized = (flux3-np.mean(flux3)) / \
                                (np.max(flux3)-np.min(flux3))
                            return flux3normalized

                        x_test_p = detrender_normalizer(x_test)
                        x_test = ((x_test - np.mean(x_test, axis=1).reshape(-1, 1)) /
                                np.std(x_test, axis=1).reshape(-1, 1))
                        x_test = np.stack([x_test, x_test_p], axis=2)
                        j_son_file = open('model_cnn.json', 'r')
                        loaded_model_j_son = j_son_file.read()
                        j_son_file.close()
                        loaded_model_cnn = model_from_json(loaded_model_j_son)
                        loaded_model_cnn.load_weights("model_cnn.h5")
                        loaded_model_cnn.summary()

                        c1, c2, c3 = st.beta_columns([1,1,1])
                        with c2:
                            cnn_button = st.button('Predict using cnn')
                        if cnn_button:
                       
                            y_predict = loaded_model_cnn.predict(x_test)[rows:rows1]

                            html_temp = """ 
                                    <div style ="background-color:black;padding:13px"> 
                                    <h2 style ="color:white;text-align:center;">The prediction probability is </h2> 
                                    </div> 
                                    """
                            st.markdown(html_temp, unsafe_allow_html=True)
                            
                            st.write(y_predict) 
                            if y_predict < 0.5:
                                html_temp = """ 
                                    <div style ="background-color:pink;padding:10px"> 
                                    <h3 style ="color:black;text-align:center;">Nope ! </h3> 
                                    </div> 
                                    """
                            else:

                                html_temp = """ 
                                    <div style ="background-color:pink;padding:10px"> 
                                    <h3 style ="color:black;text-align:center;">Wohoo ! We found an exoplanet for the star !</h3> 
                                    </div> 
                                    """
                            st.markdown(html_temp, unsafe_allow_html=True)
                    if data1 is None:
                        st.write("Please upload a csv file")
                    with st.beta_expander("Model Details of CNN"):
                        c1, c2, c3 = st.beta_columns([1,1,1])
                        with c2:
                            img1 = "cnn_model.png"
                            
                            st.image(img1)    
                
            else:
                st.warning("Incorrect Username/password")
    elif choice == "SignUp":
        main_bg = "012.jpg"
        main_bg_ext = "jpg"

        st.markdown(
            f"""
            <style>
            .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
        }}

        </style>
        """,
            unsafe_allow_html=True
        )
        
        html = """
        <div>
        <h1 style="color:black;text-align:center">Sign Up here</h1>
        </div>
        """
        st.markdown(html,unsafe_allow_html=True)
        new_username = st.text_input("CREATE A USER NAME","")
        new_password = st.text_input("CREATE A PASSWORD","")

        if st.button("SignUp"):
            
            create_table()
            all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

            all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            total_digits = 0
            total_letters = 0
            for s in new_password:
                if s in all_digits:
                    total_digits+=1
                elif s in all_letters:
                    total_letters += 1
            if new_password==' ' or len(new_password)<5 or total_digits<3 or total_letters<4:
                st.warning("Please provide a valid password of length atleast 4 alphabets and 3 digits ")
            else:
                insert(new_username,new_password)
                
    elif choice =="Visualize":
        main_bg = "012.jpg"
        main_bg_ext = "jpg"

        st.markdown(
            f"""
            <style>
            .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
        }}

        </style>
        """,
            unsafe_allow_html=True
        )
        
        html_temp = """ 
            <div style ="background-color:navy;padding:13px"> 
            <h1 style ="color:white;text-align:center;">Visualize the Light Curve</h1> 
            </div> 
                """
        st.markdown(html_temp, unsafe_allow_html=True)
        html = """
            <div>
            <h2 style = "color:black;text-align:center;">To plot and visualize the light curve of stars individually upload the data below.</h2>
            </div>
            """
        st.markdown(html,unsafe_allow_html=True)
        data = st.file_uploader(
                        label="Enter the flux points of the star", type=['csv'])


        if data is not None:
            test = pd.read_csv(data)
            x_test = test.drop('LABEL', axis=1)
            rows = st.slider("Select the input row", 1, 570, 1)
            rows1 = rows+1
            st.write(rows)
            plot = pd.DataFrame(x_test[rows:rows1].values).T

            if st.button('View the flux'):
                st.title('Light curve for star {}'.format(rows))
                st.write(x_test[rows:rows1].T)
                st.line_chart(plot)
            

    elif choice =="About":
        html_temp = """ 
        <div style ="background-color:navy;padding:13px"> 
        <h1 style ="color:white;text-align:center;">About</h1> 
        </div> 
                """
        st.markdown(html_temp, unsafe_allow_html=True)
        main_bg = "012.jpg"
        main_bg_ext = "jpg"

        st.markdown(
            f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
        }}

        </style>
        """,
            unsafe_allow_html=True
        )
        col1, col2 = st.beta_columns(2)           
        with col1:
            html_temp = """ 
                    <div style="border:5px black;background-color: #A9A9A9;border-style: outset;"> 
                    <h3 style ="color:black;text-align:center">Authors:</h3> 
                    </div> 
                    """
            st.markdown(html_temp, unsafe_allow_html=True)
            st.text(" ")
            st.text(" ")                
            st.markdown(
            """ **[Cicy K Agnes](https://www.linkedin.com/in/cicykagnes/)**""")
            st.markdown(
            """ **[Akthar Naveed](https://www.linkedin.com/in/akthar-naveed-v-921039201)**""")
            st.markdown(
            """ **[Aromal O K](https://www.linkedin.com/in/aromal-o-k-b872bb213/)**""")
            st.markdown(
            """ **[Joyal Joe](https://www.linkedin.com/in/joyal-joe-616690214)**""")
            st.markdown(
            """ **[Favian R Periera](https://www.linkedin.com/in/favian-pereira-a8b69a206)**""")
        with col2:
            html_temp = """ 
                    <div style="border:5px black;background-color: #A9A9A9;border-style: outset;"> 
                    <u>
                    <h3 style ="color:black;text-align:center">Dates and Source Code:</h3> </u>
                    </div> 
                    """
            st.markdown(html_temp, unsafe_allow_html=True)
            st.text(" ")
            st.text(" ")

            st.markdown(
                """Click here for the source code : **[Source code](https://github.com/cicykagnes)**""")

            html_temp = """ 
                    <div> 
                    <h3 style ="color:black;">Created on: 09/05/2021</h3> 
                    </div> 
                    """
            st.markdown(html_temp, unsafe_allow_html=True)
            html_temp = """ 
                    <div> 
                    <h3 style ="color:black;">Last updated: 09/06/2021</h3> 
                    </div> 
                    """
            st.markdown(html_temp, unsafe_allow_html=True)
          
if __name__=='__main__':
    
    main()
