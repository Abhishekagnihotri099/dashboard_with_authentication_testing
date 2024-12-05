def dashboard1():
    st.markdown("""
    <style>
        /* Global font color and family */
        body {
            font-family: 'Arial', sans-serif;
            color: #333;
        }

        /* Styling for sidebar */
        .sidebar .sidebar-content {
            background-color: #f4f4f4;
            color: #5d3a9b;
        }
        
        /* Styling for filter options */
        .sidebar .widget > label {
            color: #5d3a9b;
            font-weight: bold;
        }

        /* Styling for cards */
        .metric-card {
            border: 2px solid #5d3a9b;
            border-radius: 8px;
            background-color: #f0f0f0;
            padding: 20px;
            margin: 10px;
            height: 200px;  
            width: 160px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .metric-card h3 {
            color: #5d3a9b;
            font-size: 18px;
            margin-bottom: 10px;
        }

        .metric-card .value {
            font-size: 36px;
            font-weight: bold;
            color: #333;
            margin-bottom: 0px;
        }

        /* Styling for "Go Back to Home" button */
        .stButton button {
            background-color: #5d3a9b;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 30px;
            width: auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border: none;
        }

        .stButton button:hover {
            background-color: #4a2a78;
        }

        /* Centering the "Go Back to Home" button */
        .go-back-btn {
            display: flex;
            justify-content: center;
        }
    </style>
    """, unsafe_allow_html=True)
    # Display logo
    # st.image("exl.png", width=150)  # Replace 'logo.png' with the path to your logo image file

    col1, col2, col3 = st.columns([0.7, 2.6, 0.7])
    with col2:
        st.title("Claim Report Dashboard Testing")

   

    # Load data only once per session
    if "data" not in st.session_state:
        st.session_state.data = fetch_claims_data()

    # Fetch data from the database
    data = st.session_state.data

    st.title("Dashboard Navigation")
    navigation = st.selectbox("Select a Dashboard", ["Homepage", "Dashboard 1", "Dashboard 2", "Dashboard 3"])

    if not data.empty:
        # Sidebar for filters